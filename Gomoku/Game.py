from .lib import *
from .ForbiddenChecker import ThreeChecker


class Game:
    def __init__(self):
        self._board = np.zeros((15, 15), dtype=np.int)

    def get(self, x, y):
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return -1
        return self._board[x, y]

    def put(self, x, y, turn):
        if self.get(x, y) == 0:
            self._board[x, y] = turn

    def check_forbidden(self, x, y):
        origin = vector(x, y)
        directions = vector(
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
        )
        lines = np.array([[self.get(*(i * direction + origin)) for i in range(-4, 5)] for direction in directions])
        for line in lines:
            print(line)
        print(ThreeChecker.check(lines, 1))

    def show(self):
        for x in range(15):
            for y in range(15):
                if self.get(y, x) == 0:
                    print('. ', end='')
                elif self.get(y, x) == 1:
                    print('X ', end='')
                elif self.get(y, x) == 2:
                    print('O ', end='')
            print('\n', end='')
        print('\n')


