import unittest

from dungeon import Dungeon
from hero import Hero
from level_maker import Level_maker

class MyTestCase(unittest.TestCase):
    def test_something(self):

        level_maker = Level_maker()
        pillars = level_maker.getPillars(1)
        monsters = level_maker.getMonsters(1)
        herostart = level_maker.getHeroStart(1)

        hero = Hero()
        hero.point = herostart

        dungeon = Dungeon()
        dungeon.next_step(monsters[0], monsters, pillars)
        dungeon.printDungeon()


        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
