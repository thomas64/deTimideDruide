
"""
class: StatsBox
"""

# todo, de extra benodigde kolommen bekijken in vb en implementeren. ook de kolommen uit pyRPG1.

import pygame

BACKGROUNDCOLOR = pygame.Color("black")
LINECOLOR = pygame.Color("white")

FONTCOLOR1 = pygame.Color("white")
FONTCOLOR2 = pygame.Color("yellow")
FONT = 'impact'
LARGEFONTSIZE = 25
NORMALFONTSIZE = 15

POSCOLOR = pygame.Color("green")
NEGCOLOR = pygame.Color("red")


class StatsBox(object):
    """
    Alle weergegeven informatie van alle stats van een hero.
    """
    COLSY = 60
    COL1X = 50
    COL2X = 160
    COL3X = 200
    LINEH = 22

    def __init__(self, position):
        self.surface = pygame.Surface((405, 500))
        self.surface = self.surface.convert()
        self.rect = self.surface.get_rect()
        self.rect.topleft = position

        self.background = pygame.Surface(self.surface.get_size())
        self.background.fill(BACKGROUNDCOLOR)
        self.background = self.background.convert()

        self.largefont = pygame.font.SysFont(FONT, LARGEFONTSIZE)
        self.normalfont = pygame.font.SysFont(FONT, NORMALFONTSIZE)

        self.cur_item = None

    def _update(self, hero):
        self.title = self.largefont.render("Stats", True, FONTCOLOR1)

        # zet eerst even wat bepaalde waarden vast.
        if hero.lev.qty >= hero.lev.MAX:
            hero_exp_tot = "Max"
            hero_lev_next = "Max"
        else:
            hero_exp_tot = str(hero.exp.tot)
            hero_lev_next = str(hero.lev.next(hero.exp.tot))

        # zet dan alles in deze tabel met vijf kolommen. de vierde kolom is leeg voor de rects van de eerste kolom
        # todo, testen hoe dit: hero.war.bonus(hero.wpn), gaat met hero zonder wapen. bonus() checken.
        self.table_data = [
            ["XP Remaining :", str(hero.exp.rem),       "",                        None,    ""],
            ["Total XP :",     str(hero_exp_tot),       "",                        None,    ""],
            ["Next Level :",   str(hero_lev_next),      "",                        None,    ""],
            ["",               "",                      "",                        None,    ""],
            ["Weight :",       str(hero.tot_wht),       "",                        None,    self._desc('wht')],
            ["Movepoints :",   str(hero.sta_mvp),       hero.dif_mvp,              None,    self._desc('mvp')],
            ["Protection :",   str(hero.prt),           hero.sld_prt,              None,    ""],
            ["Defense :",      str(hero.tot_des),       "",                        None,    ""],
            ["Base Hit :",     str(hero.tot_hit)+" %",  hero.war.bonus(hero.wpn),  None,    ""],
            ["Damage :",       str(hero.tot_dam),       "",                        None,    ""],
            ["",               "",                      "",                        None,    ""],
        ]
        # voeg ook de 7 stats aan de table_data toe
        for stat in hero.stats_tuple:
            self.table_data.append(
                [str(stat.NAM) + " :",  str(stat.qty),  stat.ext,   None,   stat.DESC]
            )

        # vul de vierde lege kolom. hierin staan de rects van de eerste kolom. rect is voor muisklik.
        for index, row in enumerate(self.table_data):
            row[3] = self._rect(index, row[0])

        # maak dan een nieuwe tabel aan met de tekst, maar dan gerendered.
        self.table_view = []
        for index, row in enumerate(self.table_data):
            self.table_view.append(list())
            if index == self.cur_item:              # als de index van deze rij gelijk is aan waar de muis over zit,
                color = FONTCOLOR2                  # maak hem geel
            else:                                   # anders gewoon wit.
                color = FONTCOLOR1
            self.table_view[index].append(self.normalfont.render(row[0], True, color))
            self.table_view[index].append(self.normalfont.render(row[1], True, FONTCOLOR1))
            self._line(row[2], self.table_view[index])

    def _rect(self, index, text):
        """
        self.rect is de hele box zelf. Die heeft ook een position op het scherm, vandaar dat de position een soort
        offset moet krijgen hier.
        """
        rect = self.normalfont.render(text, True, FONTCOLOR1).get_rect()
        rect.topleft = self.rect.left + self.COL1X, (self.rect.top + self.COLSY) + index * self.LINEH
        return rect

    def _line(self, value, col):
        """
        Geef een regel in een kolom een bepaalde format en kleur mee aan de hand van de waarde.
        :param value: dit is een van die waarden
        :param col: in welke kolom de regel zich bevind
        """
        if value == "":
            value = 0
        if value == 0:
            value = ""
            col.append(self.normalfont.render(value, True, FONTCOLOR1))
        elif value > 0:
            value = "(+"+str(value)+")"
            col.append(self.normalfont.render(value, True, POSCOLOR))
        elif value < 0:
            value = "("+str(value)+")"
            col.append(self.normalfont.render(value, True, NEGCOLOR))

    def draw(self, screen, hero):
        """
        Update eerst de data, en teken dan al die data op de surface en die op de screen.
        Let op: self.table_view bevat maar 3 kolommen in tegenstelling tot self.table_data met 5
        :param screen: self.screen van partyscreen
        :param hero: de huidige geselecteerde hero
        """
        self._update(hero)

        self.surface.blit(self.background, (0, 0))
        pygame.draw.rect(self.background, LINECOLOR, self.surface.get_rect(), 1)

        self.surface.blit(self.title, (7, 1))
        for index, row in enumerate(self.table_view):
            self.surface.blit(row[0], (self.COL1X, self.COLSY + index * self.LINEH))
        for index, row in enumerate(self.table_view):
            self.surface.blit(row[1], (self.COL2X, self.COLSY + index * self.LINEH))
        for index, row in enumerate(self.table_view):
            self.surface.blit(row[2], (self.COL3X, self.COLSY + index * self.LINEH))

        screen.blit(self.surface, self.rect.topleft)

    def mouse_hover(self, event):
        """
        Als de muis over een item in uit de eerste visuele gaat. row[3] dat zijn de rects.
        Zet cur_item op de index van degene waar de muis over gaat.
        :param event: pygame.MOUSEMOTION uit engine.py
        :return: row[4] is de kolom met de info.
        """
        self.cur_item = None
        for index, row in enumerate(self.table_data):
            if row[3].collidepoint(event.pos):
                self.cur_item = index
                return row[4]

    @staticmethod
    def _desc(stat):
        if stat == 'wht':
            return (
                "Weight:",
                "Defines how heavy your character is equipped with gear.",
                "Weight has negative impact on movepoints and agility."
            )

        if stat == 'mvp':
            return (
                "Movepoints:",
                "Defines how many steps are your character is able to take in one turn.",
                "The more stamina your character has, the more movepoints.",
                "The more weight your character has, the less movepoints.",
                "The first column shows the number of movepoints calculated from your stamina.",
                "The second (red) column shows the calculated weight subtracted."
            )
