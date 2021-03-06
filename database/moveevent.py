
"""
class: MoveEventDatabase
"""

import aenum

from constants import Direction
from constants import PersonState


class MoveEventDatabase(aenum.NoAliasEnum):
    """
    Condition wordt op False gezet bij het eenmalig uitvoeren van de event.
    """
    move1 = dict(movement=(                     # seconden
            (PersonState.Moving,  Direction.West,  10.0),
            (PersonState.Moving,  Direction.North, 15.0),
            (PersonState.Moving,  Direction.West,   4.2)
        )
    )
    move2 = dict(movement=(  # als de movement maar 1 item heeft, dan is movement een list. dus [ ] ipv ( )
            (PersonState.Resting, Direction.South, 1.0),
            (PersonState.Resting, Direction.West,  0.5),
            (PersonState.Resting, Direction.East,  0.5),
            (PersonState.Resting, Direction.South, 0.5),
            (PersonState.Moving,  Direction.South, 0.6)
        )
    )
    move3 = dict(movement=(
            (PersonState.Moving,  Direction.South, 0.3),
            (PersonState.Moving,  Direction.North, 2.1),
            (PersonState.Moving,  Direction.West,  2.1),
            (PersonState.Moving,  Direction.South, 2.3),
            (PersonState.Moving,  Direction.West,  1.5),
            (PersonState.Moving,  Direction.South, 2.5)
        )
    )
    move4 = dict(movement=[
            (PersonState.Moving,  Direction.North, 1.9)  # als het 1 item is, dan moet het in een list. zie [ ] ipv ( )
        ]
    )


# noinspection PyTypeChecker
for event in MoveEventDatabase:
    event.value['condition'] = True
