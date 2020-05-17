from Gomoku.lib import *
from Gomoku.game import Game


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



