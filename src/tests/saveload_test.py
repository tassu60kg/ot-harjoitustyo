import unittest
from data import saveload
from services import character
from services import resources
from services import upgrades
from services import fighting

class TestSaveload(unittest.TestCase):
    def setUp(self):
        self.save = saveload.SaveLoad("data/testsave.txt")
        self.upgrade = upgrades.Upgrade([("test1",1,1), ("test2",2,2)])
        self.resources = resources.Resource(1,2)
        self.character = character.Character([["test1",1],["test2",2]])
        self.fighting = fighting.Fighting("test 1", 6)
        with open("data/testsave.txt", "w", encoding="utf-8"):
            pass #clear the file

    def test_save(self):
        self.save.save(self.upgrade,self.resources,self.character,self.fighting)
        with open("data/testsave.txt", encoding="utf-8") as file:
            n = ""
            for i in file:
                n = n + i
        self.assertEqual(n,"('test1', 1, 1), ('test2', 2, 2)\n1\n2\n['test1', 1], ['test2', 2]\n0\n100\ntest 1 1\n6\n1")

    def test_load(self):
        load = saveload.SaveLoad("data/testload.txt")
        load.load(self.upgrade,self.resources,self.character,self.fighting)
        self.assertEqual((self.upgrade.upgrades,
                          self.resources.r1,
                          self.resources.add_r1,
                          self.character.statblock,
                          self.character.ap,
                          self.character.ap_cost,
                          self.fighting.name,
                          self.fighting.iteration,
                          self.fighting.powerscale),(
                              [('test 1', 100, 1), ('test 2', 200, 2), ('test 3', 300, 3)],
                              1,
                              2,
                              [['test', 1], ['test2', 2]],
                              3,
                              100,
                              "test 1",
                              5,
                              4))
