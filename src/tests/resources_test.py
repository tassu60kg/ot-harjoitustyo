import unittest
from services import resources

class TestResource(unittest.TestCase):
    def setUp(self):
        self.resource = resources.Resource(10,10)

    def test_increase_working(self):
        self.resource.increase()
        self.assertEqual(self.resource.R1, 20)
