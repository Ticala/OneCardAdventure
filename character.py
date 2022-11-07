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
          return self.name + "(lif: " + str(self.life) + \
            ",str: " + str(self.strength) + \
            ",def: " + str(self.defence) + \
            ",mov: " + str(self.move) + \
                 ",ran: " + str(self.range) + \
                 ")"

    def canAttack(self, pillars, enemies):
        enemiesInRange = []
        things = pillars + []
        for enemy in enemies:
            things.append(enemy.point)

        # is enemy in range
        for enemy in enemies:
            distance = self.point.distance(enemy.point)
            if distance > 0 and distance <= self.range:
                #
                #  [ ][ ][ ]   [ ][ ][M]
                #  [H][ ][M]   [ ][ ][ ]
                #  [ ][ ][ ]   [H][ ][ ]
                #
                if distance == 2 or distance == 3:
                    enemiesInRange.append(enemy)
                if distance == 4 or distance == 6:
                    mpoint = self.point.avg(enemy.point)
                    if not mpoint.isHit(things):
                        enemiesInRange.append(enemy)
                #
                #  [ ][ ][M]
                #  [X][ ][ ]
                #
                if distance == 5:
                    pointfloot = self.point.avgFloor(enemy.point)
                    pointCeil = self.point.avgCeil(enemy.point)
                    if not pointfloot.isHit(things) or not pointCeil.isHit(things):
                        enemiesInRange.append(enemy)

        return enemiesInRange

    def getX(self):
        return self.point.x

    def getY(self):
        return self.point.y
