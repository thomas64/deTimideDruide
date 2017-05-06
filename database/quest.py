
"""
class: QuestDatabase
"""

import enum

from constants import QuestType
from .weapon import WeaponDatabase
from .pouchitem import PouchItemDatabase


class QuestDatabase(enum.Enum):
    """..."""

    quest6 = dict(qtype=QuestType.FetchItemQuest,
                  condition=dict(itm1=dict(nam=PouchItemDatabase.putsi, qty=1)),
                  reward=dict(itm1=dict(nam=PouchItemDatabase.niers, qty=1),
                              itm2=dict(nam=PouchItemDatabase.gold, qty=10)),
                  text=([["Suchen Sie für die Niers? Das ist der Fluss hier draußen.",
                          "Ich habe seit Jahren auf diesem Fluss gelebt."],
                         ["Ich habe eine Karte der Niers, die Sie verwenden können.",
                          "Aber zuerst müssen Sie mir helfen, meine Putsi zu finden."],
                         ["Putsi war von mein Mann. Vor Jahren nahmen sie ihn.",
                          "Die Schweine Hunde. Er blies seinen letzten Atemzug",
                          "in der Gefangenschaft im Batenburg."],
                         ["Boehoehoe."]],
                        [["Sie haben Putsi gefunden?"]],
                        ["Zullen we de mevrouw helpen?", "",
                         "Ja, laten we het beertje geven.",
                         "Nee, we hebben haast. Ze zoekt het maar lekker uit met Putsi. Auf wienerschnitsel."],
                        [["Putsi mein kleines Teddybär!"], ["Wie kann ich Ihnen danken?"]],
                        [["Gutentag Freunde. Ich bin so froh mit Putsi!"]])
                  )

    quest1 = dict(qtype=QuestType.FetchItemQuest,
                  condition=dict(itm1=dict(nam=PouchItemDatabase.herbs, qty=10)),
                  reward=dict(itm1=dict(nam=PouchItemDatabase.gold,     qty=2),
                              eqp1=dict(nam=WeaponDatabase.bronzedart,  qty=1)),
                  # deze teksten staan in QuestState volgorde.
                  text=([["Hi mister."], ["I need 10 herbs for my mommy.", "She's ill."],
                         ["Can you please help me find some?"]],
                        [["If you've got 10 herbs,", "please give them to me."]],
                        # de confirmbox tekst moet niet tussen dubbele blokhaken
                        ["Help the boy out and give him 10 herbs?", "", "Yes, of course!", "No, these are my herbs."],
                        [["Thanks a lot for the herbs!", "Now my mom will be better soon."],
                         ["Instead of the herbs I found this here in the forest.",
                          "You can have it, for helping my mommy."]],
                        [["Hi mister."], ["It seems my mommy is all better now.", "Thanks to you!"]])
                  )

    quest2 = dict(qtype=QuestType.PersonMessageQuest1,
                  subquest='quest8',
                  condition=False,  # deze gaat op True wanneer er positief gekozen is op quest8
                  reward=dict(itm1=dict(nam=PouchItemDatabase.gold,     qty=1)),  # mag ook =None zijn.
                  text=([["How are you?"], ["May I ask you something?"],
                         ["I'm a bit shy.",
                          "There is this girl that I like, but I'm afraid to tell her."],
                         ["Would you tell her for me instead? Please?",
                          "She is at the armor shop looking for a dress, and I won't",
                          "dare to come near, so I went to this shop, I'm pathetic."]],
                        [["Please do it for me. She is at the armor shop."]],
                        ["Tell him her big amazing reaction?", "",
                         "Yes, love is something amazing.", "Nah."],
                        [["Thank you for telling her!", "You can have this, for helping me out."]],
                        [["Thanks again, I owe you big time!"]])
                  )

    quest2x = dict(qtype=QuestType.PersonMessageQuest2,
                   subquest='quest7',
                   condition=False,  # deze gaat op True wanneer er met quest7 gepraat is
                   reward=None,
                   text=([["How are you?"]],
                         [["How are you?"]],
                         # de confirmbox tekst moet niet tussen dubbele blokhaken
                         ["Bring the pathetic message over to her?", "",
                          "Yes, everybody needs a chance.", "No, he has to grow up and be a man."],
                         [["I... I didn't know that...", "Thank you for telling me."]],
                         [["How are you?"], ["I'm also pretty shy myself."]])
                   )

    quest3 = dict(qtype=QuestType.FetchItemQuest,
                  condition=dict(itm1=dict(nam=PouchItemDatabase.proofnote, qty=1)),
                  reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                  text=([["Halt! You may not enter Invernia Town!",
                          "Only if you can prove that you are not a monster."]],
                        [["Halt! You may not enter Invernia Town!",
                          "Only if you can prove that you are not a monster."]],
                        # de confirmbox tekst moet niet tussen dubbele blokhaken
                        ["Show him the 'Proof of not being a monster'?", "",
                         "Yes, I want to enter the town.", "No, he's stupid!"],
                        [["It seems you are not a monster. Continue."]],
                        [["Continue."]])
                  )

    quest4 = dict(qtype=QuestType.ReceiveItemQuest,
                  condition=True,  # staat altijd op True, want je krijgt altijd wat.
                  reward=dict(itm1=dict(nam=PouchItemDatabase.proofnote, qty=1)),
                  # meerdere textscheremen zoals bij notes.
                  text=([["It's so beautiful, I can watch this scenery for hours."],
                         ["    .       .       .       .       .       .       ."],
                         ["By the way, have you been bothered", "by that halfwit soldier at our town?",
                          "He has taken it up on himself to prevent", "monsters for entering the town!"],
                         ["That may be noble, but he is not able", "to see the difference between a normal",
                          "person and an evil monster."], ["And now he asks for proof?!?"],
                         ["I'll give you a 'Proof of not being a monster',",
                          "because you seem a normal person to me.", "*sigh*"]],
                        [["It's so beautiful, I can watch this scenery for hours."],
                         ["    .       .       .       .       .       .       ."],
                         ["Ah, there you are.", "Do you want the proof or not?"]],
                        ["Accept the help of this strange man?", "",
                         "Yes, aren't we all strange?", "No, I can solve my own problems."],
                        [["Here you go."]],
                        [["It's so beautiful, I can watch this scenery for hours."],
                         ["    .       .       .       .       .       .       ."],
                         ["Did you 'prove' that you are not a monster?"]])
                  )

    quest5 = dict(qtype=QuestType.ReceiveItemQuest,
                  condition=False,  # deze gaat naar True als je op de plek bent geweest.
                  reward=dict(eqp1=dict(nam=WeaponDatabase.titaniumlongsword,  qty=1)),  # mag =None zijn.
                  text=([["Hi mister!"], ["There is this magical place in", "the forest where animals can talk."],
                         ["Have you seen it?"], ["You have to go and take a look!"]],
                        [["Have you been to the magical place", "where animals can talk?"]],
                        ["Tell the girl you saw it but could not believe it?", "",
                         "Yes, the faith of a child is important.", "No, I won't believe animals can talk!"],
                        [["You have been there!!"], ["I love doggies."],
                         ["You can have this if you keep it our secret."]],
                        [["Animals really can talk, can they?"]])
                  )

    quest7 = dict(qtype=QuestType.FetchItemsPartlyQuest,
                  condition=dict(itm1=dict(nam=PouchItemDatabase.droppings,     qty=1),
                                 itm2=dict(nam=PouchItemDatabase.shroom,        qty=12),
                                 itm3=dict(nam=PouchItemDatabase.shallot,       qty=3),
                                 itm4=dict(nam=PouchItemDatabase.rose,          qty=3),
                                 itm5=dict(nam=PouchItemDatabase.ladybug,       qty=4),
                                 itm6=dict(nam=PouchItemDatabase.wool,          qty=1),
                                 itm7=dict(nam=PouchItemDatabase.shells,        qty=2),
                                 itm8=dict(nam=PouchItemDatabase.poppy,         qty=2),
                                 itm9=dict(nam=PouchItemDatabase.cantharel,     qty=4),
                                 itm10=dict(nam=PouchItemDatabase.weegbree,     qty=2),
                                 itm11=dict(nam=PouchItemDatabase.berkenschors, qty=1),
                                 itm12=dict(nam=PouchItemDatabase.maretak,      qty=3),
                                 itm13=dict(nam=PouchItemDatabase.spiderweb,    qty=3),
                                 itm14=dict(nam=PouchItemDatabase.fluitekruid,  qty=2),
                                 itm15=dict(nam=PouchItemDatabase.knoflook,     qty=3),
                                 itm16=dict(nam=PouchItemDatabase.tomaat,       qty=2),
                                 itm17=dict(nam=PouchItemDatabase.doperwten,    qty=3)),
                  # de reward mag ook op dit moment nog maar van 1 type zijn.
                  reward=dict(itm1=dict(nam=PouchItemDatabase.gold,             qty=1)),  # Dit aantal is per geleverde itm.
                  text=([["Vrienden. Mijn naam is Zwammix."],
                         ["*HIPS*"],
                         ["Brann en de stenen hebben hun werk goed gedaan."],
                         ["*HIPS*"],
                         ["Jullie hebben mij gevonden.",
                          "Ik heb jullie nodig om mijn soepje weer te kunnen maken."],
                         ["Zonder mijn soepje ben ik mijzelf niet,",
                          "maar het lukt mij niet de soep te maken in mijn huidige staat."],
                         ["*HIPS*"],
                         ["Hebben jullie het hele recept kunnen vinden,",
                          "en de ingrediënten bij elkaar verzameld?"]],
                        [["Zijn jullie nu wel gereed om de ingrediënten te overhandigen?"], ["*HIPS*"]],
                        ["Indien je het recept niet compleet hebt kun je de ingrediënten aan Zwammix",
                         "overhandigen maar dan krijg je ook maar een deel van de beloning.",
                         "Let op! Je hebt tot 10.55 uur de tijd om het recept compleet te maken.",
                         "Als je nu kiest om te overhandigen krijg je niet nog een tweede mogelijkheid.",
                         "",
                         "Ja, ik wil onze ingrediënten overhandigen.",
                         "Nee, ik doe het later."],
                        [["Joepie, dankjewel voor de ingrediënten.",
                          "Ik ga gelijk m'n soepketel zoeken."],
                         ["*HIPS*"],
                         ["Hier is je beloning voor het zoeken van de ingrediënten."]],
                        [["Waar is m'n ketel?"], ["*HIPS*"]])
                  )

    quest8 = dict(qtype=QuestType.ReceiveItemQuest,
                  condition=False,  # deze gaat naar True als je op de plek bent geweest.
                  reward=None,  # mag =None zijn.
                  text=([["Uhm. Ik heb een klein probleempje denk ik."],
                         ["*HIPS*"],
                         ["Mijn ketel is weg.",
                          "Hebben jullie ergens mijn ketel gezien?"]],
                        [["Hebben jullie ergens mijn ketel gezien?"]],
                        ["Vertel je dat je de ketel gezien hebt?", "",
                         "Ja, we hebben een ketel zien staan in het bos hiernaast.",
                         "Nee, we hebben geen ketel gezien."],
                        [["Het bos hiernaast?"],
                         ["*HIPS*"],
                         ["Maar dat is het trollenbos.",
                          "Zijn jullie daar geweest?!"],
                         ["Dat is heeeeel gevaarlijk.",
                          "De trollen gedragen zich erg raar de laatste jaren."],
                         ["*HIPS*"],
                         ["Wat moeten ze toch met mijn ketel?",
                          "Ongeleide projectielen lijken het wel.",
                          "Maar als de ketel daar is moeten jullie hem gaan halen."],
                         ["*HIPS*"],
                         ["Ik zal jullie help...e..."],
                         ["ZZZzzzZZZzzzZZZ..."]],
                        [["Deze zin vervalt."]])
                  )

    quest9 = dict(qtype=QuestType.FetchItemQuest,
                  condition=dict(itm1=dict(nam=PouchItemDatabase.water_waal,   qty=1),
                                 itm2=dict(nam=PouchItemDatabase.water_niers,  qty=1),
                                 itm3=dict(nam=PouchItemDatabase.water_maas,   qty=1),
                                 itm4=dict(nam=PouchItemDatabase.bloem_geel,   qty=1),
                                 itm5=dict(nam=PouchItemDatabase.bloem_blauw,  qty=1),
                                 itm6=dict(nam=PouchItemDatabase.bloem_rood,   qty=1)),
                  reward=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=8)),
                  text=([["ZZZzzzZZZzzzZZZ..."],
                         ["Oh ja, sorry. Ik viel even weg."],
                         ["Ik zal jullie dus helpen om de trollen te verjagen.",
                          "Ik zal een drankje voor jullie maken.",
                          "Maar drink het niet zelf op! Het is voor de trollen.",
                          "Voor het drankje heb ik nodig:",
                          "1 Maas water",
                          "1 Waal water",
                          "1 Niers water",
                          "1 Rood bloemetje",
                          "1 Geel bloemetje",
                          "1 Blauw bloemetje"]],
                        [["Hebben jullie het al?",
                          "1 Maas water",
                          "1 Waal water",
                          "1 Niers water",
                          "1 Rood bloemetje",
                          "1 Geel bloemetje",
                          "1 Blauw bloemetje"]],
                        ["Wil je de ingrediënten overhandigen?", "", "Ja.", "Nee."],
                        [["Met dit 9 kleurige drankje kunnen jullie de trollen even bezig houden."],
                         ["*HIPS*"],
                         ["Ze eten toch alles wat je ze voorschotelt."],
                         ["*HIPS*"],
                         ["Het heeft een sterk laxerende werking.",
                          "Ze schijten hiermee 9 kleuren.",
                          "Zo hebben jullie de tijd om de ketel terug te pakken."],
                         ["*HIPS*"]],
                        [["Deze zin vervalt."]])
                  )

    quest10 = dict(qtype=QuestType.ReceiveItemQuest,
                   condition=False,  # gaat naar True als je bij het vuur van de trollen bent geweest waar de ketel stond.
                   reward=None,
                   text=(
                       [["Zijn jullie nu al terug?"]],
                       [["Zijn jullie nu al terug?"]],
                       ["Vertel je Zwammix het slechte nieuws dat de ketel en de trollen verdwenen zijn?", "",
                        "Ja natuurlijk, de waarheid is hard!",
                        "Neuh, we laten hem lekker in zijn (dronken) waan."],
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]])
                   )

    quest11 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=1)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix wat wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast iets belangrijks te vertellen. (Dit kost 1 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Trollen leven in het bos. Voorwaar ik zeg U.",
                         "Met trollen ben je zonder drankjes de klos.",
                         "Zij rieken uren in de wind.",
                         "Maar met de juiste drank worden zij uw vrind."],
                        ["Code: DE"]],
                       [["Deze zin vervalt."]])
                   )

    quest12 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=2)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 2 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Met dranken die geel zijn als de bloemen,",
                         "*HIPS* zullen trollen een juiste locatie noemen."],
                        ["Code: WA"]],
                       [["Deze zin vervalt."]])
                   )

    quest13 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=3)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 3 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Dranken die zijn als rood scharlaken,",
                         "zullen trollen spraakzaam maken.",
                         "Vertellen zullen zij over een man,",
                         "die ons ongetwijfeld helpen kan. *HIPS*"],
                        ["Code: AR"]],
                       [["Deze zin vervalt."]])
                   )

    quest14 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=4)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 4 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Door de drankjes in het violet, *HIPS*",
                         "geven trollen advies waarmee je het zonder niet redt."],
                        ["Code: HE"]],
                       [["Deze zin vervalt."]])
                   )

    quest15 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=5)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 5 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Oranje dranken oh zo zoet, *HIPS*",
                         "leiden tot advies, maar helaas niet goed."],
                        ["Code: ID"]],
                       [["Deze zin vervalt."]])
                   )

    quest16 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=6)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 6 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["De drank die is als ultramarijn,",
                         "doet de trollen vrijgevig zijn. *HIPS*"],
                        ["Code: IS"]],
                       [["Deze zin vervalt."]])
                   )

    quest17 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=7)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 7 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Met drankjes die groen zijn als blad,",
                         "verklappen trollen locaties in een stad. *HIPS*"],
                        ["Code: IN"]],
                       [["Deze zin vervalt."]])
                   )

    quest18 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=8)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 8 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Drankjes die zijn zo zwart als roet,",
                         "leiden tot advies, maar helaas niet goed. *HIPS*"],
                        ["Code: DE"]],
                       [["Deze zin vervalt."]])
                   )

    quest19 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=9)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 9 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["Grijs is de kleur van oud. *HIPS*",
                         "Geef deze drank en ontvang uw beloning in goud."],
                        ["Code: WI"]],
                       [["Deze zin vervalt."]])
                   )

    quest20 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.wine,   qty=10)),
                   reward=None,
                   text=(
                       [[" . . . . . . . . "]],
                       [[" . . . . . . . . "]],
                       ["Gaan jullie Zwammix meer wijn geven om hem weer aan de praat te krijgen?", "",
                        "Ja. Hij heeft ons vast weer iets belangrijks te vertellen. (Dit kost 10 wijn)",
                        "Nee. Laten we hem niet nog verder in zijn drankverslaving helpen."],
                       [["De drankjes in het maagdelijk wit, *HIPS*",
                        "leiden tot advies over plaatsen in een stad waar iets zit."],
                        ["Code: JN"]],
                       [["*HIPS*"],
                        ["Okee, dat waren 55 flessen wijn.",
                         "Dat is op zich best wel veel.",
                         "Misschien moet ik maar wat gaan slapen."],
                        ["Of naar het ziekenhuis..."],
                        ["*HIPS*"]])
                   )

    quest21 = dict(qtype=QuestType.ReceiveItemQuest,
                   condition=True,
                   reward=dict(itm1=dict(nam=PouchItemDatabase.bottle,  qty=8)),
                   text=([["Hoi. Ik ben Roelfke."], ["Wat leuk dat je er bent!"],
                         ["Verzamel in deze ruimte je eigen team bij elkaar.",
                          "Praat met iedereen, maar kies alleen je eigen teamgenoten."]],
                         [["Hoi. Ik ben Roelfke."], ["Wat leuk dat je er bent!"],
                          ["Verzamel in deze ruimte je eigen team bij elkaar.",
                           "Praat met iedereen, maar kies alleen je eigen teamgenoten."]],
                         ["Heb je er een beetje zin in?", "",
                          "JAAAA!!! Dit is wordt echt het meest fantastiche spel EVAH!!!!!",
                          "Nee, mogen we alsjeblieft weer naar huis? *ZUCHT*"],
                         [["Hier heb je alvast iets wat je nodig gaat hebben."]],
                         [["Heb je je team al verzameld?"]])
                   )

    quest22 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.gold,   qty=1),
                                  itm2=dict(nam=PouchItemDatabase.grapes, qty=5),
                                  itm3=dict(nam=PouchItemDatabase.bottle, qty=5)),
                   reward=dict(itm1=dict(nam=PouchItemDatabase.wine,      qty=5)),
                   text=([["Welkom in mijn wijnproeverij.",
                           "In mijn vrije tijd maak ik zelf ook wijn.",
                           "Voor 5 trossen druiven, 5 lege flessen en 1 goudstuk",
                           "kan ik voor jullie 5 flessen wijn maken."]],
                         [["Welkom in mijn wijnproeverij.",
                           "In mijn vrije tijd maak ik zelf ook wijn.",
                           "Voor 5 trossen druiven, 5 lege flessen en 1 goudstuk",
                           "kan ik voor jullie 5 flessen wijn maken."]],
                         ["Wil je dat de man 5 wijn voor je maakt?", "",
                          "Ja, ik heb wijn tekort. (Dit kost 5 trossen druiven, 5 lege flessen, 1 goud)",
                          "Nee, dankje."],
                         [["Alsjeblieft, hier heb je de wijn."]],
                         [["Deze regel wordt niet gebruikt."]])
                   )

    quest23 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen,   qty=2)),
                   reward=dict(itm1=dict(nam=PouchItemDatabase.gold,             qty=20)),
                   text=(
                       [["Haai. Mijn naam is Grandprix."],
                        ["Hoe je een trol wakker maakt die al jaren slaapt, zeg je?"],
                        ["Tja, dat is voor mij een weet en voor jou een vraag."],
                        ["Maar voor wat hoort wat maat.",
                         "Voor twee orakelstenen zal ik je het",
                         "eerste deel van de spreuk geven."]],
                       [["En, heb je twee orakelstenen voor me?"]],
                       ["Overhandig je twee orakelstenen in ruil voor een deel van de spreuk?", "",
                        "Ja, liever een spreuk dan orakelstenen toch?",
                        "Nee, hij mag die spreuk steken in een plek waar het daglicht niet kan komen."],
                       [["Ah mooi. Dankjewel.",
                         "Het eerste deel van de spreuk luidt:"],
                        ["Begin de dag met een dansje,",
                         "Code: IN"]],
                       [["Deze zin vervalt."]])
                   )

    quest24 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen,   qty=2)),
                   reward=dict(itm1=dict(nam=PouchItemDatabase.gold,             qty=20)),
                   text=(
                       [["Je wil het tweede deel van de spreuk weten?"],
                        ["Tja, dat is voor mij een weet en voor jou een vraag."],
                        ["Maar voor wat hoort wat maat.",
                         "Voor twee orakelstenen zal ik je het",
                         "tweede deel van de spreuk geven."]],
                       [["En, heb je twee orakelstenen voor me?"]],
                       ["Overhandig je twee orakelstenen in ruil voor een deel van de spreuk?", "",
                        "Ja, ik ben gek op spreuken.",
                        "Nee, ik haat spreuken."],
                       [["Ah mooi. Dankjewel.",
                         "Het tweede deel van de spreuk luidt:"],
                        ["begin de dag met een lach.",
                         "Code: MO"]],
                       [["Deze zin vervalt."]])
                   )

    quest25 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen,   qty=2)),
                   reward=dict(itm1=dict(nam=PouchItemDatabase.gold,             qty=20)),
                   text=(
                       [["Je wil het derde deel van de spreuk weten?"],
                        ["Tja, dat is voor mij een weet en voor jou een vraag."],
                        ["Maar voor wat hoort wat maat.",
                         "Voor twee orakelstenen zal ik je het",
                         "derde deel van de spreuk geven."]],
                       [["En, heb je twee orakelstenen voor me?"]],
                       ["Overhandig je twee orakelstenen in ruil voor een deel van de spreuk?", "",
                        "Ja, ik kan niet raden hoe het liedje verder zal gaan",
                        "Nee, hij praat toch alleen maar onzin."],
                       [["Ah mooi. Dankjewel.",
                         "Het derde deel van de spreuk luidt:"],
                        ["Want wie vrolijk kijkt in de morgen,",
                         "Code: SA"]],
                       [["Deze zin vervalt."]])
                   )

    quest26 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.orakelsteen,   qty=2)),
                   reward=dict(itm1=dict(nam=PouchItemDatabase.gold,             qty=20)),
                   text=(
                       [["Je wil het laatste deel van de spreuk weten?"],
                        ["Tja, dat is voor mij een weet en voor jou een vraag."],
                        ["Maar voor wat hoort wat maat.",
                         "Voor twee orakelstenen zal ik je het",
                         "laatste deel van de spreuk geven."]],
                       [["En, heb je twee orakelstenen voor me?"]],
                       ["Overhandig je twee orakelstenen in ruil voor een deel van de spreuk?", "",
                        "Nou vooruit dan maar.",
                        "Nee echt niet. De laatste orakelstenen houd ik lekker zelf."],
                       [["Ah mooi. Dankjewel.",
                         "Het laatste deel van de spreuk luidt:"],
                        ["die lacht de hele dag.",
                         "Code: NI"]],
                       [["Wat nu weer? Je hebt toch de hele spreuk gehad? Nou opbokken!"],
                        ["Oh ja, en doe de groeten aan m'n broertje Zwamnix."]])
                   )

    quest27 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Tully?"]],
                         [["Tully opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de rees!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest28 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Sully?"]],
                         [["Sully opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de spetterpoep!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest29 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Sloan?"]],
                         [["Sloan opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de sproeipoep!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest30 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Kirwin?"]],
                         [["Kirwin opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de dunne!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest31 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Duffy?"]],
                         [["Duffy opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de racekak!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest32 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Dorran?"]],
                         [["Dorran opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de schijterij!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest33 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Cinaed?"]],
                         [["Cinaed opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de spuitpoep!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )

    quest34 = dict(qtype=QuestType.FetchItemQuest,
                   condition=dict(itm1=dict(nam=PouchItemDatabase.kleuren_drankje, qty=1)),
                   reward=None,  # geen reward, maar wel remove_quest_blockers() (standaard)
                   text=([["*Grumbel* Ik dorst. *Burp*",
                           "Is mooie drankje voor Boyden?"]],
                         [["Boyden opdrinken?"]],
                         ["Geef je hem het laxerende 9 kleuren drankje van Zwammix?", "",
                          "Ja, alle trollen aan de diarree!",
                          "Nee, dat is zielig."],
                         [["Lekker. *Burp* *Prrrrt*",
                           "Ik mij eventjes excuseren."],
                          ["*Prrrrt*"]],
                         [["*Prrrrt*"]])
                   )
