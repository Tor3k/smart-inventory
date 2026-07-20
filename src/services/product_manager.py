"""
Smart Inventory

Product manager.
"""


class ProductManager:

    def __init__(self, inventory):

        self.inventory = inventory


    def add_product(self, product):

        return self.inventory.add_product(
            product
        )


    def get_products(self):

        return self.inventory.get_products()


    def get_product_by_identifier(
        self,
        identifier,
    ):

        return self.inventory.find_by_identifier(
            identifier
        )


    def get_product(
        self,
        name,
        product_category,
        unit_type=None,
    ):

        return self.inventory.find_exact_product(
            name=name,
            product_category=product_category,
            unit_type=unit_type,
        )


    def update_product(
        self,
        product,
        name=None,
        brand=None,
        cost=None,
        price=None,
    ):
        """
        Updates editable product information.
        """


        if product is None:

            return False


        if name is not None:

            name = name.strip()

            if not name:

                return False

            product.name = name



        if brand is not None:

            product.brand = brand.strip()



        if cost is not None:

            if cost < 0:

                return False

            product.cost = cost



        if price is not None:

            if price < 0:

                return False

            product.price = price



        if (
            product.cost is not None
            and product.price is not None
            and product.cost > product.price
        ):

            return False



        return True



    def remove_product(
        self,
        identifier,
    ):


        product = (
            self.inventory.find_by_identifier(
                identifier
            )
        )


        if product is None:

            return False


        return self.inventory.remove_product(
            product
        )



    def update_stock(
        self,
        identifier,
        quantity,
    ):

        return self.inventory.add_stock(
            identifier,
            quantity,
        )



    def decrease_stock(
        self,
        identifier,
        quantity,
    ):

        return self.inventory.remove_stock(
            identifier,
            quantity,
        )