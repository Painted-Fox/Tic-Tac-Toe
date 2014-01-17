/* global $ */
$(document).ready(function() {
    var winner = 0,
        boardFields = [
            [$('#field-20'), $('#field-21'), $('#field-22')],
            [$('#field-10'), $('#field-11'), $('#field-12')],
            [$('#field-00'), $('#field-01'), $('#field-02')]
        ],
        // Gets the grid into array format from the DOM elements.
        getGrid = function() {
            var grid = [[],[],[]],
                x, y;
            for (y = 0; y < 3; y++) {
                for (x = 0; x < 3; x++) {
                    if ($(boardFields[y][x]).hasClass('x')) {
                        grid[y][x] = 1;
                    } else if ($(boardFields[y][x]).hasClass('o')) {
                        grid[y][x] = -1;
                    } else {
                        grid[y][x] = 0;
                    }
                }
            }
            return grid;
        },
        // Sets the DOM elements to match a grid array representation.
        setGrid = function(grid) {
            var x, y;
            if (grid.length != 3 ||
                grid[0].length != 3 ||
                grid[1].length != 3 ||
                grid[2].length != 3) {
                    throw "Invalid grid.";
            }

            for (y = 0; y < 3; y++) {
                for (x = 0; x < 3; x++) {
                    $(boardFields[y][x])
                        .removeClass('x')
                        .removeClass('o');
                    if (grid[y][x] == 1) {
                        $(boardFields[y][x]).addClass('x');
                    } else if (grid[y][x] == -1) {
                        $(boardFields[y][x]).addClass('o');
                    }
                }
            }
        },
        // Who's turn is it?  Returns 1 or -1.
        turn = function() {
            var grid = getGrid(), moves = 0, x, y;
            for (y = 0; y < 3; y++) {
                for (x = 0; x < 3; x++) {
                    if (grid[y][x] !== 0) {
                        moves++;
                    }
                }
            }

            if (moves % 2 === 0) {
                return 1;
            } else {
                return -1;
            }
        },
        // Resets the board.
        reset = function() {
            setGrid([[0,0,0],[0,0,0],[0,0,0]]);
            winner = 0;
            $('#msg').text('');
        },
        // Allows the player to skip a turn.
        skip = function() {
            aiMove();
        },
        disableUI = function() {
            $('button').attr('disabled', 'disabled');
        },
        enableUI = function() {
            $('button').removeAttr('disabled');
        },
        // Request a move from the AI.
        aiMove = function() {
            // Make sure the user can't use the interface while we wait for
            // a response.
            disableUI();

            // Handle the response from the AI.
            var success = function(data) {
                winner = data.winner;
                setGrid(data.grid);
                if (winner !== 0) {
                    if (winner > 0) {
                        $('#msg').text("Player X wins!");
                    } else {
                        $('#msg').text("Player O wins!");
                    }
                }
            };
            // Make sure we re-enable the UI.
            var complete = function() {
                enableUI();
            };
            $.ajax({
                url: '/wopr/move',
                type: 'POST',
                data: JSON.stringify(getGrid()),
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: success,
                complete: complete
            });
        },
        // Handle button mashing, I mean clicking.
        buttonClickHandler = function() {
            if (winner === 0 &&
                !$(this).hasClass('x') &&
                !$(this).hasClass('o'))
            {
                if (turn() > 0) {
                    $(this).addClass('x');
                } else {
                    $(this).addClass('o');
                }
                aiMove();
            }
        };

    $('#board button').click(buttonClickHandler);
    $('#reset').click(reset);
    $('#skip').click(skip);

    reset();
});
