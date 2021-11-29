from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
        self.kori=[]

    def tavaroita_korissa(self):
        maara = 0
        for i in self.kori:
            maara+=i.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        hinta = 0
        for i in self.kori:
            hinta+=i.lukumaara()*i.hinta()
        return hinta
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        new = list(filter(lambda x: x.tuotteen_nimi()==lisattava.nimi(), self.kori))
        if len(new)==0:
            ostos=Ostos(lisattava)
            self.kori.append(ostos)
            return
        new[0].muuta_lukumaaraa(1)
        
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
