
"""
class: ConfirmBox
"""

import pygame

import audio as sfx
import components
import keys
import statemachine

BACKGROUNDCOLOR = pygame.Color("black")

FONT = None
FONTSIZE = 30
FONTCOLOR1 = pygame.Color("black")
FONTCOLOR2 = pygame.Color("red")
FONTPOSX = 40
FONTPOSY = 40
LINEHEIGHT = 25

TOPINDEX = 2

MESSAGESPRITE = 'resources/sprites/parchment.png'


class ConfirmBox(object):
    """
    Geeft een selectie weer op het scherm.
    """
    def __init__(self, gamestate, audio, raw_text):
        self.gamestate = gamestate
        self.audio = audio
        self.screen = pygame.display.get_surface()
        self.name = statemachine.States.MessageBox
        self.scr_capt = components.ScreenCapture()

        self.font = pygame.font.SysFont(FONT, FONTSIZE)
        self.raw_text = raw_text    # de onopgemaakte tekst
        self.vis_text = []          # de visuele tekst

        text_widths = []
        for row in raw_text:
            self.vis_text.append(self.font.render(row, True, FONTCOLOR1).convert_alpha())
            text_widths.append(self.font.render(row, True, FONTCOLOR1).get_width())
        box_width = max(text_widths) + FONTPOSX * 2
        box_height = len(self.vis_text) * LINEHEIGHT + FONTPOSY * 2

        self.surface = pygame.Surface((box_width, box_height))
        self.surface = self.surface.convert()
        self.rect = self.surface.get_rect()
        self.rect.center = (self.screen.get_width() / 2, self.screen.get_height() / 2)

        self.text_rects = []        # de text_rects om de tekst voor selecteren
        for index, row in enumerate(raw_text):
            self.text_rects.append(self._create_rect_with_offset(index, row))

        self.surface.fill(BACKGROUNDCOLOR)
        self.surface.set_colorkey(BACKGROUNDCOLOR)

        self.background = pygame.image.load(MESSAGESPRITE).convert_alpha()
        self.background = pygame.transform.scale(self.background, self.surface.get_size())

        self.cur_item = TOPINDEX

    def _create_rect_with_offset(self, index, text):
        """
        self.rect is de hele box zelf. Die heeft ook een position op het scherm, vandaar dat de position een soort
        offset moet krijgen hier.
        """
        text_rect = self.font.render(text, True, FONTCOLOR1).get_rect()
        text_rect.topleft = self.rect.left + FONTPOSX, self.rect.top + FONTPOSY + index * LINEHEIGHT
        return text_rect

    def on_enter(self):
        pass

    def on_exit(self):
        """
        Bij het sluiten van het venster.
        :return: geef de geselecteerde item terug
        """
        return self.cur_item

    def single_input(self, event):
        """
        Handelt de muis en keyboard input af.
        :param event: pygame.event.get()
        """
        if event.type == pygame.MOUSEMOTION:
            for index, item in enumerate(self.text_rects):
                if item.collidepoint(event.pos) and index >= TOPINDEX:
                    if self.cur_item != index:
                        self.cur_item = index
                    break

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == keys.LEFTCLICK:
                for index, item in enumerate(self.text_rects):
                    if item.collidepoint(event.pos) and index >= TOPINDEX:
                        self.gamestate.pop()

        elif event.type == pygame.KEYDOWN:
            if event.key == keys.EXIT:
                self.cur_item = TOPINDEX
                self.gamestate.pop()

            elif event.key in keys.SELECT:
                self.gamestate.pop()

            if event.key == keys.UP and self.cur_item > TOPINDEX:
                self.cur_item -= 1
            elif event.key == keys.UP and self.cur_item == TOPINDEX:
                self.audio.play_sound(sfx.MENUERROR)
                self.cur_item = TOPINDEX
            elif event.key == keys.DOWN and self.cur_item < len(self.raw_text) - 1:
                self.cur_item += 1
            elif event.key == keys.DOWN and self.cur_item == len(self.raw_text) - 1:
                self.audio.play_sound(sfx.MENUERROR)
                self.cur_item = len(self.raw_text) - 1

    def multi_input(self, key_input, mouse_pos, dt):
        pass

    def update(self, dt):
        """
        Herschrijf alle tekst opnieuw, maar nu met de geselecteerde item een ander kleur.
        :param dt:
        """
        self.vis_text = []          # de visuele tekst
        for index, row in enumerate(self.raw_text):
            if index == self.cur_item:
                self.vis_text.append(self.font.render(row, True, FONTCOLOR2).convert_alpha())
            else:
                self.vis_text.append(self.font.render(row, True, FONTCOLOR1).convert_alpha())

    def render(self):
        """
        Teken de tekst.
        """
        self.scr_capt.render()

        self.surface.blit(self.background, (0, 0))

        for i, line in enumerate(self.vis_text):
            self.surface.blit(line, (FONTPOSX, FONTPOSY + i * LINEHEIGHT))

        self.screen.blit(self.surface, self.rect.topleft)