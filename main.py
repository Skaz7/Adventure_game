import random
import os
import time
from enemy_class import Enemy
from hero_class import Hero

def clear_screen():
    os.system('cls')

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

# print(f"Hero's health:\n {health_bar_color}[{hero_health_bar}", " " * int((hero_max_health - hero_actual_health)/10), "]", sep="")


# Create player character
clear_screen()
Hname = input('\nPodaj swoje imię: ').title()
print(f'\n\nTworzenie postaci i przydzielanie statystyk...')
time.sleep(1)

Hhealth = 400
Hattack = random.randint(10,20)
Hdefense = random.randint(10,20)
Hranged = random.randint(10,20)
Hmagic = random.randint(10,20)
Hluck = random.randint(10,20)

player = Hero(Hname, Hhealth, Hattack, Hdefense, Hranged, Hmagic, Hluck)
print(f'\n\nStatystyki postaci {player.getName()}:')
print(f'\n{"Zdrowie:":20} {player.getHealth()}')
print(f'{"Atak:":20} {player.getAttack()}')
print(f'{"Obrona:":20} {player.getDefense()}')
print(f'{"Atak dystansowy:":20} {player.getRanged()}')
print(f'{"Magia:":20} {player.getMagic()}')
print(f'{"Szczęście:":20} {player.getLuck()}\n\n')
