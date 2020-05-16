from Gomoku.lib import *
from Gomoku.Game import Game
from Gomoku.ForbiddenChecker import _LineChecker


game = Game()
# game.show()
game.put(2, 3, 1)
game.put(3, 3, 1)
game.put(4, 3, 1)
game.put(1, 1, 1)
game.put(4, 4, 1)

game.put(2, 4, 2)
# game.put(4, 4, 2)
# game.put(1, 3, 2)
game.show()
game.check_forbidden(3, 3)


# check = Checker(
#     vector(0, 0, 1, 1, 1, 1, 1, 1, 0),
#     vector(0, 0, 0, 1, 1, 0, 1, 0, 0)
# )
# check = Checker.from_str('??.XX.X.?')
# print(check)
#
# print(check.check(vector(2, 2, 0, 1, 1, 0, 1, 0, 0), 1))
# print(check.check(vector(2, 2, 2, 1, 1, 0, 1, 0, 0), 1))
# print(check.check(vector(-1, 0, 1, 0, 1, 1, 0, 2, -1), 1))

