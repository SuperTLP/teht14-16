from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self._kori=[]

    def tavaroita_korissa(self):
        maara = 0
        for i in self._kori:
            maara+=i.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for i in self._kori:
            hinta+=i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        new = list(filter(lambda x: x.tuotteen_nimi()==lisattava.nimi(), self._kori))
        if len(new)==0:
            ostos=Ostos(lisattava)
            self._kori.append(ostos)
            return
        self._kori[self._kori.index(new[0])].muuta_lukumaaraa(1)

    def poista_tuote(self, poistettava: Tuote):
        new = list(filter(lambda x: x.tuotteen_nimi()==poistettava.nimi(), self._kori))
        if len(new)==0:
            return
        if (new[0].lukumaara()==1):
            self._kori.remove(new[0])
            return
        self._kori[self._kori.index(new[0])].muuta_lukumaaraa(-1)

    def tyhjenna(self):
        self._kori=[]
        # tyhjentää ostoskorin

    def ostokset(self):
        return self._kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
