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
        
    def produce(self, units):
        pass
    
    def get_production_efficiency(self):
        pass