class WrongTurnError(Exception):
    """Sent when the wrong player tries to make a move."""
    pass

class SpaceTakenError(Exception):
    """Sent when the selected space is already taken."""
    pass

class GameOverError(Exception):
    """Sent when the game is over and the player tries to make a move."""
    pass
