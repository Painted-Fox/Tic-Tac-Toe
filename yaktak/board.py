from yaktak.exceptions import GameOverError, SpaceTakenError, WrongTurnError

class Board:
    """Our tic-tac-toe game board."""

    def __init__(self):
        # 0 = the space is not filled.
        # 1 = x
        # -1 = o
        self.grid = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def _move(self, x, y, num):
        if num > 1 or num < -1 or num == 0:
            raise ValueError(str.format("num can only be 1 or -1. Got: {0}", num))

        if x > 2 or y > 2 or x < 0 or y < 0:
            raise IndexError(
                str.format("The x and y coordinates can be from (0, 0) to (2,2). Got: ({0},{1})", x, y))

        if not self.empty(x, y):
            raise SpaceTakenError(
                    str.format("The space ({0}, {1}) is already taken", x, y))

        if self.winner() != 0:
            raise GameOverError("The game is over.  You cannot move.")

        self.grid[y][x] = num

    def empty(self, x, y):
        return self.grid[y][x] == 0

    def xmove(self, x, y):
        if self.turn() != 1:
            raise WrongTurnError("It is not X's turn to move.")

        self._move(x, y, 1)

    def omove(self, x, y):
        if self.turn() != -1:
            raise WrongTurnError("It is not O's turn to move.")

        self._move(x, y, -1)

    def getSymbol(self, num):
        symbol = ' '
        if num == 1:
            symbol = 'X'
        elif num == -1:
            symbol = 'O'
        return symbol

    def turn(self):
        """Who's turn is it?  Returns 1, or -1."""

        moves = 0
        for i in range(0, 3):
            for j in range (0, 3):
                if self.grid[i][j] != 0:
                    moves = moves + 1

        if moves % 2 == 0:
            return 1
        else:
            return -1

    def winner(self):
        """Do we have a winner?  Returns 0, 1, or -1."""

        # Check horizontal and vertical cases
        for i in range(0, 3):
            rowsum = 0
            colsum = 0
            for j in range(0, 3):
                rowsum += self.grid[i][j]
                colsum += self.grid[j][i]

            if rowsum == 3 or colsum == 3:
                return 1
            elif rowsum == -3 or colsum == -3:
                return -1

        # Check for diagonal cases
        diagsum1 = self.grid[0][0] + self.grid[1][1] + self.grid[2][2]
        diagsum2 = self.grid[0][2] + self.grid[1][1] + self.grid[2][0]

        if diagsum1 == 3 or diagsum2 == 3:
            return 1
        elif diagsum1 == -3 or diagsum2 == -3:
            return -1

        # No winner
        return 0

    def __repr__(self):
        return str.format(
"""
{6} | {7} | {8}
---------
{3} | {4} | {5}
---------
{0} | {1} | {2}
""",
            self.getSymbol(self.grid[0][0]),
            self.getSymbol(self.grid[0][1]),
            self.getSymbol(self.grid[0][2]),
            self.getSymbol(self.grid[1][0]),
            self.getSymbol(self.grid[1][1]),
            self.getSymbol(self.grid[1][2]),
            self.getSymbol(self.grid[2][0]),
            self.getSymbol(self.grid[2][1]),
            self.getSymbol(self.grid[2][2]))

