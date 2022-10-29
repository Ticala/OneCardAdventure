class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "point:" + str(self.x) + " , " + str(self.y)

    def isHit(self, positions):
        for position in positions:
            if (position.x == self.x and position.y == self.y):
                return True
        return False
