from character import Character
from point import Point


class MonsterMaker():

    def getSpider(self, x, y):
        life = 2
        attack = 5
        defence = 4
        move = 5
        range = 3
        return Character("Spider", life, attack, defence, move, range, Point(x, y))
  
    def getTroll(self, x, y):
        life = 5
        attack = 3
        defence = 7
        move = 3
        range = 2
        return Character("Troll", life, attack, defence, move, range, Point(x, y))

    def getSkeleton(self, x, y):
        life = 3
        attack = 5
        defence = 4
        range = 4
        move = 4
        return Character("Skeleton", life, attack, defence, move, range, Point(x, y))

    def getDragon(self, x, y):
        life = 5
        attack = 5
        defence = 5
        move = 5
        range = 5
        return Character("Dragon", life, attack, defence, move, range, Point(x, y))
