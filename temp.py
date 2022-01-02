import os
import copy

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

os.system('cls')

additional_attack = 0

print('\nJaki przedmiot chcesz dodać do ekwipunku?')
choice = input('> ')

if choice not in items['weapons'] and choice not in items ['consumables']:
    print('\nTaki przedmiot nie jest dostępny')

else:
    if choice in items['weapons']:
        new_items['weapons'][choice] = {}
        new_items['weapons'][choice].update(items['weapons'][choice])
        additional_attack += new_items['weapons'][choice]['Damage']

    elif choice in items['consumables']:
        new_items['consumables'][choice] = items['consumables'][choice]
        new_items['consumables'][choice].update(items['consumables'][choice])




print()
print(new_items)
print()
print(items['weapons'])
print()
for key in items['weapons'].keys():
    print(key)
print()
