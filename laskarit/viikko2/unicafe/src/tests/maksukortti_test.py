import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortti_raha_testi1(self):
        self.maksukortti.ota_rahaa(20000)
        self.assertEqual(self.maksukortti.saldo,1000)