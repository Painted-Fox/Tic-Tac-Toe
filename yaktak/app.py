from flask import Flask, render_template, request, jsonify
from yaktak.board import Board
from yaktak import wopr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wopr/move', methods = ['POST'])
def move():
    grid = request.get_json()
    print grid
    board = Board(grid)
    move = wopr.move(board)
    board.move(move[0], move[1], board.turn())
    print board.grid

    return jsonify({ "move" : move, "grid" : board.grid })
