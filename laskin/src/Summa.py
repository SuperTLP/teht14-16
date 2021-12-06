class Summa:
    def __init__(self, sovellus, lue_syote):
        self.sovellus=sovellus
        self.lue_syote=lue_syote
    def suorita(self):
        arvo = self.lue_syote()
        self.sovellus.plus(arvo)
        self.sovellus.historia.append(self.sovellus.tulos)
    def kumoa(self):
        self.sovellus.aseta_arvo(self.cache)