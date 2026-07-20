"""
Smart Inventory

Inventory SQLite storage.
"""

from src.core.inventory import Inventory
from src.models.product import Product


class InventoryStorage:

    def __init__(self, database):

        self.database = database
        self.connection = database.get_connection()

    def save(self, inventory):

        cursor = self.connection.cursor()

        cursor.execute(
            "DELETE FROM products"
        )

        for product in inventory.get_products():

            cursor.execute(
                """
                INSERT INTO products (

                    identifier,
                    identification_type,
                    name,
                    brand,
                    product_category,
                    unit_type,
                    cost,
                    price,
                    stock,
                    quick_entry

                )

                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    product.identifier,
                    product.identification_type,
                    product.name,
                    product.brand,
                    product.product_category,
                    product.unit_type,
                    product.cost,
                    product.price,
                    product.stock,
                    int(product.quick_entry),
                ),
            )

        self.connection.commit()

    def load(self):

        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT *
            FROM products
            """
        )

        inventory = Inventory()

        for row in cursor.fetchall():

            try:

                product = Product(
                    identifier=row["identifier"],
                    name=row["name"],
                    brand=row["brand"],
                    product_category=row["product_category"],
                    unit_type=row["unit_type"],
                    cost=row["cost"],
                    price=row["price"],
                    stock=row["stock"],
                    quick_entry=bool(
                        row["quick_entry"]
                    ),
                )

                inventory.add_product(
                    product
                )

            except (
                ValueError,
                TypeError,
            ):

                continue

        return inventory