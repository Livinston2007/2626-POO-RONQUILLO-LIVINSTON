from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante


def solicitar_float(mensaje: str) -> float:
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un numero valido.")


def solicitar_entero(mensaje: str) -> int:
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Error: ingrese un numero entero valido.")


def registrar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\n--- Registrar producto ---")
    try:
        codigo = input("Codigo: ").strip()
        nombre = input("Nombre: ").strip()
        categoria = input("Categoria: ").strip()
        precio = solicitar_float("Precio: ")
        stock = solicitar_entero("Stock disponible: ")

        producto = Producto(codigo, nombre, categoria, precio, stock)
        restaurante.registrar_producto(producto)
        archivos.guardar_productos(restaurante.obtener_productos())
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"No se pudo registrar el producto: {error}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar producto ---")
    codigo = input("Codigo del producto: ").strip()
    producto = restaurante.buscar_producto_por_codigo(codigo)

    if producto is None:
        print("Producto no encontrado.")
    else:
        print(producto.mostrar_informacion())


def actualizar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\n--- Actualizar producto ---")
    codigo = input("Codigo del producto: ").strip()
    producto = restaurante.buscar_producto_por_codigo(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(producto.mostrar_informacion())
    print("Deje el campo vacio para conservar el valor actual.")

    nombre = input(f"Nuevo nombre ({producto.nombre}): ").strip()
    categoria = input(f"Nueva categoria ({producto.categoria}): ").strip()
    precio_texto = input(f"Nuevo precio ({producto.precio:.2f}): ").strip()
    stock_texto = input(f"Nuevo stock ({producto.stock}): ").strip()

    try:
        precio = float(precio_texto) if precio_texto else None
        stock = int(stock_texto) if stock_texto else None
        actualizado = restaurante.actualizar_producto(
            codigo=codigo,
            nombre=nombre or None,
            categoria=categoria or None,
            precio=precio,
            stock=stock,
        )

        if actualizado:
            archivos.guardar_productos(restaurante.obtener_productos())
            print("Producto actualizado correctamente.")
        else:
            print("No se pudo actualizar el producto.")
    except ValueError as error:
        print(f"No se pudo actualizar el producto: {error}")


def eliminar_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\n--- Eliminar producto ---")
    codigo = input("Codigo del producto: ").strip()
    producto = restaurante.buscar_producto_por_codigo(codigo)

    if producto is None:
        print("Producto no encontrado.")
        return

    print(producto.mostrar_informacion())
    confirmacion = input("Confirma eliminar este producto? (s/n): ").strip().lower()
    if confirmacion == "s" and restaurante.eliminar_producto(codigo):
        archivos.guardar_productos(restaurante.obtener_productos())
        print("Producto eliminado correctamente.")
    else:
        print("Operacion cancelada.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Productos registrados ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return

    for producto in productos:
        print(producto)
    print(f"Total: {restaurante.contar_productos()}")


def registrar_usuario(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\n--- Registrar usuario ---")
    try:
        identificacion = input("Identificacion: ").strip()
        nombre = input("Nombre: ").strip()
        correo = input("Correo: ").strip()

        usuario = Usuario(identificacion, nombre, correo)
        restaurante.registrar_usuario(usuario)
        archivos.guardar_usuarios(restaurante.obtener_usuarios())
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"No se pudo registrar el usuario: {error}")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Usuarios registrados ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return

    for usuario in usuarios:
        print(usuario)
    print(f"Total: {restaurante.contar_usuarios()}")


def vender_producto(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    print("\n--- Vender producto ---")
    identificacion = input("Identificacion del usuario: ").strip()
    codigo = input("Codigo del producto: ").strip()
    cantidad = solicitar_entero("Cantidad a vender: ")

    vendido = restaurante.vender_producto(codigo, identificacion, cantidad)
    if vendido:
        archivos.guardar_ventas(restaurante.obtener_ventas())
        archivos.guardar_productos(restaurante.obtener_productos())
        print("Venta registrada correctamente.")
    else:
        print("Venta rechazada. Verifique usuario, producto, cantidad y stock disponible.")


def consultar_ventas_usuario(restaurante: Restaurante) -> None:
    print("\n--- Consultar ventas por usuario ---")
    identificacion = input("Identificacion del usuario: ").strip()
    ventas = restaurante.consultar_ventas_por_usuario(identificacion)

    if not ventas:
        print("No hay ventas registradas para ese usuario.")
        return

    for venta in ventas:
        print(restaurante.describir_venta(venta))
    print(f"Total de ventas encontradas: {len(ventas)}")


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorias ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorias registradas.")
        return

    for categoria in sorted(categorias):
        print(f"- {categoria}")


def cargar_datos(restaurante: Restaurante, archivos: ArchivoServicio) -> None:
    productos = archivos.cargar_productos()
    usuarios = archivos.cargar_usuarios()
    ventas = archivos.cargar_ventas()

    restaurante.cargar_productos_iniciales(productos)
    restaurante.cargar_usuarios_iniciales(usuarios)
    restaurante.cargar_ventas_iniciales(ventas)

    print(
        f"Datos cargados: {len(productos)} producto(s), "
        f"{len(usuarios)} usuario(s), {len(ventas)} venta(s)."
    )


def menu() -> None:
    base_datos = Path(__file__).resolve().parent / "datos"
    archivos = ArchivoServicio(str(base_datos))
    restaurante = Restaurante()
    cargar_datos(restaurante, archivos)

    opciones = {
        "1": lambda: registrar_producto(restaurante, archivos),
        "2": lambda: buscar_producto(restaurante),
        "3": lambda: actualizar_producto(restaurante, archivos),
        "4": lambda: eliminar_producto(restaurante, archivos),
        "5": lambda: listar_productos(restaurante),
        "6": lambda: registrar_usuario(restaurante, archivos),
        "7": lambda: listar_usuarios(restaurante),
        "8": lambda: vender_producto(restaurante, archivos),
        "9": lambda: consultar_ventas_usuario(restaurante),
        "10": lambda: mostrar_categorias(restaurante),
    }

    while True:
        print("\n" + "=" * 42)
        print("          SISTEMA DE RESTAURANTE")
        print("=" * 42)
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("6. Registrar usuario")
        print("7. Listar usuarios")
        print("8. Vender producto")
        print("9. Consultar ventas por usuario")
        print("10. Mostrar categorias")
        print("0. Salir")
        print("=" * 42)

        try:
            opcion = input("Seleccione una opcion: ").strip()
        except EOFError:
            print("Hasta luego.")
            break
        if opcion == "0":
            print("Hasta luego.")
            break

        accion = opciones.get(opcion)
        if accion is None:
            print("Opcion no valida.")
            continue

        try:
            accion()
        except PermissionError:
            print("Operacion cancelada por falta de permisos sobre los archivos.")


if __name__ == "__main__":
    menu()
