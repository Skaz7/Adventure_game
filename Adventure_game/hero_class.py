from functions import levels

class Hero:
    def __init__(self, Hname, Hhealth, Hattack, Hdefense, Hmagic, Hluck, Hmoney, Hinventory, Hstate, Hexperience, Hlevel):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.magic = Hmagic
        self.luck = Hluck
        self.money = Hmoney
        self.inventory = Hinventory
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


    # when hero experience points exceends level given in level list the stats increases
    def level_up(self):
        self.level = self.level + 1
        self.health = int(self.health * 1.1)
        additional_points = 2

        while additional_points > 0:
            print(f'''{self.name}, awansowałeś na nowy poziom. Poziom Twojego zdrowia zwiększył się automatycznie.
Dodatkowo otrzymujesz 2 punkty, dzięki którym możesz zwiększych swoje statystyki.

Którą parametr chcesz rozwinąć?

1. Atak      : {self.attack}
2. Obrona    : {self.defense}
3. Magia     : {self.magic}
4. Szczęście : {self.luck}
        ''')
            choice = input(f'\nGdzie przyznasz punkt?  > ')
            if choice == '1':
                self.attack += 1
            elif choice == '2':
                self.defense += 1
            elif choice == '3':
                self.magic += 1
            elif choice == '4':
                self.luck += 1
            self.state = []
            additional_points -= 1


    def show_player_stats(self):
        print(f'\n\n{"Ekran gracza":^120}')
        print(f'{"-"*14:^120}\n')
        print(f'\t{"="*50}\n')
        print(f'\tIMIĘ: {self.name}   |   POZIOM -> {self.level}\n')
        print(f'\tDoświadczenie: {self.experience} / {levels[0]}\n')
        print(f'\t{"="*50}\n\n')
        print(f'\tSzczegółowe statystyki:\n')
        print(f'\t\t{"1. ZDROWIE":12} : {self.health}')
        print(f'\t\t{"2. ATAK":12} : {self.attack}')
        print(f'\t\t{"3. OBRONA":12} : {self.defense}')
        print(f'\t\t{"4. MAGIA":12} : {self.magic}')
        print(f'\t\t{"5. SZCZĘŚCIE":12} : {self.luck}')
        print(f'\t\t{"6. PIENIĄDZE":12} : {self.money}szt złota')

        if len(self.state) == 0 :
            print(f'\t\t{"7. STAN":12} : Wszystko w porządku, brak dodatkowych efektów\n')

        else:
            print(f'\t\t{"7. STAN":12} : {self.state[0]}\n')
        
        items_list = []
        for k, v in self.inventory.items():
            for i, j in v.items():
                items_list.append(i)

        print(f'\t\t{"8. PRZEDMIOTY":12} : {"  |  ".join(items_list)}')

        input('\n\n\nENTER - Powrót')
        return
