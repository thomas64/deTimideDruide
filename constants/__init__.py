
"""
class: GameState
class: Direction
class: PersonState
class: HealingType
class: EquipmentType
class: WeaponType
class: ItemMaterial
class: SchoolType
class: Minimals
class: StatType
class: SkillType
class: SpellType
class: QuestType
class: QuestState
class: MapMusic
class: MapTitle
class: SFX
class: Keys
class: ColumnType
"""

import enum

import aenum
import pygame


class GameState(enum.Enum):
    """
    Alle states uit het spel.
    Diegene die strings zijn, worden gebruikt als menu titel in het spel.
    """
    MainMenu = 1
    LoadMenu = "Load Game"
    SaveMenu = "Save Game"
    SettingsMenu = 4
    PauseMenu = 5

    Overworld = 6
    Battle = 7
    Conversation = 8
    PartyScreen = 9
    MessageBox = 10
    ConfirmBox = 11
    Shop = 12
    FadeBlack = 13
    LoadScreen = 14


class Direction(enum.Enum):
    """
    De vier richtingen waarheen een unit kan lopen.
    """
    North = 1
    South = 2
    West = 3
    East = 4


class PersonState(enum.Enum):
    """
    Wat kan een NPC doen?
    """
    Resting = 1
    Moving = 2


class HealingType(enum.Enum):
    """
    Alle manieren voor een Healer Skill.
    """
    hands = "Lay on Hands"
    herbs = "Heal with Herbs"


class EquipmentType(enum.Enum):
    """
    Alle equipment typen op een rij.
    """
    wpn = "Weapon"
    sld = "Shield"
    hlm = "Helmet"
    amu = "Amulet"
    arm = "Armor"
    clk = "Cloak"
    brc = "Bracelet"
    glv = "Gloves"
    rng = "Ring"
    blt = "Belt"
    bts = "Boots"
    acy = "Accessory"
    # vreemde eend, alleen voor shop
    itm = "Pouch"


class WeaponType(enum.Enum):
    """
    Alle weapon types en shield op een rij.
    """
    swd = "Sword"
    haf = "Hafted"
    pol = "Pole"
    mis = "Missile"
    thr = "Thrown"
    shd = "Shield"


class ItemMaterial(enum.Enum):
    """
    Alle materialen op een rij.
    """
    ctn = "Cotton"
    ltr = "Leather"
    wdn = "Wooden"
    brz = "Bronze"
    irn = "Iron"
    stl = "Steel"
    slv = "Silver"
    tnm = "Titanium"


class SchoolType(enum.Enum):
    """
    De 7 wizard schools.
    """
    non = ""
    spl = "Special"
    ntl = "Neutral"
    elm = "Elemental"
    nmg = "Naming"
    ncy = "Necromancy"
    str = "Star"


class Minimals(enum.Enum):
    """
    Substring wordt gebruikt om de eerste 4 chars van de .name te halen.
    Substring wordt gebruikt om de eerste 5 chars van de .value te halen.
    """
    min_int = "Min. Intelligence"
    min_wil = "Min. Willpower"
    min_dex = "Min. Dexterity"
    min_str = "Min. Strength"
    min_wiz = "Min. Wizard"


class StatType(enum.Enum):
    """..."""
    wht = "Weight"
    mvp = "Movepoints"
    prt = "Protection"
    des = "Defense"
    hit = "Hit Chance"
    dam = "Damage"

    int = "Intelligence"
    wil = "Willpower"
    dex = "Dexterity"
    agi = "Agility"
    edu = "Endurance"
    str = "Strength"
    sta = "Stamina"


class SkillType(enum.Enum):
    """..."""
    alc = "Alchemist"
    dip = "Diplomat"
    hlr = "Healer"
    lor = "Loremaster"
    mec = "Mechanic"
    mer = "Merchant"
    ran = "Ranger"
    stl = "Stealth"
    thf = "Thief"
    trb = "Troubadour"
    war = "Warrior"
    wiz = "Wizard"
    haf = "Hafted"
    mis = "Missile"
    pol = "Pole"
    shd = "Shield"
    swd = "Sword"
    thr = "Thrown"


class SpellType(enum.Enum):
    """..."""
    dis_nmg = "Dispel Naming"
    dis_ncy = "Dispel Necro"
    dis_str = "Dispel Star"
    mir = "Mirror"
    vs_elm = "vs. Elemental"
    vs_nmg = "vs. Naming"
    vs_ncy = "vs. Necromancy"
    vs_str = "vs. Star"

    air_sld = "Air Shield"
    deb = "Debilitation"
    drg_flm = "Dragon Flames"
    ert_smt = "Earth Smite"
    frb = "Fireball"
    imo = "Immolation"
    lng = "Lightning"
    rem_psn = "Remove Poison"
    str = "Strength"
    wnd = "Wind"

    ban = "Banishing"
    brl = "Brilliance"
    edu = "Endurance"
    sen_aur = "Sense Aura"
    stp = "Stupidity"
    tlp = "Teleportation"
    wks = "Weakness"

    frz_dom = "Frozen Doom"
    sol_wrt = "Solar Wrath"
    stl_gty = "Stellar Gravity"
    wos = "Web of Starlight"
    wfi = "Whitefire"

    ctr_zom = "Control Zombies"
    hst = "Haste"
    wob = "Wall of Bones"
    spr_sld = "Spirit Shield"


class QuestType(enum.Enum):
    """..."""
    FetchItemQuest = 1
    ReceiveItemQuest = 2
    FetchItemsPartlyQuest = 3
    PersonMessageQuest1 = 4
    PersonMessageQuest2 = 5
    EnemyQuest = 9


class QuestState(enum.Enum):
    """
    De volgorde en de 0, 1, 2, 3, 4 worden in het spel gebruikt. Kan dus niet zomaar aangepast worden.
    Dit heeft met de tekst in QuestDatabase te maken en get_text() in QuestItem.
    """
    Unknown = 0
    Running = 1
    Ready = 2
    Finished = 3
    Rewarded = 4


class MapMusic(enum.Enum):
    """
    Alle tmx kaarten op een rij, met de muziek erachter en ambient sound.
    De key's komen precies overeen met de .tmx namen. De values[0] en [1] komen overeen met de .ogg namen.
    """
    waal_braserie          = "ersin_forest",      "birds"
    altena                 = "house",             "fire"
    waal_brug              = "ersin_forest",      "birds"
    batenburg_kasteel      = "kasteel_batenburg", "birds"
    batenburg_schuur       = "schuur_batenburg",  None
    batenburg_huis         = "huis_batenburg",    "fire"
    batenburg_kerker       = "schuur_batenburg",  None
    grensovergang          = "ersin_forest",      "birds"
    kruising               = "ersin_forest",      "birds"
    kruising_huisje        = "house",             "fire"
    gymnich                = "gymnich",           None
    gymnich_schuur         = "schuur_batenburg",  None
    gymnich_kerkje         = "kerkje_gymnich",    None
    romerkanal             = "ersin_forest",      "birds"
    romerkanal_hol         = "ersin_cave",        None
    romerkanal_huis_1f     = "house",             None
    romerkanal_huis_2f     = "house",             None
    kruising2              = "ersin_forest",      "birds"
    druide_bos             = "ersin_forest",      "birds"
    druide_grot1           = "ersin_cave",        None
    druide_grot2           = "ersin_cave",        None
    druide_grot3           = "house",             None
    trollen_bos            = "trollen_bos",       "river"
    trollen_grot           = "ersin_cave",        None
    piesport               = "invernia_town",     "town"
    piesport_bieb          = "house",             None
    piesport_bank          = "house",             None
    piesport_bank_kelder   = "schuur_batenburg",  None
    piesport_wijnproeverij = "house",             None
    piesport_inn_1f        = "house",             None
    piesport_inn_2f        = "house",             None
    piesport_winkel        = "house",             None
    cochem_bos             = "ersin_forest",      "birds"
    cochem                 = "invernia_town",     "town"
    cochem_kasteel         = "huis_batenburg",    "fire"
    cochem_kerk            = "kerkje_gymnich",    None
    cochem_huis_1f         = "house",             None
    cochem_huis_2f         = "house",             None
    cochem_huis_3f         = "schuur_batenburg",  None
    trier_bos2             = "ersin_forest",      "birds"
    trier_bos1             = "ersin_forest",      "birds"
    trier                  = "invernia_town",     "town"
    trier_theater          = "ersin_cave",        None
    trier_kerk1            = "kerkje_gymnich",    None
    trier_kerk2            = "kerkje_gymnich",    None
    trier_klokkentoren     = "kerkje_gymnich",    None


class MapTitle(aenum.NoAliasEnum):
    """
    Alle tmx kaarten op een rij, met de Titel hoe die in beeld komt erachter.
    Ze staan in een lijst, want later worden de tmx data's aan de lijst toegevoegd.
    De key's komen precies overeen met de .tmx namen.
    """
    waal_braserie          = ["De Waal"]
    altena                 = ["Braserie Altena"]
    waal_brug              = ["De Waal"]
    batenburg_kasteel      = ["Kasteel Batenburg"]
    batenburg_schuur       = ["Kasteel Batenburg"]
    batenburg_huis         = ["Kasteel Batenburg"]
    batenburg_kerker       = ["Kasteel Batenburg"]
    grensovergang          = ["Grensovergang Duitsland"]
    kruising               = ["Kruising"]
    kruising_huisje        = ["Kruising"]
    gymnich                = ["Gymnich"]
    gymnich_schuur         = ["Gymnich"]
    gymnich_kerkje         = ["Gymnich"]
    romerkanal             = ["Het Romerkanal"]
    romerkanal_hol         = ["Het Romerkanal"]
    romerkanal_huis_1f     = ["Het Romerkanal"]
    romerkanal_huis_2f     = ["Het Romerkanal"]
    kruising2              = ["Kruising"]
    druide_bos             = ["Druïde bos"]
    druide_grot1           = ["Druïde grot"]
    druide_grot2           = ["Druïde grot"]
    druide_grot3           = ["Druïde grot"]
    trollen_bos            = ["Trollen bos"]
    trollen_grot           = ["Trollen grot"]
    piesport               = ["Piesport"]
    piesport_bieb          = ["Piesport"]
    piesport_bank          = ["Piesport"]
    piesport_bank_kelder   = ["Piesport"]
    piesport_wijnproeverij = ["Piesport"]
    piesport_inn_1f        = ["Piesport"]
    piesport_inn_2f        = ["Piesport"]
    piesport_winkel        = ["Piesport"]
    cochem_bos             = ["Bos naar Cochem"]
    cochem                 = ["Cochem"]
    cochem_kasteel         = ["Cochem"]
    cochem_kerk            = ["Cochem"]
    cochem_huis_1f         = ["Cochem"]
    cochem_huis_2f         = ["Kasteel Cochem"]
    cochem_huis_3f         = ["Kerk Cochem"]
    trier_bos2             = ["Bos naar Trier"]
    trier_bos1             = ["Bos naar Trier"]
    trier                  = ["Trier"]
    trier_theater          = ["Trier"]
    trier_kerk1            = ["Trier"]
    trier_kerk2            = ["Trier"]
    trier_klokkentoren     = ["Trier"]


class SFX(enum.Enum):
    """
    Alle geluiden. De .name moet gelijk aan het audio bestand .ogg zijn.
    """
    menu_switch = 1
    menu_select = 2
    menu_error = 3
    menu_cancel = 4
    step_grass = 10
    step_stone = 11
    step_wood = 12
    step_carpet = 13
    step_sand = 14
    coins = 20
    scroll = 21
    chest = 22
    sparkly = 23
    reward = 24
    upgrade = 25
    join = 26
    equip = 27
    message = 30
    done = 31


class Keys(enum.Enum):
    """
    Alle keys uit het spel.
    """
    Kill = pygame.K_BACKSLASH
    Grid = pygame.K_F10
    Cbox = pygame.K_F11
    Debug = pygame.K_F12

    Select = pygame.K_RETURN, pygame.K_KP_ENTER  # 2 mogelijkheden voor dezelfde constante
    Delete = pygame.K_DELETE
    Exit = pygame.K_ESCAPE
    Remove = pygame.K_BACKSPACE

    Up = pygame.K_UP
    Down = pygame.K_DOWN
    Left = pygame.K_LEFT
    Right = pygame.K_RIGHT

    Align = pygame.K_SPACE

    Mvspeed1_1 = pygame.K_LCTRL
    Mvspeed1_2 = pygame.K_RCTRL
    Mvspeed3_1 = pygame.K_LSHIFT
    Mvspeed3_2 = pygame.K_RSHIFT

    Zoomplus = pygame.K_KP_PLUS, pygame.K_PERIOD
    Zoommin = pygame.K_KP_MINUS, pygame.K_COMMA
    Zoomreset = pygame.K_KP_DIVIDE, pygame.K_SLASH

    Action = pygame.K_a
    Inv = pygame.K_i
    Prev = pygame.K_q
    Next = pygame.K_w

    Leftclick = 1
    Scrollup = 4
    Scrolldown = 5


class ColumnType(enum.Enum):
    """
    Mogelijke kolom typen voor ListBoxen
    """
    icon = 1
    s_icon = 2  # sub icon
    f_icon = 3  # formatted icon
    text = 4
