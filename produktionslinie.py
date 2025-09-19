from produktionsauftrag import Produktionsauftrag
    
class Produktionslinie:
    def __init__(self, name):
        self.name = name
        self.auftraege = []

    def add_auftrag(self, auftrag: Produktionsauftrag):
        if any(a.name == auftrag.name for a in self.auftraege):
            raise Exception(f"{auftrag.name} existiert bereits, wähle anderen Name.")
        self.auftraege.append(auftrag)

    def get_produktionslinie(self):
        return self.name

    def get_auftraege(self) -> list:
        return self.auftraege

# Beispiel:
# produktionslinie = Produktionslinie('A1')
# auftrag1 = Auftrag(1, 'Handyhülle', 100)
# produktionslinie.add_auftrag(auftrag1)

# print(f"{produktionslinie.get_produktionslinie()} hat folgende Aufträge: {produktionslinie.get_auftraege}")
