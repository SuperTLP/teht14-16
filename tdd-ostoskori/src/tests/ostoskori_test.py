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

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]
        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.hinta(), 3)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        kurkku = Tuote("Kurkku", 5)
        self.kori.lisaa_tuote(kurkku)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_ostoskorissa_yksi_ostos(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_kahden_saman_ostoksen_lisaamisen_jalkeen_korissa_tuote_ja_lukumaara_2(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), "Maito")
        self.assertEqual(ostokset[0].lukumaara(), 2)
    
    def test_tuotteen_lukumaara_vahenee_kun_poistetaan_korista(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("Maito", 3))

        self.kori.poista_tuote(Tuote("Maito", 3))
        ostokset= self.kori.ostokset()
        maara = ostokset[0].lukumaara()
        self.assertEqual(maara, 1)


    def test_poistamisen_jalkeen_kori_tyhja(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.poista_tuote(Tuote("Maito", 3))

        ostokset = self.kori.ostokset()
        hinta = self.kori.hinta()
        self.assertEqual(len(ostokset)+hinta, 0)

    def test_tyhjenna_tyhjentaa_korin(self):
        self.kori.lisaa_tuote(Tuote("Maito", 3))
        self.kori.poista_tuote(Tuote("Maito", 3))
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.lisaa_tuote(Tuote("kurpitsa", 5))
        self.kori.tyhjenna()
        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 0)
    
