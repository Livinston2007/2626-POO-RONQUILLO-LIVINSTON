from __future__ import annotations

from typing import Any


class Venta:
    """Representa la relacion entre un usuario y un producto vendido."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        if not usuario_id.strip():
            raise ValueError("La identificacion del usuario no puede estar vacia.")
        if not producto_codigo.strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        if int(cantidad) <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")

        self.usuario_id: str = usuario_id.strip()
        self.producto_codigo: str = producto_codigo.strip()
        self.cantidad: int = int(cantidad)

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> Venta:
        try:
            return Venta(
                usuario_id=datos["usuario_id"],
                producto_codigo=datos["producto_codigo"],
                cantidad=datos["cantidad"],
            )
        except KeyError as error:
            raise KeyError(f"Venta incompleta: falta la clave {error}") from error

