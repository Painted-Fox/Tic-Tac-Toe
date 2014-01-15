from flask import Flask, render_template, request, jsonify
from yaktak.board import Board

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wopr/move', methods = ['POST'])
def move():
    grid = request.get_json()
    board = Board(grid)
    return jsonify(board.grid)
