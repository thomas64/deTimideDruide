
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
    sparkly2 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.doperwten,    qty=3)))
    sparkly4 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.rose,         qty=3)))

    # kerker batenburg
    sparkly26 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.spiderweb,   qty=3)))

    # schuur batenburg
    sparkly28 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.knoflook,    qty=3)))

    # huis batenburg
    sparkly29 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.tomaat,      qty=2)))
    sparkly31 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.putsi,       qty=1)))

    # waal_braserie
    sparkly6 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wool,         qty=1)))
    sparkly23 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.weegbree,    qty=2)))

    # her en der bij grijze stenen aan de waterkant.
    sparkly7 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shells,       qty=2)))
    # her en der bij dode bomen
    sparkly24 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.berkenschors, qty=1)))

    # brug_over_de_waal
    sparkly3 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.droppings,    qty=1)))

    # kruising
    sparkly5 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.ladybug,      qty=4)))
    sparkly8 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.poppy,        qty=2)))
    sparkly25 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.maretak,     qty=3)))
    sparkly27 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.fluitekruid, qty=2)))

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
    sparkly22 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.cantharel,   qty=4)))

    # schuur gymnich
    sparkly30 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.shallot,     qty=3)))

    # aan de rivieren
    sparkly32 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_maas,  qty=1)))
    sparkly33 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_niers, qty=1)))
    sparkly34 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.water_waal,  qty=1)))

    # romerkanaal
    sparkly35 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_rood,  qty=1)))
    sparkly36 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_blauw, qty=1)))
    sparkly37 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bloem_geel,  qty=1)))
    sparkly95 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.recept2,     qty=1)))

    # altena
    sparkly50 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=3)))
    sparkly51 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=3)))
    # huis batenburg
    sparkly52 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=1)))
    sparkly63 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=2)))
    sparkly64 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=2)))
    sparkly65 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=6)))
    sparkly94 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=3)))
    # huis romer
    sparkly53 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2),
                                  itm2=dict(nam=PouchItemDatabase.bottle,      qty=2)))
    sparkly60 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=4)))
    sparkly61 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=2)))
    sparkly62 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=6)))
    # wijn piesport
    sparkly54 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2)))
    sparkly55 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2)))
    sparkly56 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2)))
    sparkly57 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2)))
    sparkly58 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=2)))
    # inn piesport
    sparkly59 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,        qty=1)))
    # schuur gymnich
    sparkly66 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.bottle,      qty=3)))
    # kruising2
    sparkly67 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly68 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=2)))
    sparkly69 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly70 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=2)))
    sparkly71 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly72 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly73 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly74 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly75 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly76 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly77 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly78 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly79 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly80 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly81 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly82 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly83 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly84 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly85 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly86 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly87 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly88 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=2)))
    sparkly89 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly90 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=2)))
    sparkly91 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly92 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=1)))
    sparkly93 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.grapes,      qty=2)))

    # cochem
    sparkly96 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.recept3,     qty=1)))
    # altena
    sparkly97 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.recept1,     qty=1)))

    # huis cochem 1f
    sparkly100 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,       qty=1)))

    # trier
    sparkly101 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly102 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly103 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly104 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly105 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly106 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly107 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))
    sparkly108 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen, qty=1)))


# noinspection PyTypeChecker
for sparkly in SparklyDatabase:
    sparkly.value['taken'] = 0
