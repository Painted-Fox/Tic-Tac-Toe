from unittest import TestCase

from yaktak import wopr
from yaktak.board import Board

class TestWopr(TestCase):
    def test_take_free_corner(self):
        """Test if the WOPR can take a free corner correctly."""

        board = Board()
        move = wopr._take_free_corner(board)
        self.assertIn(move, [(0,0),(2,0),(0,2),(2,2)])

        board = Board()
        board.xmove(0,0)
        move = wopr._take_free_corner(board)
        self.assertIn(move, [(2,0),(0,2),(2,2)])

        board = Board()
        board.xmove(0,0)
        board.omove(2,0)
        move = wopr._take_free_corner(board)
        self.assertIn(move, [(0,2),(2,2)])

        board = Board()
        board.xmove(0,0)
        board.omove(2,0)
        board.xmove(0,2)
        move = wopr._take_free_corner(board)
        self.assertIn(move, [(2,2)])

        board = Board()
        board.xmove(0,0)
        board.omove(2,0)
        board.xmove(0,2)
        board.omove(2,2)
        move = wopr._take_free_corner(board)
        self.assertIsNone(move)

    def test_take_center(self):
        """Test if the WOPR can take the center."""

        board = Board()
        self.assertEqual(wopr._take_center(board), (1,1))

        board = Board()
        board.xmove(1,1)
        self.assertIsNone(wopr._take_center(board))

    def test_take_opposite_corner(self):
        """See if WOPR can take a corner opposite to the one already taken."""

        board = Board()
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (2,2))

        board = Board()
        board.xmove(2,2)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (0,0))

        board = Board()
        board.xmove(0,2)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (2,0))

        board = Board()
        board.xmove(2,0)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (0,2))

        board = Board()
        board.xmove(0,0)
        board.omove(2,2)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

        board = Board()
        board.xmove(2,2)
        board.omove(0,0)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

        board = Board()
        board.xmove(0,2)
        board.omove(2,0)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

        board = Board()
        board.xmove(2,0)
        board.omove(0,2)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_double_threat(self):
        """See if WOPR can make a double threat move."""

        board = Board()
        move = wopr._take_double_threat(board)
        self.assertIsNone(move)

        board = Board()
        board.xmove(0,0)
        board.omove(1,0)
        board.xmove(2,2)
        board.omove(2,1)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (0,2))

        board = Board()
        board.xmove(0,0)
        board.omove(0,1)
        board.xmove(2,2)
        board.omove(1,2)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (2,0))

        board = Board()
        board.xmove(0,2)
        board.omove(2,1)
        board.xmove(2,0)
        board.omove(1,2)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (0,0))

        board = Board()
        board.xmove(0,2)
        board.omove(0,1)
        board.xmove(2,0)
        board.omove(1,0)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (2,2))

    def test_take_win(self):
        """See if the WOPR will take a winning move if one is available."""
        board = Board()
        move = wopr._take_win(board)
        self.assertIsNone(move)

        # Vertical Win for X
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        board.xmove(0,1)
        board.omove(1,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

        # Vertial Win for O
        board = Board()
        board.xmove(1,1)
        board.omove(0,0)
        board.xmove(1,2)
        board.omove(0,1)
        board.xmove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

        # Horizontal Win for X
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        board.xmove(1,0)
        board.omove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,0))

        # Horizontal Win for O
        board = Board()
        board.xmove(1,1)
        board.omove(0,0)
        board.xmove(1,2)
        board.omove(1,0)
        board.xmove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,0))

        # Diagonal 1 for X
        board = Board()
        board.xmove(0,0)
        board.omove(0,1)
        board.xmove(1,1)
        board.omove(1,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,2))

        # Diagonal 1 for O
        board = Board()
        board.xmove(1,0)
        board.omove(0,0)
        board.xmove(0,1)
        board.omove(1,1)
        board.xmove(2,1)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,2))

        # Diagonal 2 for X
        board = Board()
        board.xmove(2,0)
        board.omove(0,0)
        board.xmove(1,1)
        board.omove(1,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

        # Diagonal 2 for O
        board = Board()
        board.xmove(0,1)
        board.omove(2,0)
        board.xmove(1,0)
        board.omove(1,1)
        board.xmove(0,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))
