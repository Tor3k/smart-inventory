"""
Smart Inventory
Product model
"""


class Product:
    """
    Represents a product in the inventory.
    """

    def __init__(
        self,
        code,
        name,
        product_type,
        cost,
        price,
        stock=0,
        brand=None,
        quick_entry=False
    ):
        self.code = code
        self.name = name
        self.brand = brand
        self.product_type = product_type
        self.cost = cost
        self.price = price
        self.stock = stock
        self.quick_entry = quick_entry