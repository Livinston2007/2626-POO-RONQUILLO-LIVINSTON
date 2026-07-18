from __future__ import annotations
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente


def solicitar_numero(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


def registrar_producto(serv: Restaurante) -> None:
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = solicitar_numero("Precio: ")
    prod = Producto(codigo, nombre, categoria, precio)
    try:
        serv.registrar_producto(prod)
        print("Producto registrado.")
    except ValueError as e:
        print("Error:", e)


def registrar_bebida(serv: Restaurante) -> None:
    codigo = input("Código: ").strip()
    nombre = input("Nombre: ").strip()
    categoria = input("Categoría: ").strip()
    precio = solicitar_numero("Precio: ")
    tamano = input("Tamaño (p. ej. 500ml): ").strip()
    envase = input("Envase (botella/lata/vaso): ").strip()
    beb = Bebida(codigo, nombre, categoria, precio, tamano, envase)
    try:
        serv.registrar_producto(beb)
        print("Bebida registrada.")
    except ValueError as e:
        print("Error:", e)


def registrar_cliente(serv: Restaurante) -> None:
    identificacion = input("Identificación: ").strip()
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    cli = Cliente(identificacion, nombre, correo)
    try:
        serv.registrar_cliente(cli)
        print("Cliente registrado.")
    except ValueError as e:
        print("Error:", e)


def listar_productos(serv: Restaurante) -> None:
    productos = serv.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    print("\n== Productos ==")
    for info in productos:
        print(info)


def listar_clientes(serv: Restaurante) -> None:
    clientes = serv.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return
    print("\n== Clientes ==")
    for info in clientes:
        print(info)


def explicar_solid() -> None:
    """Muestra una explicación didáctica de los principios SOLID aplicada
    al diseño del sistema restaurante_app."""
    print("\n" + "="*12 + " Principios SOLID " + "="*12)
    print("\nS — Responsabilidad única (SRP):")
    print("  - Producto y Bebida: contienen sólo los datos y el método mostrar_informacion().")
    print("  - Cliente: representa únicamente los datos de un cliente.")
    print("  - Restaurante: gestiona el registro y listado de colecciones.")

    print("\nO — Abierto/Cerrado (OCP):")
    print("  - Bebida extiende Producto agregando atributos (p. ej. tamaño, envase) sin cambiar")
    print("    la lógica de Restaurante. Se amplía el sistema creando nuevas subclases en vez de")
    print("    modificar el servicio.")

    print("\nL — Sustitución de Liskov (LSP):")
    print("  - Donde se espera un Producto, puede usarse una Bebida. Restaurante llama a")
    print("    mostrar_informacion() en cada elemento, sin preguntar su tipo, por lo que el")
    print("    comportamiento se mantiene y no se introducen errores al sustituir subclases.")

    print("\nEjemplo práctico:")
    print("  - Registrar una Bebida: se crea un objeto Bebida (subclase de Producto) y se")
    print("    almacena en la misma lista de productos. Al listar, Restaurante ejecuta el")
    print("    método mostrar_informacion() de cada objeto y cada clase muestra sus datos")
    print("    de forma adecuada (polimorfismo).")

    print("\nConclusión:")
    print("  - Separando responsabilidades y diseñando extensiones mediante herencia adecuada,")
    print("    el sistema es más fácil de mantener y ampliar.")
    input("\nPresione Enter para continuar al menú...")


def menu() -> None:
    serv = Restaurante()
    opciones = {
        "1": registrar_producto,
        "2": registrar_bebida,
        "3": registrar_cliente,
        "4": listar_productos,
        "5": listar_clientes,
    }
    while True:
        print("\n" + "="*40)
        print("        SISTEMA DE RESTAURANTE")
        print("="*40)
        print("1. Registrar producto")
        print("2. Registrar bebida")
        print("3. Registrar cliente")
        print("-"*40)
        print("4. Listar productos")
        print("5. Listar clientes")
        print("-"*40)
        print("6. Salir")
        opcion = input("Seleccione una opción: ").strip()
        if opcion == "6":
            print("Saliendo...")
            break
        accion = opciones.get(opcion)
        if accion:
            accion(serv)
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu()
