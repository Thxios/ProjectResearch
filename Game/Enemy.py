from .imports import *
from .Object import Object
from .Bullet import EnemyBullet


class Enemy(Object):
    symbol = vector(1, 0, 0)

    vertical_speed = 0.05
    horizontal_speed = 0.1

    change_delay_max, change_delay_min = 60, 40

    fire_delay_max = 60

    def __init__(self, x, w, h):
        Object.__init__(self, x, -h, w, h)

        # self.float_position = vector(self.x, self.y, dtype=np.float)
        self.v = vector(0, self.vertical_speed)
        self.change_delay = 0
        self.fire_delay = self.fire_delay_max

    def update(self):
        self.change_direction()
        self.position += self.v
        if self.fire_delay > 0:
            self.fire_delay -= 1
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

    def fire(self, bullets: List[EnemyBullet]):
        if self.fire_delay == 0:
            origin = self.position + vector(self.w // 2, self.h)
            bullets.append(EnemyBullet(origin, origin + vector(1, 1)))
            bullets.append(EnemyBullet(origin, origin + vector(0, 1)))
            bullets.append(EnemyBullet(origin, origin + vector(-1, 1)))
            bullets.append(EnemyBullet(origin, origin + vector(-0.414, 1)))
            bullets.append(EnemyBullet(origin, origin + vector(0.414, 1)))
            self.fire_delay = self.fire_delay_max


class Obstacle(Object):
    symbol = vector(1, 0, 1)

