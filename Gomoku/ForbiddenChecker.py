from .lib import *


class _Checker:
    def __init__(self, multiply, compare):
        self.mul = multiply
        self.comp = compare

        self._str = ''
        for i in range(9):
            if self.mul[i] == 0:
                self._str += '?'
            else:
                if self.comp[i] == 0:
                    self._str += '.'
                elif self.comp[i] == 1:
                    self._str += 'X'
        #     self._str += ' '
        # self._str = self._str[:-1]

    def __str__(self):
        return self._str

    def check(self, line: np.ndarray, turn):
        # print(line * self.mul == self.comp)
        # print(line * self.mul)
        return np.all(line * self.mul == self.comp * turn) or \
               np.all(np.flip(line) * self.mul == self.comp * turn)

    @staticmethod
    def from_str(pattern):
        mul = np.zeros((9,), dtype=np.int)
        comp = np.zeros((9,), dtype=np.int)
        for i in range(9):
            if pattern[i] != '?':
                mul[i] = 1
                if pattern[i] == 'X':
                    comp[i] = 1
        return _Checker(mul, comp)


class _LineChecker:
    checker: List[_Checker]

    def check(self, lines, turn=1):
        cnt = 0
        for line in lines:
            for checker in self.checker:
                if checker.check(line, turn):
                    print(checker)
                    cnt += 1
                    break
        return cnt


class ThreeChecker(_LineChecker):
    checker = [
        _Checker.from_str('???.XX.X.'),
        _Checker.from_str('???.X.XX.'),
        _Checker.from_str('???.XXX..'),
        _Checker.from_str('??..XXX.?'),

        _Checker.from_str('??.XXX..?'),
        _Checker.from_str('??.XX.X.?'),
        _Checker.from_str('?.X.XX.??'),
    ]


class FourChecker(_LineChecker):
    checker = [
        _Checker.from_str('???.XXXX?'),
        _Checker.from_str('??.XXXX??'),
        _Checker.from_str('????XXXX.'),
        _Checker.from_str('???XXXX.?'),

        _Checker.from_str('????XX.XX'),
        _Checker.from_str('???XX.XX?'),
    ]


class FiveChecker(_LineChecker):
    checker = [
        _Checker.from_str('????XXXXX'),
        _Checker.from_str('???XXXXX?'),
        _Checker.from_str('??XXXXX??'),
    ]


class SixChecker(_LineChecker):
    checker = [
        _Checker.from_str('???XXXXXX'),
        _Checker.from_str('??XXXXXX?'),
    ]


ThreeChecker = ThreeChecker()
FourChecker = FourChecker()
FiveChecker = FiveChecker()
SixChecker = SixChecker()

