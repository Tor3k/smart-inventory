"""
Smart Inventory

Product service.
"""

from src.config.settings import Settings
from src.models.product import Product
from src.services.validation_service import ValidationService
from src.services.exceptions import DuplicateProductError


class ProductService:

    """
    Handles product creation and product-related business logic.
    """

    def __init__(self, inventory):

        self.inventory = inventory
        self.validation = ValidationService


    def generate_internal_code(self):

        number = 1

        for product in self.inventory.get_products():

            if product.identification_type == "internal":
                number += 1

        identifier = (
            f"{Settings.INTERNAL_CODE_PREFIX}{number:04d}"
        )

        while self.inventory.identifier_exists(identifier):

            number += 1

            identifier = (
                f"{Settings.INTERNAL_CODE_PREFIX}{number:04d}"
            )

        return identifier


    def calculate_suggested_price(self, cost):

        return cost * Settings.DEFAULT_PRICE_MULTIPLIER


    def validate_product_category(self, product_category):

        self.validation.validate_choice(
            product_category,
            Settings.VALID_PRODUCT_CATEGORIES,
            "product category",
        )


    def create_product(
        self,
        name,
        product_category,
        price=None,
        cost=None,
        brand=None,
        stock=0,
        identifier=None,
        unit_type="unit",
        quick_entry=False,
    ):

        name = name.strip()

        self.validate_product_category(
            product_category
        )

        self.validation.validate_required(
            name,
            "Product name",
        )

        self.validation.validate_positive(
            cost,
            "Product cost",
        )

        self.validation.validate_positive(
            price,
            "Product price",
        )

        self.validation.validate_stock(
            stock
        )


        if (
            cost is not None
            and price is not None
            and cost > price
        ):

            raise ValueError(
                "Product cost cannot be greater than sale price."
            )


        if product_category == "purchased":

            if cost is None:

                raise ValueError(
                    "Purchased products require a cost."
                )


            if not identifier:

                raise ValueError(
                    "Purchased products require a barcode."
                )


            existing = self.inventory.find_by_identifier(
                identifier
            )

            if existing is not None:

                raise DuplicateProductError(
                    existing
                )


            if price is None:

                price = self.calculate_suggested_price(
                    cost
                )


        elif product_category == "manufactured":

            if cost is None:

                raise ValueError(
                    "Manufactured products require a cost."
                )


            if price is None:

                raise ValueError(
                    "Manufactured products require a sale price."
                )


            existing = self.inventory.find_exact_product(
                name=name,
                product_category=product_category,
            )

            if existing is not None:

                raise DuplicateProductError(
                    existing
                )


            identifier = self.generate_internal_code()

            unit_type = "unit"


        elif product_category == "loose":

            identifier = None


            self.validation.validate_choice(
                unit_type,
                Settings.VALID_UNIT_TYPES,
                "unit type",
            )


            if price is None:

                raise ValueError(
                    "Loose products require a sale price."
                )


            existing = self.inventory.find_exact_product(
                name=name,
                product_category=product_category,
                unit_type=unit_type,
            )

            if existing is not None:

                raise DuplicateProductError(
                    existing
                )


        product = Product(
            identifier=identifier,
            name=name,
            brand=brand,
            product_category=product_category,
            unit_type=unit_type,
            cost=cost,
            price=price,
            stock=stock,
            quick_entry=quick_entry,
        )


        added = self.inventory.add_product(
            product
        )


        if not added:

            raise ValueError(
                "Product could not be added."
            )


        return product