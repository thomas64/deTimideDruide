
"""
class: PouchItemDatabase
"""

import enum
import os

POUCHPATH = "resources/sprites/icons/pouch"

GOLDIMG = os.path.join(POUCHPATH, "gold.png")
HERBIMG = os.path.join(POUCHPATH, "herbs.png")
SPICEIMG = os.path.join(POUCHPATH, "spices.png")
GEMSTONEIMG = os.path.join(POUCHPATH, "gemstones.png")
NOTEPIMG = os.path.join(POUCHPATH, "note.png")

GRAPESPATH = "resources/sprites/icons/pouch/grapes.png"
WINEPATH = "resources/sprites/icons/pouch/wine.png"
SHROOMSPATH = "resources/sprites/icons/pouch/shrooms.png"
CAULDRONPATH = "resources/sprites/icons/pouch/cauldron.png"


class PouchItemDatabase(enum.Enum):
    """..."""
    gold = dict(nam="Gold",                 srt=1, spr=GOLDIMG)
    herbs = dict(nam="Herbs",               srt=2, spr=HERBIMG)
    spices = dict(nam="Spices",             srt=3, spr=SPICEIMG)
    gemstones = dict(nam="Gemstones",       srt=4, spr=GEMSTONEIMG)
    proofnote = dict(nam="Proofnote",       srt=5, spr=NOTEPIMG)

    grapes = dict(nam="Grapes",  srt=4, spr=GRAPESPATH)
    wine = dict(nam="Wine",      srt=5, spr=WINEPATH)
    shroom = dict(nam="Shrooms", srt=6, spr=SHROOMSPATH)
    cauldron = dict(nam="Magic Cauldron", srt=7, spr=CAULDRONPATH)
