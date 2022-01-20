class Hero:
    def __init__(self, Hname, Hhealth, Hattack, Hdefense, Hmagic, Hluck, Hmoney, Hitems, Hstate, Hexperience, Hlevel):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.magic = Hmagic
        self.luck = Hluck
        self.money = Hmoney
        self.items = Hitems
        self.state = Hstate
        self.experience = Hexperience
        self.level = Hlevel
    
    # getters - for returning actual hero stats
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getMagic(self):
        return self.magic
    def getLuck(self):
        return self.luck
    def getMoney(self):
        return self.money
    def getItems(self):
        return self.items
    def getState(self):
        return self.state
    def getExperience(self):
        return self.experience
    def getLevel(self):
        return self.level
    
    # setters - used to change the variable (for example health)
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setDefense(self, newDefense):
        self.defense = newDefense
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setLuck(self,newLuck):
        self.luck = newLuck
    def setMoney(self,newMoney):
        self.money = newMoney
    def setItems(self, newItems):
        self.items = newItems
    def setState(self,newState):
        self.state = newState
    def setExperience(self, newExperience):
        self.experience = newExperience
    def setLevel(self,newLevel):
        self.level = newLevel

    def bleed(self):
        self.health = self.health - 5

    # when hero experience points exceends level given in level list the stats increases
    def level_up(self):
        self.level = self.level + 1
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