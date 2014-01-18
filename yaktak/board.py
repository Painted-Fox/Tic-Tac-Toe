"""
Provides the Board class, which models the Tic-Tac-Toe game board.
"""

from yaktak.exceptions import GameOverError, SpaceTakenError, WrongTurnError

def get_symbol(num):
    """Convert the numeric representation to the character representation."""
    symbol = ' '
    if num == 1:
        symbol = 'X'
    elif num == -1:
        symbol = 'O'
    return symbol

class Board:
    """Our tic-tac-toe game board.

    Coordinate map:

    (2,0) # (2,1) # (2,2)
    #####################
    (1,0) # (1,1) # (1,2)
    #####################
    (0,0) # (0,1) # (0,2)
    """

    def __init__(self, grid = None):

        if grid is not None and (
            len(grid) != 3 or
            len(grid[0]) != 3 or
            len(grid[1]) != 3 or
            len(grid[2]) != 3):

            raise IndexError("The board must have a 3x3 grid.")

        # 0 = the space is not filled.
        # 1 = x
        # -1 = o
        self.grid = grid or [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def move(self, x_pos, y_pos, num):
        """Make a move for the specified player (represented numerically)."""
        if num > 1 or num < -1 or num == 0:
            raise ValueError(
                str.format("num can only be 1 or -1. Got: {0}", num))

        if x_pos > 2 or y_pos > 2 or x_pos < 0 or y_pos < 0:
            raise IndexError(
                str.format(
                    "The x and y coordinates can be from (0, 0) to (2, 2). "
                    "Got: ({0}, {1})", x_pos, y_pos))

        if not self.empty(x_pos, y_pos):
            raise SpaceTakenError(
                str.format(
                    "The space ({0}, {1}) is already taken", x_pos, y_pos))

        if self.winner() != 0:
            raise GameOverError("The game is over.  You cannot move.")

        if self.turn() != num:
            raise WrongTurnError("It is not your turn to move.")

        self.grid[x_pos][y_pos] = num

    def empty(self, x_pos, y_pos):
        """Test if the position empty."""
        return self.get(x_pos, y_pos) == 0

    def get(self, x_pos, y_pos):
        """Get the value at a position."""
        return self.grid[x_pos][y_pos]

    def xmove(self, x_pos, y_pos):
        """Make a move for the X player."""
        self.move(x_pos, y_pos, 1)

    def omove(self, x_pos, y_pos):
        """Make a move for the O player."""
        self.move(x_pos, y_pos, -1)

    def turn(self):
        """Who's turn is it?  Returns 1, or -1."""

        moves = 0
        for i in range(0, 3):
            for j in range (0, 3):
                if self.get(i, j) != 0:
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
                rowsum += self.get(i, j)
                colsum += self.get(j, i)

            if rowsum == 3 or colsum == 3:
                return 1
            elif rowsum == -3 or colsum == -3:
                return -1

        # Check for diagonal cases
        diagsum1 = self.get(0, 0) + self.get(1, 1) + self.get(2, 2)
        diagsum2 = self.get(0, 2) + self.get(1, 1) + self.get(2, 0)

        if diagsum1 == 3 or diagsum2 == 3:
            return 1
        elif diagsum1 == -3 or diagsum2 == -3:
            return -1

        # No winner
        return 0

    def __repr__(self):
        """Represent the board as a string."""

        return str.format(
"""
{6} | {7} | {8}
---------
{3} | {4} | {5}
---------
{0} | {1} | {2}
""",
            get_symbol(self.get(0, 0)),
            get_symbol(self.get(0, 1)),
            get_symbol(self.get(0, 2)),
            get_symbol(self.get(1, 0)),
            get_symbol(self.get(1, 1)),
            get_symbol(self.get(1, 2)),
            get_symbol(self.get(2, 0)),
            get_symbol(self.get(2, 1)),
            get_symbol(self.get(2, 2)))
