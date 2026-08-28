from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante import Restaurante


def test_venta_exitosa() -> None:
    restaurante = Restaurante()
    restaurante.registrar_usuario(Usuario("1001", "Laura Gomez", "laura@email.com"))
    restaurante.registrar_producto(Producto("P001", "Hamburguesa", "Comidas", 15000, 10))

    resultado = restaurante.vender_producto("P001", "1001", 2)
    producto = restaurante.buscar_producto_por_codigo("P001")
    ventas = restaurante.consultar_ventas_por_usuario("1001")

    assert resultado is True
    assert producto is not None
    assert producto.stock == 8
    assert len(ventas) == 1
    assert ventas[0].producto_codigo == "P001"
    assert ventas[0].cantidad == 2


def test_venta_rechazada_por_stock() -> None:
    restaurante = Restaurante()
    restaurante.registrar_usuario(Usuario("1001", "Laura Gomez", "laura@email.com"))
    restaurante.registrar_producto(Producto("P001", "Hamburguesa", "Comidas", 15000, 3))

    resultado = restaurante.vender_producto("P001", "1001", 5)
    producto = restaurante.buscar_producto_por_codigo("P001")
    ventas = restaurante.consultar_ventas_por_usuario("1001")

    assert resultado is False
    assert producto is not None
    assert producto.stock == 3
    assert ventas == []


def main() -> None:
    test_venta_exitosa()
    test_venta_rechazada_por_stock()
    print("Pruebas del sistema Semana 11 completadas correctamente.")


if __name__ == "__main__":
    main()
