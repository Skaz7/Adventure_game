import unittest

class Hero(unittest.TestCase):
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
        self.health = int(self.health * 1.1)
        self.attack = int(self.attack * 1.1)
        self.defense = int(self.defense * 1.1)
        self.magic = int(self.magic * 1.1)
        self.state = []
