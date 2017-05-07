
"""
class: HeroDatabase
"""

import enum

from constants import SchoolType
from .weapon import WeaponDatabase
from .shield import ShieldDatabase
from .armor import ArmorDatabase

PATH = 'resources/sprites/heroes/'


class HeroDatabase(enum.Enum):
    """
    Alle heroes uit het spel als Enum met een dict voor de waarden.
    """
    brann = dict(nam="Brann", spr=PATH+"01s_alagos.png", fac=PATH+"01f_alagos.png",
                 lev=1, scl=SchoolType.spl,
                 int=18, wil=12, dex=15, agi=15, edu=15, str=15, sta=30,
                 alc=0, dip=0, hlr=0, lor=0, mec=0, mer=0, ran=0, stl=1, thf=0, trb=1, war=3, wiz=1,
                 haf=1, mis=3, pol=0, shd=3, swd=3, thr=0,
                 wpn=WeaponDatabase.bronzeshortsword,
                 sld=ShieldDatabase.woodenbuckler,
                 arm=ArmorDatabase.lightleatherarmor)
    gerdienke = dict(nam="Gerdienke", spr=PATH+"02s_luana.png", fac=PATH+"02f_luana.png",
                     lev=1, scl=SchoolType.elm,
                     int=14, wil=10, dex=22, agi=20, edu=10, str=8, sta=20,
                     alc=0, dip=0, hlr=0, lor=0, mec=1, mer=0, ran=0, stl=3, thf=3, trb=0, war=0, wiz=0,
                     haf=-1, mis=-1, pol=0, shd=-1, swd=1, thr=2,
                     wpn=WeaponDatabase.bronzedagger,
                     sld=None,
                     arm=ArmorDatabase.lightleatherarmor)
    anita = dict(nam="Anita", spr=PATH+"03s_grindan.png", fac=PATH+"03f_grindan.png",
                 lev=8, scl=SchoolType.non,
                 int=10, wil=8, dex=25, agi=10, edu=20, str=20, sta=40,
                 alc=-1, dip=0, hlr=0, lor=0, mec=0, mer=0, ran=0, stl=1, thf=-1, trb=0, war=4, wiz=-1,
                 haf=0, mis=-1, pol=0, shd=2, swd=4, thr=2,
                 wpn=WeaponDatabase.bronzelongsword,
                 sld=ShieldDatabase.bronzeheater,
                 arm=ArmorDatabase.heavybronzearmor)
    anja = dict(nam="Anja", spr=PATH+"04s_rydalin.png", fac=PATH+"04f_rydalin.png",
                lev=3, scl=SchoolType.nmg,
                int=22, wil=16, dex=20, agi=15, edu=16, str=10, sta=31,
                alc=0, dip=0, hlr=0, lor=1, mec=0, mer=1, ran=0, stl=0, thf=0, trb=0, war=0, wiz=4,
                haf=0, mis=-1, pol=3, shd=0, swd=3, thr=-1,
                wpn=WeaponDatabase.bronzestaff,
                sld=None,
                arm=ArmorDatabase.mediumleatherarmor,
                spl=dict(VsNecromancy=1, Endurance=4, SenseAura=1, Weakness=4))
    lourens = dict(nam="Lourens", spr=PATH+"05s_codrif.png", fac=PATH+"05f_codrif.png",
                   lev=2, scl=SchoolType.elm,
                   int=22, wil=18, dex=15, agi=12, edu=15, str=10, sta=20,
                   alc=3, dip=0, hlr=0, lor=2, mec=2, mer=0, ran=0, stl=0, thf=0, trb=0, war=0, wiz=2,
                   haf=-1, mis=-1, pol=0, shd=-1, swd=1, thr=1,
                   wpn=WeaponDatabase.bronzedagger,
                   sld=None,
                   arm=ArmorDatabase.lightleatherarmor,
                   spl=dict(DragonFlames=2))
    peter = dict(nam="Peter", spr=PATH+"06s_galen.png", fac=PATH+"06f_galen.png",
                 lev=4, scl=SchoolType.non,
                 int=15, wil=15, dex=18, agi=10, edu=20, str=25, sta=40,
                 alc=-1, dip=0, hlr=0, lor=0, mec=0, mer=0, ran=4, stl=3, thf=0, trb=0, war=5, wiz=-1,
                 haf=5, mis=3, pol=0, shd=3, swd=-1, thr=-1,
                 wpn=WeaponDatabase.ironaxe,
                 sld=ShieldDatabase.irontarge,
                 arm=ArmorDatabase.mediumironarmor)
    jurritjan = dict(nam="Jurrit Jan", spr=PATH+"07s_raiko.png", fac=PATH+"07f_raiko.png",
                     lev=12, scl=SchoolType.non,
                     int=6, wil=11, dex=14, agi=8, edu=30, str=30, sta=60,
                     alc=-1, dip=0, hlr=0, lor=-1, mec=0, mer=0, ran=0, stl=1, thf=-1, trb=-1, war=6, wiz=-1,
                     haf=0, mis=-1, pol=6, shd=4, swd=6, thr=-1,
                     wpn=WeaponDatabase.ironbroadsword,
                     sld=ShieldDatabase.ironkite,
                     arm=ArmorDatabase.heavyironarmor)
    taeke = dict(nam="Taeke", spr=PATH+"08s_kiara.png", fac=PATH+"08f_kiara.png",
                 lev=12, scl=SchoolType.elm,
                 int=15, wil=10, dex=30, agi=30, edu=20, str=15, sta=40,
                 alc=0, dip=0, hlr=1, lor=0, mec=0, mer=4, ran=0, stl=5, thf=8, trb=0, war=0, wiz=4,
                 haf=-1, mis=7, pol=2, shd=-1, swd=7, thr=-1,
                 wpn=WeaponDatabase.silverdagger,
                 sld=None, 
                 arm=ArmorDatabase.lightbronzearmor,
                 spl=dict(VsElemental=2, RemovePoison=3, Wind=3))
    luthais = dict(nam="Luthais", spr=PATH+"09s_luthais.png", fac=PATH+"09f_luthais.png",
                   lev=20, scl=SchoolType.elm,
                   int=30, wil=30, dex=20, agi=12, edu=18, str=8, sta=50,
                   alc=7, dip=0, hlr=8, lor=9, mec=6, mer=0, ran=0, stl=5, thf=0, trb=0, war=0, wiz=10,
                   haf=0, mis=-1, pol=8, shd=-1, swd=0, thr=8,
                   wpn=WeaponDatabase.bronzestaff,
                   sld=None, 
                   arm=ArmorDatabase.lightironarmor,
                   spl=dict(VsStar=8, VsNecromancy=10, Fireball=8, Mirror=8, DispelNecro=10))
    elias = dict(nam="Elias", spr=PATH+"10s_elias.png", fac=PATH+"10f_elias.png",
                 lev=18, scl=SchoolType.nmg,
                 int=30, wil=30, dex=25, agi=18, edu=30, str=20, sta=60,
                 alc=0, dip=8, hlr=0, lor=0, mec=0, mer=0, ran=0, stl=0, thf=0, trb=0, war=7, wiz=7,
                 haf=5, mis=-1, pol=5, shd=-1, swd=7, thr=-1,
                 wpn=WeaponDatabase.steellongsword,
                 sld=None, 
                 arm=ArmorDatabase.mediumsteelarmor,
                 spl=dict(VsStar=7, Banishing=7, SenseAura=7, Teleportation=7))
    nel = dict(nam="Nel", spr=PATH+"11s_onarr.png", fac=PATH+"11f_onarr.png",
               lev=18, scl=SchoolType.non,
               int=30, wil=25, dex=23, agi=15, edu=30, str=25, sta=60,
               alc=-1, dip=0, hlr=4, lor=6, mec=0, mer=0, ran=0, stl=0, thf=0, trb=7, war=9, wiz=-1,
               haf=8, mis=-1, pol=8, shd=9, swd=5, thr=8,
               wpn=WeaponDatabase.steelpoleaxe,
               sld=ShieldDatabase.steelkite,
               arm=ArmorDatabase.heavysteelarmor)
    simon = dict(nam="Simon", spr=PATH+"12s_duilio.png", fac=PATH+"12f_duilio.png",
                 lev=22, scl=SchoolType.elm,
                 int=25, wil=25, dex=30, agi=20, edu=25, str=25, sta=75,
                 alc=5, dip=10, hlr=0, lor=5, mec=0, mer=5, ran=5, stl=5, thf=5, trb=10, war=10, wiz=10,
                 haf=10, mis=-1, pol=10, shd=10, swd=10, thr=10,
                 wpn=WeaponDatabase.silvershortsword,
                 sld=ShieldDatabase.silvertarge,
                 arm=ArmorDatabase.mediumsilverarmor,
                 spl=dict(Fireball=6, AirShield=9, Strength=9, Debilitation=9, Mirror=9))
    iellwen = dict(nam="Iellwen", spr=PATH+"13s_iellwen.png", fac=PATH+"13f_iellwen.png",
                   lev=20, scl=SchoolType.str,
                   int=30, wil=25, dex=30, agi=25, edu=30, str=20, sta=60,
                   alc=0, dip=0, hlr=10, lor=0, mec=0, mer=0, ran=6, stl=6, thf=0, trb=0, war=10, wiz=8,
                   haf=5, mis=7, pol=0, shd=-1, swd=10, thr=-1,
                   wpn=WeaponDatabase.silverlongsword,
                   sld=None, 
                   arm=ArmorDatabase.lightsilverarmor,
                   spl=dict(WebOfStarlight=8, DispelStar=8, StellarGravity=8, DispelNaming=8, SolarWrath=8))
    zwammix = dict(nam="Zwammix", spr=PATH+"14s_faeron.png", fac=PATH+"14f_faeron.png",
                   lev=25, scl=SchoolType.nmg,
                   int=30, wil=30, dex=30, agi=30, edu=25, str=15, sta=80,
                   alc=10, dip=10, hlr=0, lor=10, mec=0, mer=10, ran=10, stl=10, thf=10, trb=10, war=10, wiz=-1,
                   haf=10, mis=0, pol=0, shd=0, swd=10, thr=0,
                   wpn=WeaponDatabase.titaniummace,
                   sld=None,
                   arm=ArmorDatabase.lighttitaniumarmor)

    @staticmethod
    def closing():
        """..."""
        return ["It seems your party is full already."]

    @classmethod
    def opening(cls, hero_raw):
        """
        ...
        :param hero_raw:
        'sale' is totaal van diplomat van hele party.
        """
        if hero_raw == cls.gerdienke.name:  # p(1).xpt >= 3000 - ((3000 / 100) * sale)
            return ("Hoi. Ik ben Gerdienke. Ik ben niet op sollicitatiegesprek geweest,",
                    "daarom heb ik geen tekst hier voor jou.",
                    "",
                    "Jij weet hoe lang een minuut duurt, jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.anita.name:  # p(1).xpt >= 21000 - ((21000 / 100) * sale)
            return ("Hoi. Ik ben Anita Noppe. 33 jaar, en ik kom uit Groningen.",
                    "Ik ben zeer gemotiveerd voor deze super inspirerende functie.",
                    "",
                    "Wat heb je mooie krullen, jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.anja.name:  # p(1).xpt >= 15000 - ((15000 / 100) * sale)
            return ("Mijn naam is Anja Belle.",
                    "Ik ben 34 jaar en ik woon in Utrecht.",
                    "Ik heb ontzettend veel zin om bij dit mooie bedrijf aan de slag te gaan.",
                    "",
                    "Jij kan goed logisch redeneren, jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.lourens.name:  # p(1).xpt >= 9000 - ((9000 / 100) * sale)
            return ("Hallo. Ik ben Lourens Noppe. Ik ben 27 jaar.",
                    "",
                    "Jij bent blank! Dus jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.peter.name:
            return ("Ik ben Peter Noppe. Ik ben 61 jaar en getrouwd met Nel.",
                    "Samen gelukkig getrouwd. Wij hebben er heel veel zin in",
                    "om deze vakantie met elkaar te gaan doen. En we hopen,",
                    "en we weten bijna wel zeker dat we gaan winnen.",
                    "",
                    "Jij moet er nodig even uit. Jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.jurritjan.name:  # p(1).xpt >= 300000 - ((300000 / 100) * sale)
            return ("Ik ben Jurrit Jan de Jong.",
                    "Ik ben 31 jaar en woon in Utrecht. Prachtig Utrecht.",
                    "En kijk onwijs uit naar deze komende functie. Ik heb er echt veel zin in.",
                    "",
                    "Jij bent hoog opgeleid en gemotiveerd. Jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.taeke.name:  # gold >= 10000 - ((10000 / 100) * sale)
            return ("Ik ben Taeke Hoekstra. Ik ben 27 jaar.",
                    "En geestelijk verzorgend in het MCL. Nou dat was het.",
                    "",
                    "Jij bent all-round heel geschikt. Jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.luthais.name:  # p(1).xpt >= 1200000 - ((1200000 / 100) * sale)
            return ("How do you do?",
                    "If you are in need of some teaching on your quest,",
                    "I will accompany you. I am old and not that strong",
                    "anymore, but strength doesn't always rely on",
                    "muscles. If you need me, I'll gladly join you.",
                    "",
                    "Thank you sir, welcome, please join us.",
                    "I don't want to be rude to decline your offer.")

        elif hero_raw == cls.elias.name:  # gold >= 40000 - ((40000 / 100) * sale)
            return ("Hellooo there!",
                    "You need me. Everybody needs me.",
                    "And that's obvious if you'd know me.",
                    "But of course that is possible now!",
                    "I shall join your party. And I am sure",
                    "you cannot refuse such an offer.",
                    "",
                    "You seem confident... Welcome I think?",
                    "Yes, I can.")

        elif hero_raw == cls.nel.name:  # p(1).xpt >= 1500000 - ((1500000 / 100) * sale)
            return ("In ben Nel Noppe. Ik ben getrouwd met Peter Noppe",
                    "en supergelukkig getrouwd. We breken er graag uit",
                    "omdat onze werkzaamheden heel druk zijn en we hebben",
                    "zo veel zin om de spelletjes te doen. En omdat we",
                    "zoveel zin hebben gaan we ook vet winnen.",
                    "",
                    "Dat klinkt als een hoop zelfvertrouwen. Jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.simon.name:  # gold >= 90000 - ((90000 / 100) * sale)
            return ("Ik ben Simon Hulshof. Ik ben 27 jaar, getrouwd met",
                    "Roelfke en vader van Boaz. Ik studeer voor docent economie.",
                    "Ik ben erg goed, en vind het leuk om met cijfertjes om te gaan,",
                    "en vind het leuk om met mensen in gesprek te zijn.",
                    "Dat is heel in het kort wie ik ben.",
                    "",
                    "We hebben nog geen raDIO DJ. Dus jij mag in het team.",
                    "Nee, jou heb ik liever niet.")

        elif hero_raw == cls.iellwen.name:  # special item?
            return ("Hail, traveler.",
                    "You humans are remarkable in your resilience and",
                    "in the speed with which you rise to power. Some of",
                    "you even rival our most powerful lords. And I wish",
                    "to learn more of your human ways. You have great",
                    "appeal to me. And I will join you if I may.",
                    "",
                    "We are honored.",
                    "Let's continue on our way.")

        elif hero_raw == cls.zwammix.name:  # geen idee
            return (" . . . . . . . . ",
                    " . . . . . . . . ",
                    " . . . . . . . . ",
                    " . . . . . . . . ",
                    " . . . . . . . . ",
                    "",
                    "Hij staat in de weg. Zullen we hem maar meenemen?",
                    "Nee, Zwammix in het team opnemen?!? Dat nooit!")
