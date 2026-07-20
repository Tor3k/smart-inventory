"""
Smart Inventory

Application entry point.
"""

from src.config.settings import Settings
from src.storage.inventory_storage import InventoryStorage
from src.ui.menu import Menu


def main():

    storage = InventoryStorage(
        Settings.INVENTORY_FILE
    )

    inventory = storage.load()

    menu = Menu(
        inventory
    )

    try:
        menu.show()

    except Exception as error:
        print(f"\nError inesperado: {error}")

    finally:
        storage.save(inventory)


if __name__ == "__main__":
    main()