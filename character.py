class Character:
    def __init__(self, name, life, attack, reach, defends, speed, point ):
        self.name = name
        self.life = life
        self.attack = attack
        self.reach = reach
        self.defends = defends
        self.speed = speed
        self.point = point

    def __str__(self):
        return self.name + " has \nlife: " + str(self.life) + \
         "\nattack " + str(self.attack)
