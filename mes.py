from produktionsauftrag import Produktionsauftrag
from produktionslinie import Produktionslinie
from mes_utils import mes_utils


class MES:
    def __init__(self):
        self.produktionslinien = []

    def add_produktionslinie(self, produktionslinie: Produktionslinie):
        if produktionslinie in self.produktionslinien:
            raise Exception(
                f"{produktionslinie.name} existiert bereits, wähle anderen Name."
            )
        self.produktionslinien.append(produktionslinie)

    def create_production_order(self, production_line_name, order_number) -> int:
        Produktionsauftrag(production_line_name)

    def produce_units(self, production_line_name, order_name, units):
        pass

    def get_produktionslinien(self):
        return self.produktionslinien

    def get_produktionslinie(self, name):
        for linie in self.produktionslinien:
            if linie.get_produktionslinie() == name:
                return linie
        return None


mes = MES()
produktionslinie1 = Produktionslinie('A1')
produktionslinie2 = Produktionslinie('A2')
mes.add_produktionslinie(produktionslinie1)
mes.add_produktionslinie(produktionslinie2)
mes.get_produktionslinie('A1')
print(f"{mes.get_produktionslinie('A2')}")

mes_utils = mes_utils()