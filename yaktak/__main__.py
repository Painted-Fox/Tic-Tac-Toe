from board import Board

if __name__ == '__main__':
    board = Board()
    print(board)
    board.xmove(0,0)
    board.omove(1,2)
    print(board)
    board.xmove(2,1)
    print(board)
    print(board.winner())
    board.omove(1,1)
    board.xmove(2,2)
    board.omove(1,0)
    print(board)
    print(board.winner())

    b2 = Board()
    b2.xmove(0,2)
    b2.xmove(1,1)
    b2.xmove(2,0)
    print(b2)
    print(b2.winner())
