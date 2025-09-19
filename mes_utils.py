class mes_utils:

    @staticmethod
    def get_order_by_number(produktionslinie: str, bestellnummer: int):
        if bestellnummer in produktionslinie:
            return bestellnummer
        else:
            return None

    @staticmethod
    def calculate_production_efficiency(order):
        pass