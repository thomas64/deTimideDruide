
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
    sparkly2 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.doperwten,   qty=59)))

    # brug_over_de_waal
    sparkly3 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.droppings,    qty=23)))

# noinspection PyTypeChecker
for sparkly in SparklyDatabase:
    sparkly.value['taken'] = 0
