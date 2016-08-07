
"""
class: TreasureChestDatabase
"""

from .weapon import WeaponDatabase
from .helmet import HelmetDatabase
from .pouchitem import PouchItemDatabase


# is een class en geen losse dict, want anders wordt de dict niet ververst bij een nieuwe game.
class TreasureChestDatabase(dict):
    """
    Alle schatkisten met inhoud op een rij.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self['chest20'] = dict(
            content=dict(itm1=dict(nam=PouchItemDatabase.wine,      qty=1),
                         itm2=dict(nam=PouchItemDatabase.gold,      qty=1),
                         itm3=dict(nam=PouchItemDatabase.grapes,    qty=1),
                         itm4=dict(nam=PouchItemDatabase.shroom,    qty=1),
                         itm5=dict(nam=PouchItemDatabase.cauldron,  qty=1)),
            condition=dict(pwd=dict(ask="Hoe heet Thomas?",
                                    anw="thomas")
                           )
        )

        # ersin_forest_start
        self['chest1'] = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=2),
                                           itm2=dict(nam=PouchItemDatabase.herbs,         qty=3),
                                           eqp1=dict(nam=WeaponDatabase.bronzeshortsword, qty=1),
                                           eqp2=dict(nam=HelmetDatabase.leathercap,       qty=1)))
        self['chest2'] = dict(condition=dict(thf=3),
                              content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=3)))
        self['chest3'] = dict(condition=dict(mec=2),
                              content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=4)))
        self['chest4'] = dict(condition=dict(mec=1, thf=1),
                              content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=5)))

        # ersin_cave_room1
        self['chest5'] = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=2)))
        # ersin_cave_room3
        self['chest6'] = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=2)))
        self['chest7'] = dict(content=dict(itm1=dict(nam=PouchItemDatabase.gold,          qty=2)))

        for value in self.values():
            value['opened'] = 0

    @staticmethod
    def mec_text(value):
        """..."""
        return ["There's a dangerous trap on this treasurechest.",
                "You need a level {} of the Mechanic Skill to".format(value),
                "disarm the trap."]

    @staticmethod
    def thf_text(value):
        """..."""
        return ["There's a lock on this treasurechest.",
                "You need a level {} of the Thief Skill".format(value),
                "to pick the lock."]

    @staticmethod
    def open_chest(condition, mec_v, mec_h, thf_v, thf_h):
        """..."""
        text = ["Found:"]
        if condition:
            text = ["Correct ingevoerd! De kist bevat:"]
        return text
