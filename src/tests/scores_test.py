import unittest
from scores import Scores
class TestScores(unittest.TestCase):
    def setUp(self):
        self.db = Scores(True)
        self.db.addscore("test",1)

    def test_read(self):
        self.assertEqual(self.db.readscore()[0],("test",1))

    def test_reset(self):
        self.db.resetscores()
        self.assertEqual(self.db.readscore(),[])
        