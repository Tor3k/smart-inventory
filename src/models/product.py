"""
Smart Inventory
Product model
"""


class Product:

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

    def to_dict(self):
        return {
            "code": self.code,
            "name": self.name,
            "brand": self.brand,
            "product_type": self.product_type,
            "cost": self.cost,
            "price": self.price,
            "stock": self.stock,
            "quick_entry": self.quick_entry,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            code=data["code"],
            name=data["name"],
            brand=data.get("brand"),
            product_type=data["product_type"],
            cost=data["cost"],
            price=data["price"],
            stock=data.get("stock", 0),
            quick_entry=data.get("quick_entry", False),
        )