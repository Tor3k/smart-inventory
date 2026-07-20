"""
Smart Inventory

Inventory management.
"""


class Inventory:

    def __init__(self):

        self.products = []

    def add_product(self, product):

        if product is None:
            return False

        if (
            product.identifier is not None
            and self.identifier_exists(product.identifier)
        ):
            return False

        self.products.append(product)

        return True

    def remove_product(self, product):

        if product not in self.products:
            return False

        self.products.remove(product)

        return True

    def get_products(self):

        return self.products

    def find_by_identifier(self, identifier):

        if not identifier:
            return None

        identifier = identifier.strip().upper()

        for product in self.products:

            if (
                product.identifier is not None
                and product.identifier.upper() == identifier
            ):
                return product

        return None

    def find_by_name(self, name):

        if not name:
            return []

        name = name.strip().lower()

        results = []

        for product in self.products:

            if name in product.name.lower():
                results.append(product)

        return results

    def find_exact_product(
        self,
        name,
        product_category,
        unit_type=None,
    ):

        name = name.strip().lower()

        for product in self.products:

            if (
                product.name.lower() == name
                and product.product_category
                == product_category
            ):

                if (
                    product_category != "loose"
                    or product.unit_type == unit_type
                ):
                    return product

        return None

    def identifier_exists(self, identifier):

        return (
            self.find_by_identifier(identifier)
            is not None
        )

    def add_stock(self, identifier, quantity):

        product = self.find_by_identifier(identifier)

        if product is None:
            return False

        if quantity <= 0:
            return False

        product.stock += quantity

        return True

    def remove_stock(self, identifier, quantity):

        product = self.find_by_identifier(identifier)

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

            if product.cost is not None:
                total += (
                    product.cost
                    * product.stock
                )

        return total