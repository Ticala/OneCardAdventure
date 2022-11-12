import math

from point import Point

class Character:
    def __init__(self, name, life, attack, defence, move, range, point):
        self.name = name
        self.life = life
        self.strength = attack
        self.defence = defence
        self.move = move
        self.range = range
        self.point = point

    def print(self):
        return \
          "-------------------------------\n" + \
          self.name + " has \nlife: " + str(self.life) + \
          "\n-------------------------------\n" + \
          "|str: " + str(self.strength) + \
          "|def: " + str(self.defence) + \
          "|mov: " + str(self.move) + \
          "|ran: " + str(self.range) + \
          "|" + \
          "\n-------------------------------"

    def __str__(self):
          return  "(lif: " + str(self.life) + \
            ",str: " + str(self.strength) + \
            ",def: " + str(self.defence) + \
            ",mov: " + str(self.move) + \
                 ",ran: " + str(self.range) + \
                 ")" + self.name


    def getX(self):
        return self.point.x

    def getY(self):
        return self.point.y
