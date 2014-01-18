#!/usr/bin/env python
"""
Provides the web application routing and controller logic.
"""

from flask import Flask, render_template, request, jsonify
from yaktak.board import Board
from yaktak import wopr

APP = Flask(__name__)

@APP.route('/')
def index():
    """ Present the user with the interface. """
    return render_template('index.html')

@APP.route('/wopr/move', methods = ['POST'])
def move():
    """Handle a request for the WOPR ai to make a move."""
    grid = request.get_json()
    board = Board(grid)
    wopr_move = (-1, -1)
    if board.winner() == 0:
        wopr_move = wopr.move(board)
        board.move(wopr_move[0], wopr_move[1], board.turn())

    return jsonify({
        "move" : wopr_move,
        "grid" : board.grid,
        "winner" : board.winner() })
