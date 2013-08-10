from unittest import TestCase

from yaktak.board import Board

class TestBoard(TestCase):
    def test_move(self):
        """Make sure X and O can make moves."""
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        self.assertEqual(board._board[0][0], 1, "X did not get on the board.")
        self.assertEqual(board._board[1][1], -1, "O did not get on the board.")

    def test_position(self):
        """Make sure we get on the right positions."""
        board = Board()
        board.xmove(2,1)
        board.omove(0,1)
        self.assertEqual(board._board[1][2], 1, "X in the wrong position.")
        self.assertEqual(board._board[1][0], -1, "O in the wrong position.")

    def test_whos_turn(self):
        """Check who's turn is it."""
        board = Board()
        self.assertEqual(board.turn(), 1,
                str.format("Got {0}. Expected 1. Should be X's turn",
                    board.turn()))
        board.xmove(0,0)
        self.assertEqual(board.turn(), -1,
                str.format("Got {0}. Expected -1. Should be O's turn",
                    board.turn()))
        board.omove(1,1)
        self.assertEqual(board.turn(), 1,
                str.format("Got {0}. Expected 1. Should be X's turn",
                    board.turn()))

    def test_bogus_move(self):
        """Make sure we raise an exception if we make a bogus move."""

        board = Board()

        with self.assertRaises(ValueError):
            board._move(0, 0, 0)
        with self.assertRaises(ValueError):
            board._move(0, 0, 2)
        with self.assertRaises(ValueError):
            board._move(0, 0, -2)

    def test_move_off_board(self):
        """Make sure we can't make a move that's off the board."""

        board = Board()

        with self.assertRaises(IndexError):
            board.xmove(-1, 0)
        with self.assertRaises(IndexError):
            board.xmove(0, -1)
        with self.assertRaises(IndexError):
            board.xmove(3, 0)
        with self.assertRaises(IndexError):
            board.xmove(0, 3)
