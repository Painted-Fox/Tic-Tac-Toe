from flask import Flask, render_template, request, jsonify
from yaktak.board import Board

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wopr/move', methods = ['POST'])
def move():
    """
    (2,0) # (2,1) # (2,2)
    #####################
    (1,0) # (1,1) # (1,2)
    #####################
    (0,0) # (0,1) # (0,2)
    """
    grid = request.get_json()
    board = Board(grid)
    return jsonify(board.grid)
