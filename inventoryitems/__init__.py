
"""
def: factory_empty_equipment_item
def: factory_equipment_item
def: factory_equipment_item
def: factory_all_quests
"""

# todo, uit colornote app:
# - min int gebruiken voor items?
# - mvp aan items


def factory_empty_equipment_item(equipment_type):
    """
    Geeft een 'empty' EquipmentItem object terug op verzoek van een type.
    Met **, hij verwacht een dict.
    :param equipment_type: Enum EquipmentType, dus bijv. "sld" "Shield".
    """
    from .equipment import EquipmentItem

    return EquipmentItem(**dict(typ=equipment_type))


def factory_equipment_item(enum):
    """
    :param enum: Enum waarde uit een van de equipment databases.
    :return: een object op basis van het item uit de enum database.
    """
    from .equipment import EquipmentItem

    return EquipmentItem(**enum.value)


def factory_pouch_item(enum):
    """
    :param enum: Enum waarde uit de PouchItemDatabase
    :return: een object op basis van het item uit de database
    """
    from database.pouchitem import PouchItemDatabase

    from .pouch import PouchItem
    from .pouch import HealingPotion
    from .pouch import CuringPotion
    from .pouch import StaminaPotion
    from .pouch import RestorePotion

    # de check moet op de name. door de shop kan het namelijk ook vanuit een andere enum komen, maar de naam
    # zal in ieder geval hetzelfde zijn. dus daar kan de check op.
    if enum.name == PouchItemDatabase.hlg_pot.name:
        return HealingPotion(**enum.value)
    elif enum.name == PouchItemDatabase.cur_pot.name:
        return CuringPotion(**enum.value)
    elif enum.name == PouchItemDatabase.sta_pot.name:
        return StaminaPotion(**enum.value)
    elif enum.name == PouchItemDatabase.res_pot.name:
        return RestorePotion(**enum.value)
    else:
        return PouchItem(**enum.value)


def factory_all_quests(quests_enum):
    """
    Maak een dict van QuestItem Objecten uit de Enum database.
    :param quests_enum: de enum class met alle quest data
    :return: de dict met alle quest objecten
    """

    # deepcopy() is nodig voor kopie van reward die bij een fetchitemspartly wordt aangepast
    # en dat moet natuurlijk niet terug komen in een nieuwe game.
    from copy import deepcopy

    from constants import QuestType

    from .quest import FetchItemQuestItem
    from .quest import ReceiveItemQuestItem
    from .quest import FetchItemsPartlyQuestItem
    from .quest import PersonMessageQuest1Item
    from .quest import PersonMessageQuest2Item

    quests_dict = dict()
    for quest_enum in quests_enum:
        if quest_enum.value['qtype'] == QuestType.FetchItemQuest:
            quests_dict[quest_enum.name] = FetchItemQuestItem(**deepcopy(quest_enum.value))
        elif quest_enum.value['qtype'] == QuestType.ReceiveItemQuest:
            quests_dict[quest_enum.name] = ReceiveItemQuestItem(**deepcopy(quest_enum.value))
        elif quest_enum.value['qtype'] == QuestType.FetchItemsPartlyQuest:
            quests_dict[quest_enum.name] = FetchItemsPartlyQuestItem(**deepcopy(quest_enum.value))
        elif quest_enum.value['qtype'] == QuestType.PersonMessageQuest1:
            quests_dict[quest_enum.name] = PersonMessageQuest1Item(**deepcopy(quest_enum.value))
        elif quest_enum.value['qtype'] == QuestType.PersonMessageQuest2:
            quests_dict[quest_enum.name] = PersonMessageQuest2Item(**deepcopy(quest_enum.value))
    return quests_dict
