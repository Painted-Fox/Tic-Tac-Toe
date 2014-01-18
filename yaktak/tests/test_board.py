"""
Tests for the game board model.
"""

from unittest import TestCase

from yaktak.board import Board
from yaktak.exceptions import GameOverError, SpaceTakenError, WrongTurnError

class TestBoard(TestCase):
    """Board tests."""

    def test_move(self):
        """Make sure X and O can make moves."""
        board = Board()
        board.xmove(0, 0)
        board.omove(1, 1)
        self.assertEqual(board.grid[0][0], 1, "X did not get on the board.")
        self.assertEqual(board.grid[1][1], -1, "O did not get on the board.")

    def test_position(self):
        """Make sure we get on the right positions."""
        board = Board()
        board.xmove(2, 1)
        board.omove(0, 1)
        self.assertEqual(board.grid[2][1], 1, "X in the wrong position.")
        self.assertEqual(board.grid[0][1], -1, "O in the wrong position.")

    def test_whos_turn(self):
        """Check who's turn is it."""
        board = Board()
        self.assertEqual(board.turn(), 1,
                str.format("Got {0}. Expected 1. Should be X's turn",
                    board.turn()))
        board.xmove(0, 0)
        self.assertEqual(board.turn(), -1,
                str.format("Got {0}. Expected -1. Should be O's turn",
                    board.turn()))
        board.omove(1, 1)
        self.assertEqual(board.turn(), 1,
                str.format("Got {0}. Expected 1. Should be X's turn",
                    board.turn()))

    def test_bogus_move(self):
        """Make sure we raise an exception if we make a bogus move."""
        board = Board()

        with self.assertRaises(ValueError):
            board.move(0, 0, 0)
        with self.assertRaises(ValueError):
            board.move(0, 0, 2)
        with self.assertRaises(ValueError):
            board.move(0, 0, -2)

    def test_move_offgrid(self):
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

    def test_move_to_taken_space(self):
        """Make sure we can't move into a space that's already taken."""
        board = Board()
        board.xmove(0, 0)
        board.omove(1, 1)

        with self.assertRaises(SpaceTakenError):
            board.xmove(0, 0)

    def test_wrong_turn(self):
        """Make sure we can't move on the wrong turn."""
        board = Board()
        with self.assertRaises(WrongTurnError):
            board.omove(0, 0)

        board.xmove(0, 0)
        with self.assertRaises(WrongTurnError):
            board.xmove(1, 1)

    def test_x_win_vertical(self):
        """Check win detection for X in vertical pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 2)
        self.assertEqual(board.winner(), 1)

    def test_x_win_horizontal(self):
        """Check win detection for X in horizontal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 2)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 0)
        self.assertEqual(board.winner(), 1)

    def test_x_win_diag1(self):
        """Check win detection for X in first diagonal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 2)
        self.assertEqual(board.winner(), 1)

    def test_x_win_diag2(self):
        """Check win detection for X in second diagonal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 0)
        self.assertEqual(board.winner(), 1)

    def test_o_win_vertical(self):
        """Check win detection for O in vertical pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 2)
        self.assertEqual(board.winner(), -1)

    def test_o_win_horizontal(self):
        """Check win detection for O in horizontal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(2, 0)
        self.assertEqual(board.winner(), -1)

    def test_o_win_diag1(self):
        """Check win detection for O in first diagonal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 0)
        self.assertEqual(board.winner(), 0)
        board.xmove(0, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(2, 2)
        self.assertEqual(board.winner(), -1)

    def test_o_win_diag2(self):
        """Check win detection for O in second diagonal pattern."""
        board = Board()
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 2)
        self.assertEqual(board.winner(), 0)
        board.omove(0, 2)
        self.assertEqual(board.winner(), 0)
        board.xmove(2, 1)
        self.assertEqual(board.winner(), 0)
        board.omove(1, 1)
        self.assertEqual(board.winner(), 0)
        board.xmove(1, 0)
        self.assertEqual(board.winner(), 0)
        board.omove(2, 0)
        self.assertEqual(board.winner(), -1)

    def test_move_after_win(self):
        """Check an error is raised when we try to play a game that's over."""
        board = Board()
        board.xmove(0, 0)
        board.omove(1, 0)
        board.xmove(0, 1)
        board.omove(1, 1)
        board.xmove(0, 2)

        with self.assertRaises(GameOverError):
            board.omove(1, 2)
