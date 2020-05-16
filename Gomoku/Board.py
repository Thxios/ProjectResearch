
class Board:
    def __init__(self):
        self._board = [[0 for _ in range(15)] for _ in range(15)]

    def clear(self):
        self._board = [[0 for _ in range(15)] for _ in range(15)]

    def get(self, row, col):
        if 0 <= row < 15 and 0 <= col < 15:
            return self._board[row][col]
        return 0

    def check(self):
        """Check if there is a winner.
        Returns:
            0-no winner, 1-black wins, 2-white wins
        """
        board = self._board
        # check in 4 directions
        # a coordinate stands for a specific direction, imagine the direction of a coordinate
        # relative to the origin on xy-axis
        dirs = ((1, -1), (1, 0), (1, 1), (0, 1))
        for i in range(15):
            for j in range(15):
                # if no stone is on the position, don't need to consider this position
                if board[i][j] == 0:
                    continue
                # value-value at a coord, i-row, j-col
                value = board[i][j]
                # check if there exist 5 in a line
                for d in dirs:
                    x, y = i, j
                    count = 0
                    for _ in range(5):
                        if self.get(x, y) != value:
                            break
                        x += d[0]
                        y += d[1]
                        count += 1
                    # if 5 in a line, store positions of all stones, return value
                    if count == 5:
                        # self.won = {}
                        # r, c = i, j
                        # for _ in range(5):
                        #     self.won[(r, c)] = 1
                        #     r += d[0]
                        #     c += d[1]
                        return value
        return 0

    def board(self):
        """Return the board array."""
        return self._board

