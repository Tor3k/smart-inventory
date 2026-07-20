"""
Smart Inventory

Custom exceptions.
"""


class DuplicateProductError(Exception):

    def __init__(self, product):

        self.product = product

        super().__init__(
            "Product already exists."
        )