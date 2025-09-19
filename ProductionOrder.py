class ProductionOrder:
    def __init__(self, order_number: int, product_name: str, quantity: int):
        if quantity < 0:
            raise Exception("Die Menge darf nicht negativ sein!")
        self.order_number = order_number
        self.product_name = product_name
        self.quantity = quantity
        self.produced_units = 0
        self.status = "created"

    def start(self):
        self.status = "in production"

    def finish(self):
        self.status = "completed"

    def produce(self, units: int):
        if units < 0:
            raise Exception("Überprüfen Sie Ihre Eingabe. Keine negative Stückzahlen!")
        self.produced_units += units

    def __str__(self):
        return f"Auftrag {self.order_number}: {self.product_name}, Menge: {self.quantity}, Status: {self.status}"

order1 = ProductionOrder(1, 'Hülle', 100)
order1.produce(50)
order1.produce(50)
print(f"{order1.status}")