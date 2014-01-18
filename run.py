#!/usr/bin/env python
"""
This runs the Flask app.

After running this, point your browser to http://127.0.0.1:5000/ to play
Tic-Tac-Toe.
"""

from yaktak.app import APP
APP.run(debug=True)
