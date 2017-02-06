
"""
class: TextEventDatabase
"""

import enum

HEROFACEPATH = 'resources/sprites/heroes/'
ALAGOS = HEROFACEPATH+"01f_alagos.png"


class TextEventDatabase(enum.Enum):
    """
    Er zijn meerdere messageboxen mogelijk als de verschillende teksten in meerdere lijsten staan.
    condition moet altijd True of een methode zijn, anders wordt hij niet uitgevoerd.
    """

    # noinspection PyMethodMayBeStatic
    def condition1(self, data):
        """
        Moet als aparte methode. Kon niet als lambda achter 'condition=' vanwege pickle save error.
        Het is eigenlijk een static, maar die is niet callable vanuit window, daarom geen static gemaakt.
        """
        return data.party.contains('luana')

    text2 = dict(condition=condition1,
                 text=[["hoi1"], ["hoi2"]],
                 face=[ALAGOS, HEROFACEPATH+"02f_luana.png"])
    text3 = dict(condition=True,
                 text=[["Kendall!"], ["Kendall!!"], ["Where are you?!"],
                       ["You're wife is looking for you!"], ["KENDALL!!"]],
                 face=[ALAGOS, ALAGOS, ALAGOS, ALAGOS, ALAGOS])
    text4 = dict(condition=True,
                 text=[["Where is he?"], ["He must be somewhere around here..."]],
                 face=[ALAGOS, ALAGOS])

    text1 = dict(condition=True,
                 text=[
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
                 ],
                 face=[ALAGOS, ALAGOS, ALAGOS, ALAGOS, ALAGOS])
