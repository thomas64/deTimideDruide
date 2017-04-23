
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


    note9 = PATH+'recept1.png'
    note10 = [["Gallia Belgica"]]
    note11 = [["Naar de klokkentoren"]]

    note13 = [["Hier rust Bato."],
              ["Door de code van een steen",
               "gaat een wijs man heen."],
              ["((B+C+M) x (H+L)) - (I/K) - (J/(E+F+G))",
               "= afstand"]]

    note20 = [["Prijzenkluis 1e plaats"]]
    note21 = [["Prijzenkluis 2e plaats"]]
    note22 = [["Prijzenkluis 3e plaats"]]
    note23 = [["Prijzenkluis 4e plaats"]]
