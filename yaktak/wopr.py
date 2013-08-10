"""Provides the artificial intelligence for the computer player."""

import random
from yaktak.board import Board

def move(board):
    if isinstance(board, Board) == false:
        raise TypeError("The board provided is not a recognized type.")

def _take_free_corner(board):
    """
    An aggressive strategy is to take a corner.  Choose a random corner for fun.
    Returns None if no corner is available.
    """

    corners = []
    if board.empty(0,0):
        corners.append((0,0))

    if board.empty(2,0):
        corners.append((2,0))

    if board.empty(0,2):
        corners.append((0,2))

    if board.empty(2,2):
        corners.append((2,2))


    if len(corners) == 0:
        return None
    else:
        return corners[random.randint(0, len(corners) - 1)]

def _take_center(board):
    """
    A defensive strategy is to take the center.
    Returns None if unavailable.
    """

    if board.empty(1,1):
        return (1,1)
    else:
        return None

def _take_win(board):
    """
    Take the winning move.
    Returns None if unavailable.
    """
    pass

def _take_defense(board):
    """
    Prevent the opponent from winning.
    Returns None if unnecessary.
    """
    pass
