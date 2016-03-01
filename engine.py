
"""
class: GameEngine
"""

import pygame
import pygame.gfxdraw

import audio
import console
import data
import screens.menu.content
import screens.menu.display
import screens.loadsave
import screens.overworld
import states

# todo, magic numbers overal opruimen

# todo, er gaat nog wat mis met sidestep als fps te hoog is, oorzaak onduidelijk.
FPS = 6000        # minimaal 15, anders kan hij door bomen lopen. maximaal 110, anders sidestep raar.

KILLKEY = pygame.K_BACKSPACE
EXITKEY = pygame.K_ESCAPE

DEBUGKEY = pygame.K_F12
DEBUGFONT = 'courier'
DEBUGFONTSIZE = 11
DEBUGFONTCOLOR = pygame.Color("white")
DEBUGRECT = pygame.Rect(0, 0, 600, 400)
DEBUGRECTCOLOR = (32, 32, 32, 200)


class GameEngine(object):
    """
    De grafische weergave van het scherm. Handelt de states.
    """
    def __init__(self):
        self.screen = pygame.display.get_surface()
        self.statemachine = states.StateMachine()
        self.data = data.Data()
        self.audio = audio.Audio()

        self.running = False

        self.clock = pygame.time.Clock()
        self.playtime = 0.0
        self.dt = 0.0
        self.timer = 0.0

        self.menu = None    # todo, onderverdelen in 2: self.mainmenu en self.submenu
        # todo, bouw een soort state manager? kan in engine zitten
        self.overworld = None   # todo, overworld moet self.gameplay(screen)? worden oid.

        self.debugfont = pygame.font.SysFont(DEBUGFONT, DEBUGFONTSIZE)
        self.currentstate = None
        self.key_input = None
        self.mouse_input = None
        self.scr_capt = None

        self.show_debug = False

    def main_loop(self):
        """
        Start de game loop.
        """
        self.running = True
        self._show_main_menu(self.currentstate)

        while self.running:
            self.dt = self.clock.tick(FPS)/1000.0       # limit the redraw speed to 60 frames per second
            self.playtime += self.dt

            self.currentstate = self.statemachine.peek()
            self.handle_view()
            self.handle_audio()
            self.handle_multi_input()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                self.handle_single_input(event)
            pygame.display.update()

    def handle_view(self):
        """
        Laat de weergave van de verschillende states zien.
        """
        def _show_debug():
            if self.show_debug:
                text = (
                    "FPS:               {:.2f}".format(self.clock.get_fps()),
                    "dt:                {:.3f}".format(self.dt),
                    "playtime:          {:.2f}".format(self.playtime),
                    "",
                    "currenstate:       {}".format(self.currentstate),
                    "menu:              {}".format(self.menu),
                    "overworld:         {}".format(self.overworld),
                    "scr_capt:          {}".format(self.scr_capt),
                    "mouse_input:       {}".format(self.mouse_input)
                )
                try:
                    hero = self.overworld.window.hero
                    text2 = (
                        "",
                        "partyscreen:       {}".format(self.overworld.partyscreen),
                        "",
                        "zoom:              {:.1f}".format(self.overworld.window.map1.map_layer.zoom),
                        "time_up:           {}".format(hero.time_up),
                        "time_down:         {}".format(hero.time_down),
                        "time_left:         {}".format(hero.time_left),
                        "time_right:        {}".format(hero.time_right),
                        "time_delay:        {}".format(hero.time_delay),
                        "last_direction:    {}".format(hero.last_direction),
                        "move_direction:    {}".format(hero.move_direction),
                        "movespeed:         {}".format(hero.movespeed),
                        "",
                        "old_position.x:    {}".format(hero.old_position[0]),
                        "old_position.y:    {}".format(hero.old_position[1]),
                        "",
                        "hero.rect.x:       {}".format(hero.rect.x),
                        "hero.rect.y:       {}".format(hero.rect.y),
                        "",
                        "true_position.x:   {}".format(hero.true_position[0]),
                        "true_position.y:   {}".format(hero.true_position[1]),
                        "",
                        "step_count:        {}".format(hero.step_count),
                        "step_animation:    {}".format(hero.step_animation)
                    )
                    text += text2
                except AttributeError:
                    pass
                try:
                    import screens.party.invclickbox
                    text3 = (
                        "",
                        "max_box_height     {}".format(screens.party.invclickbox.MAXBOXHEIGHT),
                        "layer_height       {}".format(self.overworld.partyscreen.invclick_box.layer_height)
                    )
                    text += text3
                except AttributeError:
                    pass
                pygame.gfxdraw.box(self.screen, DEBUGRECT, DEBUGRECTCOLOR)
                for count, line in enumerate(text):
                    self.screen.blit(self.debugfont.render(line, True, DEBUGFONTCOLOR).convert_alpha(), (0, count * 10))

        if self.currentstate == states.GameState.MainMenu or \
           self.currentstate == states.GameState.OptionsMenu or \
           self.currentstate == states.GameState.PauseMenu:
            self.menu.handle_view(self.dt, self.scr_capt)
        elif self.currentstate == states.GameState.Overworld or \
                self.currentstate == states.GameState.PartyScreen:
            self.overworld.handle_view()

        _show_debug()

    def handle_audio(self):
        """
        Geeft de juiste muziek en achtergrond geluiden weer.
        """
        audio_state_is_changed = self.statemachine.has_audio_state_changed()
        self.audio.handle_music(self.currentstate, audio_state_is_changed)
        self.audio.handle_bg_sounds(self.currentstate, audio_state_is_changed)

    def handle_multi_input(self):
        """
        Handelt de ingedrukt-houden muis en keyboard input af.
        Wordt op dit moment alleen maar gebruikt voor visuele oplichten van de buttons en character movement.
        """
        self.key_input = pygame.key.get_pressed()
        self.mouse_input = None
        if pygame.mouse.get_pressed()[0]:
            self.mouse_input = pygame.mouse.get_pos()

        if self.currentstate == states.GameState.Overworld or \
           self.currentstate == states.GameState.PartyScreen:
            self.overworld.handle_multi_input(self.key_input, self.mouse_input, self.dt)

    def handle_single_input(self, event):
        """
        Handelt de muis en keyboard input af.
        :param event: pygame.event.get()
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            console.mouse_down(event.pos, event.button)
        if event.type == pygame.KEYDOWN:
            console.keyboard_down(event.key, event.unicode)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.currentstate == states.GameState.Overworld or \
               self.currentstate == states.GameState.PartyScreen:
                self.overworld.handle_single_mouse_input(event)

        if event.type == pygame.MOUSEMOTION:
            if self.currentstate == states.GameState.PartyScreen:
                if self.overworld.partyscreen is not None:  # onverklaarbaar, anders kun je niet al muisbewegend, het
                    self.overworld.partyscreen.handle_single_mouse_motion(event)  # partyscreen verlaten.

        if event.type == pygame.KEYDOWN:
            if self.currentstate == states.GameState.Overworld or \
               self.currentstate == states.GameState.PartyScreen:
                self.overworld.handle_single_keyboard_input(event)

            if event.key == DEBUGKEY:
                self.show_debug ^= True                                     # simple boolean swith
            if event.key == KILLKEY:
                self._kill_game()                           # todo, deze, de key en de methode moeten uiteindelijk weg
            if event.key == EXITKEY:
                if self.currentstate == states.GameState.MainMenu:          # eerst de keys op het toetsenbord
                    self.audio.play_sound(self.audio.select)        # omdat escape in menu standaard geen geluid geeft
                    self._main_menu_select_exit_game()
                    return                                                  # returns, want anders zitten ze
                elif self.currentstate == states.GameState.OptionsMenu:     # de menu's in de weg
                    self.audio.play_sound(self.audio.select)
                    self._options_menu_select_back()
                    return
                elif self.currentstate == states.GameState.PauseMenu:
                    self.audio.play_sound(self.audio.select)
                    self._pause_menu_select_continue()
                    return
                elif self.currentstate == states.GameState.Overworld:
                    self.audio.play_sound(self.audio.select)
                    self._show_pause_menu()
                    return

        if self.menu:
            self._handle_menu_input(event)                                      # dan de menu's

    def _handle_menu_input(self, full_event):

        # todo, menu handler helemaal verbeteren
        # muziek later in laten komen?

        menu_choice = self.menu.handle_single_input(full_event)

        if self.currentstate == states.GameState.MainMenu:
            menu_keys = screens.menu.content.MainMenu()
            if menu_choice == menu_keys.NewGame:
                self._main_menu_select_new_game()
            elif menu_choice == menu_keys.LoadGame:
                self._main_menu_select_load_game()
            elif menu_choice == menu_keys.Options:
                self._main_menu_select_options()
            elif menu_choice == menu_keys.ExitGame:
                self._main_menu_select_exit_game()
            return

        elif self.currentstate == states.GameState.OptionsMenu:
            menu_keys = screens.menu.content.OptionsMenu()
            if menu_choice == menu_keys.Music:                             # .Music geeft de key "Music"
                self._options_menu_select_music()
            elif menu_choice == menu_keys.Sound:
                self._options_menu_select_sound()
            elif menu_choice == menu_keys.Back:
                self._options_menu_select_back()
            return

        elif self.currentstate == states.GameState.PauseMenu:
            menu_keys = screens.menu.content.PauseMenu()
            if menu_choice == menu_keys.ContinueGame:
                self._pause_menu_select_continue()
            elif menu_choice == menu_keys.SaveGame:
                self._pause_menu_select_save_game()
            elif menu_choice == menu_keys.Exit:
                self._pause_menu_select_main_menu()
            return

    def _show_main_menu(self, from_state):
        cur_item = 0
        if from_state is None:
            self.statemachine.push(states.GameState.MainMenu)
        elif from_state == states.GameState.OptionsMenu:
            cur_item = 2
        elif from_state == states.GameState.PauseMenu:
            self.scr_capt = None
            self.overworld = None
            self.statemachine.clear()
            self.statemachine.push(states.GameState.MainMenu)

        menu_items = screens.menu.content.MainMenu()
        self.menu = screens.menu.display.Display(self.screen, self.audio, menu_items, True, True, cur_item)

    def _main_menu_select_new_game(self):
        self.menu = None
        self.statemachine.pop(self.currentstate)
        self.statemachine.push(states.GameState.Overworld)
        self.overworld = screens.overworld.Overworld(self)

    def _main_menu_select_load_game(self):
        dialog = screens.loadsave.Dialog(self)
        self.overworld = screens.overworld.Overworld(self)                      # laad de overworld alvast
        if dialog.load() is None:
            self.overworld = None                                               # toch niet
        else:                                                                   # geef dan data mee aan de overworld
            self.audio.play_sound(self.audio.select)
            self.menu = None
            self.statemachine.pop(self.currentstate)
            self.statemachine.push(states.GameState.Overworld)
        pygame.event.clear()

    def _main_menu_select_options(self):
        self._show_options_menu()

    def _main_menu_select_exit_game(self):
        self.running = False

    def _show_options_menu(self):
        self.statemachine.push(states.GameState.OptionsMenu)
        # hier wordt de weergave van options gekozen
        menu_items = screens.menu.content.OptionsMenu(self.audio.music, self.audio.sound)
        self.menu = screens.menu.display.Display(self.screen, self.audio, menu_items, True, True)

    def _options_menu_select_music(self):
        settingview = self.menu.menu_texts[self.menu.cur_item]        # hier wordt de weergave
        settingview.flip_switch()                                     # later aangepast
        self.audio.flip_music()                                       # en de instelling zelf aangepast
        self.audio.write_cfg()                                        # en weggeschreven

    def _options_menu_select_sound(self):
        settingview = self.menu.menu_texts[self.menu.cur_item]
        settingview.flip_switch()
        self.audio.flip_sound()
        self.audio.write_cfg()

    def _options_menu_select_back(self):
        self.statemachine.pop(self.currentstate)
        self._show_main_menu(self.currentstate)

    def _show_pause_menu(self):
        scr_data = pygame.image.tostring(self.screen, 'RGBA')         # maak een screen capture
        self.scr_capt = pygame.image.frombuffer(scr_data, self.screen.get_size(), 'RGBA').convert()
        self.statemachine.push(states.GameState.PauseMenu)
        menu_items = screens.menu.content.PauseMenu()
        self.menu = screens.menu.display.Display(self.screen, self.audio, menu_items, False, False)

    def _pause_menu_select_continue(self):
        self.menu = None
        self.scr_capt = None
        self.statemachine.pop(self.currentstate)

    def _pause_menu_select_save_game(self):
        dialog = screens.loadsave.Dialog(self)
        if dialog.save():
            self.audio.play_sound(self.audio.select)
        pygame.event.clear()                                    # anders stapelen de geluiden zich op

    def _pause_menu_select_main_menu(self):
        self._show_main_menu(self.currentstate)

    @staticmethod
    def _kill_game():
        import sys
        pygame.quit()
        sys.exit()
