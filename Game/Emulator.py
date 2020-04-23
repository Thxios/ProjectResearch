from .imports import *
import pygame as pg
from .Game import Game


def array2surface(arr: np.ndarray) -> pg.Surface:
    return pg.surfarray.make_surface(arr * 255)


class Command:
    command = [
        0, 0
    ]

    coding = {
        pg.K_LEFT: 0,
        pg.K_RIGHT: 1,
    }

    def key_down(self, key):
        if key in self.coding:
            self.command[self.coding[key]] = 1

    def key_up(self, key):
        if key in self.coding:
            self.command[self.coding[key]] = 0


class Emulator:
    screen: pg.Surface
    running = False
    command = Command()
    clock: pg.time.Clock

    def __init__(self, game: Game):
        self.game = game

    def run(self):
        pg.init()
        self.screen = pg.display.set_mode((RENDER_WIDTH, RENDER_HEIGHT))

        self.running = True
        self.clock = pg.time.Clock()
        while self.running:
            self.main_loop()

    def main_loop(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN:
                self.command.key_down(event.key)
            elif event.type == pg.KEYUP:
                self.command.key_up(event.key)

        if self.command.command[0]:
            self.game.player.absolute_move(vector(-1, 0))
        if self.command.command[1]:
            self.game.player.absolute_move(vector(1, 0))

        self.game.loop()

        self.screen.blit(
            pg.transform.scale(
                array2surface(self.game.get_scene()),
                (RENDER_WIDTH, RENDER_HEIGHT)
            ),
            (0, 0)
        )

        pg.display.update()
        self.clock.tick(60)

