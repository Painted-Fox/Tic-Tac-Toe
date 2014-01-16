$(document).ready(function() {
    var boardFields = [
            [$('#field-20'), $('#field-21'), $('#field-22')],
            [$('#field-10'), $('#field-11'), $('#field-12')],
            [$('#field-00'), $('#field-01'), $('#field-02')]
        ], x, y,
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
                    throw "Invalid grid."
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
        // Resets the board.
        reset = function() {
            setGrid([[0,0,0],[0,0,0],[0,0,0]]);
        },
        // Allows the player to skip a turn.
        skip = function() {
            aiMove();
        },
        // Request a move from the AI.
        aiMove = function() {
            // Handle the response from the AI.
            var success = function(data) {
                setGrid(data.grid);
            };
            $.ajax({
                url: '/wopr/move',
                type: 'POST',
                data: JSON.stringify(getGrid()),
                contentType: 'application/json; charset=utf-8',
                dataType: 'json',
                success: success
            });
        },
        // Handle button mashing, I mean clicking.
        buttonClickHandler = function() {
            aiMove();
        };

    $('#board button').click(buttonClickHandler);
    $('#reset').click(reset);
    $('#skip').click(skip);

    reset();
})
