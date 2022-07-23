import os
import random
import time
import logging
import pytest
import pickle

from images import *
from constants import *
from create_characters import *
from explore_world import *
from other_classes import *
from hero_magic_attack import hero_magic_attack
from playsound import playsound


LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(
    filename="D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\test\\Test.log",
    level=logging.DEBUG,
    format=LOG_FORMAT,
    filemode="w",
)
logger = logging.getLogger()


def clear_screen():
    os.system("cls")


def delay_short():
    time.sleep(0.5)


def delay_medium():
    time.sleep(1.5)


def delay_long():
    time.sleep(3)


def roll_20_dice():
    return random.randint(1, 20)


def roll_6_dice():
    return random.randint(1, 6)


def start_game():
    clear_screen()

    game_title = "first rpg adventure"

    print(f'\n\n\n{"=" * (len(game_title) + 4):^120}')
    print(f'{"|" + " " * (len(game_title) + 4) + "|":^120}')
    print(f'{"|  " + game_title.upper() + "  |":^120}')
    print(f'{"|" + " " * (len(game_title) + 4) + "|":^120}')
    print(f'{"=" * (len(game_title) + 4):^120}\n\n\n')

    print(f'{"Choose option:          ":^120}\n')
    print(f'{"1 - New game        ":^120}')
    print(f'{"2 - Load saved game":^120}\n')
    print(f'{"Your choice:             ":^120}\n')

    # playsound(
    #     "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-game-experience-level-increased-2062.wav"
    # )
    choice = input(f"\t\t\t\t\t\t> ")

    if choice == "1":
        global player
        player = create_player_character()
        town()
    elif choice == "2":
        print(f'\n{"FUNCTION DOES NOT WORK YET":^120}')
        delay_medium()
        start_game()
    else:
        print(f'\n{"YOU CHOSE THE WRONG OPTION!":^120}')
        delay_medium()
        start_game()


def save_game():
    data = {"saved_name": player.name, 
            "saved_health": player.health, 
            "saved_maxhealth": player.maxhealth, 
            "saved_attack":player.attack,
            "saved_defense": player.defense,
            "saved_magic": player.magic,
            "saved_luck": player.luck,
            "saved_money": player.money,
            "saved_inventory": player.inventory,
            "saved_spellbook": player.spellbook,
            "saved_state": player.state,
            "saved_experience": player.experience,
            "saved_level": player.level}
    
    savefile = "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Adventure_game\\savefile.txt"
    with open(savefile, 'wb') as file:
        pickle.dump(data, file)


def hero_attack():
    """
    Chance for hit an enemy is based on hero and enemy luck, and 20-side dice roll.
    If hero hits an enemy, he gets experience points equal to hit chance and 6-side dice roll.
    When hero experience exceeds levels set in a given list, he gets a new level.
    """
    player_hit_chance = (roll_20_dice() + player.luck) - (roll_20_dice() + enemy.chance)

    if player_hit_chance > 0:

        print(f"\nYour attack was successful.")
        enemy_damage = roll_20_dice() + player.attack - enemy.defense
        player.experience = player.experience + int(
            (player_hit_chance + roll_6_dice()) * 5 * player.level * 0.5
        )

        if enemy_damage < 0:
            enemy_damage == 0

        else:
            critical_chance = random.randint(0, 100)

            if critical_chance > 90:
                print(
                    f"\nYou dealt critical damage. The Enemy has lost {int(player.attack * 1.5)} health."
                )
                # playsound(
                #     "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-boxer-getting-hit-2055.wav"
                # )
                enemy.health = int(enemy.health - int(player.attack * 1.5))
                delay_short()

            else:
                print(f"\nThe Enemy has lost {enemy_damage} health.")
                enemy.health = int(enemy.health - enemy_damage)
                # playsound(
                #     "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-boxer-getting-hit-2055.wav"
                # )
                delay_short()

    else:
        print("\nThe enemy was faster, you failed to attack.")
        delay_short()

    # player stats increased by used item are going back to previous level
    player.attack -= player_temp_stat_boost["Damage"]
    player.defense -= player_temp_stat_boost["Defense"]
    player.luck -= player_temp_stat_boost["Luck"]
    player.magic -= player_temp_stat_boost["Magic"]

    # stats boost reset
    player_temp_stat_boost["Damage"] = 0
    player_temp_stat_boost["Defense"] = 0
    player_temp_stat_boost["Luck"] = 0
    player_temp_stat_boost["Magic"] = 0

    if enemy.health <= 0:
        # hero gets 10% extra experience for defeating an enemy
        player.experience = int(player.experience * 1.1)

        if player.experience > levels[0]:
            clear_screen()
            player.level_up()
            del levels[0]

        delay_short()
        victory()

    else:
        pass


def enemy_attack():
    print(f"\nEnemy Turn.")
    delay_short()

    print(f"{enemy.name} attacks!")
    delay_short()

    enemy_hit_chance = (roll_20_dice() + enemy.chance) - (roll_20_dice() + player.luck)

    if enemy_hit_chance > 0:
        print("Enemy hits you.")
        player_damage = roll_20_dice() + enemy.attack - player.defense

        if player_damage < 0:
            delay_short()
            print(f"{enemy.name} nie zadał Ci obrażeń...")
            delay_short()

        else:
            critical_chance = roll_20_dice()

            if critical_chance > 18:
                print(f"{enemy.name} zadał Ci {int(player_damage * 1.2)} obrażeń.")
                print(
                    f"\nNiestety zadał krytyczny cios, powodując u Ciebie {enemy.special}."
                )
                player.health = player.health - int(player_damage * 1.2)
                delay_medium()

                set_player_state()

                if player.health <= 0:
                    defeat()
                delay_short()
            else:
                print(f"{enemy.name} zadał Ci {player_damage} obrażeń...")
                player.health = player.health - player_damage
                if player.health <= 0:
                    defeat()
                delay_short()
    else:
        print(f"{enemy.name} nie zdołał Cię dosięgnąć.")
        delay_short()

    check_player_state()


def check_player_state():
    if player.health <= 0:
        defeat()
    else:
        if len(player.state) == 0:
            pass
        else:
            condition = f"player.{player.state[0].lower()}()"
            eval(condition)


def use_item():
    """
    Function for using items from Hero's inventory.
    First you have to choose item type from: weapons/armor, consumables/mixtures, magical items
    Then you choose specific item from given type
    In case of consumables, its destroyed after use and removed from inventory
    In case of weapons and armor, its durability is decreased each turn of battle, and item is destroyed afters its durability reaches 0
    """
    clear_screen()

    print("\nItem of which type you want to use?\n")
    print("1 - Weapon / Armor.")
    print("2 - Consumables.")
    print("3 - Other.\n")
    print("0 - Back")

    choice = input("\n> ")

    def choose_item_type(item_type):
        clear_screen()

        print(f"\n\nItems of type {item_type.capitalize()} that you own:")

        # list of every item in Hero's inventory
        for k, v in player.inventory[item_type].items():
            print(f"\n{k.capitalize()} : ")
            print("-" * (len(k) + 5))

            for x, y in v.items():
                print(f"\t{x:10} -", y)

        # create item list from dictionary keys
        item_list = list(player.inventory.get(item_type))
        print(f"\nWhat do you want to use this turn?\n")

        for i in enumerate(item_list, start=1):
            print(*i)

        try:
            choice = int(input("\n> "))

            if choice < 0 or choice > len(item_list):
                print("\nYou chose the wrong option, please try again.")
                return

            elif choice == 0:
                return

            else:
                choosed_item_data = player.inventory[item_type][item_list[choice - 1]]
                choosed_item_name = item_list[choice - 1]

                if "Damage" in choosed_item_data:
                    player.attack = player.attack + choosed_item_data["Damage"]

                    player_temp_stat_boost["Damage"] = choosed_item_data["Damage"]

                elif "Defense" in choosed_item_data:
                    player.defense = player.defense + choosed_item_data["Defense"]

                    player_temp_stat_boost["Defense"] = choosed_item_data["Defense"]

                elif "HP" in choosed_item_data:
                    # if actual health plus potion HP exceeds max health level, potion effect is reduced
                    if player.health + choosed_item_data["HP"] > player.maxhealth:
                        player.health = player.maxhealth

                    else:
                        player.health = player.health + choosed_item_data["HP"]

                elif "MP" in choosed_item_data:
                    player.magic = player.magic + choosed_item_data["MP"]
                    player_temp_stat_boost["Magic"] = choosed_item_data["MP"]

                elif "Luck" in choosed_item_data.keys():
                    player.luck = player.luck + choosed_item_data["Luck"]
                    player_temp_stat_boost["Luck"] = choosed_item_data["Luck"]

                elif "Clear State" in choosed_item_data.keys():
                    player.state = []

                elif "Cure Poison" in choosed_item_data.keys():
                    player.state.remove("poisoned")

                elif "Cure Burn" in choosed_item_data.keys():
                    player.state.remove("burned")

                elif "Bandage" in choosed_item_data.keys():
                    player.state.remove("bleed")

                elif "Teleport" in choosed_item_data.keys():
                    destination = list(choosed_item_data.values())[0]
                    # delete teleport scroll after use
                    del choosed_item_data

                    if player.experience > levels[0]:
                        clear_screen()
                        player.level_up()
                        del levels[0]
                    else:
                        pass
                    teleport(destination)

                else:
                    pass

            use_item_text = f"You use {choosed_item_name}, your statistics increases."
            print(f"\n\n\t\t\t", "-" * (len(use_item_text) + 6))
            print(f"\t\t\t |  {use_item_text}  |")
            print(f"\t\t\t", "-" * (len(use_item_text) + 6))

            delay_short()

            # durability of item is decreased after each use. Consumables are destroyed after one use
            choosed_item_data["Durability"] -= 1

            # if item durability reaches 0, item is destroyed and removed from inventory
            if choosed_item_data["Durability"] < 1:
                print(f"\n\t\t\t\t  Item {choosed_item_name} was destroyed!\n")
                del player.inventory[item_type][f"{choosed_item_name}"]
            delay_medium()

        except ValueError:
            return

    if choice == "1":
        choose_item_type("weapons")

    elif choice == "2":
        choose_item_type("consumables")

    elif choice == "3":
        choose_item_type("other")

    elif choice == "0" or choice == "":
        return

    else:
        return


def defense():
    pass


def set_player_state():
    if len(player.state) == 0:
        player.state.append(enemy.special)

    else:
        pass


def battle():

    global enemy
    enemy = create_enemy()

    while enemy.level > player.level + 1 or enemy.level < player.level - 4:
        enemy = create_enemy()

    enemy_max_health = enemy.health
    # player.maxhealth = player.health
    turn_counter = 0

    while player.health > 0 and enemy.health > 0:

        clear_screen()
        turn_counter += 1

        print()
        print(f"BATTLE!      TURN no {turn_counter}".center(120))
        print(f"===================================".center(120))

        player_health_bar = "=" * int(player.health * 60 / player.maxhealth)

        if player.health < player.maxhealth * 0.3:
            player_health_bar_color = "\033[0;31m"

        elif player.maxhealth * 0.3 <= player.health < player.maxhealth * 0.7:
            player_health_bar_color = "\033[0;33m"

        elif player.health >= player.maxhealth * 0.7:
            player_health_bar_color = "\033[0;32m"

        print(f"\nHero - {player.name}")
        print("-" * (10 + len(player.name)))
        print(f'{"Level":19} : {player.level}')
        print(f'{"Experience":19} : {player.experience:<4} /  {levels[0]:<4}')
        print(
            f'{"Health":19} : {player.health:<4} /  {player.maxhealth:<4} {player_health_bar_color} [{player_health_bar}',
            " " * (60 - len(player_health_bar)),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Attack":19} : {player.attack}')
        print(f'{"Defense":19} : {player.defense}')
        print(f'{"Mana":19} : {player.magic}')
        print(f'{"Luck":19} : {player.luck}')
        print(f'{"Money":19} : {player.money}')
        if len(player.state) == 0:
            print(f'{"Your state":19} : ok, no additional negative conditions.')
        else:
            print(
                f'{"Your state":19} : {player.state[0].capitalize()}  -   you take extra damage every turn.'
            )
        print(f"\nEnemy - {enemy.name}")
        print("-" * (13 + len(enemy.name)))

        enemy_health_bar = "=" * int(enemy.health * 60 / enemy_max_health)

        if enemy.health < enemy_max_health * 0.3:
            enemy_health_bar_color = "\033[0;31m"

        elif enemy_max_health * 0.3 <= enemy.health < enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;33m"

        elif enemy.health >= enemy_max_health * 0.7:
            enemy_health_bar_color = "\033[0;32m"

        print(f'{"Level":19} : {enemy.level}')
        print(
            f'{"Health":19} : {enemy.health:<4} /  {enemy_max_health:<4} {enemy_health_bar_color} [{enemy_health_bar}',
            " " * (60 - len(enemy_health_bar)),
            "]",
            "\033[0m",
            sep="",
        )
        print(f'{"Attack":19} : {enemy.attack}')
        print(f'{"Defense":19} : {enemy.defense}')
        print(f'{"Magic Defense:":19} : {enemy.magicdefense}')
        print(f'{"Luck:":19} : {enemy.chance}')
        print(f'{"Special":19} : {enemy.special.capitalize()}')

        player_turn()

        if escape_from_battle:
            return

        enemy_turn()

    return


def player_turn():

    global escape_from_battle
    escape_from_battle = False

    print(f"\n{player.name}'s Turn")
    print(f" ------------------------------")
    print(f"| Available actions:\t       |")
    print(f"|\t 1 - physical attack   |")
    print(f"|\t 2 - magic attack      |")
    print(f"|\t 3 - use item          |")
    print(f"|\t 4 - defense           |")
    print(f"|\t 5 - run               |")
    print(f" ------------------------------")
    print(f"\nWhat do you do?")

    battle_action = input("> ")

    if battle_action == "1":
        hero_attack()

    elif battle_action == "2":
        hero_magic_attack()

    elif battle_action == "3":
        use_item()

    elif battle_action == "4":
        defense()

    elif battle_action == "5":
        run_chance = player.luck + roll_20_dice()
        stop_chance = enemy.chance + roll_20_dice()

        if run_chance > stop_chance:
            print(
                "\nYou managed to escape from battle, your enemy can't reach you."
            )
            delay_medium()
            if player.experience > levels[0]:
                clear_screen()
                player.level_up()
                del levels[0]
            # global escape_from_battle
            escape_from_battle = True
            return

        else:
            print(
                "\nYou failed to escape, the battle continues."
            )
            delay_medium()
            escape_from_battle = False
    else:
        print("Choose option 1 - 5!")

    return


def enemy_turn():
    if enemy.health > 0:
        enemy_attack()
        return
    else:
        # To avoid enemy turn after his death
        return


def teleport(destination):
    eval(f"{destination.lower()}()")


def victory():
    clear_screen()

    print("\n\nVictory!")

    print("\nYou stand over enemy's corpse, and wonder what to do next... ")
    print("\nYou decide to:")
    print("\n\t1 - Search the corpse, not knowing what to expect.")
    print("\t2 - Leave it alone, and continue you journey.")

    choice = input("\n> ")

    if choice == "1":
        body_search()

    elif choice == "2":
        return

    else:
        print("\nChoose option 1-2 !")
        delay_medium()
        victory()


def defeat():
    clear_screen()
    delay_short()
    print(f"\n\n{player.name}, you lost the battle and you die...")
    delay_short()
    print("Your corpse is left to be eaten by the vultures.\n\n\n\n")
    delay_short()
    quit()


def body_search():

    risk = roll_20_dice()

    # when risk dice roll fails, player looses some HP
    if risk < 3:
        print("You set off a trap!")
        delay_short()
        print("You are badly wounded.")
        delay_short()
        print(f"\nYour health is lowered permanently by {20 - risk} HP.")
        player.health = player.health - (20 - risk)
        if player.health < 1:
            defeat()
        delay_medium()
        return
    else:
        # player gets loot from enemy body
        money = roll_20_dice()
        player.money = player.money + money
        print(f"\nYou found {money} gold coins.")
        print("\nWonder if you can find any more items...")
        delay_short()

        for item_type, item in all_items.items():

            for k, v in item.items():

                loot_chance = (roll_20_dice() - int(v["Price"] / 5)) - (
                    roll_20_dice() * 2
                )

                if loot_chance > 0:

                    print(f"Great! You found something!")
                    delay_short()
                    if k in player.inventory[item_type]:
                        print(
                            f"\nUnfortunately, you have {k} in you inventory. You can't have another.\n"
                        )
                        print("The loot stays in its place.\n")
                        delay_medium()

                    else:
                        player.inventory[item_type][k] = v
                        print(f"{k.capitalize()} was added to you inventory.\n")
                        delay_medium()
                else:
                    pass

        delay_medium()
        return


def shop():
    def buy_item(item_type):
        clear_screen()

        items_list = []

        print(f"\nYour have {player.money} gold coins")
        print(
            f"\nYou chosed {item_type}, here are the items for sale in this category:\n"
        )

        for number, (item, stats) in enumerate(all_items[item_type].items(), start=1):
            print(f"\n{number}. Item: {item}")
            print("-" * (len(f"Item: {item}") + 3))
            items_list.append(item)

            for i, j in stats.items():
                print(f"\t\t\t{i:11}: {j}")

        try:
            choice = int(input("\nWhich item do you want to buy?   > ")) - 1

            if choice == "":
                return

            elif choice < 0 or choice > len(items_list) - 1:
                print("\nWrong option, choose again.")
                delay_medium()

            else:
                item_to_buy = items_list[choice]
                cost_of_item_to_buy = all_items[item_type][item_to_buy]["Price"]

                if item_to_buy in player.inventory[item_type]:
                    print("You own this item, you can't buy another.")
                    delay_medium()

                else:
                    if cost_of_item_to_buy > player.money:

                        print(
                            f"\nYou don't have enough money, you need additional {cost_of_item_to_buy - player.money} gold coins!"
                        )
                        delay_medium()

                    else:

                        for item_type, item in all_items.items():
                            for k, v in item.items():
                                if k == item_to_buy:
                                    new_item_dict = {k: v}

                                    bought_message = f"\nYou bought {item_to_buy}. You have {player.money - cost_of_item_to_buy} gols coins left."

                                    print("-" * len(bought_message))
                                    print(bought_message)
                                    print("_" * len(bought_message))
                                    player.inventory[item_type].update(new_item_dict)
                                    player.money = player.money - cost_of_item_to_buy
                                    delay_medium()

                                else:
                                    pass
        except ValueError:
            print("\nWrong option, choose again.")
            delay_medium()

        shop()

    def sell_item():
        clear_screen()

        inventory_list = []

        print("You own the following items:")

        for item_type, item in player.inventory.items():
            for name, parameters in item.items():
                inventory_list.append(name)

        for i, item in enumerate(inventory_list, start=1):
            print(i, item)

        print(f"\nYou have {player.money} gold coins.\n\n")

        choice = int(input("\nWhich item do you wan't to sell?   > ")) - 1

        if choice == "":
            return

        elif choice < 0 or choice > len(inventory_list) - 1:
            print("\nWrong option, choose again.")
            delay_medium()

        else:
            item_to_sell = inventory_list[choice]

            if item_to_sell in player.inventory["weapons"]:
                player.money = player.money + int(
                    player.inventory["weapons"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["weapons"][item_to_sell]

            elif item_to_sell in player.inventory["consumables"]:
                player.money = player.money + int(
                    player.inventory["consumables"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["consumables"][item_to_sell]

            elif item_to_sell in player.inventory["other"]:
                player.money = player.money + int(
                    player.inventory["other"][item_to_sell]["Price"] * 0.7
                )
                del player.inventory["other"][item_to_sell]

            else:
                pass

            print(f"\nYou sold {item_to_sell}.")
            inventory_list.remove(item_to_sell)
            delay_medium()

    def buy():
        clear_screen()
        print("\n\n\nItems for sale:")

        for i, item_type in enumerate(all_items, start=1):
            print(f"\n{i}. {item_type.capitalize()} :")
            print(f"{'-' * (len(item_type)+6)} ")

            for k in all_items[item_type].keys():
                print("\t", k.capitalize())

        print("\n\n")

        print("\nChoose category of items to buy (1/2/3)")
        print("\n0 - Powrót\n")

        choice = input("\n> ")

        if choice == "1":

            buy_item("weapons")

        elif choice == "2":

            buy_item("consumables")

        elif choice == "3":

            buy_item("other")

        elif choice == "0" or choice == "":
            pass

        else:
            print("\n\n\t\t\t\tWrong option, choose again.")
            delay_medium()
            return

    clear_screen()

    print("\n\n\t\t\t\t\t\t", "-" * 20)
    print("\t\t\t\t\t\t|  Witaj w sklepie!  |")
    print("\t\t\t\t\t\t", "-" * 20, "\n")
    print("Items in you inventory:")

    for item_type, item in player.inventory.items():

        for name, parameters in item.items():
            print(name)

    print(f"\nYou have {player.money} gold coins.")
    print("\nWhat do you want to do?")
    print("\n1 - Buy item")
    print("2 - Sell item")
    print("\n0 - Go back")

    choice = input("> ")

    if choice == "1":
        buy()
    elif choice == "2":
        sell_item()
    elif choice == "0":
        return
    else:
        print("\nWrong option, choose again.")
        delay_medium()
        shop()


def temple():
    clear_screen()

    heal_cost = 20

    print(f'\n\n{"Welcome to the Temple.":^120}')
    print(f'{"-"*24:^120}\n\n')
    print("\tHere you can heal you wounds and buy spells.")
    print("\tWhat would you like to do?\n")
    print(f"\n\t1 - Heal (costs {heal_cost} coins)")
    print("\t2 - Learn spells")
    print("\n\t0 - Leave Temple.")

    choice = input("\n\t> ")

    if choice == "0":
        return

    elif choice == "1":
        player.health = player.maxhealth
        player.state = []
        if player.money < 20:
            print(f"You don't have enough money!")
            delay_medium()
            pass
        else:
            player.money -= 20
            player.health = player.maxhealth
            player.state = []
            print("\t\t\nYou ragained all your health and healed your wounds.")
            delay_medium()
        temple()

    elif choice == "2":
        clear_screen()

        print(f"\n\nHere you can learn spells for 50 gold coin each.\n")

        spells_list = list(spell for spell in all_offensive_spells.keys())
        for i, spell in enumerate(spells_list):
            print(f"{i + 1}. {spell}")

        print(f"\nChoose spell number for more information, or 0 - Back")
        choosed_spell = spells_list[int(input("\n> ")) - 1]

        if choosed_spell in all_offensive_spells.keys():
            print(f"\n\t{choosed_spell}:")
            for parameter, value in all_offensive_spells[choosed_spell].items():
                print(f"\t\t{parameter:10}-  {value}".title())
            print("\nDo you want to leave this spell?")
            print("1 - Learn")
            print("2 - Back")
            if_learn_spell = input("\n> ")
            if if_learn_spell == "1":
                if player.money < 50:
                    print("\nYou don't have enough money to learn this spell.")
                    input()
                    return
                else:
                    player.money -= 50
                    player.spellbook[choosed_spell] = all_offensive_spells[
                        choosed_spell
                    ]
            elif if_learn_spell == "2":
                return
            else:
                print("\nWrong option!")

        else:
            print("Wrong number!")
        delay_medium()
        temple()


def inn():
    pass


def treasure():
    # (opened, trap, puzzle, gold, item, exp, searched)
    treasure_chest = Chest(False, False, 25, "Mana Potion", 15, False)

    def open_chest():
        if treasure_chest.opened == True:
            pass
        else:
            print(f"Unfortunately, the chest is closed.")
            print(f"Would you like to open it using lockpick?")
            choice = input("\nY/N   >").lower()

            if choice == "n":
                print("\nThe chest stays closed.")
                return

            elif choice == "y":
                if "Lockpick" in player.inventory["other"]:
                    del player.inventory["other"]["Lockpick"]
                    treasure_chest.opened = True
                    player.money += treasure_chest.gold
                    player.inventory["consumables"][treasure_chest.item] = all_items[
                        "consumables"
                    ][treasure_chest.item]
                    player.experience += treasure_chest.exp
                    treasure_chest.searched = True
                    print(f"\nIs chest opened? - {treasure_chest.opened}\n")
                    print(f"Whas there a trap? - {treasure_chest.trap}")
                    print(f"Whas there a puzzle? - {treasure_chest.puzzle}")
                    print(f"Gold found - {treasure_chest.gold}")
                    print(f"Items found - {treasure_chest.item}")
                    print(f"Experience gained - {treasure_chest.exp}")
                    print(f"Is chest searched? - {treasure_chest.searched}")
                    input()
                else:
                    print(
                        "\nYou don't have a lockpick to open the chest, so it stays closed.\n"
                    )
                    delay_medium()
            else:
                print("\nWrong choice!")
                input()
                open_chest()

    open_chest()


def poison_spikes_trap():
    clear_screen()
    print("You were not perceptive enough and you set up a trap!")
    print("Poisoned needle strikes from barely visible hole in the wall.")
    print("The needle hits you in no time, you immediately feel nauseous and dizzy")
    health_lost = player.maxhealth * 0.2
    if health_lost >= player.health:
        print(f"You lost {health_lost} HP and you DIED...")
        print("\n\n\t\t\t\t========= GAME OVER =========")
        quit()
    else:
        print(f"You lost {health_lost} HP")
        print("You should use healing spell or item to recover, otherwise you can die.")
        time.sleep(1)
        for key, value in player.inventory["consumables"].items():
            if not "Cure Poison" in key and not "Cure Poison" in value:
                print("\nYou don't have any items that could heal you.")
                print(key, value)
                input()
            else:
                print("You have some items that can heal you.")
                input()
