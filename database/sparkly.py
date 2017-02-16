
"""
class: SparklyDatabase
"""

import aenum

from .pouchitem import PouchItemDatabase


class SparklyDatabase(aenum.NoAliasEnum):
    """
    NoAliasEnum mag dezelfde values bevatten in tegenstelling tot Enum.
    Alle glinsteringen met inhoud op een rij.
    """
    # kasteel_batenburg
    sparkly1 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))


# noinspection PyTypeChecker
for sparkly in SparklyDatabase:
    sparkly.value['taken'] = 0
