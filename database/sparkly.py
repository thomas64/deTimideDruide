
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
    sparkly4 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.rose,        qty=5)))

    # waal_braserie
    sparkly6 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wool,        qty=32)))

    # her en der bij grijze stenen aan de waterkant.
    sparkly7 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shells,      qty=2)))

    # brug_over_de_waal
    sparkly3 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.droppings,   qty=23)))

    # kruising
    sparkly5 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.ladybug,     qty=3)))
    sparkly8 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.poppy,       qty=7)))

    # trollenbos
    sparkly9 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly10 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly11 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly12 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly13 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly14 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly15 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly16 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly17 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly18 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly19 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly20 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))
    sparkly21 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,     qty=1)))


# noinspection PyTypeChecker
for sparkly in SparklyDatabase:
    sparkly.value['taken'] = 0
