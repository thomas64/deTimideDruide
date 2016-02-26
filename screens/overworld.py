
"""
class: Overworld
"""

import pygame

import screens.party.display
import screens.sprites
import screens.window
import states


WINDOWWIDTH = 800
WINDOWHEIGHT = 600
WINDOWPOS = 100, 100

BACKGROUNDCOLOR = pygame.Color("black")

INVLBL = "I"
UPLBL = "Up"
DOWNLBL = "Down"
LEFTLBL = "Left"
RIGHTLBL = "Right"

CLICKBUTTON = 1
INVKEY = pygame.K_i
UPKEY = pygame.K_UP
DOWNKEY = pygame.K_DOWN
LEFTKEY = pygame.K_LEFT
RIGHTKEY = pygame.K_RIGHT

BTNWIDTH = 40
BTNHEIGHT = 40

INVX, INVY = -200, -300
UPX, UPY = -150, -300
DOWNX, DOWNY = -150, -250
LEFTX, LEFTY = -200, -250
RIGHTX, RIGHTY = -100, -250


class Overworld(object):
    """
    Overworld layout.
    """
    def __init__(self, engine):
        self.engine = engine
        self.screen = self.engine.screen
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill(BACKGROUNDCOLOR)
        self.background = self.background.convert()
        self.window = screens.window.Window(WINDOWWIDTH, WINDOWHEIGHT, self.engine.audio)

        self.partyscreen = None

        self.buttons = None
        self._init_buttons()
        self.key_input = pygame.key.get_pressed()       # dit is voor de mousepress op een button.

    def _init_buttons(self):
        """
        Maak de knoppen aan en zet ze in een lijst.
        Plaats ook de bijbehorende keys in een lijst.
        """
        bg_width = self.background.get_width()
        bg_height = self.background.get_height()

        # todo, afhankelijk van situatie, buttons niet weergeven
        # button_view = sprites.ButtonSprite((bg_width-200,   bg_height-300), "V",     pygame.K_v)
        button_inv = screens.sprites.ButtonSprite(
                                    BTNWIDTH, BTNHEIGHT, (bg_width + INVX,   bg_height + INVY),   INVLBL,   INVKEY)
        button_up = screens.sprites.ButtonSprite(
                                    BTNWIDTH, BTNHEIGHT, (bg_width + UPX,    bg_height + UPY),    UPLBL,    UPKEY)
        button_down = screens.sprites.ButtonSprite(
                                    BTNWIDTH, BTNHEIGHT, (bg_width + DOWNX,  bg_height + DOWNY),  DOWNLBL,  DOWNKEY)
        button_left = screens.sprites.ButtonSprite(
                                    BTNWIDTH, BTNHEIGHT, (bg_width + LEFTX,  bg_height + LEFTY),  LEFTLBL,  LEFTKEY)
        button_right = screens.sprites.ButtonSprite(
                                    BTNWIDTH, BTNHEIGHT, (bg_width + RIGHTX, bg_height + RIGHTY), RIGHTLBL, RIGHTKEY)
        # button_cancel = sprites.ButtonSprite((bg_width-100, bg_height-200), "C",     pygame.K_c)

        # self.buttons = [button_view, button_up, button_down, button_left, button_right, button_cancel]
        self.buttons = [button_inv, button_up, button_down, button_left, button_right]

    def handle_view(self):
        """
        Handel de view af in de window -> teken de achtergrond -> teken de window -> teken de buttons.
        """
        if self.engine.currentstate == states.GameState.Overworld:

            self.window.handle_view()

            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.window.surface, WINDOWPOS)

            for button in self.buttons:
                button.draw(self.screen, self.key_input)

        elif self.engine.currentstate == states.GameState.PartyScreen:
            self.partyscreen.handle_view()

    def handle_multi_input(self, key_input, mouse_pos, dt):
        """
        Registreert of er op de buttons wordt geklikt. En zet dat om naar keyboard input.
        :param key_input: pygame.key.get_pressed()
        :param mouse_pos: pygame.mouse.get_pos()
        :param dt: self.clock.tick(FPS)/1000.0
        """
        if self.engine.currentstate == states.GameState.Overworld:
            self.key_input = key_input

            for button in self.buttons:
                self.key_input = button.multi_click(mouse_pos, self.key_input)

            self.window.handle_multi_input(self.key_input, dt)

        elif self.engine.currentstate == states.GameState.PartyScreen:
            self.partyscreen.handle_multi_input(key_input, mouse_pos)

    def handle_single_mouse_input(self, event):
        """
        Handelt mouse events af.
        :param event: pygame.MOUSEBUTTONDOWN uit engine.py
        """
        if self.engine.currentstate == states.GameState.Overworld:
            if event.button == CLICKBUTTON:
                for button in self.buttons:
                    button_press = button.single_click(event)
                    if button_press == INVKEY:
                        self._show_party_screen()
                        break

        elif self.engine.currentstate == states.GameState.PartyScreen:
            if self.partyscreen.handle_single_mouse_input(event):       # alleen de ESC key returned een waarde
                self._close_party_screen()

    def handle_single_keyboard_input(self, event):
        """
        Handelt keyboard events af.
        :param event: pygame.KEYDOWN uit engine.py
        """
        if self.engine.currentstate == states.GameState.Overworld:
            if event.key == INVKEY:
                self._show_party_screen()
            self.window.handle_single_input(event)

        elif self.engine.currentstate == states.GameState.PartyScreen:
            if self.partyscreen.handle_single_keyboard_input(event) or event.key == INVKEY:
                self._close_party_screen()

    def _show_party_screen(self):
        self.engine.statemachine.push(states.GameState.PartyScreen)
        self.partyscreen = screens.party.display.Display(self.engine.data, self.screen)

    def _close_party_screen(self):
        self.engine.statemachine.pop(self.engine.currentstate)
        self.partyscreen = None
