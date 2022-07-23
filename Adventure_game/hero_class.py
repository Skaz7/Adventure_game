import functions

hero_max_health = 200


class Hero:
    def __init__(
        self,
        Hname,
        Hhealth,
        Hmaxhealth,
        Hattack,
        Hdefense,
        Hmagic,
        Hluck,
        Hmoney,
        Hinventory,
        Hspellbook,
        Hstate,
        Hexperience,
        Hlevel,
    ):
        self.name = Hname
        self.health = Hhealth
        self.maxhealth = Hmaxhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.magic = Hmagic
        self.luck = Hluck
        self.money = Hmoney
        self.inventory = Hinventory
        self.spellbook = Hspellbook
        self.state = Hstate
        self.experience = Hexperience
        self.level = Hlevel

    def bleed(self):
        self.health = self.health - 5

    def freeze(self):
        self.health = self.health - 2

    def burn(self):
        self.health = self.health - 10

    def poison(self):
        self.health = self.health - 7

    def stunned(self):
        pass

    # when hero experience points exceends level given in level list the stats increases
    def level_up(self):
        self.level = self.level + 1
        self.maxhealth = int(self.maxhealth * 1.1)
        self.health = self.maxhealth
        additional_points = 2

        while additional_points > 0:
            print(
                f"""{self.name}, you have advanced to a new level. Your health increased automatically.
Additionally, you get 2 points, thanks to which you can increase your statistics.

Which parameter should be strengthened??

1. Attack  : {self.attack}
2. Defence : {self.defense}
3. Magic   : {self.magic}
4. Luck    : {self.luck}
        """
            )
            functions.playsound(
                "D:\\Users\\sebas\\OneDrive\\Repositories\\Adventure_game\\Sound\\mixkit-game-level-completed-2059.wav"
            )
            choice = input(f"\nWhich parameter should be strengthened??  > ")
            if choice == "1":
                self.attack += 1
            elif choice == "2":
                self.defense += 1
            elif choice == "3":
                self.magic += 1
            elif choice == "4":
                self.luck += 1
            self.state = []
            additional_points -= 1

    def show_player_screen(self):
        print(f'\n\n{"Player screen":^120}')
        print(f'{"-"*14:^120}\n')
        print(f'\t{"="*50}\n')
        print(f"\tNAME: {self.name}   |   LEVEL -> {self.level}\n")
        print(f"\tExperience: {self.experience} / {functions.levels[0]}\n")
        print(f'\t{"="*50}\n\n')
        print(f"\tDetailed statistics:\n")
        print(f'\t\t{"1. HEALTH":12} : {self.health}')
        print(f'\t\t{"2. ATTACK":12} : {self.attack}')
        print(f'\t\t{"3. DEFENCE":12} : {self.defense}')
        print(f'\t\t{"4. MANA":12} : {self.magic}')
        print(f'\t\t{"5. LUCK":12} : {self.luck}')
        print(f'\t\t{"6. MONEY":12} : {self.money} gold coins')

        if len(self.state) == 0:
            print(
                f'\t\t{"7. STATE":12} : OK, no side effects\n'
            )

        else:
            print(f'\t\t{"7. STATE":12} : {self.state[0].capitalize()}')

        items_list = []
        for k, v in self.inventory.items():
            for i, j in v.items():
                items_list.append(i)

        print(f'\t\t{"8. ITEMS":12} : {"  |  ".join(items_list)}')
        print(f'\n\t\t{"9. USE ITEM"}')
        print(f'\n\t\t{"0. SAVE GAME"}')
        print("\n\n\nENTER - Back")

        choice = input("\n\n> ")

        if choice == "9":
            functions.use_item()
        elif choice == "0":
            functions.save_game()

        else:
            return
