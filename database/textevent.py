
"""
class: TextEventDatabase
"""

import enum

HEROFACEPATH = 'resources/sprites/heroes/'
ALAGOS = HEROFACEPATH+"01f_alagos.png"
DRUIDE = 'resources/sprites/npcs/druid01f.png'


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
        import inventoryitems
        from .pouchitem import PouchItemDatabase
        recept1 = inventoryitems.factory_pouch_item(PouchItemDatabase.recept1)
        return data.pouch.contains(recept1, 1)

    def condition6(self, data):
        return data.orakelsteen_gevonden

    def condition8(self, data):
        return data.brug_opgelopen

    def condition11(self, data):
        import inventoryitems
        from .pouchitem import PouchItemDatabase
        negen_kleuren = inventoryitems.factory_pouch_item(PouchItemDatabase.kleuren_drankje)
        return data.pouch.contains(negen_kleuren, 1)

    def condition12(self, data):
        return data.logbook['quest10'].is_rewarded()

    def condition14(self, data):
        return data.uitgespeeld

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

    text7 = dict(condition=True,
                 text=[
                     ["Wacht! Wat we ook nodig hebben is waaaater."]
                 ],
                 face=ALAGOS)

    text8 = dict(condition=condition8,
                 text=[
                     ["We moeten waaaater uit de rivier.",
                      "Nee geen waaaater uit de kraaaaan.",
                      "Want dan gaaaat de druïde eraaaaan."],
                     ["Kraaa."],
                     ["Waaaaater van verschillende rivieren",
                      "zal de druïde erg plezieren."]
                 ],
                 face=ALAGOS)

    text9 = dict(condition=True,
                 text=[
                     ["Zie daaaaar is de Zwammix de druide."],
                     ["zzzZZZzzzZZZzzzZZZzzz"]
                 ],
                 face=[ALAGOS, DRUIDE])

    text10 = dict(condition=True,
                  text=[
                     ["Kraaaa! Toktoktok."], ["Waakker worden Zwaammix!"],
                     ["*HIPS*"], ["Brann! Mijn gevleugelde vriend.", "Daar ben je eindelijk."],
                     ["*HIPS*"], ["Heb je de personen gevonden die ik zocht?"],
                     ["Jaaaa. Meester."], ["Ik zie dat u weer te diep in het glaasje heeft gekeken?", "Kraa!"],
                     ["Maak je niet druk.",
                      "Ik heb altijd gedacht dat drinken slecht voor me was,",
                      "dus ik ben gestopt met denken.",
                      "Iedereen praat over mijn drinken,",
                      "maar niemand over mijn dorst."]
                  ],
                  face=[ALAGOS, ALAGOS, DRUIDE, DRUIDE, DRUIDE, DRUIDE, ALAGOS, ALAGOS, DRUIDE])

    text11 = dict(condition=condition11,
                  text=[
                      ["Kraaaa! De trollen zijn weer weg gegaaaaan.",
                       "En ze hebben de ketel niet laten staaaan."],
                      ["Wat moeten ze toch met die roestige ketel",
                       "van de druïde? Dit moet de druïde weten."]
                  ],
                  face=ALAGOS)

    text12 = dict(condition=condition12,
                  text=[
                      ["Kraaa! Nee niet weer. Hij is weer stil.",
                       "En we hebben nog steeds geen soep. Kraaa!"],
                      ["Hoe krijgen we hem weer aan de praat?"],
                      ["Aaaaaaahaaaa! Nu weet ik het! Zijn wijn was op.",
                       "Hij mag dan nu wel weer nuchter zijn,",
                       "maar zonder zijn wijn, is hij weer timide."],
                      ["Ik ben bang dat we hem weer dronken zullen moeten gaan voeren.",
                       "Voor nu laten we hem even met rust,",
                       "maar ik denk dat vanaf 15.00 uur vanmiddag",
                       "Zwammix wel weer een wijntje zal lusten."],
                      ["Jaaaaa. Kraaaaaa!"]
                  ],
                  face=ALAGOS)

    text13 = dict(condition=True,
                  text=[["*Grumble* Niet naar binnen jij!"]],
                  face='resources/sprites/npcs/troll01f.png')

    text14 = dict(condition=condition14,
                  text=[
                      ["Gefeliciteerd!"],
                      ["Je hebt dit spelverhaal tot een goed einde volbracht."],
                      ["De ketel en Zwammix leefden nog lang en gelukkig."],
                      [" . . . . . . . . "],
                  ],
                  face=[ALAGOS, ALAGOS, ALAGOS, DRUIDE])


for text in TextEventDatabase:
    if type(text.value['face']) == str:  # als het nog geen list is, zet het om naar een list van faces.
        size = len(text.value['text'])
        text.value['face'] = [text.value['face']] * size
