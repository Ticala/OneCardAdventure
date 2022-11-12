import random
from character import Character
from point import Point


class Hero(Character):

    dieStrenght=0

    def __init__(self):
        Character.__init__(self, "Charles", 6, 1, 1, 1, 2, Point(0, 0))

    def __str__(self):
        return Character.__str__(self)

    def getTotalMov(self):
        return self.move + self.dieMove

    def getTotalStr(self):
        return self.strength + self.dieStrenght

    def getTotalDef(self):
        return self.defence + self.dieDefence

    def setDicePower(self):
        print("Rolling you dice")
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice3 = random.randint(1, 6)
        print("{} {} {}".format(dice1,dice2,dice3))

        power = input("Select powers(MSD)")
        while (len(power) != 3 and "S" not in power and "M" not in power and "D" not in power):
            power = input("Choose you power like (SMD)")

        self.setPower( power[0], dice1)
        self.setPower( power[1], dice2)
        self.setPower( power[2], dice3)

    def canAttackHero(self, pillars, enemies):
        enemiesInRange = []
        things = pillars + []
        for enemy in enemies:
            things.append(enemy.point)

        # is enemy in range
        for enemy in enemies:
            distance = self.point.distance(enemy.point)
            if distance > 0 and distance <= enemy.range:
                if self.distance_test(distance, enemy, things):
                    enemiesInRange.append(enemy)
        return enemiesInRange

    def can_attack_monster(self, pillars, enemies):
        enemiesInRange = []
        things = pillars + []
        for enemy in enemies:
            things.append(enemy.point)

        # is enemy in range
        for enemy in enemies:
            distance = self.point.distance(enemy.point)
            if distance > 0 and distance <= self.range:
                    enemiesInRange.append(enemy)
        return enemiesInRange


    def distance_test(self, distance, enemy, things):
        #
        #  [H][M][ ]   [ ][M][ ]
        #  [ ][ ][ ]   [H][ ][ ]
        #
        hitter = (distance == 2 or distance == 3)
        #
        #  [ ][ ][ ]   [ ][ ][M]
        #  [H][ ][M]   [ ][ ][ ]
        #  [ ][ ][ ]   [H][ ][ ]
        #
        if distance == 4 or distance == 6:
            mpoint = self.point.avg(enemy.point)
            if not mpoint.isHit(things):
                hitter = True
        #
        #  [ ][ ][M]
        #  [X][ ][ ]
        #
        if distance == 5:
            pointfloot = self.point.avgFloor(enemy.point)
            pointCeil = self.point.avgCeil(enemy.point)
            if not pointfloot.isHit(things) or not pointCeil.isHit(things):
                hitter = True
        return hitter


    def setPower(self, trait, die):
        if (trait == "S"):
            self.dieStrenght = die
        if (trait == "M"):
            self.dieMove = die
        if (trait == "D"):
            self.dieDefence = die

    def setUpgrade(self, price):
        if (price[0].upper() == "H"):
            self.life = 6;
        elif (price[0].upper() == "D"):
            self.defence += 1
        elif (price[0].upper() == "A"):
            self.defence += 1
        elif (price[0].upper() == "M"):
            self.defence += 1

    def attackMonster(self, monster):
        print("Hero attack with {} {}".format(self.strength, self.dieStrenght))
        print("Monster defends with {} ".format(monster.defence))
        damage = (self.strength + self.dieStrenght) // monster.defence
        monster.life -= damage
        print("Monster takes {} damage.".format(damage))

    def attackmonster(self, monsterInRange):
        return monsterInRange[0]
