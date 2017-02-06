
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
            (PersonState.Resting, Direction.South, 3.0),
            (PersonState.Moving,  Direction.South, 1.65),
        )
    )
    move2 = dict(movement=(
            (PersonState.Resting, Direction.South, 1.0),
            (PersonState.Resting, Direction.West,  0.5),
            (PersonState.Resting, Direction.East,  0.5),
            (PersonState.Resting, Direction.South, 0.5),
            (PersonState.Moving,  Direction.South, 0.6),
        )
    )


# noinspection PyTypeChecker
for event in MoveEventDatabase:
    event.value['condition'] = True
