
"""
class: TreasureChestDatabase
"""

import aenum
import datetime

from .weapon import WeaponDatabase
from .helmet import HelmetDatabase
from .boots import BootsDatabase
from .pouchitem import PouchItemDatabase


class TreasureChestDatabase(aenum.NoAliasEnum):
    """
    Alle schatkisten met inhoud op een rij.
    """

    # romerkanal
    chest100 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44),
                                 itm2=dict(nam=PouchItemDatabase.bottle,        qty=3)),
                    condition=dict(pwd=dict(ask="Raadsels. Code 1e plek:", anw="fgxzy3")))
    chest101 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33),
                                 itm2=dict(nam=PouchItemDatabase.grapes,        qty=2)),
                    condition=dict(pwd=dict(ask="Raadsels. Code 2e plek:", anw="hjkip5")))
    chest102 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=2)),
                    condition=dict(pwd=dict(ask="Raadsels. Code 3e plek:", anw="jkfrd3")))
    chest103 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=4)),
                    condition=dict(pwd=dict(ask="Raadsels. Code 4e plek:", anw="plsrt7")))

    # bank dag 2
    chest104 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44),
                                 itm2=dict(nam=PouchItemDatabase.bottle,        qty=1)),
                    condition=dict(pwd=dict(ask="Ingrediënten. Code 1e plek:", anw="gvfr5t")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest105 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33),
                                 itm2=dict(nam=PouchItemDatabase.grapes,        qty=1)),
                    condition=dict(pwd=dict(ask="Ingrediënten. Code 2e plek:", anw="jgtr8y")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest106 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Ingrediënten. Code 3e plek:", anw="cvfr4w")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest107 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Ingrediënten. Code 4e plek:", anw="klyu9n")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))

    chest108 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44),
                                 itm2=dict(nam=PouchItemDatabase.bottle,        qty=2)),
                    condition=dict(pwd=dict(ask="Champignons. Code 1e plek:", anw="fcvt90")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest109 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33),
                                 itm2=dict(nam=PouchItemDatabase.bottle,        qty=2)),
                    condition=dict(pwd=dict(ask="Champignons. Code 2e plek:", anw="hjky87")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest110 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Champignons. Code 3e plek:", anw="vfdr44")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))
    chest111 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Champignons. Code 4e plek:", anw="sxdj12")),
                    time1=datetime.datetime(2017, 5, 14, 17, 00),
                    time2=datetime.datetime(2017, 5, 16, 12, 00))

    # bank dag 4
    chest112 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Triviant. Code 1e plek:", anw="hhdrf5")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest113 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33)),
                    condition=dict(pwd=dict(ask="Triviant. Code 2e plek:", anw="cvdet3")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest114 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Triviant. Code 3e plek:", anw="xjopl9")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest115 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11)),
                    condition=dict(pwd=dict(ask="Triviant. Code 4e plek:", anw="sxfre0")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))

    chest116 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44),
                                 itm2=dict(nam=PouchItemDatabase.knoflook,      qty=4)),
                    condition=dict(pwd=dict(ask="Sterren. Code 1e plek:", anw="sarty4")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest117 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33),
                                 itm2=dict(nam=PouchItemDatabase.knoflook,      qty=4)),
                    condition=dict(pwd=dict(ask="Sterren. Code 2e plek:", anw="cghyu8")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest118 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22),
                                 itm2=dict(nam=PouchItemDatabase.knoflook,      qty=4)),
                    condition=dict(pwd=dict(ask="Sterren. Code 3e plek:", anw="bhjds1")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))
    chest119 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11),
                                 itm2=dict(nam=PouchItemDatabase.knoflook,      qty=4)),
                    condition=dict(pwd=dict(ask="Sterren. Code 4e plek:", anw="kjopi7")),
                    time1=datetime.datetime(2017, 5, 16, 12, 00),
                    time2=datetime.datetime(2017, 5, 17, 12, 00))

    # bank dag 5
    chest120 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Spotten. Code 1e plek:", anw="jopft7")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest121 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33)),
                    condition=dict(pwd=dict(ask="Spotten. Code 2e plek:", anw="cxghb3")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest122 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Spotten. Code 3e plek:", anw="mmgft8")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest123 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11)),
                    condition=dict(pwd=dict(ask="Spotten. Code 4e plek:", anw="aaxcp9")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))

    chest124 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Knoflookkoning. Code 1e plek:", anw="wqikp7")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest125 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33)),
                    condition=dict(pwd=dict(ask="Knoflookkoning. Code 2e plek:", anw="vvgre6")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest126 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Knoflookkoning. Code 3e plek:", anw="mjhio6")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))
    chest127 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11)),
                    condition=dict(pwd=dict(ask="Knoflookkoning. Code 4e plek:", anw="xdhuy3")),
                    time1=datetime.datetime(2017, 5, 17, 12, 00),
                    time2=datetime.datetime(2017, 5, 19, 12, 00))

    # bank dag 7
    chest128 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Druïdegames. Code 1e plek:", anw="ffjkp2")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest129 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33)),
                    condition=dict(pwd=dict(ask="Druïdegames. Code 2e plek:", anw="ghbde7")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest130 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Druïdegames. Code 3e plek:", anw="zawtr8")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest131 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11)),
                    condition=dict(pwd=dict(ask="Druïdegames. Code 4e plek:", anw="ppcwk6")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))

    chest132 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Wijnproeverij. Code 1e plek:", anw="ttwkb5")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest133 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Wijnproeverij. Code 2e plek:", anw="xxgyu9")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest134 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Wijnproeverij. Code 3e plek:", anw="nhjew0")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))
    chest135 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11),
                                 itm2=dict(nam=PouchItemDatabase.wine,          qty=1)),
                    condition=dict(pwd=dict(ask="Wijnproeverij. Code 4e plek:", anw="kkfcw3")),
                    time1=datetime.datetime(2017, 5, 19, 12, 00),
                    time2=datetime.datetime(2017, 5, 20, 12, 00))

    # bank dag 8
    chest136 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Wandelroute. Code 1e plek:", anw="hhgfm8")),
                    time1=datetime.datetime(2017, 5, 20, 12, 00),
                    time2=datetime.datetime(2017, 5, 22, 12, 00))
    chest137 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=33)),
                    condition=dict(pwd=dict(ask="Wandelroute. Code 2e plek:", anw="sxfrq2")),
                    time1=datetime.datetime(2017, 5, 20, 12, 00),
                    time2=datetime.datetime(2017, 5, 22, 12, 00))
    chest138 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Wandelroute. Code 3e plek:", anw="lhvru6")),
                    time1=datetime.datetime(2017, 5, 20, 12, 00),
                    time2=datetime.datetime(2017, 5, 22, 12, 00))
    chest139 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=11)),
                    condition=dict(pwd=dict(ask="Wandelroute. Code 4e plek:", anw="zzjgb8")),
                    time1=datetime.datetime(2017, 5, 20, 12, 00),
                    time2=datetime.datetime(2017, 5, 22, 12, 00))

    chest140 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Wijnschip. Code:", anw="fvhgu7")),
                    time1=datetime.datetime(2017, 5, 20, 12, 00),
                    time2=datetime.datetime(2017, 5, 22, 12, 00))

    chest144 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Grandprix. Code:", anw="insomnia")),
                    time1=datetime.datetime(2017, 5, 22,  6, 00),
                    time2=datetime.datetime(2017, 5, 22, 23, 00))

    # bank dag 10
    chest145 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=88)),
                    condition=dict(pwd=dict(ask="Trollenoorlog. Code 1e plek:", anw="gddvu8")),
                    time1=datetime.datetime(2017,  5, 22, 12, 00),
                    time2=datetime.datetime(2099, 12, 31, 23, 59))
    chest146 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=66)),
                    condition=dict(pwd=dict(ask="Trollenoorlog. Code 2e plek:", anw="zsjhn9")),
                    time1=datetime.datetime(2017,  5, 22, 12, 00),
                    time2=datetime.datetime(2099, 12, 31, 23, 59))
    chest147 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Trollenoorlog. Code 3e plek:", anw="wbhjo9")),
                    time1=datetime.datetime(2017,  5, 22, 12, 00),
                    time2=datetime.datetime(2099, 12, 31, 23, 59))
    chest148 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=22)),
                    condition=dict(pwd=dict(ask="Trollenoorlog. Code 4e plek:", anw="vfduj3")),
                    time1=datetime.datetime(2017,  5, 22, 12, 00),
                    time2=datetime.datetime(2099, 12, 31, 23, 59))

    # wijnproeverij
    chest150 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=44)),
                    condition=dict(pwd=dict(ask="Wijn zuipen. Code:", anw="dewaarheidisindewijn")),
                    time1=datetime.datetime(2017, 5, 16,  7, 00),
                    time2=datetime.datetime(2017, 5, 16, 21, 00))


    # huis cochem 1f
    chest200 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.wine,          qty=1)))

    chest300 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.cauldron,      qty=1)),
                    condition=dict(pwd=dict(ask="Code:", anw="bedanktvoorhetspelen")))



    chest20 = dict(
        content=dict(itm1=dict(nam=PouchItemDatabase.wine, qty=1),
                     itm2=dict(nam=PouchItemDatabase.gold, qty=1),
                     itm3=dict(nam=PouchItemDatabase.grapes, qty=1),
                     itm4=dict(nam=PouchItemDatabase.shroom, qty=1),
                     itm5=dict(nam=PouchItemDatabase.cauldron, qty=1)),
        condition=dict(pwd=dict(ask="Hoe heet Thomas?",
                                anw="thomas")
                       )
    )

    # ersin_forest_center
    chest1 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.hlg_pot,       qty=3)))
    chest2 = dict(condition=dict(thf=3),
                  content=dict(eqp1=dict(nam=WeaponDatabase.bronzeshortsword, qty=1),
                               eqp2=dict(nam=HelmetDatabase.leathercap,       qty=1)),
                  time1=datetime.datetime(2016, 10, 19, 2, 00),
                  time2=datetime.datetime(2099, 10, 19, 2, 15))
    chest3 = dict(condition=dict(mec=2),
                  content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=4)))
    chest4 = dict(condition=dict(mec=1, thf=1),
                  content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=5)))
    chest8 = dict(condition=dict(thf=2),
                  content=dict(eqp1=dict(nam=BootsDatabase.leatherboots,      qty=1),
                               itm1=dict(nam=PouchItemDatabase.gold,          qty=2)))
    # ersin_cave_room1
    chest5 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=2)))
    # ersin_cave_room3
    chest6 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.hlg_pot,       qty=2)))
    chest7 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.fir_flk,       qty=2)))
    # ersin_forest_invernia
    chest9 = dict(content=dict(itm1=dict(nam=PouchItemDatabase.ant_pot,       qty=1)))

    @staticmethod
    def mec_text(value):
        """..."""
        return ["There's a dangerous trap on this treasure chest.",
                "You need a rank {} of the Mechanic Skill to".format(value),
                "disarm the trap."]

    @staticmethod
    def thf_text(value):
        """..."""
        return ["There's a lock on this treasure chest.",
                "You need a rank {} of the Thief Skill".format(value),
                "to pick the lock."]

    @staticmethod
    def open_chest(condition, mec_v, mec_h, thf_v, thf_h):
        """..."""
        text = ["Found:"]
        if condition:
            text = ["Correct ingevoerd! De kist bevat:"]
        return text


# noinspection PyTypeChecker
for chest in TreasureChestDatabase:
    chest.value['opened'] = 0
