"""
Smart Inventory

Application entry point.
"""

from src.core.inventory import Inventory
from src.ui.menu import Menu


def main():

    inventory = Inventory()

    menu = Menu(inventory)

    menu.show()


if __name__ == "__main__":
    main() 