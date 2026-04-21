import unittest
from services import character
from services import resources

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = character.Character([["test",0],["test2",0] ],
                 0,100)
        self.resource = resources.Resource(100,100)

    def test_buy_ap(self):
        self.character.buy_ap(self.resource)
        self.assertEqual(self.character.ap, 1)

    def test_can_not_buy_ap(self):
        resource_new = resources.Resource(10,10)
        self.character.buy_ap(resource_new)
        self.assertEqual(self.character.ap, 0)

    def test_buy_skill(self):
        character_new = character.Character([["test",0],["test2",0] ],
                 1,100)
        character_new.upgrade(1)
        self.assertEqual(character_new.statblock[1][1],1)

    def test_can_not_buy_skill(self):
        self.character.upgrade(1)
        self.assertEqual(self.character.statblock[1][1],0)
