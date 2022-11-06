import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "point:(" + str(self.x) + " , " + str(self.y)+")"

    def distance(self, point):
        d_normal = (self.x - point.x) ** 2 + (self.y - point.y)

        match d_normal:
            case 0:
                return 0
            case 1:
                return 2
            case 2:
                return 3
            case 4:
                return 4
            case 5:
                return 5
            case 8:
                return 6
            case _:
                return 999

    def avg(self, point):
        return Point( (point.x + self.x)/2, ( point.x + self.x)/2 )

    def avgFloor(self, point):
        floorx = math.floor((point.x + self.x) / 2)
        floory = math.floor((point.y + self.y) / 2)
        return Point(floorx, floory)

    def avgCeil(self, point):
        ceilx = math.ceil((point.x + self.x) / 2)
        ceily = math.ceil((point.y + self.y) / 2)
        return Point(ceilx, ceily)

    def move(self, direction):
            x = self.x
            y = self.y

            if "N" in direction:
                y += 1
                print("N")
            if "S" in direction:
                y -= 1
                print("S")

            if "E" in direction:
                x += 1
                print("E")
            if "W" in direction:
                print("W")
                x -= 1

            if 0 > x or x > 4 or 0 > y or y > 4:
                return self
            else:
                return Point(x,y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def samePlace(self, point):
        return self.getX() == point.getX() and self.getY()== point.getY()
    
    def isHit(self, points):
        for point in points:
            if self.samePlace(point):
                return True
        return False


