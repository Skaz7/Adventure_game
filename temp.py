import os
import random

items = {'weapons':
             {'Knife': {'Damage': 10, 'Durability': 5, 'Defense': 0, 'Cost': 25},
              'Sword': {'Damage': 15, 'Durability': 10, 'Defense': 0, 'Cost': 35},
              'Axe': {'Damage': 20, 'Durability': 15, 'Defense': 0, 'Cost': 50},
              'Spear': {'Damage': 15, 'Durability': 7, 'Defense': 7, 'Cost': 40},
              'Shield': {'Damage': 0, 'Durability': 7, 'Defense': 10, 'Cost': 35},
              'Armor': {'Damage': 0, 'Durability': 10, 'Defense': 15, 'Cost': 50}},
         'consumables':
             {'Life Potion': {'HP': 40, 'MP': 0, 'Cost': 10},
              'Big Life Potion': {'HP': 80, 'MP': 0, 'Cost': 20},
              'Mana Potion': {'HP': 0, 'MP': 10, 'Cost': 10},
              'Big Mana Potion': {'HP': 0, 'MP': 20, 'Cost': 20}}}


new_items = {'weapons': {}, 'consumables': {}}


def roll_20_dice():
    # imitates 20-side dice roll
    return random.randint(1, 20)


os.system('cls')

for item_type, item in items.items():

    for k, v in item.items():

        print(k, v)

        loot_chance = (roll_20_dice() - int(v['Cost'] / 5)) - (roll_20_dice() * 2)

        if loot_chance > 0:

            print(f'Sukces! Różnica wynosiła {loot_chance}')

        else:

            print(f'Porażka... Różnica wysoniła {loot_chance}')
        print()
