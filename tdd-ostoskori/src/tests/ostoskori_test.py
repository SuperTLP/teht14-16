import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_tuotteen_lisaamisen_jalkeen_1_tavara(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_tuotteen_lisaamisen_jalkeen_hinta_oikea(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.assertEqual(self.kori.hinta(), 5)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_2_tuotetta(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.lisaa_tuote(Tuote("kurkku", 6))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_hinta_sama_kuin_tuotteiden_hintojen_summa(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.lisaa_tuote(Tuote("kurkku", 6))

        self.assertEqual(self.kori.hinta(), 11)

    def test_kaksi_samaa_tuotetta_kaksi_tavaraa_korissa(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
    
    def test_kahden_saman_tuotteen_hinta_sama_kuin(self):
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.assertEqual(self.kori.hinta(), 10)

    
