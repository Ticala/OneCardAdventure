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
                if value < 90 and value >-1:
                    lin += " "
                lin += " " + str(value) + " "
            print (lin)
            print("--------------------")

    def next_step(self, monster, monsters, pillars):
        for pillar in pillars:
            self.dungeon[pillar.getX()][pillar.getY()] = 99
        for mon in monsters:
            self.dungeon[mon.getX()][mon.getY()] = 98

        map = {0: [monster.point] }
        for i in range(1,20):
            map.update({i: []})

        for i in range(20):
            points = map[i]
            for point in points:
                print(point)
                self.set_distance(point.x - 1, point.y, i + 2, map)
                self.set_distance(point.x + 1, point.y, i + 2, map)
                self.set_distance(point.x, point.y - 1, i + 2, map)
                self.set_distance(point.x, point.y + 1, i + 2, map)
            for point in points:
                self.set_distance(point.x - 1, point.y - 1, i + 3, map)
                self.set_distance(point.x - 1, point.y + 1, i + 3, map)
                self.set_distance(point.x + 1, point.y - 1, i + 3, map)
                self.set_distance(point.x + 1, point.y + 1, i + 3, map)
        map.pop(i)

    def set_distance(self, x, y, distance, map):
        if x < 0 or x > 4:
            return
        if y < 0 or y > 4:
            return
        if self.dungeon[x][y] != -1:
            return

        self.dungeon[x][y] = distance
        map.get(distance).append(Point(x,y))
    def getV(self,x,y):
        return self.dungeon[x][y]



