from .lib import *
from .ForbiddenChecker import ThreeChecker, FourChecker, FiveChecker, SixChecker


class Game:
    def __init__(self):
        self._board = np.zeros((15, 15), dtype=np.int)

    def get(self, x, y):
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return -1
        return self._board[x, y]

    def board(self):
        return self._board

    def valid(self, x, y, turn) -> bool:
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return False
        if self.get(x, y) != 0:
            return False

        lines = self.get_direction_lines(x, y, turn)

        if turn == BLACK:
            _six = SixChecker.check(lines, turn)
            _five = FiveChecker.check(lines, turn)
            if _five > _six:
                print('BLACK win')
                return True
            if _six:
                return False
            if ThreeChecker.check(lines, turn) >= 2:
                return False
            if FourChecker.check(lines, turn) >= 2:
                return False

        elif turn == WHITE:
            if FiveChecker.check(lines, turn):
                print('WHITE win')
                return True

        return True

    def put(self, x, y, turn):
        # if self.valid(x, y, turn):
        #     self._board[x, y] = turn
        self._board[x, y] = turn

    def get_direction_lines(self, x, y, put=None):
        origin = vector(x, y)
        lines = np.array([[self.get(*(i * direction + origin)) for i in range(-4, 5)] for direction in directions])
        if put is not None:
            for line in lines:
                line[4] = put
        return lines

    def check_forbidden(self, x, y):
        pass

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


