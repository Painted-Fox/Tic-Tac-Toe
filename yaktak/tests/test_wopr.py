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
