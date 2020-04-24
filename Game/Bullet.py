from .imports import *
from .Object import Coordinate


class Bullet(Coordinate):
    def __init__(self, x, y, v: np.ndarray):
        Coordinate.__init__(self, x, y)
        self.v = v

    def update(self):
        self.position += self.v

    def in_screen(self):
        return 0 <= self.x < SCREEN_WIDTH and 0 <= self.y < SCREEN_HEIGHT


class PlayerBullet(Bullet):
    speed = 2

    def __init__(self, x, y):
        Bullet.__init__(self, x, y, vector(0, -self.speed))

