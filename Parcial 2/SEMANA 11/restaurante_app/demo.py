"""Demostracion simple del sistema de restaurante para Semana 11."""

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


def demo_interactiva() -> None:
    restaurante = Restaurante()

    restaurante.registrar_usuario(Usuario("1001", "Laura Gomez", "laura@email.com"))
    restaurante.registrar_usuario(Usuario("1002", "Carlos Ruiz", "carlos@email.com"))

    restaurante.registrar_producto(Producto("P001", "Hamburguesa", "Comidas", 15000, 10))
    restaurante.registrar_producto(Producto("B001", "Limonada", "Bebidas", 5000, 8))

    print("Productos iniciales:")
    for producto in restaurante.listar_productos():
        print(producto)

    print("\nVenta de 2 hamburguesas para usuario 1001:")
    if restaurante.vender_producto("P001", "1001", 2):
        print("Venta registrada correctamente.")
    else:
        print("Venta rechazada.")

    print("\nProductos despues de la venta:")
    for producto in restaurante.listar_productos():
        print(producto)

    print("\nVentas del usuario 1001:")
    for venta in restaurante.consultar_ventas_por_usuario("1001"):
        print(restaurante.describir_venta(venta))

    print("\nIntento de venta con stock insuficiente:")
    if restaurante.vender_producto("P001", "1001", 50):
        print("Venta registrada correctamente.")
    else:
        print("Venta rechazada por validaciones de usuario, producto, cantidad o stock.")


if __name__ == "__main__":
    demo_interactiva()
