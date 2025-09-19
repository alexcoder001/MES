from ProductionOrder import ProductionOrder

class ProductionLine:
    def __init__(self, name: str):
        self.name = name
        self.orders = []

    def add_order(self, order: ProductionOrder):
        if order in self.orders:
            raise Exception(
                f"{order.order_number} existiert bereits in dieser Produktionslinie."
            )
        if order.quantity < 0:
            raise Exception("Die Menge darf nicht negativ sein!")
        self.orders.append(order)

    def get_production_line(self):
        return self.name

    def get_orders(self) -> list:
        return self.orders

    def __str__(self):
        return f"Produktionslinie {self.name} hat folgende Aufträge: {self.get_orders()}"
