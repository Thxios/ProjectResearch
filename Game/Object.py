from .imports import *


class Object:
    symbol: np.ndarray

    def __init__(self, width, height, x, y):
        self.position = vector(x, y)
        self.w = width
        self.h = height
        self.surface = np.array([[self.symbol for _ in range(self.w)] for _ in range(self.h)])
        self.v = vector(0, 0)

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

    def absolute_move(self, delta: np.ndarray):
        self.position += delta

    def apply_velocity(self):
        self.position += self.v
