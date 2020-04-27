from .imports import *
from .Object import Coordinate


class Bullet(Coordinate):
    symbol: np.ndarray
    speed: float

    def __init__(self, x, y, v: np.ndarray):
        Coordinate.__init__(self, x, y)
        self.v = v

    def update(self):
        self.position += self.v

    def in_screen(self):
        return 0 <= self.x_int < SCREEN_WIDTH and 0 <= self.y_int < SCREEN_HEIGHT


class PlayerBullet(Bullet):
    symbol = vector(1, 1, 0)
    speed = 1

    def __init__(self, x, y):
        Bullet.__init__(self, x, y, vector(0, -self.speed))


class EnemyBullet(Bullet):
    symbol = vector(1, 0, 1)
    speed = 0.3

    def __init__(self, start: np.ndarray, toward: np.ndarray):
        direction = (toward - start) / np.sqrt(np.sum((toward - start) ** 2))
        Bullet.__init__(self, *start, direction * self.speed)

