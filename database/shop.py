
"""
class: ShopDatabase
"""

import enum

from constants import EquipmentType
from constants import WeaponType
from constants import ItemMaterial

from .pouchitem import PouchItemDatabase as PiDb


PATH = 'resources/sprites/npcs/'
FEXT = 'f.png'
SEXT = 's.png'


class ShopDatabase(enum.Enum):
    """
    ...
    """

    shop10 = dict(content=[(EquipmentType.itm,
                            [PiDb.wine, PiDb.grapes,
                             PiDb.bloem_rood, PiDb.bloem_blauw, PiDb.bloem_geel,
                             PiDb.water_maas, PiDb.water_niers, PiDb.water_waal])],
                  name='youngwoman04')




    shop1 = dict(content=[WeaponType.swd, WeaponType.haf, WeaponType.pol, WeaponType.mis, WeaponType.thr],
                 material=[ItemMaterial.brz],
                 name='man01')
    shop2 = dict(content=[EquipmentType.arm, EquipmentType.sld, EquipmentType.hlm],
                 material=[ItemMaterial.wdn, ItemMaterial.ltr],
                 name='man50')
    shop3 = dict(content=[EquipmentType.clk, EquipmentType.blt, EquipmentType.bts, EquipmentType.glv],
                 material=[ItemMaterial.ctn, ItemMaterial.ltr],
                 name='man52')
    shop4 = dict(content=[EquipmentType.amu, EquipmentType.rng, EquipmentType.brc],
                 name='youngwoman04')
    shop5 = dict(content=[EquipmentType.acy, (EquipmentType.itm,
                                              [PiDb.herbs, PiDb.spices, PiDb.hlg_pot, PiDb.ant_pot, PiDb.fir_flk]),
                          ],  # [itm for itm in PiDb if itm.value.get('val')] voor alle p_items met val
                 name='youngwoman03')

    @staticmethod
    def welcome_text():
        """..."""
        return ("Goedendag, welkom in mijn winkel.",
                "In het 'Buy' gedeelte zie je wat je",
                "kunt kopen. Het 'Sell' gedeelte geeft",
                "weer wat je al in je bezit hebt. Maar het daadwerkelijk",
                "verkopen van spullen is uitgeschakeld voor dit spel.",
                "Hier kun je spullen kopen die je nodig hebt voor",
                "quests, maar tegen een boete. Deze spullen zijn",
                "namelijke gratis te vinden in deze spelwereld, maar",
                "hier kun je ze kopen voor goud, mocht je ze echt",
                "nergens kunnen vinden.")

for shop in ShopDatabase:
    shop.value['face'] = PATH+shop.value['name']+FEXT
    shop.value['sprite'] = PATH+shop.value['name']+SEXT
