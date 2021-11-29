from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
        self.kori=[]
        self.tavaroiden_maara=0
        self._hinta=0
    def tavaroita_korissa(self):
        return self.tavaroiden_maara

        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        return self._hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        ostos=Ostos(lisattava)
        self.kori.append(ostos)
        self.tavaroiden_maara+=1
        self._hinta+=lisattava.hinta()
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
