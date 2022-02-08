import random
import csv
from explore_world import clear_screen

from enemy_class import Enemy
from hero_class import Hero


def create_player_character():

    points_to_spend = 10

    Hname = input("\n\n\t\t\t\t\t\tPodaj swoje imię: ").title() 

    attributes_dict = {"Attack": 13, "Defense": 13, "Magic": 13, "Luck": 13}

    while points_to_spend > 0:
        clear_screen()
        print(f'\nWitaj w nowej przygodzie {Hname}!')
        print(f'''\nPoniżej wyświetlone są Twoje początkowe statystyki.
Możesz je zmodyfikować przydzielając dodatkowe punkty do poszczególnych pozycji.
Zdecyduj którą ze swoich cech chcesz wzmocnić.
Pozostałe do dyspozycji punkty: {points_to_spend}\n
        ''')
        i = 1
        for attribute, value in attributes_dict.items():
            print(f'{i}. {attribute:12}: {value}')
            i += 1

        attribute_to_enhance = input("\n> ")

        if attribute_to_enhance == '1':
            attributes_dict["Attack"] += 1
        elif attribute_to_enhance == '2':
            attributes_dict["Defense"] += 1
        elif attribute_to_enhance == '3':
            attributes_dict["Magic"] += 1
        elif attribute_to_enhance == '4':
            attributes_dict["Luck"] += 1
        else:
            input('\nNieprawidłowa opcja!')
            continue
        points_to_spend -= 1

    Hhealth = 200
    Hmaxhealth = 200
    Hattack = attributes_dict["Attack"]
    Hdefense = attributes_dict["Defense"]
    Hmagic = attributes_dict["Magic"]
    Hluck = attributes_dict["Luck"]
    Hmoney = 99
    Hitems = {"weapons": {}, "consumables": {}, "other": {}}
    Hstate = []
    Hexperience = 0
    Hlevel = 1

    return Hero(
        Hname,
        Hhealth,
        Hmaxhealth,
        Hattack,
        Hdefense,
        Hmagic,
        Hluck,
        Hmoney,
        Hitems,
        Hstate,
        Hexperience,
        Hlevel,
    )


def create_enemy():

    with open(
        "D:\\users\\sebas\\onedrive\\repositories\\Adventure_game\\Adventure_game\\enemies.csv",
        "r",
        newline="",
    ) as file:
        reader = csv.reader(file)
        data = random.choice(list(reader))

    level = int(data[0])
    name = data[1]
    health = int(data[2])
    attack = int(data[3])
    defense = int(data[4])
    magicdefense = int(data[5])
    chance = int(data[6])
    special = data[7]

    return Enemy(
        level, name, health, attack, defense, magicdefense, chance, special
    )
