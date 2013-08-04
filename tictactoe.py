# Our game board.
# 0 = the space is not filled.
# 1 = x
# 2 = o
board = [[0,0,0],
        [0,0,0],
        [0,0,0]]

def _move(x, y, num):
    board[y][x] = num

def xmove(x, y):
    _move(x, y, 1)

def omove(x, y):
    _move(x, y, 2)

def display():
    print str.format(
            '{0} | {1} | {2}',
            getSymbol(board[0][0]),
            getSymbol(board[0][1]),
            getSymbol(board[0][2]))
    print '---------'
    print str.format(
            '{0} | {1} | {2}',
            getSymbol(board[1][0]),
            getSymbol(board[1][1]),
            getSymbol(board[1][2]))
    print '---------'
    print str.format(
            '{0} | {1} | {2}',
            getSymbol(board[2][0]),
            getSymbol(board[2][1]),
            getSymbol(board[2][2]))
    print ''

def getSymbol(num):
    symbol = ' '
    if (num == 1):
        symbol = 'X'
    elif (num == 2):
        symbol = 'O'
    return symbol

display()
xmove(0,0)
omove(1,2)
display()
xmove(2,1)
display()
