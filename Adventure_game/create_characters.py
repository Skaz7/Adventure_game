import random
import csv

from enemy_class import Enemy
from hero_class import Hero



def create_player_character():

    Hname = input("\nPodaj swoje imię: ").title() 
    Hhealth = 200
    Hmaxhealth = 200
    Hattack = random.randint(10, 20)
    Hdefense = random.randint(10, 20)
    Hmagic = random.randint(10, 20)
    Hluck = random.randint(18, 20)
    Hmoney = random.randint(80, 120)
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
        data = list(reader)

    data.pop(0)

    level = int(data[0][0])
    name = data[0][1]
    health = int(data[0][2])
    attack = int(data[0][3])
    defense = int(data[0][4])
    magicdefense = int(data[0][5])
    chance = int(data[0][6])
    special = data[0][7]

    return Enemy(
        level, name, health, attack, defense, magicdefense, chance, special
    )
