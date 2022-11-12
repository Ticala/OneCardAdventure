import unittest

from  hero import Hero
from levelMaker import Level_maker
from point import Point


class MyTestCase(unittest.TestCase):
    def test_something(self):


        lm = Level_maker()
        hero = Hero()
        monsters = lm.getMonsters(1)
        self.assertEqual(len(monsters), 2)  # add assertion here

        pillars = lm.getPillars(1)
        for pillar in pillars:
            print(pillar)

        self.assertFalse(hero.can_attack_monster(pillars, monsters))  # add assertion here

        print(monsters[0])
        monsters[0].point = Point(1, 1)
        self.assertTrue(hero.can_attack_monster(pillars, monsters))  # add assertion here


if __name__ == '__main__':
    unittest.main()
