
"""
class: HelmetDatabase
"""

import enum

from constants import EquipmentType
from constants import ItemMaterial


SPRITEPATH = 'resources/sprites/icons/equipment/helmet1.png'


class HelmetDatabase(enum.Enum):
    """..."""
    #                                                       val=prt**2+6
    customhelmet = dict(nam="Custom Helmet",        srt=1,  val=2,  shp=False, wht='X', prt='X',        col=0,   row=64,
                        min_wht=6, max_wht=1, min_prt=1, max_prt=6,
                        cus=True, clt=1, ltr=1, wod=0, mtl=10,
                        desc=("Creating a Custom Helmet requires 1 Cloth, 1 Leather and 10 metals.", " ",
                              "Weight: 1 - 6", "Protection: 1 - 6"))

    leathercap = dict(nam="Leather Cap",            srt=2,  val=7,  shp=True,  wht=1, prt=1,             col=0,   row=0, mtr=ItemMaterial.ltr)
    bronzehelmet = dict(nam="Bronze Helmet",        srt=3,  val=10, shp=True,  wht=2, prt=2,             col=32,  row=0, mtr=ItemMaterial.brz)
    ironhelmet = dict(nam="Iron Helmet",            srt=5,  val=15, shp=True,  wht=3, prt=3,             col=64,  row=0, mtr=ItemMaterial.irn)
    steelhelmet = dict(nam="Steel Helmet",          srt=7,  val=22, shp=True,  wht=4, prt=4,             col=96,  row=0, mtr=ItemMaterial.stl)
    silverhelmet = dict(nam="Silver Helmet",        srt=9,  val=31, shp=True,  wht=5, prt=5,             col=128, row=0, mtr=ItemMaterial.slv)
    titaniumhelmet = dict(nam="Titanium Helmet",    srt=11, val=42, shp=False, wht=2, prt=5,             col=160, row=0, mtr=ItemMaterial.tnm)

    helmofknowledge = dict(nam="Helm of Knowledge", srt=13, val=7,  shp=False, wht=2, prt=1,      int=3, col=0,   row=32)
    helmofwisdom = dict(nam="Helm of Wisdom",       srt=14, val=7,  shp=False, wht=2, prt=1,      wil=5, col=32,  row=32)
    helmofcharisma = dict(nam="Helm of Charisma",   srt=15, val=7,  shp=False, wht=2, prt=1,      dip=2, col=64,  row=32)
    helmofinsight = dict(nam="Helm of Insight",     srt=16, val=7,  shp=False, wht=2, prt=1,      lor=2, col=96,  row=32)
    helmoftempests = dict(nam="Helm of Tempests",   srt=17, val=7,  shp=False, wht=2, prt=1,      war=2, col=128, row=32)

    wizardhat = dict(nam="Wizard Hat",              srt=18, val=6,  shp=False, wht=0, max_bat=10, wiz=1, col=160, row=32)


for hlm in HelmetDatabase:
    hlm.value['typ'] = EquipmentType.hlm
    hlm.value['spr'] = SPRITEPATH
