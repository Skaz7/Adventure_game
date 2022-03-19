from explore_world import clear_screen
from functions import *
import logging


def hero_magic_attack():
    clear_screen()

    def cast_spell(spell):
        print(f"\n\n\t\tYou cast a spell {spell}")

        if functions.player.spellbook[spell]["weakness"] == functions.enemy.special:

            functions.enemy.health -= functions.player.spellbook[spell]["power"] * 2
            # functions.playsound(
            #     "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-boxer-getting-hit-2055.wav"
            # )

            functions.player.experience += int(
                (functions.player.spellbook[spell]["power"] + functions.roll_20_dice())
                * 2
            )
            print("\nYou took advantage of your enemy's weakness")
            print(
                f"\nYou've dealt {functions.player.spellbook[spell]['power'] * 2} damage to you enemy."
            )

        else:
            functions.enemy.health -= functions.player.spellbook[spell]["power"]
            functions.player.experience += int(
                functions.player.spellbook[spell]["power"] + functions.roll_20_dice()
            )
            # functions.playsound(
            #     "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-boxer-getting-hit-2055.wav"
            # )
            print(
                f"\nYou've dealt {functions.player.spellbook[spell]['power']} damage to you enemy."
            )

        functions.player.magic -= functions.player.spellbook[spell]["mana cost"]
        functions.delay_medium()

    spellbook_list = [spell for spell in functions.player.spellbook.keys()]

    print("\nSpells you own:\n")

    for i, spell in enumerate(spellbook_list, start=1):
        print(f"{i}. {spell}")
    print("\nWhich spell do you want to cast?")

    picked_spell = spellbook_list[int(input("> ")) - 1]
    spell = functions.player.spellbook[picked_spell]
    logging.debug(f"Used spell: {picked_spell}")

    print(f"\nYou choosed:")
    print(f"\n\t{picked_spell}:")

    for parameter, value in spell.items():
        print("\t", parameter.title().ljust(10, ".") + str(value).title())
    print("\n1 - Cast this Spell")
    print("2 - Go Back")

    choice = input("> ")

    if choice == "1":
        if functions.player.magic < spell["mana cost"]:
            print("\nYou don't have enough mana to cast this spell.")
            functions.delay_medium()
            hero_magic_attack()
        else:
            cast_spell(picked_spell)
        return

    elif choice == "2":
        pass

    input()

    return
