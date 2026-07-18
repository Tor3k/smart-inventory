"""
Smart Inventory

Console menu.
"""

from src.services.product_service import ProductService


class Menu:

    def __init__(self, inventory):

        self.inventory = inventory
        self.product_service = ProductService(inventory)


    def show(self):

        while True:

            print("\n" + "=" * 42)
            print("SMART INVENTORY".center(42))
            print("=" * 42)

            print("""
1. Crear producto
2. Mostrar inventario
3. Buscar producto
4. Ingresar stock
5. Registrar venta
0. Salir
""")

            option = input("Seleccione una opción: ")

            if option == "1":
                self.create_product()

            elif option == "2":
                self.show_inventory()

            elif option == "3":
                self.search_product()

            elif option == "4":
                self.add_stock()

            elif option == "5":
                self.sell_product()

            elif option == "0":
                print("\nCerrando Smart Inventory...")
                break

            else:
                print("\nOpción inválida.")


    def create_product(self):

        print("\n=== Crear producto ===")

        name = input("Nombre: ")

        product_type = input(
            "Tipo (purchased/manufactured): "
        ).lower()

        cost = float(
            input("Costo: ")
        )

        brand = input(
            "Marca (opcional): "
        )

        try:

            product = self.product_service.create_product(
                name=name,
                product_type=product_type,
                cost=cost,
                brand=brand
            )

            print("\nProducto creado correctamente.")
            print(f"Código: {product.code}")

        except ValueError as error:

            print(f"\nError: {error}")


    def show_inventory(self):

        print("\n=== Inventario ===")

        products = self.inventory.get_products()

        if not products:
            print("No hay productos registrados.")
            return

        for product in products:

            print("-" * 42)
            print(f"Código : {product.code}")
            print(f"Nombre : {product.name}")
            print(f"Marca  : {product.brand or '-'}")
            print(f"Tipo   : {product.product_type}")
            print(f"Costo  : ${product.cost:.0f}")
            print(f"Precio : ${product.price:.0f}")
            print(f"Stock  : {product.stock}")


    def search_product(self):

        print("\n=== Buscar producto ===")

        name = input("Nombre: ")

        results = self.inventory.find_by_name(name)

        if not results:
            print("No se encontraron productos.")
            return

        for product in results:

            print("-" * 42)
            print(f"Código : {product.code}")
            print(f"Nombre : {product.name}")
            print(f"Marca  : {product.brand or '-'}")
            print(f"Tipo   : {product.product_type}")
            print(f"Costo  : ${product.cost:.0f}")
            print(f"Precio : ${product.price:.0f}")
            print(f"Stock  : {product.stock}")


    def add_stock(self):

        print("\n=== Ingresar stock ===")

        code = input("Código del producto: ")

        quantity = int(
            input("Cantidad: ")
        )

        result = self.inventory.add_stock(
            code,
            quantity
        )

        if result:
            print("\nStock actualizado correctamente.")

        else:
            print("\nNo fue posible actualizar el stock.")


    def sell_product(self):

        print("\n=== Registrar venta ===")

        code = input("Código del producto: ")

        quantity = int(
            input("Cantidad vendida: ")
        )

        result = self.inventory.remove_stock(
            code,
            quantity
        )

        if result:
            print("\nVenta registrada correctamente.")

        else:
            print(
                "\nNo fue posible registrar la venta."
            )