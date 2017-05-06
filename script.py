
"""
class: Script
"""

import datetime

import characters
from constants import Direction

from database import HeroDatabase
from database import QuestDatabase

from database import TreasureChestDatabase
from database import SparklyDatabase
from database import ChapterDatabase
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
        :param debug_mode:
        :param data: self.engine.data
        """

        timestamp = datetime.datetime.now()
        if timestamp > datetime.datetime(2017, 5, 13, 12, 00):
            return False

        # Vul de heroes database met alle hero objecten die in factory zijn gemaakt.
        data.heroes = characters.factory_all_heroes(HeroDatabase)
        data.logbook = inventoryitems.factory_all_quests(QuestDatabase)
        # Treasure chest en Sparklies worden geen losse objecten, maar blijven 1 object met meerdere dicts.
        data.treasure_chests = database.factory(TreasureChestDatabase)
        data.sparklies = database.factory(SparklyDatabase)
        data.chapters = database.factory(ChapterDatabase)
        data.move_events = database.factory(MoveEventDatabase)
        data.text_events = database.factory(TextEventDatabase)

        # Vul de party aan met de eerste hero
        data.party.add(data.heroes['brann'], verbose=False)

        # if debug_mode:
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.kleuren_drankje)
        #     data.pouch.add(pouch_item, 8, verbose=False)
        # eqp_item = inventoryitems.factory_equipment_item(WeaponDatabase.bronzemace)
        # data.inventory.add_i(eqp_item, verbose=False)
        # pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.gold)
        # data.pouch.add(pouch_item, 1, verbose=False)
        # pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.grapes)
        # data.pouch.add(pouch_item, 1, verbose=False)
        # pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.wine)
        # data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.putsi)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shroom)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.rose)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.ladybug)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.wool)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shells)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.poppy)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.cantharel)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.weegbree)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.berkenschors)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.maretak)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.spiderweb)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.fluitekruid)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.knoflook)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.shallot)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.tomaat)
        #     data.pouch.add(pouch_item, 1, verbose=False)
        #     pouch_item = inventoryitems.factory_pouch_item(PouchItemDatabase.doperwten)
        #     data.pouch.add(pouch_item, 1, verbose=False)

        data.map_name = 'waal_braserie'
        data.map_pos = 'start_game'     # dit is de naam van de startpositie object in de tmx map
        data.map_dir = Direction.West

        data.custom_inventory_counter = 0

        data.kaart_bekeken = False
        data.barman_gepraat = False
        data.orakelsteen_gevonden = False
        data.brug_opgelopen = False
        data.uitgespeeld = False

        return True

    @staticmethod
    def load_game(data):
        """
        Als de speler op een bepaalde datum een savegame laadt. Dan verschijnt hij op een bepaalde map.
        """
        timestamp = datetime.datetime.now()
        if datetime.datetime(2017, 5, 14, 6, 00) < timestamp < datetime.datetime(2017, 5, 16, 15, 00):
            data.map_name = 'kruising'
            data.map_pos = 'start_game'
            data.map_dir = Direction.East
        elif datetime.datetime(2017, 5, 16, 15, 00) < timestamp < datetime.datetime(2099, 12, 31, 23, 59):
            data.map_name = 'piesport_inn_2f'
            data.map_pos = 'start_game'
            data.map_dir = Direction.South

    @staticmethod
    def intro_text():
        """..."""
        return ["Duizend jaar geleden.",
                "Hier niet ver vandaan,",
                "vlak boven de rivier de Waal..."]
