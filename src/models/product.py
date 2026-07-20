"""
Smart Inventory

Product model.
"""

from src.config.settings import Settings


class Product:

    def __init__(
        self,
        identifier,
        name,
        product_category,
        cost,
        price,
        stock=0,
        brand=None,
        unit_type="unit",
        quick_entry=False,
    ):

        if product_category not in Settings.VALID_PRODUCT_CATEGORIES:
            raise ValueError(
                "Invalid product category."
            )

        if not isinstance(name, str) or not name.strip():
            raise ValueError(
                "Product name cannot be empty."
            )

        identification_type = (
            Settings.CATEGORY_IDENTIFICATION[
                product_category
            ]
        )

        if (
            identification_type in ("barcode", "internal")
            and not identifier
        ):
            raise ValueError(
                "This product requires an identifier."
            )

        if identification_type == "manual":
            identifier = None

        if product_category != "loose":
            unit_type = "unit"

        if unit_type not in Settings.VALID_UNIT_TYPES:
            raise ValueError(
                "Invalid unit type."
            )

        if cost is not None and cost < 0:
            raise ValueError(
                "Product cost cannot be negative."
            )

        if price is not None and price < 0:
            raise ValueError(
                "Product price cannot be negative."
            )

        if stock < 0:
            raise ValueError(
                "Product stock cannot be negative."
            )

        self.identification_type = identification_type
        self.identifier = identifier

        self.name = name.strip()
        self.brand = brand

        self.product_category = product_category
        self.unit_type = unit_type

        self.cost = cost
        self.price = price
        self.stock = stock

        self.quick_entry = quick_entry

    def to_dict(self):

        return {
            "identification_type": self.identification_type,
            "identifier": self.identifier,
            "name": self.name,
            "brand": self.brand,
            "product_category": self.product_category,
            "unit_type": self.unit_type,
            "cost": self.cost,
            "price": self.price,
            "stock": self.stock,
            "quick_entry": self.quick_entry,
        }

    @classmethod
    def from_dict(cls, data):

        return cls(
            identifier=data.get("identifier"),
            name=data["name"],
            product_category=data["product_category"],
            cost=data.get("cost"),
            price=data.get("price"),
            stock=data.get("stock", 0),
            brand=data.get("brand"),
            unit_type=data.get("unit_type", "unit"),
            quick_entry=data.get("quick_entry", False),
        )