import os
import random
import time
import json
from create_characters import create_player_character, create_enemy

def clear_screen():
    os.system('cls')


def import_items_from_file():
    with open('D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\items.json', 'r') as file:
        global items
        items = json.load(file)


def roll_20_dice():
    return random.randint(0,20)


def victory():
        clear_screen()
        print('\n\n\n\n\n\t\t\t\t********************')
        print('\t\t\t\t*  ZWYCIĘSTWO !!!  *')
        print('\t\t\t\t********************\n\n\n\n')
        time.sleep(2)

        print(f'{player.getName()}, czy chcesz grać dalej? (T/N)')

        choice = input('> ').lower()

        if choice == 't':
            battle()

        elif choice == 'n':
            print('\t\t\t\t********************')
            print('\t\t\t\t*  DO ZOBACZENIA!  *')
            print('\t\t\t\t********************\n\n\n')
            quit()

        else:
            print('\t\t\t\t\n\nMusisz wybrać T lub N')
            time.sleep(1)
            victory()


def attack():
    player_hit_chance = (roll_20_dice() + player.getLuck()) - (roll_20_dice() + enemy.getChance())

    if player_hit_chance > 0:

        print(f'\nUdało Ci się zadać cios.') 
        enemy_damage = roll_20_dice() + player.getAttack() - enemy.getDefense()

        if enemy_damage < 0:
            enemy_damage == 0

        else:
            pass
        print(f'\n Przeciwnik odniósł {enemy_damage} obrażeń.')
        enemy.setHealth(enemy.getHealth() - enemy_damage)
        time.sleep(1)

    else:
        print('\nNie udało Ci się zadać ciosu, przeciwnik był sprytniejszy.')
        time.sleep(1)

    if enemy.getHealth() <= 0:
        victory()

    else:
        print(f'\nCzas na ruch przeciwnika.')
        time.sleep(1)

        print(f'{enemy.getName()} atakuje!')
        time.sleep(1)

        enemy_hit_chance = (roll_20_dice() + enemy.getChance()) - (roll_20_dice() + player.getLuck())

        if enemy_hit_chance > 0:
            print('Jego cios Cię dosięgnął.')
            player_damage = roll_20_dice() + enemy.getAttack() - player.getDefense()

            if player_damage < 0:
                time.sleep(1)
                print(f'{enemy.getName()} nie zadał Ci obrażeń...')

            else:   
                time.sleep(1)
                print(f'{enemy.getName()} zadał Ci {player_damage} obrażeń...')
                player.setHealth(player.getHealth() - player_damage)
                time.sleep(2)
        else:
            print(f'{enemy.getName()} nie zdołał Cię dosięgnąć.')
            time.sleep(2)


def magic_attack():
    enemy_damage = roll_20_dice() + player.getMagic() - enemy.getMagicdefense() 

    print(f'\n Zadałeś przeciwnikowi {enemy_damage} obrażeń.')
    enemy.setHealth(enemy.getHealth() - enemy_damage)
    time.sleep(1)


def use_item(item):
    clear_screen()
    print('\n\nPosiadane przez Ciebie przedmioty:')

    pass


def defense():
    print('Obrona nie jest opcją, musisz atakować!')
    time.sleep(1)


def run():
    run_chance = player.getLuck() + roll_20_dice()
    stop_chance = enemy.getChance() + roll_20_dice()

    if run_chance > stop_chance:
        print('\nUdało Ci się uciec z miejsca potyczki, przeciwnik nie może Cię dogonić.')
        time.sleep(2)
        battle()

    else:
        print('\nNie udało Ci się uciec, przeciwnik był sprytniejszy i walka trwa dalej.')
        time.sleep(2)
        return


def battle():

    global enemy
    enemy = create_enemy()
    enemy_max_health = enemy.getHealth()
    player_max_health = player.getHealth()

    while True:
        clear_screen()

        print('''\n\t\t\t\t\t#####################
        \t\t\t\t#    TRWA WALKA!    #
        \t\t\t\t#####################\n''')

        player_health_bar = '=' * int(player.getHealth() / 2)

        if player.getHealth() < player_max_health * 0.3:
            player_health_bar_color = '\033[0;31m'

        elif player_max_health * 0.3 <= player.getHealth() < player_max_health * 0.7:
            player_health_bar_color = '\033[0;33m'

        elif player.getHealth() >= player_max_health * 0.7:
            player_health_bar_color = '\033[0;32m'

        print(f'\nBohater - {player.getName()}')
        print('-' * (10 + len(player.getName())))       
        print(f'{"Zdrowie:":16} {player.getHealth()} {player_health_bar_color} [{player_health_bar}',
            ' ' * int((player_max_health - player.getHealth())/2), ']', '\033[0m', sep='')
        print(f'{"Atak:":16} {player.getAttack()}')
        print(f'{"Obrona:":16} {player.getDefense()}')
        print(f'{"Magia:":16} {player.getMagic()}')
        print(f'{"Szczęście:":16} {player.getLuck()}')
        print(f'{"Pieniądze:":16} {player.getMoney()}\n')


        print(f'\nPrzeciwnik - {enemy.getName()}')
        print('-' * (13 + len(enemy.getName())))
        
        enemy_health_bar = '=' * int(enemy.getHealth() / 2)

        if enemy.getHealth() < enemy_max_health * 0.3:
            enemy_health_bar_color = '\033[0;31m'

        elif enemy_max_health * 0.3 <= enemy.getHealth() < enemy_max_health * 0.7:
            enemy_health_bar_color = '\033[0;33m'

        elif enemy.getHealth() >= enemy_max_health * 0.7:
            enemy_health_bar_color = '\033[0;32m'


        print(f'{"Zdrowie":17} {enemy.getHealth()} {enemy_health_bar_color} [{enemy_health_bar}',
            ' ' * int((enemy_max_health - enemy.getHealth())/2),']', '\033[0m', sep='')
        print(f'{"Atak":17} {enemy.getAttack()}')
        print(f'{"Obrona":17} {enemy.getDefense()}')
        print(f'{"Obrona magiczna:":17} {enemy.getMagicdefense()}')
        print(f'{"Szansa trafienia:":17} {enemy.getChance()}')
       
        print(f'\n--------------------------------')
        print(f'| Możliwe akcje:\t       |')
        print(f'|\t 1 - atak fizyczny     |')
        print(f'|\t 2 - atak magiczny     |')
        print(f'|\t 3 - użycie przedmiotu |')
        print(f'|\t 4 - obrona            |')
        print(f'|\t 5 - ucieczka          |')
        print(f'--------------------------------')
        print(f'\nCo robisz?')
        
        battle_action = input('> ')

        if battle_action == '1':
            attack()
        elif battle_action == '2':
            magic_attack()
        elif battle_action == '3':
            pass
        elif battle_action == '4':
            defense()
        elif battle_action == '5':
            run()
        else:
            print('Wybierz opcję z zakresu 1 - 5!')


def welcome():
    clear_screen()

    print('\033[0m', '\n\n\t\t\t\tWitaj w nowej przygodzie!')
    print('\n\t\t\t\tZacznij od stworzenia swojego bohatera.')
    print('\n\t\t\t\tPo podaniu imienia statystyki zostaną przydzielone automatycznie.')

    global player
    import_items_from_file()
    player = create_player_character()
    for i in range(0, len(player.getItems())):
        if player.getItems()[i][0] in items['weapons']:
            print('JEST')
            print(player.getItems()[i][0])
            time.sleep(3)
        else:
            print('NIE MA')
            print(player.getItems()[i][0])
            time.sleep(3)
welcome()
battle()

