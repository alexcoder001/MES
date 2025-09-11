from production_line import ProductionLine
from production_order import ProductionOrder
from mes_utils import mes_utils


class MES:
    def __init__(self):
        self.production_lines = []

    def add_production_line(self, name):
        production_line = ProductionLine(name=name)
        self.production_lines.append(production_line)

    def create_production_order(self, production_line_name, order_number) -> int:
        ProductionOrder(production_line_name)

    def produce_units(self, production_line_name, order_name, units):
        pass

    def get_production_lines(self):
        return self.production_lines

    def get_production_line(self, name):
        for line in self.production_lines:
            if line.get_production_line_name() == name:
                return line
        return None

mes = MES()
mes.add_production_line("Line A")

line = mes.get_production_line("Line A")
print(f"Found line: {line.get_production_line_name() if line else 'Not found'}")
print(f"All lines: {mes.get_production_lines()}")