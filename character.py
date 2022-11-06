import math

from point import Point

class Character:
    def __init__(self, name, life, attack, move, defends, range, point ):
        self.name = name
        self.life = life
        self.attack = attack
        self.move = move
        self.defends = defends
        self.range = range
        self.point = point

    def __str__(self):
        return self.name + " has \nlife: " + str(self.life) + \
         "\nattack " + str(self.attack) + \
         " range   " + str(self.range) + \
         " defends " + str(self.defends) + \
         " move    " + str(self.move) + \
         " place   " + str(self.point)

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
