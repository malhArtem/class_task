ELEMENT_BONUS = {
    "fire": {"ice": 1.5, "nature": 1.5, "water": 0.5},
    "ice": {"fire": 0.5, "lightning": 1.5, "earth": 1.5},
    "lightning": {"water": 1.5, "ice": 0.5, "air": 1.5}
}


def calculate_damage(spell, wizard):
    """
    Рассчитывает итоговый урон с учетом стихий
    fire > ice > lightning > water > fire
    Возвращает: модифицированный урон
    """
    damage = spell.power * ELEMENT_BONUS[wizard.element].get(spell.name, 1)
    return damage


class Spell:
    def __init__(self, name, element, power, cost, level):
        self.name = name
        self.element = element
        self.power = power
        self.cost = cost
        self.level = level



class Wizard:
    def __init__(self, name, element):
        self.name = name
        self.element = element
        self.level = 1
        self.health = 100
        self.mana = 50
        self.experience = 0
        self.known_spells = []
        self.inventory = []


    def get_info(self):
        print(f"{self.name}[{self.level}]"
              f"\nhealth: {self.health}"
              f"\nmana: {self.mana}"
              f"\nexperience: {self.experience}")


    def learn_spell(self, spell):
        if spell.name in self.known_spells:
            print("заклинание уже изучено")
            return False
        if spell.level > self.level:
            print("Не хватает уровня")
            return False
        self.known_spells.append(spell)
        return True


    def cast_spell(self, target, spell):
        if spell not in self.known_spells:
            print("Заклинание не изучено")
            return False
        if self.mana < spell.cost:
            print("Недостаточно маны")
            return False

        damage = calculate_damage(spell, self)
        target.health -= damage
        print(f"Вы наносите {damage} урона {target.name}")
        if target.health <= 0:
            target.health = 0
        return True


class Monster:
    def __init__(self,name,  health, damage, element, xp):
        self.name = name
        self.element = element
        self.health = health
        self.damage = damage
        self.xp = xp

    def get_info(self):
        print(f"{self.name}[HP:{self.health} DM:{self.damage}]")


    def attack(self, target):
        target.health -= self.damage
        print(f"{self.name} наносит вам {self.damage} урона")
        if target.health <= 0:
            target.health = 0