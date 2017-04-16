
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
                          "in der Gefangenschaft."],
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

    quest2 = dict(qtype=QuestType.PersonMessageQuest,
                  reward=dict(itm1=dict(nam=PouchItemDatabase.gold,     qty=1)),  # mag ook =None zijn.
                  people=dict(person74='main',
                              person75='sub1'),
                  text=dict(person74=([["How are you?"], ["May I ask you something?"],
                                       ["I'm a bit shy.",
                                        "There is this girl that I like, but I'm afraid to tell her."],
                                       ["Would you tell her for me instead? Please?",
                                        "She is at the armor shop looking for a dress, and I won't",
                                        "dare to come near, so I went to this shop, I'm pathetic."]],
                                      [["Please do it for me. She is at the armor shop."]],
                                      [[" "]],
                                      [["Thank you for telling her!", "You can have this, for helping me out."]],
                                      [["Thanks again, I owe you big time!"]]),
                            person75=([["How are you?"]],
                                      [["How are you?"]],
                                      # de confirmbox tekst moet niet tussen dubbele blokhaken
                                      ["Bring the pathetic message over to her?", "",
                                       "Yes, everybody needs a chance.", "No, he has to grow up and be a man."],
                                      [["I... I didn't know that...", "Thank you for telling me."]],
                                      [["How are you?"], ["I'm also pretty shy myself."]])
                            )
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
                        [[" "]], [[" "]], [[" "]],
                        [["It's so beautiful, I can watch this scenery for hours."],
                         ["    .       .       .       .       .       .       ."],
                         ["Did you 'prove' that you are not a monster?"]])
                  )

    quest5 = dict(qtype=QuestType.GoSomewhereQuest,
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
                         ["*Hikkup*"],
                         ["Brann en de stenen hebben hun werk goed gedaan."],
                         ["*Hikkup*"],
                         ["Jullie hebben mij gevonden.",
                          "Ik heb jullie nodig om mijn soepje weer te kunnen maken."],
                         ["Zonder mijn soepje ben ik mijzelf niet,",
                          "maar het lukt mij niet de soep te maken in mijn huidige staat."],
                         ["*Hikkup*"],
                         ["Hebben jullie het hele recept kunnen vinden,",
                          "en de ingrediënten bij elkaar verzameld?"]],
                        [["Zijn jullie nu wel gereed om de ingrediënten te overhandigen?"], ["*Hikkup*"]],
                        ["Indien je het recept niet compleet hebt kun je de ingrediënten aan Zwammix",
                         "overhandigen maar dan krijg je ook maar een deel van de beloning.",
                         "Let op! Je hebt tot 10.55 uur de tijd om het recept compleet te maken.",
                         "Als je nu kiest om te overhandigen krijg je niet nog een tweede mogelijkheid.",
                         "",
                         "Ja, ik wil onze ingrediënten overhandigen.",
                         "Nee, ik doe het later."],
                        [["Joepie, dankjewel voor de ingrediënten.",
                          "Ik ga gelijk m'n soepketel zoeken."],
                         ["*Hikkup*"],
                         ["Hier is je beloning voor het zoeken van de ingrediënten."]],
                        [["Waar is m'n ketel?"], ["*Hikkup*"]])
                  )
