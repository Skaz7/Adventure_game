import os
import time
from create_characters import create_player_character, create_enemy

def clear_screen():
    os.system('cls')


def battle():
    while enemy.getHealth() > 0:
        clear_screen()
        print('''\n                     #####################
                     #    TRWA WALKA!    #
                     #####################\n\n'''
    )
        print(f'\nBohater - {player.getName()}:')
        print(f'\n{"Zdrowie:":16} {player.getHealth()}')
        print(f'{"Atak:":16} {player.getAttack()}')
        print(f'{"Obrona:":16} {player.getDefense()}')
        print(f'{"Atak dystansowy:":16} {player.getRanged()}')
        print(f'{"Magia:":16} {player.getMagic()}')
        print(f'{"Szczęście:":16} {player.getLuck()}\n\n')
        print(f'\n\nPrzeciwnik - {enemy.getName()}')
        print(f'\n{"Zdrowie":17} {enemy.getHealth()}')
        print(f'{"Atak":17} {enemy.getAttack()}')
        print(f'{"Obrona":17} {enemy.getDefense()}')
        print(f'{"Obrona magiczna:":17} {enemy.getMagicdefense()}')
        print(f'{"Szansa trafienia:":17} {enemy.getChance()}\n\n')
        print(f'\nMożliwe akcje:')
        print(f'\t1 - atak fizyczny')
        print(f'\t2 - atak dystansowy')
        print(f'\t3 - atak magiczny')
        print(f'\t4 - obrona')
        print(f'\t5 - ucieczka')
        print(f'\nCo robisz?')
        
        battle_action = input('> ')

        if battle_action == '1':
            dmg = player.getAttack() - enemy.getDefense() 
            print(f'\n Zadałeś przeciwnikowi {dmg} obrażeń.')
            enemy.setHealth(enemy.getHealth() - dmg)
            time.sleep(1)
        elif battle_action == '2':
            pass
        elif battle_action == '3':
            pass
        elif battle_action == '4':
            pass
        elif battle_action == '5':
            quit()
        else:
            print('Wybierz opcję z zakresu 1 - 5!')
    print('\n\n\t\t\t\tZWYCIĘSTWO !!!')

clear_screen()

player = create_player_character()
enemy = create_enemy()

battle()