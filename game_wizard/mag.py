from game_wizard.classes import Spell, Wizard, Monster


def battle(wizard: Wizard, monster: Monster):
    while True:
        spell = fireball
        wizard.cast_spell(monster, spell)
        if monster.health <= 0:
            wizard.experience += monster.xp
            print(f"{monster.name} погибает")
            return True

        monster.attack(wizard)
        if wizard.health <= 0:
            print(f"Вас убил {monster.name}")
            print("___YOU LOSE___")
            return False



fireball = Spell("Огненный шар",
                 "fire",
                 25,
                 15,
                 1)

ice_shard = Spell("Ледяные осколки",
                 "ice",
                 20,
                 12,
                 1)

spells = [fireball, ice_shard, ]


wizard1 = Wizard("Пендальф", "fire")
wizard1.get_info()
wizard1.learn_spell(fireball)
goblin1 = Monster(name="Goblin", health=60, damage=15, element="fire", xp=30)
goblin1.get_info()

battle(wizard1, goblin1)