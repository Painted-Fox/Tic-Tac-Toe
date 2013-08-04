class Board:
    """Our tic-tac-toe game board."""

    def __init__(self):
        # 0 = the space is not filled.
        # 1 = x
        # 2 = o
        self.board = [[0,0,0],
                      [0,0,0],
                      [0,0,0]]

    def _move(self, x, y, num):
        self.board[y][x] = num

    def xmove(self, x, y):
        self._move(x, y, 1)

    def omove(self,x, y):
        self._move(x, y, 2)

    def getSymbol(self, num):
        symbol = ' '
        if (num == 1):
            symbol = 'X'
        elif (num == 2):
            symbol = 'O'
        return symbol

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

