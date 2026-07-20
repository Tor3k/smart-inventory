"""
Smart Inventory

Search service.
"""


class SearchService:

    def __init__(self, inventory):

        self.inventory = inventory

    def search_by_identifier(
        self,
        identifier,
    ):

        return self.inventory.find_by_identifier(
            identifier
        )

    def search_by_name(self, name):

        return self.inventory.find_by_name(
            name
        )

    def search_by_category(
        self,
        product_category,
    ):

        results = []

        for product in self.inventory.get_products():

            if (
                product.product_category
                == product_category
            ):
                results.append(product)

        return results