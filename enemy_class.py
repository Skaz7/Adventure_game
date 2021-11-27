import random
import math

class Enemy:
    def __init__(self, Ename, Ehealth, Eattack, Especial, Echance):
        self.name = Ename
        self.health = Ehealth
        self.attack = Eattack
        self.special = Especial
        self.chance = Echance


    # getters for enemy class
    def getName(self):
        return self.name
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def getSpecial(self):
        return self.special

    def getChance(self):
        return self.chance
    
    # setters for enemy class
    def setName(self, newName):
        self.name = newName

    def setHealth(self, newHealth):
        self.health = newHealth

    def setAttack(self, newAttack):
        self.attack = newAttack
    
    def setSpecial(self, newSpecial):
        self.special = newSpecial
    
    def setChance(self, newChance):
        self.chance = newChance
    
    