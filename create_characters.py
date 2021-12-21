from hero_class import Hero
from enemy_class import Enemy
from main import clear_screen
import random
import os

# Create player character
clear_screen()
Hname = input('\nPodaj swoje imię: ').title()
print(f'\n\nTworzenie postaci i przydzielanie statystyk...')

Hhealth = 400
Hattack = random.randint(10,20)
Hdefense = random.randint(10,20)
Hranged = random.randint(10,20)
Hmagic = random.randint(10,20)
Hluck = random.randint(10,20)

player = Hero(Hname, Hhealth, Hattack, Hdefense, Hranged, Hmagic, Hluck)
print(f'\n\nStatystyki postaci {player.getName()}:')
print(f'\n{"Zdrowie:":16} {player.getHealth()}')
print(f'{"Atak:":16} {player.getAttack()}')
print(f'{"Obrona:":16} {player.getDefense()}')
print(f'{"Atak dystansowy:":16} {player.getRanged()}')
print(f'{"Magia:":16} {player.getMagic()}')
print(f'{"Szczęście:":16} {player.getLuck()}\n\n')

# Create Enemy characteristics
Ename = input('\nPodaj imię przeciwnika: ').title()
print(f'\n\nTworzenie postaci i przydzielanie statystyk...')

Ehealth = 500
Eattack = random.randint(10,20)
Edefense= random.randint(10,20)
Emagicdefense = random.randint(10,20)

enemy = Enemy(Ename, Ehealth, Eattack, Edefense, Emagicdefense)
print(f'\n\nStatystyki postaci {enemy.getName()}:')
print(f'\n{"Zdrowie:":16} {enemy.getHealth()}')
print(f'{"Atak:":16} {enemy.getAttack()}')
print(f'{"Obrona:":16} {enemy.getDefense()}')
print(f'{"Obrona magiczna:":16} {enemy.getMagicdefense()}')


input()

def draw_enemy():
    with open('D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\adjective.txt', 'r', encoding='utf-8') as adj_file:
        lines = adj_file.readlines()
        adjective = lines[random.randint(0, len(lines)-1)][:-1]
    with open('D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\animal.txt', 'r', encoding='utf-8') as animal_file:
        lines2 = animal_file.readlines()
        animal = lines2[random.randint(0, len(lines2)-1)][:-1]
    enemy1 = [adjective, animal]
    Ename = (enemy1[0], enemy1[1])

