"""Provides the artificial intelligence for the computer player."""

import random
from copy import deepcopy
from yaktak.board import Board

def move(board):
    """Request a move from the wopr"""

    if isinstance(board, Board) == False:
        raise TypeError("The board provided is not a recognized type.")

    # If we are O, always take center if we can.
    if board.turn() == -1 and board.grid[1][1] == 0:
        return (1, 1)

    wopr_move = (_take_win(board) or
            _take_defense(board) or
            _take_double_threat(board) or
            _take_opposite_corner(board) or
            _defend_double_threat(board) or
            _take_free_corner(board) or
            _take_center(board) or
            _take_any(board))

    return wopr_move

def _take_free_corner(board):
    """
    An aggressive strategy is to take a corner.  Choose a random corner for fun.
    Returns None if no corner is available.
    """

    corners = []
    if board.empty(0, 0):
        corners.append((0, 0))

    if board.empty(2, 0):
        corners.append((2, 0))

    if board.empty(0, 2):
        corners.append((0, 2))

    if board.empty(2, 2):
        corners.append((2, 2))


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
    if board.get(0, 0) == myturn and board.empty(2, 2):
        return (2, 2)
    elif board.get(2, 2) == myturn and board.empty(0, 0):
        return (0, 0)
    elif board.get(2, 0) == myturn and board.empty(0, 2):
        return (0, 2)
    elif board.get(0, 2) == myturn and board.empty(2, 0):
        return (2, 0)
    else:
        return None

def _take_double_threat(board):
    """
    Make a move that creates a double threat to the player.  We're guaranteed to
    win next turn if we can make this move.
    Returns None if unavailable.
    """

    # Who's turn am I playing for?
    myturn = board.turn()

    if board.get(0, 0) == myturn and board.get(2, 2) == myturn:
        if board.empty(0, 1) and board.empty(0, 2) and board.empty(1, 2):
            return (0, 2)
        elif board.empty(1, 0) and board.empty(2, 0) and board.empty(2, 1):
            return (2, 0)

    elif board.get(0, 2) == myturn and board.get(2, 0) == myturn:
        if board.empty(0, 1) and board.empty(0, 0) and board.empty(1, 0):
            return (0, 0)
        elif board.empty(2, 1) and board.empty(2, 2) and board.empty(1, 2):
            return (2, 2)

    return None

def _take_center(board):
    """
    A defensive strategy is to take the center.
    Returns None if unavailable.
    """

    if board.empty(1, 1):
        return (1, 1)
    else:
        return None

def _take_win(board):
    """
    Take the winning move.
    Returns None if unavailable.
    """

    # Who's turn am I playing for?
    myturn = board.turn()

    for i in range(0, 3):
        for j in range(0, 3):
            if board.empty(i, j):
                # Copy the board and see if we can make a winning move here.
                # This might not be the most efficient solution, but it's
                # straightforward.
                simulation = Board(grid=deepcopy(board.grid))
                simulation.move(i, j, myturn)
                if simulation.winner() == myturn:
                    return (i, j)

    return None

def _take_defense(board):
    """
    Prevent the opponent from winning.
    Returns None if unnecessary.
    """

    # Who's turn am I playing for?
    myturn = board.turn()
    opponent = -(myturn)

    for i in range(0, 3):
        for j in range(0, 3):
            if board.empty(i, j):
                # Copy the board and see if we can make a winning move here.
                # This might not be the most efficient solution, but it's
                # straightforward.
                simulation = Board(grid=deepcopy(board.grid))

                # Cheat so we can see if we can find a position where the
                # opponent wins without taking our own turn.  This avoids
                # an extra layer of loops.
                simulation.grid[i][j] = opponent

                # If the opponent can win here, move to this location so
                # that we prevent our opponent from winning.
                if simulation.winner() == opponent:
                    return (i, j)

    return None

def _take_any(board):
    """
    Take any free space at random.
    """

    available = []
    for i in range(0, 3):
        for j in range(0, 3):
            if board.empty(i, j):
                available.append((i, j))

    if len(available) == 0:
        return None

    return available[random.randint(0, len(available) - 1)]

def _defend_double_threat(board):
    """
    Prevent a double threat scenario.
    TODO: Find a cleaner way to do this.
    """

    myturn = board.turn()
    opponent = -(myturn)
    threat = False

    # Double threat coming from corners
    if (board.grid[0][0] == opponent and
        board.grid[2][2] == opponent and
        board.grid[2][0] == 0 and
        board.grid[0][2] == 0) or (
        board.grid[2][0] == opponent and
        board.grid[0][2] == opponent and
        board.grid[0][0] == 0 and
        board.grid[2][2] == 0):

        threat = True

    # Double threat coming from a corner and a side
    elif (board.grid[0][0] == opponent and (
            board.grid[1][2] == opponent or
            board.grid[2][1] == opponent)) or (
        board.grid[2][0] == opponent and (
            board.grid[0][1] == opponent or
            board.grid[1][2] == opponent)) or (
        board.grid[2][2] == opponent and (
            board.grid[1][0] == opponent or
            board.grid[0][1] == opponent)) or (
        board.grid[0][2] == opponent and (
            board.grid[1][0] == opponent or
            board.grid[2][1] == opponent)):

        threat = True


    if threat:
        if board.grid[1][0] == 0 and board.grid[1][2] == 0:
            return (1, 0)

        if board.grid[2][1] == 0 and board.grid[0][1] == 0:
            return (0, 1)


    # Double threat coming from two sides
    if (board.grid[1][0] == opponent and board.grid[0][1] and
            board.grid[0][0] == 0 and
            board.grid[2][0] == 0 and
            board.grid[0][2] == 0):
        return (0, 0)
    elif (board.grid[1][0] == opponent and board.grid[2][1] and
            board.grid[0][0] == 0 and
            board.grid[2][0] == 0 and
            board.grid[2][2] == 0):
        return (2, 0)
    elif (board.grid[1][2] == opponent and board.grid[2][1] and
            board.grid[2][0] == 0 and
            board.grid[0][2] == 0 and
            board.grid[2][2] == 0):
        return (2, 2)
    elif (board.grid[1][2] == opponent and board.grid[0][1] and
            board.grid[0][0] == 0 and
            board.grid[0][2] == 0 and
            board.grid[2][2] == 0):
        return (0, 2)


    return None
