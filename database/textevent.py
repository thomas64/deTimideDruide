
"""
class: TextEventDatabase
"""

import enum

HEROFACEPATH = 'resources/sprites/heroes/'
ALAGOS = HEROFACEPATH+"01f_alagos.png"


# noinspection PyMethodMayBeStatic,PyMissingOrEmptyDocstring
class TextEventDatabase(enum.Enum):
    """
    Er zijn meerdere messageboxen mogelijk als de verschillende teksten in meerdere lijsten staan.
    condition moet altijd True of een methode zijn, anders wordt hij niet uitgevoerd.
    """

    def condition1(self, data):
        """
        Moet als aparte methode. Kon niet als lambda achter 'condition=' vanwege pickle save error.
        Het is eigenlijk een static, maar die is niet callable vanuit window, daarom geen static gemaakt.
        """
        return data.party.contains('luana')

    def condition2(self, data):
        return data.kaart_bekeken

    def condition3(self, data):
        return data.barman_gepraat

    def condition4(self, data):
        return not data.barman_gepraat

    def condition5(self, data):
        return data.recept_bekeken

    def condition6(self, data):
        return data.orakelsteen_gevonden

    text99 = dict(condition=condition1,
                  text=[["hoi1"], ["hoi2"]],
                  face=[ALAGOS, HEROFACEPATH+"02f_luana.png"])

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
                     "op zoek naar de druïde. Jaaa."],
                    ["Hij heeft jullie nodig. Kraaa. ",
                     "Verzamel je team bijeen! ",
                     "Ik gaaaa met jullie mee.",
                     "Kom! Er is geen tijd te verliezen!",
                     "Ga gauw naar binnen hier. Kraaa."]
                 ],
                 face=ALAGOS)

    text2 = dict(condition=condition2,
                 text=[
                     ["Jaaa. Deze kaart moet het zijn. Kraaa.",
                      "Trek van plaats naar plaats 1 rechte lijn."]
                 ],
                 face=ALAGOS)

    text3 = dict(condition=condition3,
                 text=[
                     ["Kraaa. Die stenen waar de barman het over heeft. Kraa.",
                      "We moeten die zien te vinden."],
                     ["Jaaa. Bij zijn kasteel zijn de stenen begraaaaven.",
                      "Baaaato is zijn naaaaam."],
                     ["Kraaa. Laaaten we gaaaaan."]
                 ],
                 face=ALAGOS)

    text4 = dict(condition=condition4,
                 text=[
                     ["Nee, gaaaa nog niet weg.",
                      "Vergeet niet eerst met de barman te praaaten."]
                 ],
                 face=ALAGOS)

    text5 = dict(condition=condition5,
                 text=[
                     ["Jaaa. Dit is van het recept van de druïde. Kraaa.",
                      "We moeten zoveel mogelijk ingrediënten zien te verzaaaamelen voor de druïde."],
                     ["Kraaa. Maaar het recept is niet compleet. Jaaa.",
                      "Om de zwammix te laten smaaaken, zijn deze ingrediënten niet genoeg."],
                     ["Voor de smaaaaak kunnen we veel meer ingrediënten gebruiken uit de naaatuur.",
                      "Nee geen winkel of markt. Kraaa. De natuur."],
                     ["Zoek in het bos, op de akker en in elke boomgaaaaard.",
                      "Is het eetbaaaar? Dan is het de moeite waaaaard."]
                 ],
                 face=ALAGOS)

    text6 = dict(condition=condition6,
                 text=[
                     ["Wat een mooie kei. Kraaa.",
                      "Die zou in mijn tuintje niet misstaan. Jaaa."]
                 ],
                 face=ALAGOS)


for text in TextEventDatabase:
    if type(text.value['face']) == str:  # als het nog geen list is, zet het om naar een list van faces.
        size = len(text.value['text'])
        text.value['face'] = [text.value['face']] * size