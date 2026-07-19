"""
Smart Inventory

Inventory management.
"""


class Inventory:

    def __init__(self):
        self.products = []


    def add_product(self, product):

        if self.code_exists(product.code):
            return False

        self.products.append(product)

        return True


    def get_products(self):
        return self.products


    def find_by_code(self, code):

        code = code.upper()

        for product in self.products:

            if product.code.upper() == code:
                return product

        return None


    def find_by_name(self, name):

        results = []

        for product in self.products:

            if name.lower() in product.name.lower():
                results.append(product)

        return results


    def code_exists(self, code):
        return self.find_by_code(code) is not None


    def add_stock(self, code, quantity):

        product = self.find_by_code(code)

        if product is None:
            return False

        if quantity <= 0:
            return False

        product.stock += quantity

        return True


    def remove_stock(self, code, quantity):

        product = self.find_by_code(code)

        if product is None:
            return False

        if quantity <= 0:
            return False

        if quantity > product.stock:
            return False

        product.stock -= quantity

        return True


    def calculate_inventory_value(self):

        total = 0

        for product in self.products:
            total += product.cost * product.stock

        return total