
"""
class: MainMenu
"""

from components import LoadScreen
from components import MessageBox
from components import Transition
from constants import GameState
from data import Data
from script import Script

from .basemenu import BaseMenu
import screens.menu


class MainMenu(BaseMenu):
    """
    De mainmenu items.
    """
    def __init__(self, engine):
        super().__init__(engine)

        self.content = ['New Game',
                        'Load Game',
                        'Settings',
                        'Exit']

    def on_select(self, menu_item, title, animation, scr_capt, index):
        """
        Zie BaseMenu.
        :param menu_item: zie BaseMenu
        :param title: zie BaseMenu
        :param animation: zie BaseMenu
        :param scr_capt: zie BaseMenu
        :param index: zie BaseMenu
        """
        if menu_item.text == "New Game":
            self.engine.audio.fade_bg_music()
            self.engine.data = Data()
            if Script.new_game(self.engine.data, self.engine.debug_mode):  # als het voor de datum is
                # als deze stack leeg is, komt Overworld er op.
                self.engine.gamestate.push(Transition())
                self.engine.gamestate.deep_pop()
                self.engine.gamestate.push(MessageBox(Script.intro_text(), scr_capt=False, last=True))
                self.engine.gamestate.push(Transition())
                self.engine.gamestate.push(LoadScreen())
                self.engine.gamestate.push(Transition(wait=2))
                self.engine.force_bg_music = True

        elif menu_item.text == "Load Game":
            push_object = screens.menu.create_menu(GameState.LoadMenu, self.engine)
            self.engine.gamestate.push(push_object)
            self.engine.gamestate.push(Transition())

        elif menu_item.text == "Settings":
            push_object = screens.menu.create_menu(GameState.SettingsMenu, self.engine,
                                                   title1=title, animation1=animation)
            self.engine.gamestate.push(push_object)

        elif menu_item.text == "Exit":
            self.on_quit()

    def on_quit(self):
        """
        Zie BaseMenu. Stopt de engine.
        """
        self.engine.running = False
