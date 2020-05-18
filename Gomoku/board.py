from lib import *
from .validation import ThreeChecker, FourChecker, FiveChecker, SixChecker


class Board:
    def __init__(self, board):
        self.board = board

    def get(self, x, y):
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return -1
        return self.board[x, y]

    def valid(self, x, y, turn) -> bool:
        if x < 0 or x >= 15 or y < 0 or y >= 15:
            return False
        if self.get(x, y) != 0:
            return False

        lines = self._get_direction_lines(x, y, turn)

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
        self.board[x, y] = turn

    def _get_direction_lines(self, x, y, put=None):
        origin = vector(x, y)
        lines = np.array([[self.get(*(i * direction + origin)) for i in range(-4, 5)] for direction in directions])
        if put is not None:
            for line in lines:
                line[4] = put
        return lines
