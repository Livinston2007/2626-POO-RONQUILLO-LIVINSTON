class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []  # Lista para administrar los productos registrados

    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado exitosamente al restaurante '{self.nombre}'.")

    def mostrar_menu(self):
        """Muestra la información de todos los productos del restaurante."""
        print(f"\n--- Menú de {self.nombre} ---")
        if not self.productos:
            print("No hay productos registrados en el menú por el momento.")
        else:
            for producto in self.productos:
                # Polimorfismo en acción:
                # Cada objeto (Platillo o Bebida) responde a mostrar_informacion() a su manera
                print(producto.mostrar_informacion())
        print("----------------------------\n")
