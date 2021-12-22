from hero_class import Hero
from enemy_class import Enemy
from main import clear_screen
import random
import os

# Create player character
def create_player_character():
    Hname = input('\nPodaj swoje imię: ').title()

    Hhealth = 400
    Hattack = random.randint(10,20)
    Hdefense = random.randint(10,20)
    Hranged = random.randint(10,20)
    Hmagic = random.randint(10,20)
    Hluck = random.randint(10,20)

    player = Hero(Hname, Hhealth, Hattack, Hdefense, Hranged, Hmagic, Hluck)
    print(f'\nBohater - {player.getName()}:')
    print(f'\n{"Zdrowie:":16} {player.getHealth()}')
    print(f'{"Atak:":16} {player.getAttack()}')
    print(f'{"Obrona:":16} {player.getDefense()}')
    print(f'{"Atak dystansowy:":16} {player.getRanged()}')
    print(f'{"Magia:":16} {player.getMagic()}')
    print(f'{"Szczęście:":16} {player.getLuck()}\n\n')


# Create enemy character
def create_enemy():
    
    with open('D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\adjective.txt', 'r', encoding='utf-8') as adj_file:
        lines = adj_file.readlines()
        adjective = lines[random.randint(0, len(lines)-1)][:-1]

    with open('D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\animal.txt', 'r', encoding='utf-8') as animal_file:
        lines2 = animal_file.readlines()
        animal = lines2[random.randint(0, len(lines2)-1)][:-1]

    health = random.randint(200,250)
    attack = random.randint(5,10)
    defense = random.randint(5,10)
    magicdefense = random.randint(5,10)
    chance = random.randint(50,100)

    return Enemy(adjective + ' ' + animal, health, attack, defense, magicdefense, chance)

enemy = create_enemy()

print(f'\n\nPrzeciwnik - {enemy.getName()}')
print(f'\n{"Zdrowie":17} {enemy.getHealth()}')
print(f'{"Atak":17} {enemy.getAttack()}')
print(f'{"Obrona":17} {enemy.getDefense()}')
print(f'{"Obrona magiczna:":17} {enemy.getMagicdefense()}')
print(f'{"Szansa trafienia:":17} {enemy.getChance()}\n\n')


# Create health bars for battle
def health_bars():
    enemy_max_health = 500
    enemy_actual_health = 500
    enemy_health_bar = '=' * int(enemy_actual_health / 10)

    print(f"\nEnemy's health:\n [{enemy_health_bar}", " " * int((enemy_max_health - enemy_actual_health)/10), "]", sep="")


    hero_max_health = 400
    hero_actual_health = random.randint(200, hero_max_health)
    hero_health_bar = '=' * int(hero_actual_health / 10)

    if hero_actual_health < hero_max_health * 0.3:
        health_bar_color = '\033[0;31m'
    elif hero_actual_health >= hero_max_health * 0.3 and hero_actual_health < hero_max_health * 0.7:
        health_bar_color = '\033[0;33m'
    elif hero_actual_health >= hero_max_health * 0.7:
        health_bar_color = '\033[0;32m'