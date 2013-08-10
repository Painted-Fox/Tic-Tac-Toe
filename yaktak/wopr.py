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

def _take_opposite_corner(board):
    """
    The second move of the aggressive strategy is to take the opposite corner of
    the one you already took.
    Returns None if unavailable.
    """

    # Who's turn am I playing for?
    myturn = board.turn()

    # Check what corner we already have and return the opposite corner.
    if board.get(0,0) == myturn and board.empty(2,2):
        return (2,2)
    elif board.get(2,2) == myturn and board.empty(0,0):
        return (0,0)
    elif board.get(2,0) == myturn and board.empty(0,2):
        return (0,2)
    elif board.get(0,2) == myturn and board.empty(2,0):
        return (2,0)
    else:
        return None

def _take_double_threat(board):
    """
    Make a move that creates a double threat to the player.  We're guranteed to
    win next turn if we can make this move.
    Returns None if unavailable.
    """

    # Who's turn am I playing for?
    myturn = board.turn()

    if board.get(0,0) == myturn and board.get(2,2) == myturn:
        if board.empty(0,1) and board.empty(0,2) and board.empty(1,2):
            return (0,2)
        elif board.empty(1,0) and board.empty(2,0) and board.empty(2,1):
            return (2,0)

    elif board.get(0,2) == myturn and board.get(2,0) == myturn:
        if board.empty(0,1) and board.empty(0,0) and board.empty(1,0):
            return (0,0)
        elif board.empty(2,1) and board.empty(2,2) and board.empty(1,2):
            return (2,2)

    return None

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
