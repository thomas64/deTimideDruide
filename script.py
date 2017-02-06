
"""
class: Script
"""

import characters
from constants import Direction

from database import HeroDatabase
from database import QuestDatabase

from database import TreasureChestDatabase
from database import SparklyDatabase
from database import MoveEventDatabase
from database import TextEventDatabase

from database import PouchItemDatabase
from database import WeaponDatabase

import database
import inventoryitems


class Script:
    """
    Alle momenten van het spel
    """

    @staticmethod
    def new_game(data, debug_mode):
        """
        Wat te doen bij het starten van een nieuw spel.
        :param data: self.engine.data
        """
        # Vul de heroes database met alle hero objecten die in factory zijn gemaakt.
        data.heroes = characters.factory_all_heroes(HeroDatabase)
        data.logbook = inventoryitems.factory_all_quests(QuestDatabase)
        # Treasure chest en Sparklies worden geen losse objecten, maar blijven 1 object met meerdere dicts.
        data.treasure_chests = database.factory(TreasureChestDatabase)
        data.sparklies = database.factory(SparklyDatabase)
        data.move_events = database.factory(MoveEventDatabase)
        data.text_events = database.factory(TextEventDatabase)

        # Vul de party aan met de eerste hero
        data.party.add(data.heroes['brann'], verbose=False)

        eqp_item = inventoryitems.factory_equipment_item(WeaponDatabase.bronzemace)
        data.inventory.add_i(eqp_item, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.gold)
        data.pouch.add(pouch_item, 1, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.grapes)
        data.pouch.add(pouch_item, 1, verbose=False)
        pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.wine)
        data.pouch.add(pouch_item, 1, verbose=False)

        if debug_mode:
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.droppings)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shroom)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.rose)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.ladybug)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.wool)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shells)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.poppy)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.cantharel)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.weegbree)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.berkenschors)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.maretak)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.spiderweb)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.fluitekruid)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.knoflook)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shallot)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.tomaat)
            data.pouch.add(pouch_item, 1, verbose=False)
            pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.doperwten)
            data.pouch.add(pouch_item, 1, verbose=False)

        data.map_name = 'braserie_ad_waal'
        data.map_pos = 'start_game'     # dit is de naam van de startpositie object in de tmx map
        data.map_dir = Direction.South

        data.custom_inventory_counter = 0

    @staticmethod
    def intro_text():
        """..."""
        return ["A long time ago in a galaxy far,",
                "far away...."]
