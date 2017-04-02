import random
class animal(object):
    def __init__(self, species = None):
        print"Animal"
        self.health = 100
        self.species = species
        self.walk = 10
        self.run =20
    def running(self):
        self.run -= 5
