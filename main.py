import random

from hero import Hero
from point import Point
from levelMaker import Level_maker
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

            # move Hero
            movement = hero.move + hero.dieMove
            has_attacked = False

            direction = "X"
            gameHelper.printMap(hero, monsters, pillars)

            while ( movement > 1 or ( not has_attacked and direction != "A")) and direction != "":
                direction = get_hero_action(has_attacked, direction, movement)

                if "A" == direction and not has_attacked:
                    has_attacked = heroAttack(hero, monsters, pillars)
                else:
                    movement = heroMove(direction, hero, monsters, movement, pillars)

                gameHelper.printMap(hero, monsters, pillars)

            # remove dead monsters
            for monster in monsters:
                if monster.life < 1:
                    monsters.remove(monster)

            # move monsters

            # how many are in range
            attackers = hero.canAttackHero(pillars, monsters)
            attackers_count = len(attackers)
            monster_strengh = 0
            if attackers_count == 1:
                monster_strengh = attackers[0].strength
                print("A monster attack with {} strength".format( monster_strengh))
            elif attackers_count > 1:
                monster_strengh = attackers[0].strength * attackers_count
                print("{} monsters attack with {} strength".format( attackers_count, monster_strengh))

            if monster_strengh >= hero.strength:
                damage = monster_strengh // hero.getTotalStr()
                print("Hero takes {} damage".format(damage))
                hero.life -= damage

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
                if hero.life == 0:
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
        for idx, monster in monsterInRange:
            print(monster.point+"--" + str(idx))
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
