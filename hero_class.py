class Hero:
    def __init__(self, Hname, Hhealth, Hattack, Hdefense, Hranged, Hmagic, Hluck):
        self.name = Hname
        self.health = Hhealth
        self.attack = Hattack
        self.defense = Hdefense
        self.ranged = Hranged
        self.magic = Hmagic
        self.luck = Hluck
    
    # getters - for returning actual hero stats
    def getName(self):
        return self.name
    def getHealth(self):
        return self.health
    def getAttack(self):
        return self.attack
    def getDefense(self):
        return self.defense
    def getRanged(self):
        return self.ranged
    def getMagic(self):
        return self.magic
    def getLuck(self):
        return self.luck
    
    # setters - used to change the variable (for example health)
    def setHealth(self, newHealth):
        self.health = newHealth
    def setAttack(self, newAttack):
        self.attack = newAttack
    def setDefense(self, newDefense):
        self.defense = newDefense
    def setRanged(self, newRanged):
        self.ranged = newRanged
    def setMagic(self, newMagic):
        self.magic = newMagic
    def setLuck(self,newLuck):
        self.luck = newLuck
    