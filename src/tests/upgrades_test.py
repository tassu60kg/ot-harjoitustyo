import unittest
from services import resources
from services import upgrades

class TestUpgrade(unittest.TestCase):
    def setUp(self):
        self.resource = resources.Resource(100,0)
        self.upgrade = upgrades.Upgrade([("test 1", 100, 1), ("test 2", 200, 1)])

    def test_can_buy(self):
        self.upgrade.buy(self.resource, 0)
        self.assertEqual(self.resource.R1, 0)

    def test_can_not_buy(self):
        self.upgrade.buy(self.resource, 1)
        self.assertEqual(self.resource.R1, 100)

    def test_buy_addR1_increases(self):
        self.upgrade.buy(self.resource, 0)
        self.assertEqual(self.resource.addR1, 1)

    def test_can_not_buy_does_not_increase_addR1(self):
        self.upgrade.buy(self.resource, 1)
        self.assertEqual(self.resource.addR1, 0)
