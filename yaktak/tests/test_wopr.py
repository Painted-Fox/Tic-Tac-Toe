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

    def test_take_opposite_corner_x_unavailable(self):
        """X tries to take a on opposite corner, but there is none."""
        board = Board()
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_opposite_corner_x_0_0(self):
        """X takes the corner opposite of (0,0)"""
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (2,2))

    def test_take_opposite_corner_x_2_2(self):
        """X takes the corner opposite of (2,2)"""
        board = Board()
        board.xmove(2,2)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (0,0))

    def test_take_opposite_corner_x_0_2(self):
        """X takes the corner opposite of (0,2)"""
        board = Board()
        board.xmove(0,2)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (2,0))

    def test_take_opposite_corner_x_2_0(self):
        """X takes the corner opposite of (2,0)"""
        board = Board()
        board.xmove(2,0)
        board.omove(1,1)
        move = wopr._take_opposite_corner(board)
        self.assertEqual(move, (0,2))

    def test_take_opposite_corner_o_unavailable_0_0(self):
        """O tries to take a on opposite corner, X is already at (0,0)."""
        board = Board()
        board.xmove(0,0)
        board.omove(2,2)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_opposite_corner_o_unavailable_2_2(self):
        """O tries to take a on opposite corner, X is already at (2,2)."""
        board = Board()
        board.xmove(2,2)
        board.omove(0,0)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_opposite_corner_o_unavailable_0_2(self):
        """O tries to take a on opposite corner, X is already at (0,2)."""
        board = Board()
        board.xmove(0,2)
        board.omove(2,0)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_opposite_corner_o_unavailable_2_0(self):
        """O tries to take a on opposite corner, X is already at (2,0)."""
        board = Board()
        board.xmove(2,0)
        board.omove(0,2)
        move = wopr._take_opposite_corner(board)
        self.assertIsNone(move)

    def test_take_double_threat_unavailable(self):
        """There is no double threat move."""
        board = Board()
        move = wopr._take_double_threat(board)
        self.assertIsNone(move)

    def test_take_double_threat_x_0_0_low(self):
        """X makes a double threat move starting at (0,0) and taking low."""
        board = Board()
        board.xmove(0,0)
        board.omove(1,0)
        board.xmove(2,2)
        board.omove(2,1)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (0,2))

    def test_take_double_threat_x_0_0_high(self):
        """X makes a double threat move starting at (0,0) and taking high."""
        board = Board()
        board.xmove(0,0)
        board.omove(0,1)
        board.xmove(2,2)
        board.omove(1,2)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (2,0))

    def test_take_double_threat_x_0_2_low(self):
        """X makes a double threat move starting at (0,2) and taking low."""
        board = Board()
        board.xmove(0,2)
        board.omove(2,1)
        board.xmove(2,0)
        board.omove(1,2)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (0,0))

    def test_take_double_threat_x_0_2_high(self):
        """X makes a double threat move starting at (0,2) and taking high."""
        board = Board()
        board.xmove(0,2)
        board.omove(0,1)
        board.xmove(2,0)
        board.omove(1,0)
        move = wopr._take_double_threat(board)
        self.assertEqual(move, (2,2))

    def test_take_win_unavailable(self):
        """The winning move should be unavailable."""
        board = Board()
        move = wopr._take_win(board)
        self.assertIsNone(move)

    def test_take_win_x_vert(self):
        """X can win vertically."""
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        board.xmove(0,1)
        board.omove(1,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

    def test_take_win_o_vert(self):
        """O can win vertically."""
        board = Board()
        board.xmove(1,1)
        board.omove(0,0)
        board.xmove(1,2)
        board.omove(0,1)
        board.xmove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

    def test_take_win_x_horiz(self):
        """X can win horizontally."""
        board = Board()
        board.xmove(0,0)
        board.omove(1,1)
        board.xmove(1,0)
        board.omove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,0))

    def test_take_win_o_horiz(self):
        """O can win horizontally."""
        board = Board()
        board.xmove(1,1)
        board.omove(0,0)
        board.xmove(1,2)
        board.omove(1,0)
        board.xmove(2,2)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,0))

    def test_take_win_x_diag1(self):
        """X can win diagonally for first pattern."""
        board = Board()
        board.xmove(0,0)
        board.omove(0,1)
        board.xmove(1,1)
        board.omove(1,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,2))

    def test_take_win_o_diag1(self):
        """O can win diagonally for first pattern."""
        board = Board()
        board.xmove(1,0)
        board.omove(0,0)
        board.xmove(0,1)
        board.omove(1,1)
        board.xmove(2,1)
        move = wopr._take_win(board)
        self.assertEqual(move, (2,2))

    def test_take_win_x_diag1(self):
        """X can win diagonally for second pattern."""
        board = Board()
        board.xmove(2,0)
        board.omove(0,0)
        board.xmove(1,1)
        board.omove(1,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))

    def test_take_win_o_diag1(self):
        """O can win diagonally for second pattern."""
        board = Board()
        board.xmove(0,1)
        board.omove(2,0)
        board.xmove(1,0)
        board.omove(1,1)
        board.xmove(0,0)
        move = wopr._take_win(board)
        self.assertEqual(move, (0,2))
