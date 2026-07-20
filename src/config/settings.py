"""
Smart Inventory
System settings
"""


class Settings:

    # Taxes

    VAT_RATE = 0.19

    # Pricing

    DEFAULT_PRICE_MULTIPLIER = 1.40

    # Internal identifiers

    INTERNAL_CODE_PREFIX = "LOC"

    # Inventory

    LOW_STOCK_WARNING = 5

    # Storage

    INVENTORY_FILE = "inventory.json"

    # Product categories

    VALID_PRODUCT_CATEGORIES = (
        "purchased",
        "manufactured",
        "loose",
    )

    CATEGORY_IDENTIFICATION = {
        "purchased": "barcode",
        "manufactured": "internal",
        "loose": "manual",
    }

    # Product units

    VALID_UNIT_TYPES = (
        "unit",
        "kg",
    )