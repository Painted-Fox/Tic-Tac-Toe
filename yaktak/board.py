class Board:
    """Our tic-tac-toe game board."""

    def __init__(self):
        # 0 = the space is not filled.
        # 1 = x
        # -1 = o
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def _move(self, x, y, num):
        if (num > 1 or num < -1 or num == 0):
            raise ValueError('num can only be 1 or -1.')

        self.board[y][x] = num

    def xmove(self, x, y):
        self._move(x, y, 1)

    def omove(self,x, y):
        self._move(x, y, -1)

    def getSymbol(self, num):
        symbol = ' '
        if num == 1:
            symbol = 'X'
        elif num == -1:
            symbol = 'O'
        return symbol

    def winner(self):
        """Do we have a winner?  Returns 0, 1, or -1."""

        # Check horizontal and vertical cases
        for i in range(0, 3):
            rowsum = 0
            colsum = 0
            for j in range(0, 3):
                rowsum += self.board[i][j]
                colsum += self.board[j][i]

            if rowsum == 3 or colsum == 3:
                return 1
            elif rowsum == -3 or colsum == -3:
                return -1

        # Check for diagonal cases
        diagsum1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
        diagsum2 = self.board[0][2] + self.board[1][1] + self.board[2][0]

        if diagsum1 == 3 or diagsum2 == 3:
            return 1
        elif diagsum2 == -3 or diagsum2 == -3:
            return -1

        # No winner
        return 0

    def __repr__(self):
        return str.format(
'''
{6} | {7} | {8}
---------
{3} | {4} | {5}
---------
{0} | {1} | {2}
''',
            self.getSymbol(self.board[0][0]),
            self.getSymbol(self.board[0][1]),
            self.getSymbol(self.board[0][2]),
            self.getSymbol(self.board[1][0]),
            self.getSymbol(self.board[1][1]),
            self.getSymbol(self.board[1][2]),
            self.getSymbol(self.board[2][0]),
            self.getSymbol(self.board[2][1]),
            self.getSymbol(self.board[2][2]))

