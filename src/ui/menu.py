"""
Smart Inventory

Console menu.
"""

from src.services.product_service import ProductService
from src.services.product_manager import ProductManager
from src.services.search_service import SearchService
from src.services.exceptions import DuplicateProductError


class Menu:

    def __init__(self, inventory):

        self.inventory = inventory
        self.product_service = ProductService(inventory)
        self.product_manager = ProductManager(inventory)
        self.search_service = SearchService(inventory)


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
6. Modificar producto
0. Salir
""")

            option = input(
                "Seleccione una opción: "
            )


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


            elif option == "6":

                self.update_product()


            elif option == "0":

                print(
                    "\nCerrando Smart Inventory..."
                )

                break


            else:

                print(
                    "\nOpción inválida."
                )



    # ==========================
    # INPUT VALIDATIONS
    # ==========================


    def _get_required_text(self, message):

        while True:

            value = input(
                message
            ).strip()


            if value:

                return value


            print(
                "Este campo es obligatorio."
            )



    def _get_positive_float(self, message):

        while True:

            try:

                value = float(
                    input(message)
                )


                if value < 0:

                    print(
                        "El valor no puede ser negativo."
                    )

                    continue


                return value


            except ValueError:

                print(
                    "Ingrese un número válido."
                )



    def _get_optional_float(self, message):

        while True:

            value = input(
                message
            ).strip()


            if value == "":

                return None


            try:

                value = float(value)


                if value < 0:

                    print(
                        "El valor no puede ser negativo."
                    )

                    continue


                return value


            except ValueError:

                print(
                    "Ingrese un número válido."
                )



    # ==========================
    # CREATE PRODUCT
    # ==========================


    def create_product(self):

        print(
            "\n=== Crear producto ==="
        )


        name = self._get_required_text(
            "Nombre: "
        )


        print("""
Categoría del producto:

1. Producto con código de barras
2. Producto propio
3. Venta por Kg. o Unidad
""")


        option = input(
            "Seleccione una opción: "
        )


        if option == "1":

            product_category = "purchased"


        elif option == "2":

            product_category = "manufactured"


        elif option == "3":

            product_category = "loose"


        else:

            print(
                "\nOpción inválida."
            )

            return



        identifier = None
        unit_type = "unit"



        if product_category == "purchased":

            identifier = self._get_required_text(
                "Código de barras: "
            )



        if product_category == "loose":

            print("""
Unidad de venta:

1. Unidad
2. Kilogramo
""")


            unit_option = input(
                "Seleccione una opción: "
            )


            if unit_option == "1":

                unit_type = "unit"


            elif unit_option == "2":

                unit_type = "kg"


            else:

                print(
                    "\nOpción inválida."
                )

                return



        brand = input(
            "Marca (opcional): "
        ).strip()



        if product_category == "loose":

            cost = self._get_optional_float(
                "Costo (opcional): "
            )

        else:

            cost = self._get_positive_float(
                "Costo: "
            )



        if product_category == "purchased":

            price = None

        else:

            price = self._get_positive_float(
                "Precio de venta: "
            )



        try:

            product = self.product_service.create_product(
                name=name,
                product_category=product_category,
                identifier=identifier,
                cost=cost,
                price=price,
                brand=brand,
                unit_type=unit_type,
            )


            print(
                "\nProducto creado correctamente."
            )


            if product.identifier:

                print(
                    f"Identificador: {product.identifier}"
                )


            print(
                f"Precio venta: ${product.price:.0f}"
            )



        except DuplicateProductError as error:

            product = error.product


            print(
                "\nProducto existente encontrado:"
            )


            self._print_product(
                product
            )


            option = input(
                "\n¿Desea modificar este producto? (s/n): "
            ).lower()


            if option == "s":

                self.update_product(
                    product
                )



        except ValueError as error:

            print(
                f"\nError: {error}"
            )



    # ==========================
    # UPDATE PRODUCT
    # ==========================


    def update_product(self, product=None):

        print(
            "\n=== Modificar producto ==="
        )


        if product is None:

            identifier = self._get_required_text(
                "Código / Identificador: "
            )


            product = (
                self.product_manager.get_product_by_identifier(
                    identifier
                )
            )


            if product is None:

                print(
                    "\nProducto no encontrado."
                )

                return



        print(
            "Deje vacío para mantener el valor actual."
        )


        name = input(
            f"Nombre [{product.name}]: "
        ).strip()


        brand = input(
            f"Marca [{product.brand or '-'}]: "
        ).strip()


        cost = input(
            f"Costo [{product.cost}]: "
        ).strip()


        price = input(
            f"Precio [{product.price}]: "
        ).strip()



        cost = (
            float(cost)
            if cost
            else None
        )


        price = (
            float(price)
            if price
            else None
        )



        updated = self.product_manager.update_product(
            product,
            name=name if name else None,
            brand=brand if brand else None,
            cost=cost,
            price=price,
        )


        if updated:

            print(
                "\nProducto actualizado correctamente."
            )

        else:

            print(
                "\nNo fue posible actualizar el producto."
            )



    # ==========================
    # INVENTORY
    # ==========================


    def show_inventory(self):

        print(
            "\n=== Inventario ==="
        )


        products = (
            self.product_manager.get_products()
        )


        if not products:

            print(
                "No hay productos registrados."
            )

            return



        for product in products:

            self._print_product(
                product
            )



    def search_product(self):

        print(
            "\n=== Buscar producto ==="
        )


        name = self._get_required_text(
            "Nombre: "
        )


        results = (
            self.search_service.search_by_name(
                name
            )
        )


        if not results:

            print(
                "No se encontraron productos."
            )

            return



        for product in results:

            self._print_product(
                product
            )



    def add_stock(self):

        print(
            "\n=== Ingresar stock ==="
        )


        identifier = self._get_required_text(
            "Código / Identificador: "
        )


        quantity = int(
            self._get_positive_float(
                "Cantidad: "
            )
        )


        result = self.product_manager.update_stock(
            identifier,
            quantity,
        )


        if result:

            print(
                "\nStock actualizado correctamente."
            )

        else:

            print(
                "\nIdentificador inexistente o cantidad inválida."
            )



    def sell_product(self):

        print(
            "\n=== Registrar venta ==="
        )


        identifier = self._get_required_text(
            "Código / Identificador: "
        )


        quantity = int(
            self._get_positive_float(
                "Cantidad vendida: "
            )
        )


        result = self.product_manager.decrease_stock(
            identifier,
            quantity,
        )


        if result:

            print(
                "\nVenta registrada correctamente."
            )

        else:

            print(
                "\nIdentificador inexistente, cantidad inválida o stock insuficiente."
            )



    # ==========================
    # DISPLAY
    # ==========================


    def _print_product(self, product):

        print(
            "-" * 42
        )

        print(
            f"Categoría     : {product.product_category}"
        )

        print(
            f"Identificación: {product.identification_type}"
        )

        print(
            f"Código        : {product.identifier or '-'}"
        )

        print(
            f"Nombre        : {product.name}"
        )

        print(
            f"Marca         : {product.brand or '-'}"
        )

        print(
            f"Unidad        : {product.unit_type}"
        )


        if product.cost is None:

            print(
                "Costo         : Pendiente"
            )

        else:

            print(
                f"Costo         : ${product.cost:.0f}"
            )


        print(
            f"Precio        : ${product.price:.0f}"
        )

        print(
            f"Stock         : {product.stock}"
        )