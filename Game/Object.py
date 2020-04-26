from .imports import *


class Coordinate:
    def __init__(self, x, y):
        self.position = vector(x, y)

    @property
    def x(self):
        return self.position[0]

    @x.setter
    def x(self, x):
        self.position[0] = x

    @property
    def y(self):
        return self.position[1]

    @y.setter
    def y(self, y):
        self.position[1] = y

    @property
    def x_int(self):
        return round(self.position[0])

    @property
    def y_int(self):
        return round(self.position[1])

    def absolute_move(self, delta: np.ndarray):
        self.position += delta


class Object(Coordinate):
    symbol: np.ndarray

    def __init__(self, x, y, width, height):
        Coordinate.__init__(self, x, y)
        self.w = width
        self.h = height
        self.surface = np.array([[self.symbol for _ in range(self.h)] for _ in range(self.w)])
        self.v = vector(0, 0)

    def apply_velocity(self):
        self.position += self.v

    def update(self):
        pass
