class Produktionsauftrag:
    def __init__(self, bestellnummer: int, produktname: str, menge: int):
        self.bestellnummer = bestellnummer
        self.produktname = produktname
        self.menge = menge
        self.status = "created"

    def start(self):
        self.status = "in production"

    def finish(self):
        self.status = "completed"

    def produce_units(self, units):
        pass
