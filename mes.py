from ProductionOrder import ProductionOrder
from ProductionLine import ProductionLine
from mes_utils import mes_utils


class MES:
    def __init__(self):
        self.production_lines = {}

    def add_production_line(self, name: str):
        if name in self.production_lines:
            raise Exception(f"{name} existiert bereits, wähle anderen Name.")
        self.production_lines[name] = ProductionLine(name)

    def get_production_line(self, name: str):
        return self.production_lines.get(name, None)

    def add_production_order(self, line_name: str, order: ProductionOrder):
        line = self.get_production_line(line_name)
        if not line:
            raise Exception(f'Produktionslinie {line_name} existiert nicht.')
        line.add_order(order)
        return order

    def produce_units(self, production_line_name: str, order_number: int, units: int):
        line = self.get_production_line(production_line_name)
        if not line:
            raise Exception(f"Produktionslinie {production_line_name} existiert nicht.")
        order = mes_utils.get_order_by_number(line.get_orders(), order_number)

        order.start()
        order.produce(units)
        if order.produced_units >= order.quantity:
            order.finish()
        return order


    def get_production_lines(self):
        return list(self.production_lines.values())


mes = MES()
mes.add_production_line("Linie A")
order1 = ProductionOrder(1, 'Handy', 10)
mes.add_production_order('Linie A', order1)
mes.get_production_line('Linie A')

print(f"{mes.produce_units('Linie A', 1, 20)}")
