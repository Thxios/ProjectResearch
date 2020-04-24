from .imports import *
from .Object import Object


class Player(Object):
    symbol = np.ones((SCENE_CHANNEL,))
    move_speed = 1
    max_fire_delay = 10

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

