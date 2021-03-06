
"""
class: BuyBox
"""

import pygame

from components import ListBox
from constants import ColumnType
from constants import EquipmentType
import inventoryitems

COLUMN1X = 0
COLUMN2X = 34
COLUMN3X = 210

TOTALCOLUMNS = ((ColumnType.f_icon, COLUMN1X, "", ""),
                (ColumnType.text,   COLUMN2X, "Item", "Name:"),
                (ColumnType.text,   COLUMN3X, "Gold", "Cost:"))


class BuyBox(ListBox):
    """
    De box waar alle items uit de database te zien zijn, mits ze de 'shop' eigenschap hebben.
    """
    def __init__(self, x, y, width, height, equipment_database, sum_merchant):
        super().__init__(x, y, width, height)

        self.sale = sum_merchant

        self.total_columns = TOTALCOLUMNS
        self.column1x = COLUMN1X    # deze is voor de baseclass
        self.row_nr_with_rect = 3   # row[3]
        self.row_nr_with_obj = 4    # row[4]

        self.table_data = []
        self._fill_table_data(equipment_database)
        self.table_view = []
        self._setup_table_view()
        self._setup_scroll_layer()

        self.cur_item = None
        self._update_rects_in_layer_rect_with_offset()

    def _fill_table_data(self, equipment_database):

        for equipment_item in equipment_database.values():

            # speciaal alleen voor pouchitems
            if equipment_item.value['typ'] == EquipmentType.itm:

                pouch_item_obj = inventoryitems.factory_pouch_item(equipment_item)
                pouch_item_spr = pygame.image.load(pouch_item_obj.SPR).convert_alpha()
                pouch_item_nam = pouch_item_obj.NAM
                pouch_item_val = str(round(pouch_item_obj.VAL - ((pouch_item_obj.VAL / 100) * self.sale)))
                self.table_data.append(
                    # row[0],            row[1],         row[2],    row[3],    row[4]
                    [pouch_item_spr, pouch_item_nam, pouch_item_val, None, pouch_item_obj]
                )

            else:
                if equipment_item.value['shp']:
                    equipment_item_obj = inventoryitems.factory_equipment_item(equipment_item)
                    equipment_item_spr = pygame.image.load(equipment_item_obj.SPR).subsurface(
                        equipment_item_obj.COL, equipment_item_obj.ROW, self.subsurw, self.subsurh).convert_alpha()
                    equipment_item_nam = equipment_item_obj.NAM
                    equipment_item_val = str(round(equipment_item_obj.VAL - ((equipment_item_obj.VAL/100) * self.sale)))
                    self.table_data.append(
                        # row[0],                   row[1],         row[2],         row[3],     row[4]
                        [equipment_item_spr, equipment_item_nam, equipment_item_val, None, equipment_item_obj]
                    )

    def mouse_click(self, event):
        """
        :param event: pygame.MOUSEBUTTONDOWN uit shopscreen
        """
        for index, row in enumerate(self.table_data):
            if row[3].collidepoint(event.pos):
                self.cur_item = index
                selected_item = row[4]
                value = int(row[2])

                return True, selected_item, value

        return False, None, None
