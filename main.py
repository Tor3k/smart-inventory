"""
Smart Inventory

Application entry point.
"""

from src.config.settings import Settings
from src.storage.database import Database
from src.storage.inventory_storage import InventoryStorage
from src.ui.menu import Menu


def main():

    database = Database(
        Settings.DATABASE_FILE
    )

    storage = InventoryStorage(
        database
    )

    inventory = storage.load()

    menu = Menu(
        inventory
    )

    try:

        menu.show()

    except Exception as error:

        print(
            f"\nError inesperado: {error}"
        )

    finally:

        storage.save(
            inventory
        )

        database.close()


if __name__ == "__main__":

    main()