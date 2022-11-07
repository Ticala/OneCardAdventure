from hero import Hero
from point import Point

def printMap(hero, monsters, pillars):
    # print map
    print("------------------------------")
    for i in range(5):
        row = ""
        for j in range(5):
          point = Point(j, 4-i)
          if point.samePlace(hero):
            row += "  H  !"
          elif point.isHit(pillars):
            row += "[   ]!"
          elif point.isHit(monsters):
            for monster in monsters:
                if monster.point.samePlace(point):
                    row += " \\" + str(monster.life) + "/ !"
          else:
            row += "     !"
        print("!" + row + "")
    print("------------------------------")
