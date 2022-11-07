from character import Character
from point import Point


class MonsterMaker():

    def getSpider(self, x, y):
        return Character("Spider", 2, 5, 4, 5, 3, Point(x, y))

    def getTroll(self, x, y):
        return Character("Troll", 5, 3, 7, 3, 2, Point(x, y))

    def getSkeleton(self, x, y):
        return Character("Skeleton", 3, 5, 4, 4, 4, Point(x, y))

    def getDragon(self, x, y):
        return Character("Dragon", 5, 5, 5, 5, 5, Point(x, y))
