
"""
class: NoteDatabase
"""

import enum

PATH = 'resources/images/'


class NoteDatabase(enum.Enum):
    """
    Er zijn meerdere messageboxen mogelijk als de verschillende teksten in meerdere lijsten staan.
    Single plaatjes zijn ook mogelijk, maar dan moet het een string zijn.
    """
    # invernia_inn_1f
    note1 = [["You shouldn't read other people's mail."]]
    note2 = [["The cup seems to be empty."]]
    # invernia_inn_2f
    note3 = PATH+'landkaart.jpg'
    # invernia_guild
    note4 = [["You found a secret book."],
             ["But there are no pages..."]]
    # ersin_forest
    note5 = [["There is a small note pinned to the tent:"],
             ["I'm out admiring the scenery.",
              "I'll be back...",
              " ",
              "                      John the Hiker"]]
    note6 = [["What a strange statue...",
              "You might wonder what it's here for."]]
    note7 = [["That's right, it's a pole sticking out of the water."]]


    note10 = [["Gallia Belgica"]]
    note11 = [["Naar de klokkentoren"]]

    note13 = [["Hier rust Bato."],
              ["Door de code van een steen",
               "gaat een wijs man heen."],
              ["((B+C+M) x (H+L)) - (I/K) - (J/(E+F+G))",
               "= afstand"]]

    note15 = [["Stelen doen we niet he!"]]
    note16 = [["Je bent een prachtig persoon."]]
    note17 = [["Er staan letters in dit boek..."],
              ["Zou het iets kunnen betekenen?"]]
    note18 = [["De pot is leeg."]]
    note19 = [["De put is leeg."]]

    note20 = [["Prijzenkluis 1e plaats"]]
    note21 = [["Prijzenkluis 2e plaats"]]
    note22 = [["Prijzenkluis 3e plaats"]]
    note23 = [["Prijzenkluis 4e plaats"]]

    note32 = PATH+'wijnstreek.png'
    note33 = PATH+'planten1.png'
    note34 = PATH+'planten2.png'
    note35 = PATH+'knopen1.png'
    note36 = PATH+'knopen2.png'
    note37 = PATH+'knopen3.png'
    note38 = PATH+'insecten.png'

    note40 = [["Dit lijkt op het boek waar alle reserveringen in staan."]]
    note41 = [["Wijsheid verwerven: het is zoveel beter dan goud."]]
    note42 = [["Wat een hoop zangbundels."]]
    note43 = [["Een vlinder kan niet zonder vleugels."],
              ["Een ijsbeer kan niet zonder kou."],
              ["En ik..."],
              ["ik kan niet zonder jou."]]
    note44 = [["Dankjewel Herne.",
               "We hebben hier een weekendje heerlijk bij kunnen komen in het mooie Cochem.",
               "De kamer was schoon en netjes, en het eten heerlijk.",
               "We komen graag nog een keer langs.",
               "Tot gauw!",
               "Truus en Gerard"]]
    note45 = [["Zie erop toe dat niemand kwaad met kwaad vergeldt en streef",
               "altijd naar het goede, zowel voor elkaar als voor ieder ander."]]
    note46 = [["Goede raad ligt op de bodem van een mensenhart,",
               "als water in een diepe put, wie inzicht heeft weet eruit te putten."]]
    note47 = [["Hier vereren wij Baäl en Astarte."]]
    note48 = [["Aantekeningen van het spel De Timide Druïde"]]
    note49 = [["'Op het vergeten terug te brengen van een boek staat een boete van 1349 goud per dag.'"],
              ["Hmmm... Deze bibliotheek zal wel rijk zijn."]]
    note50 = [["Je gaat toch niet post van de koning zitten lezen?"]]
    note51 = [["Dat ziet eruit als een interessant wetsvoorstel."]]
    note52 = [["Goud maakt niet gelukkig."]]
