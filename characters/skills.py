
"""
class: Skill
class: etc
"""

from constants import SkillType


PATH = 'resources/sprites/icons/skills/'

# todo, description aanpassen van skills. wanneer skills meer of anders kunnen, zoals pick locks voor thief.
# todo, docstrings


class Skill(object):
    """
    Skill baseclass voor skills.
    """
    TRAININGSCOSTS = (20, 8, 12, 16, 20, 24, 28, 32, 36, 40, "Max")
    MAXIMUM = 10                        # maximum mogelijk, is voor alle skills 10

    def __init__(self, name, raw, upgrade, quantity):
        self.NAM = name
        self.RAW = raw
        self.ICON = PATH+name.lower()+'.png'
        self.UPG = upgrade              # upgrade formule constante
        self.qty = quantity             # standaard hoeveelheid op te waarderen stat (tot bijv 30)
        self.ext = 0                    # extra: wat geeft equipment item voor pos/neg extra
        self.DESC = None

    @property
    def nxt_lev(self):
        """
        ...
        :return:
        """
        quantity = self.qty + 1
        if quantity == self.MAXIMUM + 1:
            quantity = "Max"
        return quantity

    @property
    def gold_cost(self):
        """
        ...
        :return:
        """
        if self.qty == -1:
            return 0
        else:
            return self.TRAININGSCOSTS[self.qty]

    @property
    def xp_cost(self):
        """
        ...
        :return:
        """
        xp_for_next_level = round(self.UPG * ((self.qty + 1)**2))
        if self.qty == self.MAXIMUM:
            xp_for_next_level = "Max"
        return xp_for_next_level
        # todo, loremaster skill gebruiken voor 'korting'

    def is_able_to_train(self, xp_amount, gold_amount):
        """
        ...
        :return:
        """
        if self.qty == -1:
            return False, ["You cannot train {}.".format(self.NAM)]
        elif self.qty >= self.MAXIMUM:
            return False, ["You cannot train {} any further.".format(self.NAM)]
        elif self.xp_cost > xp_amount:
            return False, ["You need {} more XP to".format(self.xp_cost - xp_amount),
                           "train {}.".format(self.NAM)]
        elif self.gold_cost > gold_amount:
            return False, ["You need {} more gold to".format(self.gold_cost - gold_amount),
                           "train {}.".format(self.NAM)]
        else:
            return True, None

    def upgrade(self):
        """
        ...
        :return:
        """
        self.qty += 1

    @property
    def tot(self):
        """
        Ext en qty vormen samen totaal.
        self.tot = self.qty + self.ext
        total: quantity + extra
        """
        total = self.qty + self.ext
        if total < 0 or self.qty <= 0:
            total = 0
        return total

    def positive_quantity(self):
        """
        ...
        """
        if self.qty >= 1:
            return True
        return False

    def show_info(self):
        """
        show_info is polymorph met EquipmentItem()
        :return:
        """
        return self.DESC


class Alchemist(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.alc.value, SkillType.alc.name, 12, quantity)
        self.DESC = "Allows the character to manufacture various potions out of Herbs, Spices and Gemstones. " \
                    "A higher Alchemist rank means a higher chance to successfully create a potion."


class Diplomat(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.dip.value, SkillType.dip.name, 4, quantity)
        self.DESC = "The higher the Diplomat rank, the lower are the conditions of new heroes who wants to join " \
                    "the party. For every 1 Diplomat rank gained, 1% lower conditions. Cumulative for all characters."


class Healer(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.hlr.value, SkillType.hlr.name, 8, quantity)
        self.DESC = "Allows the character to heal another character in combat. " \
                    "Character may use herbs to double the amount of damage restored. " \
                    "A higher Healer rank means more restoration of damage."


class Loremaster(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.lor.value, SkillType.lor.name, 6, quantity)
        self.DESC = "Lowers the XP needed for training Stats(?), Skills and Spells. " \
                    "For every 1 Loremaster rank gained, 1% less XP is needed."


class Mechanic(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.mec.value, SkillType.mec.name, 4, quantity)
        self.DESC = "Allows the character to upgrade inventory with metals. The process also costs gold. " \
                    "A higher Mechanic rank means a higher chance to successfully upgrade an item. " \
                    "The item is destroyed when upgrade is unsuccessful."


class Merchant(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.mer.value, SkillType.mer.name, 6, quantity)
        self.DESC = "The higher the Merchant rank, the lower the prices when buying (and the higher the " \
                    "prices when selling) in shops. For every 1 Merchant rank gained, 1% extra gold in your " \
                    "favor. Cumulative for all characters."


class Ranger(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.ran.value, SkillType.ran.name, 8, quantity)
        self.DESC = "Helps to increase the amount of Herbs, Spices, Gemstones and Metals " \
                    "when searching for materials. More characters " \
                    "with this skill will help to find even more materials."


class Stealth(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.stl.value, SkillType.stl.name, 4, quantity)
        self.DESC = "Makes it easier to flee from combat. For every 1 Stealth rank gained, 1% more chance " \
                    "to flee. Cumulative for all characters. Also when in combat, for every 2 Stealth ranks " \
                    "gained, the enemy thinks the character is 1 position further away."


class Thief(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.thf.value, SkillType.thf.name, 8, quantity)
        self.DESC = "Improves character's chance to hit and increases damage " \
                    "inflicted FROM BEHIND in combat. For every 1 Thief rank gained, " \
                    "2% more chance to hit and 3% more damage."


class Troubadour(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.trb.value, SkillType.trb.name, 8, quantity)
        self.DESC = "Allows character to play and sing inspirationally, improving your party's chance " \
                    "to hit in combat and reducing the enemy's chance to hit. For every 1 Troubadour " \
                    "rank gained, 2% more chance to hit."


class Warrior(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.war.value, SkillType.war.name, 8, quantity)
        self.DESC = "Improves base hit of character's weapon. Especially weapons with a low base hit. " \
                    "It also allows the possibility of scoring critical hits in combat. For every 1 " \
                    "Warrior rank gained, 2% extra chance for a critical hit. And overall, it improves " \
                    "combat damage and defenses."

    def bonus(self, wpn):
        """
        Berekent de warrior bonus.
        :param wpn: EquipmentItem object van weapon
        :return: de formule of anders 0
        """
        if self.positive_quantity() and wpn.is_not_empty():
            return round((47 - ((wpn.HIT / 10) * 5)) * (self.tot / 10))
        return 0


class Wizard(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.wiz.value, SkillType.wiz.name, 12, quantity)
        self.DESC = "At the moment, Wizard does nothing."


class Hafted(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.haf.value, SkillType.haf.name, 3.2, quantity)
        self.DESC = "Improves character's chance to hit and increases damage inflicted with Hafted weapons in " \
                    "combat. For every 1 Hafted rank gained, 2% more chance to hit and 1% more damage."


class Missile(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.mis.value, SkillType.mis.name, 4.8, quantity)
        self.DESC = "Improves character's chance to hit and increases damage inflicted with Missile weapons in " \
                    "combat. For every 1 Missile rank gained, 2% more chance to hit and 1% more damage."


class Pole(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.pol.value, SkillType.pol.name, 3.2, quantity)
        self.DESC = "Improves character's chance to hit and increases damage inflicted with Pole weapons in combat. " \
                    "For every 1 Pole rank gained, 2% more chance to hit and 1% more damage."


class Shield(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.shd.value, SkillType.shd.name, 4, quantity)
        self.DESC = "Improves character's defenses when wearing a shield in combat. A shield doesn't defend " \
                    "character's back."


class Sword(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.swd.value, SkillType.swd.name, 4.8, quantity)
        self.DESC = "Improves character's chance to hit and increases damage inflicted with all types of swords " \
                    "and daggers in combat. For every 1 Sword rank gained, 2% more chance to hit and 1% more damage."


class Thrown(Skill):
    """
    ...
    """
    def __init__(self, quantity):
        super().__init__(SkillType.thr.value, SkillType.thr.name, 3.2, quantity)
        self.DESC = "Improves character's chance to hit and increases damage inflicted with Thrown weapons in " \
                    "combat. For every 1 Thrown rank gained, 2% more chance to hit and 1% more damage."
