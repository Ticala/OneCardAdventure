import random
from character import Character
from point import Point


class Hero(Character):

    dieStrenght=0

    def __init__(self):
        Character.__init__(self, "Charles", 6, 1, 1, 1, 2, Point(0, 0))

    def __str__(self):
        return Character.__str__(self)

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
