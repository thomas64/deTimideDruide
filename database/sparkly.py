
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
    sparkly1 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen,  qty=1)))
    sparkly2 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.doperwten,    qty=59)))
    sparkly4 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.rose,         qty=5)))

    # kerker batenburg
    sparkly26 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.spiderweb,   qty=1)))

    # schuur batenburg
    sparkly28 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.knoflook,    qty=7)))

    # huis batenburg
    sparkly29 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.tomaat,      qty=10)))
    sparkly31 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.putsi,       qty=1)))

    # waal_braserie
    sparkly6 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wool,         qty=32)))
    sparkly23 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.weegbree,    qty=3)))

    # her en der bij grijze stenen aan de waterkant.
    sparkly7 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shells,       qty=2)))
    # her en der bij dode bomen
    sparkly24 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.berkenschors, qty=2)))

    # brug_over_de_waal
    sparkly3 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.droppings,    qty=23)))

    # kruising
    sparkly5 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.ladybug,      qty=3)))
    sparkly8 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.poppy,        qty=7)))
    sparkly25 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.maretak,     qty=4)))
    sparkly27 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.fluitekruid, qty=4)))

    # trollenbos
    sparkly9 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,       qty=1)))
    sparkly10 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly11 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly12 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly13 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly14 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly15 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly16 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly17 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly18 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly19 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly20 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))
    sparkly21 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shroom,      qty=1)))

    # grensovergang
    sparkly22 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.cantharel,   qty=3)))

    # schuur gymnich
    sparkly30 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shallot,     qty=30)))

    # aan de rivieren
    sparkly32 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_maas,  qty=1)))
    sparkly33 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_niers, qty=1)))
    sparkly34 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_waal,  qty=1)))

    # romerkanaal
    sparkly35 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_rood,  qty=1)))
    sparkly36 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_blauw, qty=1)))
    sparkly37 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_geel,  qty=1)))


# noinspection PyTypeChecker
for sparkly in SparklyDatabase:
    sparkly.value['taken'] = 0
