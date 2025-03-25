import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_raha_luotu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(),1000)

    def test_edulliset_luotu_oikein(self):
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukaat_luotu_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_edulliset_maksu_toimii(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_edulliset_maksu_toimii2(self):
        self.kassapaate.syo_edullisesti_kateisella(240)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_edulliset_ei_myy_jos_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset,0)

    def test_maukkaat_maksu_toimii(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_maukkaat_maksu_toimii2(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_maukkaat_ei_myy_jos_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)

        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_edulliset_kortilla(self): 
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti),True)
        
    def test_saldo_oikein_kortilla_edullisesti(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,760)

    def test_myydyt_edulliset_nousevat(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset,1)
    
    def test_saldo_ei_riita_edullisesti(self):
        kortti = Maksukortti(100)

        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(kortti.saldo,100)

    def test_myynti_ei_tapahdu_edullisesti(self):
        kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti),False)
        
    def test_myytyjen_maara_ei_muutu_edullisesti(self):
        kortti = Maksukortti(100)

        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(self.kassapaate.edulliset,0)
    
    def test_kassapaate_saldo_oikein_kortilla_edullisesti(self):

        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)

    def test_maukkaasti_kortilla(self): 
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti),True)
        
    def test_saldo_oikein_kortilla_maukkaasti(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.maksukortti.saldo,600)
    
    def test_myydyt_maukkaat_nousevat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_saldo_ei_riita_maukkaasti(self):
        kortti = Maksukortti(100)

        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(kortti.saldo_euroina(),1)

    def test_myynti_ei_tapahdu_maukkaasti(self):
        kortti = Maksukortti(100)

        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti),False)
        
    def test_myytyjen_maara_ei_muutu_maukkaasti(self):
        kortti = Maksukortti(100)

        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat,0)

    def test_kassapaate_saldo_oikein_kortilla_maukkaasti(self):

        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
    
    def test_lataus_onnistuu(self):
       self.kassapaate.lataa_rahaa_kortille(self.maksukortti,1000)
       self.assertEqual(self.kassapaate.kassassa_rahaa,101000)

    def test_lataus_negatiivisesti(self):
       self.kassapaate.lataa_rahaa_kortille(self.maksukortti,-1000)
       self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
       self.assertEqual(self.maksukortti.saldo_euroina(),10)



    def test_print_ja_loput_testit(self):
        
        self.assertEqual(str(self.maksukortti),"Kortilla on rahaa 10.00 euroa")