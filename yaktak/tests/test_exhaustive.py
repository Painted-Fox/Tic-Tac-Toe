"""
Tests the WOPR against an exhaustive player.
"""

from unittest import TestCase
from copy import deepcopy

from yaktak.board import Board
from yaktak import wopr

class ExhaustivePlayer(TestCase):
    """Exhaustive Player."""

    def exhaust(self, player, board):
        if player == board.winner():
            # Exhaustive player won against the player.
            return board
        if board.winner() != 0 or board.draw():
            # The WOPR has won or successfully created a draw.
            return None

        for i in range(0, 3):
            for j in range(0, 3):
                # Skip taken fields.
                if board.grid[i][j] != 0:
                    continue

                # Create copies of the board
                b = Board(grid=deepcopy(board.grid))
                # Make our move
                b.move(i, j, player)

                # Did we win?
                if player == b.winner():
                    return b

                # Did we reach a draw?
                if b.draw():
                    return None

                # Let the WOPR play.
                wopr_move = wopr.move(b)
                b.move(wopr_move[0], wopr_move[1], b.turn())

                # Recurse into the new board state.
                result = self.exhaust(player, b)
                if result is not None:
                    return result

    def test_exhaust_x(self):
        """Determine if we can win by playing X."""

        result = self.exhaust(1, Board())

        self.assertIsNone(result)
