from .imports import *
from .Object import Object


class Enemy(Object):
    symbol = vector(1, 0, 0)

    vertical_speed = 0.1
    horizontal_speed = 0.2

    change_delay_max, change_delay_min = 60, 40

    def __init__(self, x, w, h):
        Object.__init__(self, x, -h, w, h)

        self.float_position = vector(self.x, self.y, dtype=np.float)
        self.v = vector(0, self.vertical_speed)
        self.change_delay = 0

    def update(self):
        self.change_direction()
        self.float_position += self.v
        self.x = round(self.float_position[0])
        self.y = round(self.float_position[1])
        # print(self.position)

    def change_direction(self):
        if self.change_delay < 20:
            self.v[0] = 0
        if self.change_delay > 0:
            self.change_delay -= 1
            return
        self.change_delay = randint(self.change_delay_min, self.change_delay_max)
        if self.x - 10 < 0:
            direction = 1
        elif self.x + self.w + 10 >= SCREEN_WIDTH:
            direction = 0
        else:
            direction = randint(-1, 1)
        self.v[0] = direction * self.horizontal_speed


class Obstacle(Object):
    symbol = vector(1, 0, 1)

