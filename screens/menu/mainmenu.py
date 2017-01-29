
"""
class: MainMenu
"""

from components import MessageBox
from components import Transition
from constants import GameState
from data import Data
from screens import Overworld
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
                        'Options',
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
            self.engine.data = Data()
            Script.new_game(self.engine.data)
            push_object = Overworld(self.engine)
            self.engine.gamestate.change(push_object)

            # todo, dit moet echt weg hier, naar de juiste plek
            brann_face = 'resources/sprites/heroes/01f_alagos.png'
            # background = 'resources/sprites/black.png'
            intro_text = [
                ["Kraa. Mijn naam is Brann. Kraa.",
                 "Neem nog maar even een lekker slokje van jullie koffie."],
                ["Kraa. Want vanaf nu is het eerst wel even gedaaaan met jullie rust. Kraaa.",
                 "Zwammix heeft mij gevraaaagd jullie op te zoeken in deze maaaagische wereld."],
                ["Deze wereld loopt parallel aan de wereld waar jullie je nu in bevinden.",
                 "Echt waaaaar.",
                 "Maaaar wat jullie nu meemaken gebeurt pas over duizend jaaar.",
                 "Jaaaaa. Het duurt lang heel lang."],
                ["Jaaa. Je zult het misschien niet geloven,",
                 "maar jullie zitten nu hiernaaaaaast bij Lodewijk Altenaaaaa.",
                 "Lekker aan de koffie. Kraaa. ",
                 "Maaaar het is tijd dat jullie op pad gaaaan, ",
                 "op zoek naar de druïde. ",
                 "Jaaa."],
                ["Hij heeft jullie nodig. Kraaa. ",
                 "Verzamel je team bijeen! ",
                 "Ik gaaaa met jullie mee.",
                 "Kom! Er is geen tijd te verliezen! ",
                 "Kraaa."]
            ]

            for i, text_part in enumerate(reversed(intro_text)):
                push_object = MessageBox(self.engine.gamestate, self.engine.audio, text_part, brann_face,
                                         scr_capt=None, last=(True if i == 0 else False))
                self.engine.gamestate.push(push_object)

            self.engine.gamestate.push(Transition(self.engine.gamestate))

        elif menu_item.text == "Load Game":
            push_object = screens.menu.create_menu(GameState.LoadMenu, self.engine)
            self.engine.gamestate.push(push_object)
            self.engine.gamestate.push(Transition(self.engine.gamestate))

        elif menu_item.text == "Options":
            push_object = screens.menu.create_menu(GameState.OptionsMenu, self.engine,
                                                   title1=title, animation1=animation)
            self.engine.gamestate.push(push_object)

        elif menu_item.text == "Exit":
            self.on_exit()

    def on_exit(self):
        """
        Zie BaseMenu. Stopt de engine.
        """
        self.engine.running = False
