
"""
class: GameState
"""

import enum


class GameState(enum.Enum):
    """
    State machine constants for the StateMachine class
    """
    MainMenu = 1
    OptionsMenu = 2
    PauseMenu = 3
    OverWorld = 4