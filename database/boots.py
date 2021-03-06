
"""
class: BootsDatabase
"""

import enum

from constants import EquipmentType
from constants import ItemMaterial


SPRITEPATH = 'resources/sprites/icons/equipment/boots1.png'


class BootsDatabase(enum.Enum):
    """..."""
    #                                                     val=prt**2+8
    customboots = dict(nam="Custom Boots",        srt=1,  val=2,  shp=False, wht='X', prt='X',        col=128, row=32,
                       min_wht=6, max_wht=1, min_prt=1, max_prt=6,
                       cus=True, clt=2, ltr=4, wod=0, mtl=6,
                       desc=("Creating Custom Boots requires 2 Cloth, 4 Leather and 6 metals.", " ",
                             "Weight: 1 - 6", "Protection: 1 - 6"))

    leatherboots = dict(nam="Leather Boots",      srt=2,  val=9,  shp=True,  wht=1, prt=1,        col=0,   row=0,  mtr=ItemMaterial.ltr)
    bronzeboots = dict(nam="Bronze Boots",        srt=3,  val=12, shp=True,  wht=2, prt=2,        col=32,  row=0,  mtr=ItemMaterial.brz)
    ironboots = dict(nam="Iron Boots",            srt=5,  val=17, shp=True,  wht=3, prt=3,        col=64,  row=0,  mtr=ItemMaterial.irn)
    steelboots = dict(nam="Steel Boots",          srt=7,  val=24, shp=True,  wht=4, prt=4,        col=96,  row=0,  mtr=ItemMaterial.stl)
    silverboots = dict(nam="Silver Boots",        srt=9,  val=33, shp=True,  wht=5, prt=5,        col=128, row=0,  mtr=ItemMaterial.slv)
    titaniumboots = dict(nam="Titanium Boots",    srt=11, val=44, shp=False, wht=2, prt=5,        col=160, row=0,  mtr=ItemMaterial.tnm)

    bootsofmotion = dict(nam="Boots of Motion",   srt=13, val=9,  shp=False, wht=0,        mvp=1, col=0,  row=32)
    bootsofspeed = dict(nam="Boots of Speed",     srt=14, val=18, shp=False, wht=0,        mvp=2, col=32, row=32)
    woodsmansboots = dict(nam="Woodsman's Boots", srt=15, val=9,  shp=False, wht=2, prt=1, ran=2, col=64, row=32)
    silenceboots = dict(nam="Silence Boots",      srt=16, val=9,  shp=False, wht=0,        stl=2, col=96, row=32)


for bts in BootsDatabase:
    bts.value['typ'] = EquipmentType.bts
    bts.value['spr'] = SPRITEPATH
