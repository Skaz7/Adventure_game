from battle_functions import battle, clear_screen
from create_characters import create_player_character
from images import *


def welcome():

    print("\033[0m", "\n\nWitaj w nowej przygodzie!")
    print("\nZacznij od stworzenia swojego bohatera.")
    print("\nPo podaniu imienia statystyki zostaną przydzielone automatycznie.")


clear_screen()
welcome()
# create_player_character()
battle()
