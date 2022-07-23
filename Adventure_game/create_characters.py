import random
import csv
from explore_world import clear_screen

from enemy_class import Enemy
from hero_class import Hero


def create_player_character():

    points_to_spend = 10

    Hname = input("\n\n\t\t\t\t\t\tWhat's your name: ").title()

    attributes_dict = {"Attack": 13, "Defense": 13, "Magic": 13, "Luck": 13}

    while points_to_spend > 0:
        clear_screen()
        print(f"\nWelcome to the new adventure, {Hname}!")
        print(
            f"""\nYour initial stats are displayed below.
You can modify them by assigning additional points to individual stat.
Decide which of your traits you want to strengthen.
Remaining points available: {points_to_spend}\n
        """
        )
        i = 1
        for attribute, value in attributes_dict.items():
            print(f"{i}. {attribute:12}: {value}")
            i += 1

        attribute_to_enhance = input("\n> ")

        if attribute_to_enhance == "1":
            attributes_dict["Attack"] += 1
        elif attribute_to_enhance == "2":
            attributes_dict["Defense"] += 1
        elif attribute_to_enhance == "3":
            attributes_dict["Magic"] += 1
        elif attribute_to_enhance == "4":
            attributes_dict["Luck"] += 1
        else:
            input("\nWrong option!")
            continue
        points_to_spend -= 1

    Hhealth = 200
    Hmaxhealth = 200
    Hattack = attributes_dict["Attack"]
    Hdefense = attributes_dict["Defense"]
    Hmagic = attributes_dict["Magic"]
    Hluck = attributes_dict["Luck"]
    Hmoney = 99
    Hinventory = {"weapons": {}, "consumables": {}, "other": {}}
    Hspellbook = {
        "Sparks": {
            "element": "fire",
            "power": 10,
            "weakness": "freeze",
            "mana cost": 5,
            "level": 1,
        },
        "Cold": {
            "element": "freeze",
            "power": 10,
            "weakness": "burn",
            "mana cost": 5,
            "level": 1,
        },
    }
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
        Hinventory,
        Hspellbook,
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
    # regions = data[8]

    return Enemy(level, name, health, attack, defense, magicdefense, chance, special)
