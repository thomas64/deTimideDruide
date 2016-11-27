
"""
class: GameState
class: Direction
class: PersonState
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
"""

import enum

import pygame


class GameState(enum.Enum):
    """
    Alle states uit het spel.
    Diegene die strings zijn, worden gebruikt als menu titel in het spel.
    """
    MainMenu = 1
    LoadMenu = "Load Game"
    SaveMenu = "Save Game"
    OptionsMenu = 4
    PauseMenu = 5

    Overworld = 6
    Battle = 7
    Conversation = 8
    PartyScreen = 9
    MessageBox = 10
    Shop = 11
    FadeBlack = 12


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
    PersonMessageQuest = 2
    ReceiveItemQuest = 3
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
    braserie_ad_waal  = "ersin_forest",  "river"
    braserie_altena   = "invernia_town", "fire"
    brug_od_waal      = "ersin_forest",  "river"
    kasteel_batenburg = "invernia_town", "river"
    # ersin_forest_center =       "ersin_forest",  "birds"
    # invernia_town =             "invernia_town", "town"
    # ersin_forest_hole =         "ersin_cave",    None

class MapTitle(enum.Enum):
    """
    Alle tmx kaarten op een rij, met de Titel hoe die in beeld komt erachter.
    De key's komen precies overeen met de .tmx namen.
    """
    braserie_ad_waal  = "Braserie aan de Waal"
    braserie_altena   = "Braserie Altena"
    brug_od_waal      = "Brug over de Waal"
    kasteel_batenburg = "Kasteel Batenburg"


class SFX(enum.Enum):
    """
    Alle geluiden. De .name moet gelijk aan het audio bestand .ogg zijn.
    """
    menu_switch = 1
    menu_select = 2
    menu_error = 3
    menu_cancel = 4
    step_grass = 5
    step_stone = 6
    step_wood = 7
    step_carpet = 8
    coins = 9
    scroll = 10
    chest = 11
    sparkly = 12


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
