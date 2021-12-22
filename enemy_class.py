class Enemy:
    def __init__(self, Ename, Ehealth, Eattack, Edefense, Emagicdefense, Echance):
        self.name = Ename
        self.health = Ehealth
        self.attack = Eattack
        self.defense = Edefense
        self.magicdefense = Emagicdefense
        self.chance = Echance


    # getters for enemy class
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def getDefense(self):
        return self.defense
    
    def getMagicdefense(self):
        return self.magicdefense
    
    def getChance(self):
        return self.chance

    
    # setters for enemy class
    def setName(self, newName):
        self.name = newName

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack
    
    def setDefense(self, newDefense):
        self.defense = newDefense
    
    def setMagicdefense(self, newMagicdefense):
        self.magicdefense = newMagicdefense

    def setChance(self, newChance):
        self.chance = newChance