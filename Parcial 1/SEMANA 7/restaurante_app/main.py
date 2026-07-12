"""
Punto de entrada del sistema de restaurante (SEMANA 7).
Muestra un menú interactivo por consola para registrar, listar y buscar productos y clientes.
"""
from servicios.restaurante import Restaurante
from modelos.producto import Producto
from modelos.cliente import Cliente


def mostrar_menu() -> None:
    print("\n" + "=" * 40)
    print("\tSISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("-" * 40)
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("-" * 40)
    print("7. Salir")


def solicitar_producto() -> Producto:
    print("\nRegistrar nuevo producto")
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio_raw = input("Precio (ej: 12.50): ").strip()
    disponible_raw = input("¿Disponible? (s/n) [s]: ").strip().lower() or "s"
    disponible = disponible_raw.startswith("s")
    # Constructor validará los datos
    producto = Producto(nombre, categoria, precio_raw, disponible)
    return producto


def solicitar_cliente() -> Cliente:
    print("\nRegistrar nuevo cliente")
    id_cliente = input("ID cliente: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    cliente = Cliente(id_cliente, nombre, correo)
    return cliente


def main():
    servicio = Restaurante()
    servicio.precargar_ejemplos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                p = solicitar_producto()
                servicio.registrar_producto(p)
                print("Producto registrado con éxito:")
                print(p.mostrar_informacion())
            except Exception as e:
                print(f"Error al registrar producto: {e}")

        elif opcion == "2":
            productos = servicio.listar_productos()
            print(f"\nListado de productos ({len(productos)}):")
            for prod in productos:
                print(" -", prod.mostrar_informacion())

        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
            p = servicio.buscar_producto(nombre)
            if p:
                print("Producto encontrado:")
                print(p.mostrar_informacion())
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            try:
                c = solicitar_cliente()
                servicio.registrar_cliente(c)
                print("Cliente registrado con éxito:")
                print(c.mostrar_informacion())
            except Exception as e:
                print(f"Error al registrar cliente: {e}")

        elif opcion == "5":
            clientes = servicio.listar_clientes()
            print(f"\nListado de clientes ({len(clientes)}):")
            for cli in clientes:
                print(" -", cli.mostrar_informacion())

        elif opcion == "6":
            id_buscar = input("Ingrese el ID del cliente a buscar: ").strip()
            c = servicio.buscar_cliente(id_buscar)
            if c:
                print("Cliente encontrado:")
                print(c.mostrar_informacion())
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    # Ejecutar el programa
    main()

