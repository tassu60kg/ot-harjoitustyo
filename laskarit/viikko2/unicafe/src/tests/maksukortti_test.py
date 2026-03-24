import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_lataarahaa(self):
        self.maksukortti.lataa_rahaa(1000)
        
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_raha_otto(self):
        self.maksukortti.ota_rahaa(500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 5.0)

    def test_raha_otto_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)
    
    def test_raha_ei_otto(self):
        self.maksukortti.ota_rahaa(7777)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_raha_ei_otto_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(7777), False)

    def test_print_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")