from production_order import ProductionOrder

class ProductionLine:
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order=ProductionOrder):
        if order in self.orders:
            print("Order already exists, please choose another order.")
        else:
            self.orders.append(order)

    def get_production_line_name(self):
        return self.name

    def get_orders(self):
        return self.orders  

    # Test
prodLine = ProductionLine('Line A')
prodLine.add_order('Order #1')

print(f'{prodLine.get_production_line_name()} has following orders: {prodLine.get_orders()}')