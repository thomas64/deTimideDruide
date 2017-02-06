
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
        return ["There's a dangerous trap on this treasurechest.",
                "You need a rank {} of the Mechanic Skill to".format(value),
                "disarm the trap."]

    @staticmethod
    def thf_text(value):
        """..."""
        return ["There's a lock on this treasurechest.",
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
