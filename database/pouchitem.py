
"""
class: PouchItemDatabase
"""

import enum
import os

from constants import EquipmentType


POUCHPATH = "resources/sprites/icons/pouch"

GOLDIMG = os.path.join(POUCHPATH, "gold.png")
HERBIMG = os.path.join(POUCHPATH, "herbs.png")
SPICEIMG = os.path.join(POUCHPATH, "spices.png")
GEMSTONEIMG = os.path.join(POUCHPATH, "gemstones.png")
POTIONBLUE = os.path.join(POUCHPATH, "potion_blue.png")
POTIONGREEN = os.path.join(POUCHPATH, "potion_green.png")
POTIONPURPLE = os.path.join(POUCHPATH, "potion_purple.png")
POTIONRED = os.path.join(POUCHPATH, "potion_red.png")
POTIONWHITE = os.path.join(POUCHPATH, "potion_white.png")
POTIONYELLOW = os.path.join(POUCHPATH, "potion_yellow.png")

NOTEPIMG = os.path.join(POUCHPATH, "note.png")

GRAPESPATH = "resources/sprites/icons/pouch/grapes.png"
WINEPATH = "resources/sprites/icons/pouch/wine.png"
SHROOMSPATH = "resources/sprites/icons/pouch/shrooms.png"
CAULDRONPATH = "resources/sprites/icons/pouch/cauldron.png"


class PouchItemDatabase(enum.Enum):
    """..."""
    gold = dict(nam="Gold",           srt=1,  spr=GOLDIMG,
                desc="Gold can be used to pay for goods or services.")
    herbs = dict(nam="Herbs",         srt=2,  spr=HERBIMG,        val=1,
                 desc="Herbs are used in magical spells and in creating potions. "
                      "They also contain healing possibilities.")
    spices = dict(nam="Spices",       srt=3,  spr=SPICEIMG,       val=1,
                  desc="Spices are used in magical spells and in creating potions.")
    gemstones = dict(nam="Gemstones", srt=4,  spr=GEMSTONEIMG,    val=1,
                     desc="Gemstones are used in magical spells and in creating potions.")

    proofnote = dict(nam="Proofnote", srt=21, spr=NOTEPIMG,
                     desc="A written note that says that you are not a monster.")

    hlg_pot = dict(nam="Healing Potion",      srt=5, spr=POTIONBLUE,    val=4,  hrb=3, spc=0, gms=0, alc=1,
                   desc="Restores a fifth of the drinker's lost Endurance and Stamina. Creating a "
                        "Healing Potion requires 3 Herbs and an Alchemist rank of at least 1.")
    cur_pot = dict(nam="Curing Potion",       srt=6, spr=POTIONBLUE,    val=8,  hrb=3, spc=2, gms=0, alc=3,
                   desc="A more powerful version of the Healing Potion, restores a third of the "
                        "drinker's lost Endurance and Stamina. Creating a "
                        "Curing Potion requires 3 Herbs, 2 Spices and an Alchemist rank of at least 3.")
    sta_pot = dict(nam="Stamina Potion",      srt=7, spr=POTIONWHITE,   val=11, hrb=4, spc=2, gms=0, alc=5,
                   desc="Restores all Stamina to the drinker. Creating a "
                        "Stamina Potion requires 4 Herbs, 2 Spices and an Alchemist rank of at least 5.")
    res_pot = dict(nam="Restore Potion",      srt=8, spr=POTIONWHITE,   val=15, hrb=5, spc=3, gms=0, alc=7,
                   desc="Restores full health to the drinker. Creating a "
                        "Restore Potion requires 5 Herbs, 3 Spices and an Alchemist rank of at least 7.")

    fir_flk = dict(nam="Fire Flask",          srt=9,  spr=POTIONRED,    val=4,  hrb=0, spc=1, gms=2, alc=1,
                   desc="A sticky, incendiary liquid that bursts into flame on contact with air. Creating a "
                        "Fire Flask requires 1 Spice, 2 Gemstones and an Alchemist rank of at least 1.")
    inf_flk = dict(nam="Inferno Flask",       srt=10, spr=POTIONRED,    val=9,  hrb=0, spc=3, gms=3, alc=3,
                   desc="A more powerful version of the Fire Flask. A sticky, incendiary liquid that bursts "
                        "into flame on contact with air. Creating an "
                        "Inferno Flask requires 3 Spices, 3 Gemstones and an Alchemist rank of at least 3.")
    acd_flk = dict(nam="Acid Flask",          srt=11, spr=POTIONGREEN,  val=10, hrb=0, spc=2, gms=3, alc=5,
                   desc="This vicious fluid eats into the flesh of any creature it touches, doing continuous damage. "
                        "Creating an "
                        "Acid Flask requires 2 Spices, 3 Gemstones and an Alchemist rank of at least 5.")
    slp_flk = dict(nam="Sleep Gas Flask",     srt=12, spr=POTIONGREEN,  val=13, hrb=3, spc=0, gms=3, alc=7,
                   desc="A liquid that vaporizes when exposed to air, forming a gas that drains the "
                        "mobility of those who breathe it. Creating a "
                        "Sleep Gas Flask requires 3 Herbs, 3 Gemstones and an Alchemist rank of at least 7.")

    ant_pot = dict(nam="Antidote Potion",     srt=13, spr=POTIONYELLOW, val=5,  hrb=1, spc=2, gms=0, alc=2,
                   desc="Halts the effects of poison, but does not restore damage already inflicted by poison. "
                        "Creating an "
                        "Antidote Potion requires 1 Herb, 2 Spices and an Alchemist rank of at least 2.")
    prt_pot = dict(nam="Protection Potion",   srt=14, spr=POTIONPURPLE, val=8,  hrb=2, spc=3, gms=1, alc=2,
                   desc="Temporarily increases the Protection of the drinker by 5 points during 1 battle. Creating a "
                        "Protection Potion requires 2 Herbs, 3 Spices, 1 Gemstone and an Alchemist rank of at least 2.")
    int_pot = dict(nam="Intelligence Potion", srt=15, spr=POTIONPURPLE, val=12, hrb=2, spc=1, gms=3, alc=6,
                   desc="Temporarily increases the Intelligence of the drinker by 5 points during 1 battle. Creating a "
                   "Intelligence Potion requires 2 Herbs, 1 Spice, 3 Gemstones and an Alchemist rank of at least 6.")
    wil_pot = dict(nam="Willpower Potion",    srt=16, spr=POTIONPURPLE, val=12, hrb=3, spc=2, gms=1, alc=6,
                   desc="Temporarily increases the Willpower of the drinker by 5 points during 1 battle. Creating a "
                        "Willpower Potion requires 3 Herbs, 2 Spices, 1 Gemstone and an Alchemist rank of at least 6.")
    dex_pot = dict(nam="Dexterity Potion",    srt=17, spr=POTIONPURPLE, val=12, hrb=1, spc=3, gms=2, alc=6,
                   desc="Temporarily increases the Dexterity of the drinker by 5 points during 1 battle. Creating a "
                        "Dexterity Potion requires 1 Herb, 3 Spices, 2 Gemstones and an Alchemist rank of at least 6.")
    agi_pot = dict(nam="Agility Potion",      srt=18, spr=POTIONPURPLE, val=12, hrb=3, spc=1, gms=2, alc=6,
                   desc="Temporarily increases the Agility of the drinker by 5 points during 1 battle. Creating a "
                        "Agility Potion requires 3 Herbs, 1 Spice, 2 Gemstones and an Alchemist rank of at least 6.")
    str_pot = dict(nam="Strength Potion",     srt=19, spr=POTIONPURPLE, val=12, hrb=1, spc=2, gms=3, alc=6,
                   desc="Temporarily increases the Strength of the drinker by 5 points during 1 battle. Creating a "
                        "Strength Potion requires 1 Herb, 2 Spices, 3 Gemstones and an Alchemist rank of at least 6.")
    stl_pot = dict(nam="Stealth Potion",      srt=20, spr=POTIONPURPLE, val=10, hrb=2, spc=2, gms=2, alc=4,
                   desc="Temporarily increases the Stealth rank of the drinker by 3 points during 1 battle. Creating a "
                        "Stealth Potion requires 2 Herbs, 2 Spices, 2 Gemstones and an Alchemist rank of at least 4.")

    # clarity_potion = dict(nam="Clarity Potion", srt=5, spr=REDPOTION, val=2,
    #                       desc="Temporarily improves the mental clarity of the character who drinks it, "
    #                            "assisting attempts to use the Loremaster skill. Creating a "
    #                            "Clarity Potion requires 3 Spices and an Alchemist rank of at least 3.")
    # charisma_potion = dict(nam="Charisma Potion", srt=5, spr=REDPOTION, val=2,
    #                        desc="Temporarily makes the drinker more charming and sociable, improving chances of "
    #                             "successfully using the Diplomacy skill. Creating a Charisma Potion "
    #                             "requires 1 Herb, 1 Gemstone, 2 Spices and an Alchemist rank of at least 2.")
    # defense_potion = dict(nam="Defense Potion", srt=5, spr=REDPOTION, val=2,
    #                       desc="Temporarily increases the defense (AP /armor protection) of the drinker, "
    #                            "reducing damage inflicted by opponents. Creating a "
    #                            "Defense Potion requires 2 Gemstones and an Alchemist rank of at least 2.")
    # restore_potion = dict(nam="Restore Potion", srt=5, spr=POTIONWHITE, val=2,
    #                       desc="In combat, this potion dispels the effects of Stupidity, Clumsiness, Debilitation, "
    #                            "Weakness, Exhaustion, and Wraith Touch. It has no effect out of combat. Creating a "
    #                            "Restore Potion requires 2 Gemstones, 2 Spices and an Alchemist rank of at least 3.")

    grapes = dict(nam="Grapes",                     srt=6, spr=GRAPESPATH,              desc="")
    wine = dict(nam="Wine",                         srt=7, spr=WINEPATH,                desc="")
    shroom = dict(nam="Shrooms",                    srt=8, spr=SHROOMSPATH,             desc="")
    cauldron = dict(nam="Magic Cauldron",           srt=9, spr=CAULDRONPATH,            desc="")

    # todo, methods hier definieren voor de potions hun werkingen.


for itm in PouchItemDatabase:
    itm.value['typ'] = EquipmentType.itm
