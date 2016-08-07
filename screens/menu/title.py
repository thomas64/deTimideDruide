
"""
class: MenuTitle
"""

import pygame

TITLETEXT = "De Timide Druïde"
TITLEFONT = 'colonna'
TITLEFONTSIZE = 150
TITLEFONTCOLOR = pygame.Color("gray12")
TITLEPOSX = 10
TITLEPOSY = 10

SUBTEXT = ""
SUBFONT = None
SUBFONTSIZE = 50
SUBFONTCOLOR = pygame.Color("gray36")
SUBPOSX = 200
SUBPOSY = 160

VERSIONTEXT = "Speciale (Uitgeklede) Noppe Event Editie pyRPG v1.03"
VERSIONFONT = 'verdana'
VERSIONFONTSIZE = 12
VERSIONFONTCOLOR = pygame.Color("white")
VERSIONPOSX = -350
VERSIONPOSY = -20


class Title(object):
    """
    De mainmenu titel.
    """
    def __init__(self, title=TITLETEXT, sub=SUBTEXT):
        self.titlefont = pygame.font.SysFont(TITLEFONT, TITLEFONTSIZE)
        self.subfont = pygame.font.SysFont(SUBFONT, SUBFONTSIZE)
        self.versionfont = pygame.font.SysFont(VERSIONFONT, VERSIONFONTSIZE)
        self.title = self.titlefont.render(title, True, TITLEFONTCOLOR).convert_alpha()
        self.sub = self.subfont.render(sub, True, SUBFONTCOLOR).convert_alpha()
        self.version = self.versionfont.render(VERSIONTEXT, True, VERSIONFONTCOLOR).convert_alpha()

    def render(self, screen):
        """
        Tekent de titel op de screen.
        :param screen: self.screen van de menuscreen
        """
        screen.blit(self.title, (TITLEPOSX, TITLEPOSY))
        screen.blit(self.sub, (SUBPOSX, SUBPOSY))
        screen.blit(self.version, (screen.get_width() + VERSIONPOSX, screen.get_height() + VERSIONPOSY))
