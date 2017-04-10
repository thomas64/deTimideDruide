
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


class PeopleDatabase(enum.Enum):
    """Mogelijkheid om time1 en time2 op te nemen als een person op een specifiek tijdstip aanwezig moet zijn."""

    person100 = dict(name='druid01',     text=[["*Hick*"]])

    person200 = dict(name='troll01',     text=[["*Grunt*"]])

    person300 = dict(name='soldier01',   text=[["Goedendag."],
                                               ["Welkom in het kasteel."]])

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

    person402 = dict(name='soldier01',     text=[["Halt! U komt het ryck van Nimmegen niet in.",
                                                  "Ik heb orders van de keizer. Keer terug!"]],
                     time1=datetime.datetime(1999, 12, 31, 23, 59),
                     time2=datetime.datetime(2017,  5, 13, 12, 00))

    person500 = dict(name='roelfke01',      text=[["Hoi. Ik ben Roelfke."],
                                                  ["Wat leuk dat je er bent!"],
                                                  ["Verzamel je eigen team maar snel bij elkaar."]])
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
                                         text=[["Trespassing is not allowed!"]])

    # ersin_forest_spring
    person82 = dict(name='animal02',     text=[["Woof"], [" . . . "], ["I mean, hello there."]])

    # ersin_forest_center
    person50 = dict(name='boy01',        quest=QuestDatabase.quest1)
    person81 = dict(name='girl02',       quest=QuestDatabase.quest5)

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
    person75 = dict(name='youngwoman02', quest=QuestDatabase.quest2)
    # invernia_school
    person78 = dict(name='woman03',      text=[["The magic here is from another world!"]])

for person in PeopleDatabase:
    person.value['face'] = PATH+person.value['name']+FEXT
    person.value['sprite'] = PATH+person.value['name']+SEXT
