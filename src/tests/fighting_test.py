import unittest
from services import fighting

class TestFighting(unittest.TestCase):
    def setUp(self):
        self.fighting = fighting.Fighting("test", 2)

    def test_get_power(self):
        self.fighting.get_power([["1",2],["2",2],["3",2],["4",2],["5",2],["6",2]])
        self.assertAlmostEqual(self.fighting.character_power,2.347,2)

    def test_fight_can_win(self):
        self.fighting.character_power = 2.2
        self.assertEqual(self.fighting.fight(), True)

    def test_fight_can_not_win(self):
        self.fighting.character_power = 1.9
        self.assertEqual(self.fighting.fight(), False)

    def test_scale(self):
        self.fighting.scale()
        self.assertEqual((self.fighting.iteration,self.fighting.name,self.fighting.powerscale)
                         ,(2,"test 2",4))
