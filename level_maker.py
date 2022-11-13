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
        mm = MonsterMaker()
        if level == 1:
            spider1 = mm.getSpider(3, 4)
            spider2 = mm.getSpider(4, 2)
            return [spider1, spider2]

        if level == 2:
            sk1 = mm.getSkeleton(0, 3)
            sk2 = mm.getSkeleton(2, 4)
            return [sk1, sk2]

        if level == 3:
            tr1 = mm.getTroll(3, 4)
            return [tr1]
        if level == 4:
            dr1 = mm.getDragon()
            return [dr1]
        if level == 5:
            spider1 = mm.getSpider(5, 0)
            spider2 = mm.getSpider(5, 4)
            spider3 = mm.getSpider(1, 4)
            return [spider1, spider2, spider3]

        if level == 6:
            sk1 = mm.getSkeleton(0, 0)
            sk2 = mm.getSkeleton(1, 3)
            sk3 = mm.getSkeleton(1, 4)
            return [sk1, sk2, sk3]

        if level == 7:
            tr1 = mm.getTroll(4, 1)
            tr2 = mm.getTroll(2, 3)
            return [tr1, tr2]

        if level == 8:
            dr1 = mm.getDragon(0, 1)
            dr2 = mm.getDragon(3, 4)
            return [dr1, dr2]

        if level == 9:
            spider1 = mm.getSpider(0, 4)
            spider2 = mm.getSpider(2, 0)
            spider3 = mm.getSpider(2, 2)
            spider4 = mm.getSpider(4, 1)
            return [spider1, spider2, spider3, spider4]

        if level == 10:
            sk1 = mm.getSkeleton(0, 1)
            sk2 = mm.getSkeleton(1, 2)
            sk3 = mm.getSkeleton(2, 3)
            sk4 = mm.getSkeleton(4, 4)
            return [sk1, sk2, sk3, sk4]

        if level == 11:
            tr1 = mm.getTroll(1, 4)
            tr2 = mm.getTroll(3, 4)
            tr3 = mm.getTroll(4, 2)
            return [tr1, tr2, tr3]

        if level == 12:
            dr1 = mm.getDragon(0, 1)
            dr2 = mm.getDragon(0, 3)
            dr3 = mm.getDragon(2, 3)
            return [dr1, dr2, dr3]

        return []

    def getHeroStart(self, level):
        return Point(4*((level+1) % 2), 0)