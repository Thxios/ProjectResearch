from .imports import *
from .Object import Object
from .Player import Player
from .Enemy import Enemy
from .Bullet import PlayerBullet, EnemyBullet


class Game:
    def __init__(self):
        self.background = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_CHANNEL))
        self.player = Player(10, 20)

        self.enemies: List[Enemy] = []
        self.player_bullet: List[PlayerBullet] = []
        self.enemy_bullet: List[EnemyBullet] = []

        self.generate_enemy()
        self.generate_enemy()
        self.generate_enemy()

    def draw_scene(self) -> np.ndarray:
        self.background = np.zeros((SCREEN_WIDTH, SCREEN_HEIGHT, SCENE_CHANNEL))
        self.draw_object(self.player)

        for enemy in self.enemies:
            self.draw_object(enemy)

        for enemy_bullet in self.enemy_bullet:
            self.background[enemy_bullet.x_int, enemy_bullet.y_int] = EnemyBullet.symbol

        for player_bullet in self.player_bullet:
            self.background[player_bullet.x_int, player_bullet.y_int] = PlayerBullet.symbol

        return self.background

    def draw_object(self, obj: Object):
        x_start = max(obj.x_int, 0)
        y_start = max(obj.y_int, 0)
        x_end = min(obj.x_int + obj.w, SCREEN_WIDTH)
        y_end = min(obj.y_int + obj.h, SCREEN_HEIGHT)

        if x_end < 0 or y_end < 0:
            return
        if x_start >= SCREEN_WIDTH or y_start >= SCREEN_HEIGHT:
            return

        obj_x_start = max(-obj.x_int, 0)
        obj_y_start = max(-obj.y_int, 0)
        obj_x_end = min(SCREEN_WIDTH - obj.x_int, obj.w)
        obj_y_end = min(SCREEN_HEIGHT - obj.y_int, obj.h)

        # print(type(obj_x_start), type(obj_y_start), type(obj_x_end), type(obj_y_end))
        # print(type(x_start), type(y_start), type(x_end), type(y_end))

        # print((obj_x_start, obj_x_end), (obj_y_start, obj_y_end))
        # print((x_start, x_end), (y_start, y_end))
        # print(self.background[x_start: x_end, y_start: y_end].shape)
        # print(obj.surface[obj_x_start: obj_x_end, obj_y_start: obj_y_end].shape)

        # print(
        #     self.background[
        #         x_start: x_end, y_start: y_end
        #     ]
        # )
        # print(
        #     obj.surface[
        #         obj_x_start: obj_x_end, obj_y_start: obj_y_end
        #     ]
        # )

        self.background[
            x_start: x_end, y_start: y_end
        ] = \
            obj.surface[
                obj_x_start: obj_x_end, obj_y_start: obj_y_end
            ]

    def loop(self):
        self.player.update()

        i = 0
        while i < len(self.enemies):
            if self.enemies[i].y > SCREEN_HEIGHT:
                del self.enemies[i]
            else:
                self.enemies[i].update()
                self.enemies[i].fire(self.enemy_bullet)
                i += 1

        i = 0
        while i < len(self.player_bullet):
            self.player_bullet[i].update()
            if self.player_bullet[i].in_screen():
                i += 1
            else:
                del self.player_bullet[i]

        i = 0
        while i < len(self.enemy_bullet):
            self.enemy_bullet[i].update()
            if self.enemy_bullet[i].in_screen():
                i += 1
            else:
                del self.enemy_bullet[i]

    def generate_enemy(self):
        self.enemies.append(Enemy(randint(5, SCREEN_WIDTH - 5 - 4), 4, 6))

    def set_command(self, command: List[int]):
        for movement in (LEFT, RIGHT, UP, DOWN):
            if command[movement]:
                self.player.command_move(movement)
        if command[FIRE]:
            if self.player.fire():
                self.player_bullet.append(PlayerBullet(self.player.x + 1, self.player.y))
