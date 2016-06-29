
"""
class: BeltDatabase
"""

import enum

from constants import EquipmentType


# todo, alle gordels afmaken

SPRITEPATH = 'resources/sprites/icons/equipment/belt1.png'


class BeltDatabase(enum.Enum):
    """..."""
    leatherbelt = dict(nam="Leather Belt", srt=1, val=100, shp=True, wht=1, prt=1, col=0, row=0)
    testbelt2 = dict(nam="Test Belt 2",    srt=2, val=200, shp=True, wht=2, prt=2, col=0, row=0)


for blt in BeltDatabase:
    blt.value['typ'] = EquipmentType.blt
    blt.value['spr'] = SPRITEPATH
