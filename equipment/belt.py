
"""
class: BeltDatabase
"""

import collections

import equipment.equipment as eqp

# todo, alle gordels afmaken

SPRITEPATH = ''


class BeltDatabase(collections.OrderedDict):
    """
    Zie accessory
    """
    def __init__(self, *args, **kwds):
        super().__init__(*args, **kwds)

        self['leatherbelt'] = dict(nam="Leather Belt", srt=1, val=100, shp=True, wht=1, prt=1)
        self['testbelt2'] = dict(nam="Test Belt 2",    srt=2, val=200, shp=True, wht=2, prt=2)

    def factory(self, key_name):
        """
        Zie accessory
        :param key_name:
        """
        if key_name is None:
            return eqp.EquipmentItem(eqp.EquipmentType.blt)
        belt = self[key_name]
        belt['spr'] = SPRITEPATH
        return eqp.EquipmentItem(eqp.EquipmentType.blt, **belt)
