from .imports import *


class Coordinate:
    def __init__(self, x, y):
        self.position = vector(x, y, dtype=np.float)

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
        return int(round(self.position[0]))

    @property
    def y_int(self):
        return int(round(self.position[1]))

    def absolute_move(self, delta: np.ndarray):
        self.position += delta


class Object(Coordinate):
    symbol: np.ndarray
    code: int

    def __init__(self, x, y, width, height):
        Coordinate.__init__(self, x, y)
        self.w = width
        self.h = height
        self.surface = np.array([[self.symbol for _ in range(self.h)] for _ in range(self.w)])
        self.v = vector(0, 0, dtype=np.float)

    def apply_velocity(self):
        self.position += self.v

    def update(self):
        pass

    def collide_point(self, point):
        x, y = point[0], point[1]
        return 0 <= x - self.x_int < self.w and 0 <= y - self.y_int < self.h
