from ProductionOrder import ProductionOrder

class mes_utils:

    @staticmethod
    def get_order_by_number(orders, order_number):
        for order in orders:
            if order.order_number == order_number:
                return order
        return None

    @staticmethod
    def calculate_production_efficiency(order: ProductionOrder):
        if order.quantity == 0:
            return 0
        return (order.produced_units / order.quantity) * 100