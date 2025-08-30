class ProductionOrder:
    def __init__(self, order_number, product_name, quantity):
        self.order_number = order_number
        self.product_name = product_name
        self.quantity = quantity
        self.status = 'created'
        
    def get_order_number(self):
        return self.order_number

    def start(self):
        self.status = 'in production'
        
    def finish(self):
        self.status = 'completed'
        
    # def produce(self, units):

    # def get_production_efficiency(self):

class ProductionLine: 
    def __init__(self, name):
        self.name = name
        self.orders = []

    def add_order(self, order = ProductionOrder):
        if order in self.orders:
            print('Order already exists, please choose another order.')
        else:
            self.orders.append(order)

    def get_production_line_name(self):
        return self.name
        
    def get_orders(self):
        return self.orders


class MES: 
    def __init__(self):
        return self

    def add_production_line(self, name):
        self.name = ProductionLine(name)
        
#     def create_production_order(self, production_line_name, order_number): int

#     def produce_units(self, production_line_name, order_name, units):
        
#     def get_production_lines(self):

    def get_production_line(self, name):
        return self.name


# class mes_utils:

#     @staticmethod
#     def get_order_by_number(production_line, order_number):

#     @staticmethod
#     def calculate_production_efficiency(order):

productionLine1 = MES.add_production_line('Line A')

print(f'Production Line: {productionLine1.get_production_line_name()}. There are following orders there: {productionLine1.get_orders()}')