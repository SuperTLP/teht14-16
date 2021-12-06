class Kumoa:
    def __init__(self, sovellus):
        self.sovellus=sovellus
    def suorita(self):
        try:
            self.sovellus.historia.pop(len(self.sovellus.historia)-1)
            self.sovellus.tulos=self.sovellus.historia[len(self.sovellus.historia)-1]
        except Exception:
            pass

