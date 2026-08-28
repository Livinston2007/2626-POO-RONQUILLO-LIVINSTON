from __future__ import annotations

from typing import Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class Restaurante:
    """Administra colecciones y reglas de negocio del restaurante."""

    def __init__(
        self,
        productos: list[Producto] | None = None,
        usuarios: list[Usuario] | None = None,
        ventas: list[Venta] | None = None,
    ) -> None:
        self._productos: list[Producto] = productos or []
        self._usuarios: list[Usuario] = usuarios or []
        self._ventas: list[Venta] = ventas or []

    def registrar_producto(self, producto: Producto) -> None:
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            raise ValueError(f"Codigo de producto duplicado: {producto.codigo}")
        self._productos.append(producto)

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> bool:
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False

        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre del producto no puede estar vacio.")
            producto.nombre = nombre.strip()
        if categoria is not None:
            if not categoria.strip():
                raise ValueError("La categoria del producto no puede estar vacia.")
            producto.categoria = categoria.strip()
        if precio is not None:
            if float(precio) < 0:
                raise ValueError("El precio del producto no puede ser negativo.")
            producto.precio = float(precio)
        if stock is not None:
            if int(stock) < 0:
                raise ValueError("El stock del producto no puede ser negativo.")
            producto.stock = int(stock)

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        for indice, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                self._productos.pop(indice)
                return True
        return False

    def listar_productos(self) -> list[str]:
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_categorias_unicas(self) -> set[str]:
        return {producto.categoria for producto in self._productos}

    def registrar_usuario(self, usuario: Usuario) -> None:
        if self.buscar_usuario_por_identificacion(usuario.identificacion) is not None:
            raise ValueError(f"Identificacion de usuario duplicada: {usuario.identificacion}")
        self._usuarios.append(usuario)

    def buscar_usuario_por_identificacion(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None

    def eliminar_usuario(self, identificacion: str) -> bool:
        for indice, usuario in enumerate(self._usuarios):
            if usuario.identificacion == identificacion:
                self._usuarios.pop(indice)
                return True
        return False

    def listar_usuarios(self) -> list[str]:
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int,
    ) -> bool:
        usuario = self.buscar_usuario_por_identificacion(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if usuario is None or producto is None:
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        ventas_usuario: list[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id == identificacion_usuario:
                ventas_usuario.append(venta)
        return ventas_usuario

    def describir_venta(self, venta: Venta) -> str:
        producto = self.buscar_producto_por_codigo(venta.producto_codigo)
        nombre_producto = producto.nombre if producto is not None else "Producto no encontrado"
        return (
            f"Usuario: {venta.usuario_id} | Producto: {venta.producto_codigo} - "
            f"{nombre_producto} | Cantidad: {venta.cantidad}"
        )

    def contar_productos(self) -> int:
        return len(self._productos)

    def contar_usuarios(self) -> int:
        return len(self._usuarios)

    def contar_ventas(self) -> int:
        return len(self._ventas)

    def obtener_productos(self) -> list[Producto]:
        return list(self._productos)

    def obtener_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def obtener_ventas(self) -> list[Venta]:
        return list(self._ventas)

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        self._productos = productos

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        self._usuarios = usuarios

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        self._ventas = ventas
