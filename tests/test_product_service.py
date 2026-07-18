"""
Smart Inventory

Product service test.
"""

from src.core.inventory import Inventory
from src.services.product_service import ProductService


def main():

    print("=== Product Service Test ===")


    # Create inventory
    inventory = Inventory()


    # Create service
    product_service = ProductService(inventory)


    # Create purchased product
    product = product_service.create_product(
        name="Coca Cola 1.5L",
        product_type="purchased",
        cost=900,
        brand="Coca Cola",
        stock=24
    )


    print("\nProduct created:")
    print("----------------")
    print(f"Code: {product.code}")
    print(f"Name: {product.name}")
    print(f"Brand: {product.brand}")
    print(f"Type: {product.product_type}")
    print(f"Cost: {product.cost}")
    print(f"Price: {product.price}")
    print(f"Stock: {product.stock}")


    print("\nInventory:")
    print("-----------")


    for item in inventory.get_products():
        print(
            f"{item.code} - "
            f"{item.name}"
        )


if __name__ == "__main__":
    main()