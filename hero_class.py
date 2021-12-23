class Hero:
    def __init__(self, Hname, Hhealth, Hattack, Hdefense, Hmagic, Hluck, Hmoney):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.magic = Hmagic
        self.luck = Hluck
        self.money = Hmoney
    
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