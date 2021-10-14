import time
import os

# Wytypowanie jak gracz może odpowiedzieć
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["T", "t", "tak"]
no = ["N", "n", "nie"]


# Bazowe statystyki
race = []
charisma = 0
strength = 0
wisdom = 0


# Funkcja czyszczenia ekranu
def clear_screen():

    os.system("cls")


# Rozdanie puktów statystyk z puli 20 punktów
def statistics():

    remain_points = 20


# Tworzenie postaci
def create_character():

    clear_screen()

    print('Podaj swoje imię:')
    player_name = input('\n>>> ')

    while True:
        try:
            print('\nJaką rasę wybierasz?')
            print('\n1 - Człowiek')
            print('2 - Elf')
            print('3 - Krasnolud')
            print('4 - Ork')
            player_race = int(input('\n>>> '))

        except ValueError:
            print('\nMusisz wybrać cyfrę 1 - 4!\n')
            continue

        # if player_race < 1 or player_race > 4:
        #     print('\nMusisz wybrać cyfrę 1 - 4!\n')
        #     continue

        if player_race == 1:
            charisma += 1
        elif player_race == 2:
            wisdom += 1
        elif player_race == 3:
            strength += 1
        elif player_race == 4:
            print('Jesteś tak brzydki że nikt nie chce z Tobą gadać.')
            print('\nPRZEGRAŁEŚ!')
        else:
            print('\nMusisz wybrać cyfrę 1 - 4!\n')
            continue

# Początek gry
def start_game():

    create_character()

    print('Siedzisz przy stole w obskurnej karczmie. Za oknem ')




#############################################################
# PROGRAM GŁÓWMNY #
#############################################################

start_game()