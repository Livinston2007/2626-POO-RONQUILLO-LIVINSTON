from pathlib import Path

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante


def test_persistencia_completa() -> None:
    carpeta = Path("datos_test")
    archivos = ArchivoServicio(str(carpeta))

    restaurante = Restaurante()
    restaurante.registrar_usuario(Usuario("2002", "Mateo Ruiz", "mateo@email.com"))
    restaurante.registrar_producto(Producto("B001", "Limonada", "Bebidas", 5000, 6))
    assert restaurante.vender_producto("B001", "2002", 2)

    archivos.guardar_productos(restaurante.obtener_productos())
    archivos.guardar_usuarios(restaurante.obtener_usuarios())
    archivos.guardar_ventas(restaurante.obtener_ventas())

    restaurante_cargado = Restaurante(
        productos=archivos.cargar_productos(),
        usuarios=archivos.cargar_usuarios(),
        ventas=archivos.cargar_ventas(),
    )

    producto = restaurante_cargado.buscar_producto_por_codigo("B001")
    ventas = restaurante_cargado.consultar_ventas_por_usuario("2002")

    assert producto is not None
    assert producto.stock == 4
    assert restaurante_cargado.buscar_usuario_por_identificacion("2002") is not None
    assert len(ventas) == 1
    assert ventas[0].cantidad == 2

    for archivo in carpeta.glob("*.json"):
        archivo.unlink()
    carpeta.rmdir()


def main() -> None:
    test_persistencia_completa()
    print("Prueba de persistencia Semana 11 completada correctamente.")


if __name__ == "__main__":
    main()
