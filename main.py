import random

from dungeon import Dungeon
from hero import Hero
from point import Point
from level_maker import Level_maker
import gameHelper


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
    for level in range(1, 13):
        print("-------------------------------------")
        print("This is level: " + str(level))
        print("-------------------------------------")
        print("")
        print("")
        print("")

        hero.point = levelmaker.getHeroStart(level)
        monsters = levelmaker.getMonsters(level)
        pillars = levelmaker.getPillars(level)

        while len(monsters) > 0 and hero.life > 0:

            # print monsters
            print(monsters[0])
            print(hero)
            gameHelper.printMap(hero, monsters, pillars)

            # roll dice and get extra powers
            hero.setDicePower()

            # print map
            gameHelper.printMap(hero, monsters, pillars)

            # move Hero
            movement = hero.move + hero.dieMove
            has_attacked = False
            direction = "X"
            while (movement > 1 or (not has_attacked and direction != "A")) and direction != "":
                direction = get_hero_action(has_attacked, direction, movement)

                if "A" == direction and not has_attacked:
                    has_attacked = heroAttack(hero, monsters, pillars)
                    for monster in monsters:
                        if monster.life < 1:
                            monsters.remove(monster)
                else:
                    movement = heroMove(direction, hero, monsters, movement, pillars)

                gameHelper.printMap(hero, monsters, pillars)


            for monster in monsters:

                if monster.point.distance(hero.point) > 3:
                    dungeonM = Dungeon()
                    dungeonH = Dungeon()
                    dungeonM.next_step(monster, monsters, pillars)
                    dungeonH.next_step(hero, monsters, pillars)
                    monster.point = find_best_place(dungeonH, dungeonM, monster)

            # how many are in range
            attackers = hero.canAttackHero(pillars, monsters)
            attackers_count = len(attackers)
            monster_strengh = 0
            if attackers_count == 1:
                monster_strengh = attackers[0].strength
                print("A monster attack with {} strength".format(monster_strengh))
            elif attackers_count > 1:
                monster_strengh = attackers[0].strength * attackers_count
                print("{} monsters attack with {} strength".format(attackers_count, monster_strengh))

            print("Hero defends with {}".format(hero.getTotalStr()))

            if monster_strengh >= hero.getTotalStr():
                damage = monster_strengh // hero.getTotalStr()
                print("Hero takes {} damage".format(damage))
                hero.life -= damage

            # Calculate Hero life left
            print("You move and fight. You have " + str(hero.life) + " life left")


            if len(monsters) == 0:
                # Level up or heal
                hero.setUpgrade()
            else:
                if hero.life < 1:
                    playerLose()
                    return
    playerWin()
    return


def get_hero_action(has_attacked, direction, movement):
    if movement > 1:
        print_rossetta()
        if has_attacked:
            direction = input("Move({})".format(movement))
        else:
            direction = input("Move({}) or (A)ttack?".format(movement))
    else:
        direction = input("(A)ttack?".format(movement))
    return direction

def find_best_place(dungeonH, dungeonM, monster):
    point = monster.point
    moves = monster.move
    minimum = 99
    minMoves = 99
    for x in range(5):
        for y in range(5):
            valueH = dungeonH.getV(x, y)
            valueM = dungeonM.getV(x, y)
            if moves >= valueM and minimum >= valueH and valueH > 0:
                if valueH == 2:
                    minimum = 3
                else:
                    minimum = valueH

                if minimum == 3:
                    if minMoves > valueH:
                        minMoves = valueH
                        point = Point(x, y)
                else:
                    point = Point(x, y)

    return point

def print_rossetta():
    print("NW  N  NE")
    print("  \ | /  ")
    print("W - * - E")
    print("  / | \  ")
    print("SW  S  SE")


def heroMove(direction, hero, monsters, movement, pillars):
    newPoint = hero.point.move(direction)
    distance = newPoint.distance(hero.point)
    if not newPoint.isHit(pillars):
        if not newPoint.isHit(monsters):
            if movement >= distance:
                hero.point = newPoint
                movement -= distance
    return movement


def heroAttack(hero, monsters, pillars):
    monsterInRange = hero.can_attack_monster(pillars, monsters)
    count = len(monsterInRange)
    if count == 0:
        print("No one to attack")
        return False

    if count == 1:
        hero.attackMonster(monsterInRange[0])
    elif count > 1:
        for i in range(count):
            print(str(monsterInRange[i].point) + "--" + str(i))
        number = input("Select monster no. to attack?")
        hero.attackMonster(monsterInRange[int(number)])
    return True


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
