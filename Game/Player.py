from .imports import *
from .Object import Object


class Player(Object):
    symbol = np.ones((SCENE_CHANNEL,))

    move_speed = 0.5
    max_fire_delay = 20

    def __init__(self, x, y):
        Object.__init__(self, x, y, PLAYER_WIDTH, PLAYER_HEIGHT)

        self.fire_delay = self.max_fire_delay

    def update(self):
        if self.fire_delay > 0:
            self.fire_delay -= 1

    def fire(self):
        if self.fire_delay == 0:
            self.fire_delay = self.max_fire_delay
            return True
        return False

    def command_move(self, command):
        if command == LEFT:
            self.absolute_move(vector(-self.move_speed, 0))
        if command == RIGHT:
            self.absolute_move(vector(self.move_speed, 0))
        if command == UP:
            self.absolute_move(vector(0, -self.move_speed))
        if command == DOWN:
            self.absolute_move(vector(0, self.move_speed))

        self.x = clamp(self.x, 0, SCREEN_WIDTH - PLAYER_WIDTH)
        self.y = clamp(self.y, 0, SCREEN_HEIGHT - PLAYER_HEIGHT)

