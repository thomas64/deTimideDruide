
"""
Alle print commando's van het spel.
"""


def keyboard_down(event_key, event_unicode):
    """
    Engine.handle_single_input()
    :param event_key: integer
    :param event_unicode: string
    """
    print("Keyboard, key={}, unicode={}".format(event_key, event_unicode))


def mouse_down(event_pos, event_button):
    """
    Engine.handle_single_input()
    :param event_pos: tuple
    :param event_button: integer
    """
    print("Mouse, pos={}, button={}".format(event_pos, event_button))


def state_push(state):
    """
    StateMachine.push()
    :param state: Enum
    """
    print("Game pushed {}".format(state))


def state_pop(state):
    """
    StateMachine.pop()
    :param state: Enum
    """
    print("Game popped {}".format(state))


def state_clear():
    """
    StateMachine.clear()
    """
    print("Game cleared all states.")


def corrupt_options():
    """
    Audio._load_cfg()
    """
    print('Corrupt options file.')


def load_gamedata():
    """
    Dialog.load()
    """
    print("Loading gamedata...")


def save_gamedata():
    """
    Dialog.load()
    """
    print("Saving gamedata...")


def corrupt_gamedata():
    """
    Dialog.save()
    """
    print('Corrupt gamedata.')


def hero_join_party(hero_name, party_name):
    """
    Party.add()
    :param hero_name: string
    :param party_name: string
    """
    print("{} joined {}.".format(hero_name, party_name))


def hero_double_join(hero_name, party_name):
    """
    Party.add()
    :param hero_name: string
    :param party_name: string
    """
    print("{} is already in {}.".format(hero_name, party_name))


def hero_full_party(party_name):
    """
    Party.add()
    :param party_name: string
    """
    print("{} is full.".format(party_name))


def hero_leave_party(hero_name, party_name):
    """
    Party.remove()
    :param hero_name: string
    :param party_name: string
    """
    print("{} left {}.".format(hero_name, party_name))


def hero_not_in_party(hero_name, party_name):
    """
    Party.remove()
    :param hero_name: string
    :param party_name: string
    """
    print("{} is not in {}.".format(hero_name, party_name))


def leader_not_leave_party():
    """
    Party.remove()
    """
    print("The party leader cannot leave his own party!")


def add_equipment_item(equipment_item_quantity, equipment_item_name, inventory_name):
    """
    Inventory.add()
    :param equipment_item_quantity: integer
    :param equipment_item_name: string
    :param inventory_name: string
    """
    print("Put {} {} in {}.".format(equipment_item_quantity, equipment_item_name, inventory_name))


def quantity_less_than_one():
    """
    Inventory.add()
    """
    print("That is not possible.")


def equipment_item_name_not_in_database(equipment_item_name):
    """
    EquipmentDatabase.factory()
    :param equipment_item_name: string
    """
    print("Cannot find {} in database.".format(equipment_item_name))
