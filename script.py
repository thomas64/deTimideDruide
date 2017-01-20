
"""
class: Script
"""

import characters
from constants import Direction
from database import HeroDatabase
from database import SparklyDatabase
from database import TreasureChestDatabase
from database import WeaponDatabase
from database import PouchItemDatabase
import inventoryitems


class Script:
    """
    Alle momenten van het spel
    """

    @staticmethod
    def new_game(data):
        """
        Wat te doen bij het starten van een nieuw spel.
        :param data: self.engine.data
        """
        # Vul de heroes database met alle hero objecten die in factory zijn gemaakt.
        data.heroes = characters.factory_all_heroes(HeroDatabase)
        # Treasure chest en Sparklies worden geen losse objecten, maar blijven 1 object met meerdere dicts.
        data.treasure_chests = TreasureChestDatabase()
        data.sparklies = SparklyDatabase()

        # Vul de party aan met de eerste hero
        data.party.add(data.heroes['noppie'], verbose=False)

        eqp_item = inventoryitems.factory_equipment_item(WeaponDatabase.bronzemace)
        data.inventory.add_i(eqp_item, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.gold)
        data.pouch.add(pouch_item, 1, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.grapes)
        data.pouch.add(pouch_item, 1, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.wine)
        data.pouch.add(pouch_item, 1, verbose=False)

        data.map_name = 'braserie_ad_waal'
        data.map_pos = 'start_game'     # dit is de naam van de startpositie object in de tmx map
        data.map_dir = Direction.South

        data.custom_inventory_counter = 0
