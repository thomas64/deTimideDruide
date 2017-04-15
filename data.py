
"""
class: Data
"""

import containers


class Data(object):
    """
    Hier is alle gamedata.
    """
    def __init__(self):

        self.heroes = dict()
        self.logbook = dict()
        self.treasure_chests = dict()
        self.sparklies = dict()
        self.chapters = dict()
        self.move_events = dict()
        self.text_events = dict()

        self.party = containers.Party()
        self.inventory = containers.Inventory()
        self.pouch = containers.Pouch()

        self.map_name = None
        self.map_pos = None
        self.map_dir = None

        self.custom_inventory_counter = 0

        self.kaart_bekeken = False
        self.barman_gepraat = False
        self.recept_bekeken = False
        self.orakelsteen_gevonden = False
        self.brug_opgelopen = False
