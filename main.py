import random

from hero import Hero
from point import Point
from levelMaker import Level_maker


def showRules():
    print("\n\n\nThe objective of the gave is to escape the dungeon")
    print("--------------------------------------------------------")
    print("each round you role 3 dice and distribute they values to your ")
    print("characters stats. then you move and fight the monster")
    print("")
    print("")
    print("")


def theGame():
    levelmaker = Level_maker()
    hero = Hero()
    for level in range(12):

        print("-------------------------------------")
        print("This is level: " + str(level + 1))
        print("-------------------------------------")
        print("")
        print("")
        print("")


        monsters = levelmaker.getMonsters(level)
        pillars = levelmaker.getPillars(level)
        levelmaker.getHeroStart(level)

        while len(monsters) > 0 and hero.life > 0:

            # print monsters
            for monster in monsters:
                print(monster)

            print(Hero)

            # roll dice and get ekstra powers
            hero.setDicePower()

            # move Hero
            movement = hero.move + hero.dieMove
            attack = False

            direction = "X"
            printMap(hero, monsters, pillars)

            while movement > 1 and direction != "":
                direction = input("Move {} where N/S/E/W or (A)ttack?".format(movement))
                if ("A" == direction):
                        monsterInRange = hero.canAttack(pillars, monsters)

                        if len(monsterInRange) == 1:
                            hero.attackMonster(monsterInRange[0])
                            attack = True
                        elif len(monsterInRange) > 1:
                            for idx, monster in monsterInRange:
                                print( monster + str(idx) )
                            number = input("Select monster no. to attack?")
                            hero.attackMonster(monsterInRange[int(number)])
                            attack = True
                else:
                    newPoint = hero.point.move(direction)
                    distance = newPoint.distance(hero.point)
                    print(direction)
                    if not newPoint.isHit(pillars): 
                        if not newPoint.isHit(monsters):
                            if  movement >= distance:
                                hero.point = newPoint
                                movement -= distance

                printMap(hero, monsters, pillars)

            # remove dead monsters

            # move monsters

            # how many are in range
            #hero.canAttack

            # Monsters attack


            # Calculate Hero life left
            print("You move and fight. You have " + str(hero.life) + " life left")

            if input("is monster killed? (Y/N)") == "Y":
                monsters.pop(0)
                print("yeah one monster is dead\n\n")

                if len(monsters) == 0:
                    # Level up or heal
                    price = input("Do you want to (h)eal, or get more (m)ovement, (a)ttack or (d)efence")
                    hero.SetPrice(price)
            else:
                print("monster move and fight")
                hero.life = hero.life - 1
                if hero.life == 0:
                    playerLose()
                    return
    playerWin()
    return


def printMap(hero, monsters, pillars):
    # print map
    print("--------------------")
    for i in range(5):
        row = ""
        for j in range(5):
          point = Point(j, 4-i)
          if point.samePlace(hero):
            row += "  H  !"
          elif point.isHit(pillars):
            row += "[   ]!"
          elif point.isHit(monsters):
            row += " \X/ !"
          else:        
            row += "     !"
        print("!" + row + "")
    print("--------------------")


def playerWin():
    print("\n\n\nOh yes, You are free and alive.")


def playerLose():
    print("\n\n\nOh no, You are dead.")


#####################################################
#  The begining
#####################################################

print("One Card Dungeon, python version")


# Rules
rules = input("Would you like to learn the rules (Y/N)?")
if (rules + "N").upper()[0] == "Y":
    showRules()

theGame()   

# while ("Y" == input("Try again (Y/N)".upper())):
#    theGame()

print("this is the end")
