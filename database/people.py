
"""
class: PeopleDatabase
"""

import datetime
import enum

from .chapter import ChapterDatabase
from .quest import QuestDatabase


PATH = 'resources/sprites/npcs/'
FEXT = 'f.png'
SEXT = 's.png'

HEROFACEPATH = 'resources/sprites/heroes/'
ALAGOS = HEROFACEPATH+"01f_alagos.png"
DRUIDE = PATH + 'druid01' + FEXT
YMIR = PATH + 'troll02' + FEXT
THOMAS = PATH + 'thomas01' + FEXT


class PeopleDatabase(enum.Enum):
    """
    Mogelijkheid om time1 en time2 op te nemen als een person op een specifiek tijdstip aanwezig moet zijn.
    Mogelijkheid om face alvast mee te geven, deze moet in een list. person80 is een voorbeeld.
    """

    person100 = dict(name='druid01',     quest=QuestDatabase.quest7,
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 16, 11, 00))

    person101 = dict(name='druid01',     quest=(QuestDatabase.quest8,
                                                QuestDatabase.quest9,
                                                QuestDatabase.quest10),
                     time1=datetime.datetime(2017,  5, 16, 11,  1),
                     # time1=datetime.datetime(2009,  5, 16, 11,  1), # deze tijd is om te testen.
                     time2=datetime.datetime(2017,  5, 16, 15, 00))

    person102 = dict(name='druid01',     quest=(QuestDatabase.quest11,
                                                QuestDatabase.quest12,
                                                QuestDatabase.quest13,
                                                QuestDatabase.quest14,
                                                QuestDatabase.quest15,
                                                QuestDatabase.quest16,
                                                QuestDatabase.quest17,
                                                QuestDatabase.quest18,
                                                QuestDatabase.quest19,
                                                QuestDatabase.quest20),
                     time1=datetime.datetime(2017,  5, 16, 15, 1),
                     # time1=datetime.datetime(2009,  5, 16, 11,  1),  # deze tijd is om te testen.
                     time2=datetime.datetime(2017,  5, 17, 3, 00))

    person103 = dict(name='druid01',     text=[["Zwaaaammix!"],
                                               [" . . . . . . . . "],
                                               ["*Zucht*",
                                                "Ik denk dat we er weer wat wijn in moeten gieten helaas.",
                                                "Hierzo!"],
                                               [" . . . . . . . . "],
                                               ["*KLOK* *KLOK* *KLOK*"],
                                               ["Ha. Daar zijn jullie weer."],
                                               ["*HIPS* Hebben jullie de knoflookkoning gevonden?"],
                                               ["Ja. Hij vertelde ons dat de trollen de zwammix hebben gemaaaaaakt,",
                                                "omdat ze die ook zo graaaaag eens zouden proeven."],
                                               ["Wat zeg je? Maar dat is een ramp! *HIPS*",
                                                "De Zwammix heeft een verschrikkelijke werking op trollen.",
                                                "Ze deden de laatste tijd ook al zo raar.",
                                                "Heeft hij ook iets gezegd over Ymir, de leider van de trollen?"],
                                               ["Jaaaaa. Ymir slaaaaaaapt de laatste tijd alleen maaaaaar.",
                                                "En de rest van de trollen zijn ook erg slaaaaaperig."],
                                               ["Pfieuw! Dan hebben we nog hoop. *HIPS*"],
                                               ["Waarschijnlijk omdat de trollen de zwammix hebben gemaakt",
                                                "zonder de ketel, is de werking van de soep erg afgezakt."],
                                               ["Wanneer de soep goed bereid wordt en door",
                                                "trollen wordt gegeten resulteert dit in verstening!",
                                                "Iets wat ik de trollen geenszins toewens.",
                                                "Daarom gaf ik de soep nooit aan hen. *HIPS*"],
                                               ["Blijkbaar omdat ze de ketel niet hadden,",
                                                "zijn de trollen alleen wat slaperig.",
                                                "En Ymir, gulzig als hij is, is nu het slaperigst van allemaal."],
                                               ["*HIPS* Maar nu de trollen ook de ketel hebben,",
                                                "en hun leider slaapt, is er haast bij."],
                                               ["Het zal ze binnenkort dan waarschijnlijk",
                                                "wel lukken de zwammix te maken."],
                                               ["Ooooh. Waarom zijn ze ook zo nieuwsgierig.",
                                                "Ik heb nooit door gehad dat ze zo jaloers waren.",
                                                "Ik dacht dat ze zo nors waren omdat ik steeds",
                                                "paddenstoelen uit hun bos kwam halen. *HIPS*"],
                                               ["Maaaaar Zwammix, dan moeten we nu",
                                                "zo snel mogelijk Ymir zien te vinden."],
                                               ["Je hebt gelijk Brann. *HIPS*",
                                                "De soep is nu bijzaak."],
                                               ["Een echte druïde zorgt goed voor de natuur.",
                                                "Hij is spaarzaam en sober *HIPS* en helpt iedereen waar hij kan."],
                                               ["Maar Ymir vinden dat is één ding, hem uit zijn slaap halen is twee.",
                                                "Ik ken iemand die de spreuk kent om wie dan ook uit de diepste",
                                                "slaap te halen. Ik hoop dat hij mee wil werken."],
                                               ["Dat is mooi meester. Maaaaaaar met zoveel wijn zijn uw",
                                                "verbaaaaaale kwaliteiten zijn niet meer je van het."],
                                               ["Veel wijn? Dat valt wel mee. *HIPS*",
                                                "Maar dit is een uitgelezen kans om jullie kwaliteiten in te zetten.",
                                                "Ik heb al gemerkt dat jullie niet op je mondje zijn gevallen."],
                                               ["Zaterdag moeten we uitvinden waar Ymir is.",
                                                "We kunnen dan maandag Ymir uit zijn slaap ontwaken."],
                                               ["Vrijdag gaan we kijken wie van jullie de beste kwaliteiten",
                                                "heeft voor een druïde. De winnaar krijgt de eer Ymir te ontwaken",
                                                "uit zijn slaap. *HIPS*"],
                                               ["Let the Druïdegames begin!!!"]],
                     face=[ALAGOS, DRUIDE, ALAGOS, DRUIDE, DRUIDE, DRUIDE, DRUIDE, ALAGOS, DRUIDE, ALAGOS, DRUIDE, DRUIDE,
                           DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, ALAGOS, DRUIDE, DRUIDE, DRUIDE, ALAGOS, DRUIDE,
                           DRUIDE, DRUIDE, DRUIDE],
                     chapter=ChapterDatabase.chapter1,
                     time1=datetime.datetime(2017, 5, 17,  4, 00),
                     time2=datetime.datetime(2017, 5, 17, 23, 00))

    person104 = dict(name='druid01',     text=[[" . . . . . . . . "],
                                               ["Ik heb het gevoel dat een hoop",
                                                "kennis vandaag van pas zal komen.",
                                                "Kraaaa!"]],
                     face=[DRUIDE, ALAGOS],
                     time1=datetime.datetime(2017, 5, 19,  4, 0),
                     time2=datetime.datetime(2017, 5, 19, 18, 00))

    person105 = dict(name='druid01',     text=[[" . . . . . . . . "]],
                     time1=datetime.datetime(2017, 5, 19, 18, 00),
                     time2=datetime.datetime(2017, 5, 22,  6, 00))

    person106 = dict(name='druid01',
                     time1=datetime.datetime(2017, 5, 22,  6,  1),
                     time2=datetime.datetime(2017, 5, 22, 13, 00),
                     face=[DRUIDE, ALAGOS, ALAGOS, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE, DRUIDE],
                     text=[[" . . . . . . . . "],
                           ["Oh ja natuurlijk, eerst wijn, dan pas kan hij praten."],
                           ["Hier Zwammix, drink maar lekker deze fles wijn."],
                           [" . . . . . . . . "],
                           ["*KLOK* *KLOK* *KLOK*"],
                           ["Ik was even aan het pissen, ogenblikje hoor."],
                           ["*ZIP*"],
                           ["Ha. Daar zijn jullie weer."],
                           ["Ok DIO's. Of zal ik ondertussen maar gewoon druïdes zeggen.",
                            "Jullie hebben jezelf dubbel en dwars bewezen als volwaardige druïdes."],
                           ["We weten inmiddels waar we Ymir kunnen vinden.",
                            "Maar om hem wakker te maken moeten we bij",
                            "mijn sacherijnige broer Grandprix zijn.",
                            "Hij weet namelijk hóe we Ymir wakker moeten maken,",
                            "maar ik vrees dat hij dit niet zomaar prijs gaat geven."],
                           ["Hij woont in Trier en heeft een heel leger trollen in zijn macht.",
                            "En we zullen dat leger moeten gaan verslaan ben ik bang."],
                           ["Aan jullie nu eerst de taak om een zo groot mogelijk",
                            "leger te verzamelen in Trier, en dat dan te gaan trainen."],
                           ["Als zijn leger verslagen is, kan ik",
                            "ongestoord mijn kunsten vertonen.",
                            "Daarna kunnen we door naar de",
                            "Genovevahohle om daar Ymir te ontwaken."]])

    person107 = dict(name='druid02',    quest=(QuestDatabase.quest23,
                                               QuestDatabase.quest24,
                                               QuestDatabase.quest25,
                                               QuestDatabase.quest26))

    person108 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de Keizerthermen in Trier."]])
    person109 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de Palastgarten in Trier."]])
    person110 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de Porta Nigra in Trier."]])
    person111 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de klokkentoren van de Lieve-vrouwe-kerk van Trier."]])
    person112 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de Dom van Trier."]])
    person113 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in een emmer in een achtertuin in Trier."]])
    person114 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in het Amfitheater van Trier."]])
    person115 = dict(name='troll01',     text=[["*Grumbel* Een steen is te vinden in de vijver in een achtertuin in Trier."]])

    person116 = dict(name='troll01',     quest=QuestDatabase.quest27,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person117 = dict(name='troll01',     quest=QuestDatabase.quest28,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person118 = dict(name='troll01',     quest=QuestDatabase.quest29,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person119 = dict(name='troll01',     quest=QuestDatabase.quest30,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person120 = dict(name='troll01',     quest=QuestDatabase.quest31,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person121 = dict(name='troll01',     quest=QuestDatabase.quest32,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person122 = dict(name='troll01',     quest=QuestDatabase.quest33,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person123 = dict(name='troll01',     quest=QuestDatabase.quest34,
                     time1=datetime.datetime(2017,  5, 22, 16, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))

    person124 = dict(name='troll02', text=[["ZZZzzzZZZzzzZZZ..."],
                                           ["Ah kijk, hier ligt Ymir te slaaaapen.",
                                            "Zullen we de spreuk maaaaar zeggen?"],
                                           ["Begin de dag met een dansje,",
                                            "Begin de dag met een lach.",
                                            "Want wie vrolijk kijkt in de morgen,",
                                            "die lacht de hele dag."],
                                           [" . . . . . . . . "],
                                           ["MHUAAAA!!! Zo dat was een lekker soepje.",
                                            "Laat het hoofdgerecht maar komen."],
                                           ["Kraaa. Maaaaar Ymir. Je hebt jaaaaaaren geslaaaapen."],
                                           ["JA! Zo voelt het inderdaad wel nu je het zegt.",
                                            "Ik heb een stijve rug van heb ik jou daar. *KRAK*"],
                                           ["Waaaaarom heb je de zwammix gemaaaaakt?"],
                                           ["Oh. Ik was nieuwsgierig. Dingen die niet mogen",
                                            "vragen om uitgeprobeerd te worden. Vind je niet?"],
                                           ["Jaaaa. Maaaar je was er bijnaaa geweest.",
                                            "Want zelfs door een enkele druppel zwammix alleen,",
                                            "veranderen trollen al in steen."],
                                           ["Tjonge. Vandaar dat Zwammix altijd zo moeilijk deed.",
                                            "Weet ik veel. Waarom zegt die man ook niks.",
                                            "Hij had toch kunnen waarschuwen toen ik zijn receptenboek had gepikt."],
                                           ["Jaaa Ymir. Zwammix zegt nu eenmaal niks zonder wijn of zijn soep.",
                                            "Je had geluk dat de laaaaatste bladzijde niet in het boek zat."],
                                           ["Hoezo?"],
                                           ["Nou zonder de ketel werkt de soep niet.",
                                            "Gelukkig maaaaar voor jullie."],
                                           ["Oh? En wat hebben mijn lieve trolleknolletjes",
                                            "uitgspookt toen ik lekker lag te slapen?"],
                                           ["Tully heeft de laaaaatste bladzijde gepikt van Zwammix",
                                            "toen hij zijn roes lag uit te slaaaapen, en ook de ketel",
                                            "van de druïde meegenomen. Het had niet veel gescheeld",
                                            "of hij was erin geslaaaagd de soep te maken."],
                                           ["Je trolleknolletjes zitten nu met zijn allen",
                                            "het bos te bemesten zal ik maaaaar zeggen."],
                                           ["Nou. Blijkbaar had het dus niet veel gescheeld",
                                            "of de Moezeldaltrol was uitgestorven geweest."],
                                           ["Hoe kan ik jullie bedanken?"],
                                           ["Het is goed zo, we zouden alleen graaaaag de ketel terug willen."],
                                           ["Die ketel mogen jullie meenemen.",
                                            "Ik hoef dat enge ding niet."],
                                           ["Ik vermoed dat de ketel in onze pannenkist zit hier.",
                                            "daar stoppen we altijd onze pannen in."],
                                           ["De code om de kist te openen is:",
                                            "'tefaljedenktookaanalles'."],
                                           ["Kraaaa! Dat doen we."],
                                           ["Let op! Als je de kist opent is het spel voorbij.",
                                            "Ga dus indien nodig nog eerst naar de bank in",
                                            "Piesport om je beloningen op te halen, of doe",
                                            "eventueel nog andere dingen die je moet doen.",
                                            "Daarna kun je hier altijd alsnog de kist openen."]
                                           ],

                     face=[YMIR, ALAGOS, ALAGOS, YMIR, YMIR, ALAGOS, YMIR, ALAGOS, YMIR, ALAGOS, YMIR, ALAGOS, YMIR,
                           ALAGOS, YMIR, ALAGOS, ALAGOS, YMIR, YMIR, ALAGOS, YMIR, YMIR, YMIR, ALAGOS, THOMAS])


    person200 = dict(name='troll01',     text=[["*Burp*"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 16, 11, 00))
    person201 = dict(name='ketel01',     text=[["He kijk nou, dit is de ketel van de Zwammix!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 16, 11, 00))
    person202 = dict(name='steen01',     text=[["Ik hoor gesnurk achter deze steen.", "Wat kan dat zijn?"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 22, 16, 00))

    person300 = dict(name='soldier01',   text=[["Goedendag."],
                                               ["Welkom in Kasteel Batenburg."]])

    person301 = dict(name='soldier01',   text=[["Het is niet toegestaan de kasteelmuur te betreden."],
                                               ["Dus opzouten!!!"]])

    person400 = dict(name='man50',      text=[["Wat zeg je?", "Of ik de druïde ken?"],
                                              ["Ooh, je bedoelt Zwammix?",
                                               "Of zeg maar gerust Zwamniks.",
                                               "Zoveel zegt hij namelijk niet."],
                                              ["Jaren geleden heb ik hem hier nog gezien met ene Bato.",
                                               "De Druïde zei geen woord.",
                                               "Zijn vriend was iets spraakzamer."],
                                              ["Hij had het over stenen die bij zijn kasteel begraven waren.",
                                               "Hier aan de wand hangt een kaart.",
                                               "Daar zou je het kasteel op moeten kunnen vinden."],
                                              ["Waarom deze stenen daar waren begraven kon ik niet verstaan.",
                                               "Maar uit de gebaren van de druïde meende ik te begrijpen dat",
                                               "jaren later deze stenen nog van pas zouden komen. "],
                                              ["Zijn vriend had het over een soep. ",
                                               "Maar vanwege zijn zwakke gestel kon hij de druïde niet ",
                                               "helpen om de soep te maken. "],
                                              ["Bij hun vertrek zijn ze iets vergeten mee te nemen.",
                                               "Waar heb ik dat toch gelaten? Het moet hier ergens zijn..."]])

    person402 = dict(name='soldier01',     text=[["Halt! U komt het ryck van Nimmegen niet in tot 13-05 12:45 uur.",
                                                  "Ik heb orders van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 13, 12, 45))
    person403 = dict(name='soldier01',     text=[["Sie haben jetzt keinen Zugang zu Germania bis 13-05 13:45 Uhr."]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 13, 13, 45))
    person404 = dict(name='soldier01',   text=[["Herzlich willkommen in Germania."]])
    person405 = dict(name='soldier01',   text=[["Halt! U komt Gallia Belgica nooit en te nimmer meer in.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(2017, 5, 14, 6, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person406 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 14-05 's ochtends.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 14, 6, 00))
    person407 = dict(name='soldier01',   text=[["Halt! Het Romerkanal is nooit en te nimmer meer te bereiken.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(2017, 5, 14, 21, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person408 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 13-05 15:15 uur.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 13, 15, 15))
    person409 = dict(name='soldier01',   text=[["Halt! Gymnich is nooit en te nimmer meer te bereiken.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(2017, 5, 14, 21, 00),
                     time2=datetime.datetime(2099, 12, 31, 23, 59))
    person410 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 16-05 's ochtends.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 16,  6, 00))
    person411 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 17-05 's ochtends.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 17, 6, 00))
    person412 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 22-05 's ochtends.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 22, 6, 00))
    person413 = dict(name='soldier01',   text=[["Halt! Deze weg is afgesloten tot 20-05 's ochtends.",
                                                "Ik heb order van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 20, 6, 00))

    person500 = dict(name='roelfke01',      quest=QuestDatabase.quest21)
    person501 = dict(name='sieger01',       text=[["Hi. Ik ben Sieger."],
                                                  ["Zijn jullie klaar voor een avontuur?"],
                                                  ["Maak jullie borst maar nat!"]])
    person502 = dict(name='thomas01',       text=[["Hallo. Ik ben Thomas.", "Het brein achter deze wereld."],
                                                  ["Doet iets het niet? Dan kun je bij mij terecht."]])
    person503 = dict(name='machteld01',     text=[["Hoi. Ik ben Machteld."],
                                                  ["Ik zal lekker voor jullie koken als",
                                                   "jullie goed je best doen! Succes!"]])
    person504 = dict(name='dianne01',       text=[["Hoi. Ik ben Dianne.", "Moeder van Nynke."],
                                                  ["Nynke! Niet te dicht bij de open haard!"]])
    person505 = dict(name='nynke01',        text=[["Huhuhu. MHUAAAA!!!"]])
    person506 = dict(name='boaz01',         text=[["AAP!!"]])

    person507 = dict(name='animal04',       text=[["Eh, what's up, doc?"]])
    person508 = dict(name='animal05',       text=[["Beehh!"]])

    # huisje kruising1
    person509 = dict(name='oldwoman01',     quest=QuestDatabase.quest6)

    # kerkje gymnich
    person510 = dict(name='priest01',       text=[["En dan zijn we nu aangekomen bij de schriftlezing van vandaag.",
                                                   "Want zo staat er geschreven in Numeri 21:14:"],
                                                  ["Daarom wordt gezegd in het boek van de oorlogen des HEEREN:",
                                                   "Tegen ...*SNORK*...eb, in een wervelwind, en tegen de beken Arnon,"],
                                                  ["En dan bladeren we door naar Jesaja 60:6.",
                                                   "Hier lezen we het volgende:"],
                                                  ["Een hoop keme...*SNORK*... zal u bedekken,"],
                                                  ["Naar deze plaats zult u zich moeten begeven.",
                                                   "Wie oren heeft om te horen, die hore. Amen!"]])
    person511 = dict(name='nun01',          text=[["Sssst. Ik luister naar de schriftlezing van mijn man."]])
    person512 = dict(name='sieger01',       text=[["Pepermuntje?"]])
    person513 = dict(name='oldman01',       text=[["ZZZzzzZZZzzzZZZ..."]])
    person514 = dict(name='roelfke01',      text=[["Hallelujah!"]])
    person515 = dict(name='dianne01',       text=[["Shalom."]])
    person516 = dict(name='oldwoman02',     text=[["Ave Maria."]])
    person517 = dict(name='machteld01',     text=[["Amen."]])
    person518 = dict(name='youngman02',     text=[["Kent u Jezus al?"]])
    person519 = dict(name='man02',          text=[["God loves you and so do I."]])
    person520 = dict(name='woman01',        text=[["Ik kom u vrede en geluk brengen."]])
    person521 = dict(name='boy01',          text=[["Wat een saaie preek."]])
    person522 = dict(name='girl02',         text=[["Duurt veel te lang."]])
    person523 = dict(name='thomas01',       text=[["Wanneer komt Teun weer eens spreken?"]])
    person524 = dict(name='youngman01',     text=[["HashiraPaloeriGaftarösti."]])
    person525 = dict(name='youngwoman01',   text=[["De bijbel vertelt dat tongentaal altijd uitgelegd moet worden.",
                                                   "Hij zegt: 'Prijs de Heer! Hij is uw verlosser.'"]])
    person526 = dict(name='youngwoman03',   text=[["Wauw, ik ben echt geboeid."]])
    person527 = dict(name='woman02',        text=[["Wees gegroet."]])
    person528 = dict(name='man01',          text=[["Bent u al volwassen gedoopt?"]])

    # wijnproeverij
    person529 = dict(name='man52',          quest=QuestDatabase.quest22)

    person530 = dict(name='man01',         text=[["Of ik de Druïde ken?"],
                                                 ["*Hikkup* Jazeker."],
                                                 ["Maar ik heb hem hier al een tijdje niet meer gezien.",
                                                  "*Hikkup* Hij kwam hier vroeger vaak bloemetjes plukken."],
                                                 ["Dit bos staat bekend om zijn mooie bloemen. *Hikkup*",
                                                  "Vooral de rode, gele en blauwe bloemen zijn bijzonder.",
                                                  "Deze komen enkel in dit bos voor, en hebben een",
                                                  "heilzame werking in de handen van de druïde. *Hikkup*"],
                                                 ["Ik heb in het verleden het een keer in mijn hoofd",
                                                  "gehaald om thee te zetten van de bloemetjes.",
                                                  "Dat heb ik geweten."],
                                                 ["*Hikkup* *Hikkup*"]])

    person531 = dict(name='man54',         text=[["Ik hoorde jullie praten over een magische soep.",
                                                  "Klopt dat? Mogelijk dat ik jullie kan helpen."],
                                                 ["Jaren terug heb ik hier een wezen te logeren gehad.",
                                                  "Hij betaalde goed, maar ik kon de kamer na zijn",
                                                  "bezoek gelijk renoveren. Wat een lucht. Blegh!",
                                                  "Ik word er nog onpasselijk van als ik er aan denk."],
                                                 ["Hij was geobsedeerd door een of andere soep."],
                                                 ["Als ik jullie was zou ik de route van het Romer Kanal",
                                                  "een stuk volgen. Dat heeft hij toen ook gedaan.",
                                                  "Mogelijk dat jullie nog belangrijke informatie vinden",
                                                  "over de soep die hij aan het maken was."]])

    person532 = dict(name='man53',          text=[["Hai. Herne is de naam.",
                                                   "Maar ik ben ook wel bekend",
                                                   "als de knoflookkoning.",
                                                   "Wat moeten jullie hier?"],
                                                  ["Wij vroegen ons af of u ons meer",
                                                   "kan vertellen over de trollen?"],
                                                  ["Tuurlijk kan ik dat. Ik ben jager van beroep.",
                                                   "Zodoende heb ik jaren lang met hun leider Ymir opgetrokken.",
                                                   "Maar ik heb hem al een tijd niet meer gesproken.",
                                                   "Hij slaapt de hele tijd als ik hem bezoek."],
                                                  ["Maar waarom zou ik jullie over de trollen vertellen?",
                                                   "Hebben jullie ooit gehoord van privacy?",
                                                   "En wat schiet ik ermee op om de plannen van de",
                                                   "trollen even uit de doeken te doen voor jullie?"],
                                                  ["Jaaaawel, maar het zit zo.",
                                                   "De trollen hebben de ketel",
                                                   "gepikt van Zwammix.",
                                                   "Het is van groot belang dat",
                                                   "Zwamnix zijn ketel terug krijgt."],
                                                  ["Oh Zwammix zeg je?",
                                                   "Nou zeg maar Zwamnix hoor.",
                                                   "Zo spraakzaam is hij niet."],
                                                  ["Ja daaaaarom juist.",
                                                   "Hij moet nodig zijn soepje drinken."],
                                                  ["Oh. Hij moet zijn soepje drinken, en de trollen",
                                                   "mogen zoals gewoonlijk niet eens even proeven?",
                                                   "Klinkt niet echt eerlijk. Denk jij wel?!",
                                                   "Niet zo raar toch dat de trollen de ketel hebben gejat.",
                                                   "Zwamnix heeft het er zelf naar gemaakt!"],
                                                  ["Hoe bedoel je?"],
                                                  ["Oh heel simpel. De trollen hebben nooit van de zwammix",
                                                   "mogen proeven. Verder mochten Jan en alleman dat wel.",
                                                   "Ze zijn stik jaloers natuurlijk."],
                                                  ["Ze hebben nu zelf geprobeerd de soep te maken,",
                                                   "maar dit is niet helemaal goed gegaan.",
                                                   "Na hun eerste brouwsel zijn ze erg",
                                                   "slaperig als je het mij vraagt."],
                                                  ["Oh? Dat klinkt niet goed.",
                                                   "Maar waaaaaarom hebben ze de ketel dan gejat,",
                                                   "als ze de soep al gemaaaaaakt hebben?"],
                                                  ["Dat weet ik niet.",
                                                   "Maar een paar dagen terug had ik Tully hier te slapen.",
                                                   "Hij is een van de trollen en hij had een briefje bij zich,",
                                                   "maar heeft het niet meer mee genomen.",
                                                   "Misschien dat je het boven nog ergens kan vinden."]],
                     face=[PATH + 'man53' + FEXT, ALAGOS, PATH + 'man53' + FEXT, PATH + 'man53' + FEXT, ALAGOS,
                           PATH + 'man53' + FEXT, ALAGOS, PATH + 'man53' + FEXT, ALAGOS, PATH + 'man53' + FEXT,
                           PATH + 'man53' + FEXT, ALAGOS, PATH + 'man53' + FEXT])

    person550 = dict(name='animal01',   text=[["De druïde die boletenchips maakte eindigde direct",
                                               "voor of direct na de druïde die een kat heeft."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person551 = dict(name='animal02',   text=[["De druïde met het vogelnestje drinkt rooibos thee."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person552 = dict(name='animal03',   text=[["De druïde uit het grauwe wilgenbos is één plaats",
                                               "hoger geëindigd dan de druïde uit het witte esdoornbos."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person553 = dict(name='animal04',   text=[["De druïde uit het grauwe wilgenbos drinkt wijn."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person554 = dict(name='animal04',   text=[["De druïde die cantharellen in roomsaus maakt heeft een uil."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person555 = dict(name='animal04',   text=[["De druïde uit het gewone platanenbos maakt schimmelkaas."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person556 = dict(name='animal05',   text=[["De druïde die als 3e is geëindigd drinkt geitenmelk."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person557 = dict(name='animal05',   text=[["De druïde met de vlechten won de kookwedstrijd."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person558 = dict(name='animal05',   text=[["De druïde te paard eindigde direct voor of",
                                               "direct na de druïde die schimmelkaas maakte."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person559 = dict(name='animal06',   text=[["De kale druïde heeft een vos als huisdier."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person560 = dict(name='animal07',   text=[["De druïde die zwarte truffel salade maakte, drinkt bokbier."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person561 = dict(name='animal08',   text=[["De druïde met de baard maakte vliegenzwammensoep."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person562 = dict(name='animal09',   text=[["De druïde met de snor woont in het rode kastanjebos."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person563 = dict(name='animal09',   text=[["De druïde met de vlechten eindigde direct voor of",
                                               "direct na de druïde die uit het blauwe sparrenbos komt."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))
    person564 = dict(name='animal09',   text=[["De druïde die boletenchips maakte is direct voor",
                                               "of direct na de druïde geëindigd die water dronk."]],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))

    person565 = dict(name='animal08',   text=[["Piep piep piep."],
                                              ["*uche*"],
                                              ["Piep... ik lust wel een blokje kaas."],
                                              ["Kraaaa. Dat is vreemd, deze muis praat!",
                                               "Zouden er meer dieren zijn vandaag",
                                               "die ons iets willen vertellen?"]],
                     face=[PATH + 'animal08' + FEXT, PATH + 'animal08' + FEXT, PATH + 'animal08' + FEXT, ALAGOS],
                     time1=datetime.datetime(2017, 5, 20,  6, 00),
                     time2=datetime.datetime(2017, 5, 20, 23, 00))

    # standard characters
    person1 = dict(name='boy01',         text=[["Hi mister."]])
    person2 = dict(name='boy02',         text=[["Hi mister."]])
    person3 = dict(name='girl01',        text=[["Hi mister."]])
    person4 = dict(name='girl02',        text=[["Hi mister."]])
    person5 = dict(name='youngman01',    text=[["How are you?"]])
    person6 = dict(name='youngman02',    text=[["How are you?"]])
    person7 = dict(name='youngwoman01',  text=[["How are you?"]])
    person8 = dict(name='youngwoman02',  text=[["How are you?"]])
    person9 = dict(name='man01',         text=[["How are you?"]])
    person10 = dict(name='man02',        text=[["How are you?"]])
    person11 = dict(name='woman01',      text=[["How are you?"]])
    person12 = dict(name='woman02',      text=[["How are you?"]])
    person13 = dict(name='oldman01',     text=[["How do you do?"]])
    person14 = dict(name='oldman02',     text=[["How do you do?"]])
    person15 = dict(name='oldwoman01',   text=[["How do you do?"]])
    person16 = dict(name='oldwoman02',   text=[["How do you do?"]])
    person17 = dict(name='animal01',     text=[["Meow"]],
                    # voorbeeld van time1 en time2
                    time1=datetime.datetime(2016, 10, 19, 2, 00),
                    time2=datetime.datetime(2099, 10, 19, 2, 15))
    person18 = dict(name='animal02',     text=[["Woof"]])
    person19 = dict(name='animal03',     text=[["Cluck"]])

    # ersin_forest_invernia
    person76 = dict(name='soldier01',    quest=QuestDatabase.quest3)
    person77 = dict(name='soldier01',    text=[["I'm terribly sorry sir, but I can",
                                               "not allow you to go any further."],
                                               ["It's dangerous to go alone."]])
    person80 = dict(name='soldier01',    chapter=ChapterDatabase.chapter1,
                                         text=[["Trespassing is not allowed!"],
                                               ["I'm sorry."]],
                    face=[PATH+'soldier01'+FEXT, ALAGOS])

    # ersin_forest_spring
    person82 = dict(name='animal02',     text=[["Woof"], [" . . . "], ["I mean, hello there."]])

    # ersin_forest_center
    person50 = dict(name='boy01',        quest=QuestDatabase.quest1)
    person81 = dict(name='girl02',       quest=QuestDatabase.quest5)
    person83 = dict(name='boy01',        quest=(QuestDatabase.quest6,   # een persoon kan meerdere quests achter
                                                QuestDatabase.quest5,   # elkaar hebben. op deze manier.
                                                QuestDatabase.quest1))

    # ersin_waterfall
    person51 = dict(name='man54',        quest=QuestDatabase.quest4)

    # invernia_town
    person52 = dict(name='boy01',        text=[["Hi mister!", "We're playing hide and seek.",
                                               "I'm seeking, where are they?"]])
    person53 = dict(name='girl01',       text=[["Aaw, I'm already caught."]])
    person54 = dict(name='girl02',       text=[["Psst, I'm hiding, please don't say anything."]])
    person55 = dict(name='boy02',        text=[["Teehee, he'll never find me here."]])
    # invernia_inn_1f
    person56 = dict(name='youngwoman01', text=[["Ouch! This tea is still to hot to drink."]])
    person57 = dict(name='youngman01',   text=[["The rooms are pretty cheap in this town.",
                                                "I've heard people tell of other places",
                                                "where they ask a lot more for a room."]])
    # invernia_inn_2f
    person58 = dict(name='youngwoman02', text=[["The food is so nice!"]])
    person59 = dict(name='youngman02',   text=[["She is so nice!"]])
    person60 = dict(name='woman52',      text=[["I wan't to go out, but my husband is always",
                                                "so busy with his work. I'm bored."]])
    person61 = dict(name='man50',        text=[["Argh, so much work to do."]])
    person62 = dict(name='maid01',       text=[["Sometimes these rooms are so dirty.",
                                               "What are people doing? Do they eat in bed?"]])
    # invernia_house_left
    person63 = dict(name='man01',        text=[["What are you doing inside our home?"]])
    person64 = dict(name='woman01',      text=[["What are you doing inside our home?"]])
    person65 = dict(name='boy01',        text=[["Are you here for mommy and daddy?"]])
    person66 = dict(name='girl01',       text=[["Are you here for mommy and daddy?"]])
    # invernia_house_right
    person67 = dict(name='man02',        text=[["What are you doing inside our home?"]])
    person68 = dict(name='woman02',      text=[["What are you doing inside our home?"]])
    person69 = dict(name='boy02',        text=[["Are you here for mommy and daddy?"]])
    person70 = dict(name='girl02',       text=[["Are you here for mommy and daddy?"]])
    # invernia_house_big_1f
    person71 = dict(name='priest01',     text=[["It's a busy life, taking care for all these orphans."]])
    person72 = dict(name='nun01',        text=[["It's a busy life, taking care for all these orphans."]])
    # invernia_house_big_2f
    person73 = dict(name='maid01',       text=[["These people are so sweet, taking care for all those children."]])
    # invernia_weapon_shop
    person74 = dict(name='youngman02',   quest=QuestDatabase.quest2)
    # invernia_armor_shop
    person75 = dict(name='youngwoman02', quest=QuestDatabase.quest2x)
    # invernia_school
    person78 = dict(name='woman03',      text=[["The magic here is from another world!"]])

    @staticmethod
    def get_active_quest(quest_data, logbook):
        """
        Als een persoon meerdere quests heeft, dan zoekt hij naar de huidige quest.
        :param quest_data: person_enum_val['quest']. bijv QuestDatabase.quest2
        :param logbook: self.engine.data.logbook
        :return: het quest object uit de logbook
        """
        # meerdere quests
        if type(quest_data) == tuple:
            # loop dan door al zijn quests
            for index, quest in enumerate(quest_data):
                quest_key = quest.name
                the_quest = logbook[quest_key]
                # en als er nog eentje niet rewarded is, voer die dan uit.
                # OF als je bij de laatste quest bent, die mag je nog wel een keer uitvoeren.
                if not the_quest.is_rewarded() or index == len(quest_data) - 1:
                    return the_quest
        # of als de persoon 1 quest heeft
        else:
            quest_key = quest_data.name
            the_quest = logbook[quest_key]
            return the_quest


for person in PeopleDatabase:
    if not person.value.get('face'):  # als er nog geen face is stop ze in een list van faces.
        if person.value.get('text'):  # een quest heeft geen 'text'
            size = len(person.value['text'])
            person.value['face'] = [PATH+person.value['name']+FEXT] * size
        else:
            person.value['face'] = PATH + person.value['name'] + FEXT  # bij een quest.
    person.value['sprite'] = PATH+person.value['name']+SEXT
