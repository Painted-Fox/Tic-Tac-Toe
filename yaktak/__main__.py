from board import Board

if __name__ == '__main__':
    board = Board()
    print(board)
    board.xmove(0,0)
    board.omove(1,2)
    print(board)
    board.xmove(2,1)
    print(board)
