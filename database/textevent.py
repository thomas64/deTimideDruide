
"""
class: TextEventDatabase
"""

import enum

HEROFACEPATH = 'resources/sprites/heroes/'
ALAGOS = HEROFACEPATH+"01f_alagos.png"
DRUIDE = 'resources/sprites/npcs/druid01f.png'
THOMAS = 'resources/sprites/npcs/thomas01f.png'
YMIR = 'resources/sprites/npcs/troll02f.png'
TROL = 'resources/sprites/npcs/troll01f.png'
HERNE = 'resources/sprites/npcs/man53f.png'
LODEWIJK = 'resources/sprites/npcs/man50f.png'
PUTSI = 'resources/sprites/npcs/oldwoman01f.png'
DRUIDE2 = 'resources/sprites/npcs/druid02f.png'


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

    def condition15(self, data):
        if data.logbook['quest8'].is_rewarded() and data.logbook['quest9'].is_unknown():
            return True
        else:
            return False

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
                     "Jaaaaa. Het duurt lang, heel lang."],
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
                     ["Kraaa. Die steen waar de barman het over heeft. Kraa.",
                      "We moeten die zien te vinden."],
                     ["Jaaa. Bij zijn kasteel is de steen begraaaaven.",
                      "Baaaato is zijn naaaaam."],
                     ["Ga vlug de kaaaart bekijken en gaaa ook datgene hier",
                      "binnen zoeken wat de barman zei over de soep."]
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
                      "Is het eetbaaaar? Dan is het de moeite waaaaard."],
                     ["Het recept zit nu in je 'Inventory'.",
                      "Deze is benaderbaar met de 'I' knop.",
                      "In je Inventory kun je het recept aanklikken",
                      "om het in te zien. Belangrijk! Vergeet dat niet."]
                 ],
                 face=[ALAGOS, ALAGOS, ALAGOS, ALAGOS, THOMAS])

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
                       "maar niemand over mijn dorst."],
                      ["Oké teamgenoten, soort van goed nieuws.",
                       "We hebben 'geluk'. Zwammix is nu dronken en dus praatgraag.",
                       "We moeten van dit moment gebruik maken om nu zoveel",
                       "mogelijk uit deze timide druïde te halen."],

                  ],
                  face=[ALAGOS, ALAGOS, DRUIDE, DRUIDE, DRUIDE, DRUIDE, ALAGOS, ALAGOS, DRUIDE, ALAGOS])

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
                      ["Aaaaaaahaaaa! Nu weet ik het! Zijn wijn is op.",
                       "Hij mag dan nu wel weer nuchter zijn,",
                       "maar zonder zijn wijn, is hij weer timide."],
                      ["Ik ben bang dat we hem weer dronken zullen moeten gaan voeren."],
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
                      ["Zwammix maakte zijn soep, en is nu spraakzaam als nooit tevoren.",
                       "Nu het voortbestaan van het ambacht 'druïde' is veiliggesteld met",
                       "negen vers klaargestoomde druïdes heeft hij ervoor gekozen zijn",
                       "carrière voort te zetten in de rap scene.",
                       "Wel blijft hij nog parttime zorg dragen voor alle bewoners van het Moezeldal.",
                       "De wijn heeft hij sindsdien niet meer aangeraakt.",
                       "Zijn lever is bijna weer hersteld."],
                      ["Ymir nam weer de leiding over de trollen van het Moezeldal.",
                       "Na deze ervaring is hij een klein beetje minder dom,",
                       "wetende dat de druïde het beste voor heeft met de trollen.",
                       "Slapen heeft hij sindsdien niet meer gedaan,",
                       "net als overigens alle andere moezeldaltrollen."],
                      ["Tully en de andere trollen hebben nog weken last gehad van hun darmen.",
                       "Het trollenbos is hierdoor in geen tijden zo vruchtbaar geweest als nu.",
                       "Na een bezoekje aan de druïde is hun stoelgang weer de oude geworden."],
                      ["Herne kon na lange tijd zijn vriendschap met Ymir weer oppakken.",
                       "Eens per twee weken trekken zij er op uit om te jagen."],
                      ["Lodewijk deed goede zaken met zijn Brasserie Altena.",
                       "Zijn nakomelingen hebben de brasserie uitgebouwd tot wat het nu is.",
                       "U kunt hier nog altijd terecht voor uw feesten en partijen."],
                      ["Het oude vrouwtje kon na herenigd te zijn met haar Putsi rusten.",
                       "Zij stierf met Putsi in haar armen."],
                      ["Grandprix bleef nog lang druïde.",
                       "Hij heeft zich gestort op het ontwikkelen van een zeer snelle formule.",
                       "Vandaag de dag staat deze formule nog steeds bekend als de Formule 1."],
                      ["Brann heeft nog jaren lang met Zwammix opgetrokken.",
                       "Ze hadden na al die jaren stilte samen nog een hoop te bespreken."],
                      [" . . . . . . . . "],
                      ["En jullie? Jullie mogen jezelf nu druïde noemen.",
                       "Na dit spannende avontuur zijn jullie nu zeker los vertrouwd.",
                       "En onthoudt! Wij maken deel uit van het geheel, 'het universum'.",
                       "Onze taak moet zijn dat we onze cirkel van compassie vergroten,",
                       "zodat alle levende wezens en de gehele natuur in al haar schoonheid",
                       "erdoor omvat worden."],
                      ["Bedankt voor het spelen!"]
                  ],
                  face=[THOMAS, THOMAS, THOMAS, DRUIDE, YMIR, TROL, HERNE, LODEWIJK, PUTSI, DRUIDE2, ALAGOS,
                        DRUIDE, DRUIDE, THOMAS])

    text15 = dict(condition=condition15,
                  text=[["Nee, we moeten eerst naar Zwammix gaaaaan!",
                         "Hij alleen kan ons helpen met de trollen."]],
                  face=ALAGOS)

    text16 = dict(condition=True,
                  text=[["Kraaaa. Laaaaten we eerst hier rechts gaan."],
                        ["Het bos daar heeft een hoop goede ingrediënten."]],
                  face=[ALAGOS, ALAGOS])


for text in TextEventDatabase:
    if type(text.value['face']) == str:  # als het nog geen list is, zet het om naar een list van faces.
        size = len(text.value['text'])
        text.value['face'] = [text.value['face']] * size
