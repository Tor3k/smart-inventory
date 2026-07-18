"""
Smart Inventory

Product service.
"""

from src.models.product import Product
from src.config.settings import Settings


class ProductService:
    """
    Handles product creation and product-related business logic.
    """

    VALID_PRODUCT_TYPES = [
        "purchased",
        "manufactured"
    ]


    def __init__(self, inventory):
        self.inventory = inventory


    def generate_internal_code(self):
        """
        Generates an internal product code.
        Example: LOC0001
        """

        number = len(self.inventory.get_products()) + 1

        code = f"{Settings.INTERNAL_CODE_PREFIX}{number:04d}"

        while self.inventory.code_exists(code):
            number += 1
            code = f"{Settings.INTERNAL_CODE_PREFIX}{number:04d}"

        return code


    def calculate_suggested_price(self, cost):
        return cost * Settings.DEFAULT_PRICE_MULTIPLIER


    def validate_product_type(self, product_type):
        if product_type not in self.VALID_PRODUCT_TYPES:
            raise ValueError(
                "Invalid product type. "
                "Use 'purchased' or 'manufactured'."
            )


    def create_product(
        self,
        name,
        product_type,
        cost,
        brand=None,
        price=None,
        stock=0,
        barcode=None,
        quick_entry=False
    ):

        self.validate_product_type(product_type)

        if cost < 0:
            raise ValueError(
                "Product cost cannot be negative."
            )

        if stock < 0:
            raise ValueError(
                "Product stock cannot be negative."
            )

        if barcode:
            code = barcode
        else:
            code = self.generate_internal_code()

        if price is None:
            price = self.calculate_suggested_price(cost)

        product = Product(
            code=code,
            name=name,
            brand=brand,
            product_type=product_type,
            cost=cost,
            price=price,
            stock=stock,
            quick_entry=quick_entry
        )

        added = self.inventory.add_product(product)

        if not added:
            raise ValueError(
                "Ya existe un producto con ese código."
            )

        return product