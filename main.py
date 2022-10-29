import random
from hero import Hero
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
    print(Hero)
    for level in range(12):
        print("This is level: " + str(level + 1))

        monsters = levelmaker.getMonsters(level)
        pillars = levelmaker.getPillars(level)

        while len(monsters) > 0 and hero.life > 0:

            # print monsters
            for monster in monsters:
                print(monster)

            # roll dice and get ekstra powers
            hero.setDicePower()

            # print map

            # move Hero
            attOrMov = input("(A)ttack or (M)ove")

            direction = input("Move where?")

            # Hero attack monsters

            # remove dead monsters

            # move monsters

            # Monsters attack

            # how many are in range

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
if ((rules + "N").upper()[0] == "Y"):
    showRules()

theGame()
# while ("Y" == input("Try again (Y/N)".upper())):
#    theGame()

print("this is the end")
