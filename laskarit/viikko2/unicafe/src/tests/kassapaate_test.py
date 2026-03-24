import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    #tylsät testit

    def test_raha_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    def test_edulliset_luotu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_luotu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    #edullinen myynti

    def test_edullinen_myynti_kateinen(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_myynti_kateinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(250), 10)

    def test_edullinen_kateinen_ei_myy(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kateinen_ei_myy_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    #maukas myynti

    def test_maukas_myynti_kateinen(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_myynti_kateinen_vaihtoraha(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(410), 10)

    def test_maukas_kateinen_ei_myy(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukas_kateinen_ei_myy_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    #edullinen kortti

    def test_edullinen_myynti_kortti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullinen_myynti_kortti_raha_kassapaate(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 7.6)
    
    def test_edullinen_myynti_kortti_ei_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
    
    def test_edullinen_myynti_kortti_ei_rahaa_ei_lähde(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 1.0)
    
    def test_edullinen_myynti_kortti_kassa_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    #maukas kortti

    def test_maukas_myynti_kortti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukas_myynti_kortti_raha_kassapaate(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.0)
    
    def test_maukas_myynti_kortti_ei_rahaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
    
    def test_maukas_myynti_kortti_ei_rahaa_ei_lähde(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo_euroina(), 1.0)
    
    def test_maukas_myynti_kortti_kassa_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000.0)

    #kortti lataus

    def test_kortti_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 20.0)

    def test_kortti_lataus_huono_summa(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1000)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)
    