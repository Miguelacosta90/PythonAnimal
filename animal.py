import random
class animal(object):
    def __init__(self, name, species = None):
        print"Animal"
        self.name = name
        self.health = 100
        self.species = species
        self.walk = 10
        self.run =20
    def displayHealth(self):
        print self.health, self.name
        return self
    def running(self):
        self.health -= 5
        return self
    def walking(self):
        self.health -= 1
        return self

class dog(animal):
    def life(self):
        self.health += 50
        return self
    def pet(self):
        self.health += 5
        return self

class Dragon(animal):
    def dragonLife(self):
        self.health += 70
        return self
    def fly(self):
        self.health -= 10
        return self
    def myName(self):
        print "this is a Dragon"
        return self

D = Dragon("Dragon", "old ass animal").dragonLife().walking().walking().walking().running().running().fly().fly().myName().displayHealth()
lion = dog("petter", "cat").life().walking().walking().walking().running().running().pet().displayHealth()
tiger = animal("charls","cat").walking().walking().walking().running().displayHealth()
