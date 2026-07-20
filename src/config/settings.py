"""
Smart Inventory

System settings.
"""


class Settings:

    # Taxes

    VAT_RATE = 0.19

    # Pricing

    DEFAULT_PRICE_MULTIPLIER = 1.40

    INTERNAL_CODE_PREFIX = "LOC"

    LOW_STOCK_WARNING = 5

    DATABASE_FILE = "inventory.db"

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

    VALID_UNIT_TYPES = (
        "unit",
        "kg",
    )