"""
Smart Inventory

Console display.
"""

import os


MENU_WIDTH = 42


def clear_screen():
    os.system("cls")


def print_header(title):

    clear_screen()

    print("=" * MENU_WIDTH)
    print(title.center(MENU_WIDTH))
    print("=" * MENU_WIDTH)
    print()


def pause():
    input("\nPresione ENTER para continuar...")