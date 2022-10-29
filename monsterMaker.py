from character import Character
from point import Point


class MonsterMaker():

    def getSpider(x, y):
        return Character("Spider", 2, 5, 4, 4, 3, Point(x, y))

    def getTroll(x, y):
        return Character("Troll", 3, 3, 7, 7, 2, Point(x, y))

    def getSkeleton(x, y):
        return Character("Skeleton", 1, 3, 3, 3, 4, Point(x, y))

    def getDragon(x, y):
        return Character("Dragon", 4, 5, 5, 5, 5, Point(x, y))
