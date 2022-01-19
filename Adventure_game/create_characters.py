import random

from enemy_class import Enemy
from hero_class import Hero


# Create player character
def create_player_character():
    """
    Creates player character with statistics based on random values between 10 and 20.
    Player name is based on input by user.
    """

    Hname = input("\nPodaj swoje imię: ").title()

    Hhealth = 200
    Hattack = random.randint(10, 20)
    Hdefense = random.randint(10, 20)
    Hmagic = random.randint(10, 20)
    Hluck = random.randint(10, 20)
    Hmoney = random.randint(20, 40)
    Hitems = {
        "weapons": {
            "Knife": {"Damage": 10, "Durability": 5, "Price": 25},
            "Axe": {"Damage": 20, "Durability": 15, "Cost": 50},
            "Shield": {"Defense": 10, "Durability": 7, "Cost": 35},
        },
        "consumables": {
            "Life Potion": {"HP": 40, "Durability": 1, "Cost": 10},
            "Mana Potion": {"MP": 10, "Durability": 1, "Cost": 10},
        },
        "other": {

        }
    }
    Hstate = []
    Hexperience = 0
    Hlevel = 1

    return Hero(
        Hname,
        Hhealth,
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


# Create enemy character
def create_enemy():
    """
    Creates enemy character, with statistics based on random values between 5 and 10.
    Enemy name is created from adjective and animal name both taken randomly from two files.
    """

    with open(
        "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\adjective.txt",
        "r",
        encoding="utf-8",
    ) as adj_file:
        lines = adj_file.readlines()
        adjective = lines[random.randint(0, len(lines) - 1)][:-1]

    with open(
        "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\animal.txt",
        "r",
        encoding="utf-8",
    ) as animal_file:
        lines2 = animal_file.readlines()
        animal = lines2[random.randint(0, len(lines2) - 1)][:-1]

    health = random.randint(100, 150)
    attack = random.randint(5, 10)
    defense = random.randint(5, 10)
    magicdefense = random.randint(5, 10)
    chance = random.randint(10, 20)

    return Enemy(
        adjective + " " + animal, health, attack, defense, magicdefense, chance
    )
