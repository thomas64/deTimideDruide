
"""
class: MainMenu
"""

import screens.menu.basemenu
import screens.menu.manager
import screens.overworld


class MainMenu(screens.menu.basemenu.BaseMenu):
    """
    De mainmenu items.
    """
    def __init__(self, engine):
        super().__init__(engine)

        self.inside['NewGame'] = 'New Game'
        self.inside['LoadGame'] = 'Load Game'
        self.inside['Options'] = 'Options'
        self.inside['ExitGame'] = 'Exit'

    def on_select(self, menu_item, scr_capt):
        """
        Zie BaseMenu.
        :param menu_item: zie BaseMenu
        :param scr_capt: zie BaseMenu
        """
        if menu_item.func == self.NewGame:
            push_object = screens.overworld.Overworld(self.engine)
            self.engine.gamestate.change(push_object)

        elif menu_item.func == self.LoadGame:
            push_object = screens.menu.manager.create_menu(screens.menu.manager.MenuItems.LoadMenu, self.engine)
            self.engine.gamestate.push(push_object)

        elif menu_item.func == self.Options:
            push_object = screens.menu.manager.create_menu(screens.menu.manager.MenuItems.OptionsMenu, self.engine)
            self.engine.gamestate.push(push_object)

        elif menu_item.func == self.ExitGame:
            self.on_exit()

    def on_exit(self):
        """
        Zie BaseMenu. Stopt de engine.
        """
        self.engine.running = False

    def on_delete(self, key, index, scr_capt):
        """
        Zie BaseMenu.
        :param key: zie BaseMenu
        :param index: zie BaseMenu
        :param scr_capt: zie BaseMenu
        """
        pass