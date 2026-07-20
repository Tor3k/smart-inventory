"""
Smart Inventory

Inventory JSON storage.
"""

import json

from src.core.inventory import Inventory
from src.models.product import Product


class InventoryStorage:

    def __init__(self, file_path):

        self.file_path = file_path

    def save(self, inventory):

        data = [
            product.to_dict()
            for product in inventory.get_products()
        ]

        with open(
            self.file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def load(self):

        try:

            with open(
                self.file_path,
                "r",
                encoding="utf-8",
            ) as file:

                data = json.load(file)

        except (
            FileNotFoundError,
            json.JSONDecodeError,
        ):

            return Inventory()

        inventory = Inventory()

        if not isinstance(data, list):
            return inventory

        for product_data in data:

            try:

                product = Product.from_dict(
                    product_data
                )

                inventory.add_product(product)

            except (
                KeyError,
                ValueError,
                TypeError,
            ):

                continue

        return inventory