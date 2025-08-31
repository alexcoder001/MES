from production_line import ProductionLine
from production_order import ProductionOrder
from mes_utils import mes_utils

class MES: 
    def __init__(self):
        self.production_lines = []

    def add_production_line(self, name):
        self.production_lines.append(name)
        
        
    # def create_production_order(self, production_line_name, order_number) -> int:

    # def produce_units(self, production_line_name, order_name, units):
        
    def get_production_lines(self):
        return self.production_lines

    # def get_production_line(self, name):
    #     return ProductionLine.get_production_line_name()
