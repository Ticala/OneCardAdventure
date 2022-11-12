from point import Point


class Dungeon:

    def __init__(self):
        self.dungeon =[
            [-1, -1, -1 , -1, -1],
            [-1, -1, -1 , -1, -1],
            [-1, -1, -1 , -1, -1],
            [-1, -1, -1 , -1, -1],
            [-1, -1, -1 , -1, -1]]

    def __str__(self):
        return self.dungeon

    def printDungeon(self):
        print("--------------------")
        for y in range(5):
            lin = ""
            for x in range(5):
                value = self.dungeon[x][y]
                if value < 10 and value >-1:
                    lin += " "
                lin +=  " " + str(value) + " "
            print (lin)
            print("--------------------")

    def next_step(self, monster, monsters, pillars, hero):

        monster_point = monster.point
        if hero.point.distance(monster_point)>2:
            return monster_point

        for i in range(20):
            map[i] = []

        map[0] = { monster_point }
        map = { 0, [monster_point] }

        for i in range(20):
            print(i)
            points = map[0]
            for point in points:
                for xx in range(max(0, point.x - 1), min(4, point.x + 1)):
                    for yy in range(max(0, point.y - 1), min(4, point.y + 1)):
                        if self.dungeon[xx][yy] == -1:
                            p = Point(xx, yy)
                            distance_to_point = i + point.distance(p)
                            self.dungeon[xy][yy] = distance_to_point
                            map[distance_to_point].append(p)
                map.pop(i)

