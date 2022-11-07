from monsterMaker import MonsterMaker
from point import Point


class Level_maker:

    @staticmethod
    def getPillars(level):
        if level % 4 == 1:
            return [Point(1, 1), Point(3, 1), Point(3, 3)]
        if level % 4 == 2:
            return [Point(1, 1), Point(1, 3), Point(3, 3)]
        if level % 4 == 3:
            return [Point(0, 2), Point(3, 1), Point(3, 2)]
        if level % 4 == 4:
            return [Point(1, 2), Point(1, 3), Point(5, 2)]

    @staticmethod
    def getMonsters(level):

        if level == 1:
            spider1 = MonsterMaker.getSpider(3, 4)
            spider2 = MonsterMaker.getSpider(4, 2)
            return [spider1, spider2]

        if level == 2:
            sk1 = MonsterMaker.getSkeleton(0, 3)
            sk2 = MonsterMaker.getSkeleton(2, 4)
            return [sk1, sk2]

        if level == 3:
            tr1 = MonsterMaker.getTroll(3, 4)
            return [tr1]
        if level == 4:
            dr1 = MonsterMaker.getDragon()
            return [dr1]
        if level == 5:
            spider1 = MonsterMaker.getSpider(5, 0)
            spider2 = MonsterMaker.getSpider(5, 4)
            spider3 = MonsterMaker.getSpider(1, 4)
            return [spider1, spider2, spider3]

        if level == 6:
            sk1 = MonsterMaker.getSkeleton(0, 0)
            sk2 = MonsterMaker.getSkeleton(1, 3)
            sk3 = MonsterMaker.getSkeleton(1, 4)
            return [sk1, sk2, sk3]

        if level == 7:
            tr1 = MonsterMaker.getTroll(4, 1)
            tr2 = MonsterMaker.getTroll(2, 3)
            return [tr1, tr2]

        if level == 8:
            dr1 = MonsterMaker.getDragon(0, 1)
            dr2 = MonsterMaker.getDragon(3, 4)
            return [dr1, dr2]

        if level == 9:
            spider1 = MonsterMaker.getSpider(0, 4)
            spider2 = MonsterMaker.getSpider(2, 0)
            spider3 = MonsterMaker.getSpider(2, 2)
            spider4 = MonsterMaker.getSpider(4, 1)
            return [spider1, spider2, spider3, spider4]

        if level == 10:
            sk1 = MonsterMaker.getSkeleton(0, 1)
            sk2 = MonsterMaker.getSkeleton(1, 2)
            sk3 = MonsterMaker.getSkeleton(2, 3)
            sk4 = MonsterMaker.getSkeleton(4, 4)
            return [sk1, sk2, sk3, sk4]

        if level == 11:
            tr1 = MonsterMaker.getTroll(1, 4)
            tr2 = MonsterMaker.getTroll(3, 4)
            tr3 = MonsterMaker.getTroll(4, 2)
            return [tr1, tr2, tr3]

        if level == 12:
            dr1 = MonsterMaker.getDragon(0, 1)
            dr2 = MonsterMaker.getDragon(0, 3)
            dr3 = MonsterMaker.getDragon(2, 3)
            return [dr1, dr2, dr3]

        return []

    def getHeroStart(self, level):
        return Point(level/2, 4)