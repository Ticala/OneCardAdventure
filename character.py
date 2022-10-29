import math

from point import Point
class Character:
    def __init__(self, name, life, attack, reach, defends, speed, point ):
        self.name = name
        self.life = life
        self.attack = attack
        self.reach = reach
        self.defends = defends
        self.speed = speed
        self.point = point

    def __str__(self):
        return self.name + " has \nlife: " + str(self.life) + \
         "\nattack " + str(self.attack)

    def canAttack(self, pillars, enemies):

        things = []
        for pillar in pillars:
            things.append(pillar)
        for enemy in enemies:
            things.append(enemy.point)

        # is enemy in range
        for enemy in enemies:
            distance = enemy.point.distance(enemy.point)
            if distance <= self.range:
                #
                #  [ ][ ][ ]   [ ][ ][H]
                #  [X][ ][M]   [ ][ ][ ]
                #  [ ][ ][ ]   [X][ ][ ]
                #
                if distance == 4 or distance == 6:
                    mpoint = Point( (enemy.point.x + self.point.x)/2, ( enemy.point.x + self.point.x)/2 )
                    if mpoint.isHit(things):
                        return False
                #
                #  [ ][ ][M]
                #  [X][ ][ ]
                #
                if distance == 5:
                    pointfloot = self.point.avgFloor(enemy.point)
                    pointCeil = self.point.avgCeil(enemy.point)

                    if !pointfloot.isHit(things) or !pointCeil.isHit(things):
                        return false


        return  True