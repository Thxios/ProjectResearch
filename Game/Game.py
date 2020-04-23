from .imports import *
from .Object import Object


class Game:
    def __init__(self):
        self.background = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_CHANNEL))
        self.player = Player(10, 20)


    def get_scene(self) -> np.ndarray:
        self.background = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_CHANNEL))
        self.draw_object(self.player)
        return self.background

    def draw_object(self, obj: Object):
        x_start = max(obj.x, 0)
        y_start = max(obj.y, 0)
        x_end = min(obj.x + obj.w, SCREEN_WIDTH)
        y_end = min(obj.y + obj.h, SCREEN_HEIGHT)

        if x_end < 0 or y_end < 0:
            return

        obj_x_start = max(-obj.x, 0)
        obj_y_start = max(-obj.y, 0)
        obj_x_end = min(SCREEN_WIDTH - obj.x, obj.w)
        obj_y_end = min(SCREEN_HEIGHT - obj.y, obj.h)

        # print(self.background[x_start: x_end, y_start: y_end].shape)
        # print(obj.surface[obj_x_start: obj_x_end, obj_y_start: obj_y_end].shape)

        self.background[
            x_start: x_end, y_start: y_end
        ] = \
            obj.surface[
                obj_x_start: obj_x_end, obj_y_start: obj_y_end
            ]

    def loop(self):
        pass


class Player(Object):
    symbol = np.ones((SCENE_CHANNEL,))

    def __init__(self, x, y):
        Object.__init__(self, PLAYER_WIDTH, PLAYER_HEIGHT, x, y)
