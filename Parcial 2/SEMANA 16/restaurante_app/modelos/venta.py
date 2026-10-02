from __future__ import annotations

from datetime import datetime
from typing import Any


class Venta:
    """Representa la relación entre un usuario y un producto en una operación de venta."""

    def __init__(self, usuario: str, producto_codigo: str, fecha: str | None = None) -> None:
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío.")
        if not producto_codigo.strip():
            raise ValueError("El código del producto no puede estar vacío.")

        self.usuario: str = usuario.strip()
        self.producto_codigo: str = producto_codigo.strip()
        self.fecha: str = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "usuario": self.usuario,
            "producto_codigo": self.producto_codigo,
            "fecha": self.fecha,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> "Venta":
        try:
            return Venta(
                usuario=datos["usuario"],
                producto_codigo=datos["producto_codigo"],
                fecha=datos.get("fecha"),
            )
        except KeyError as error:
            raise KeyError(f"Venta incompleta: falta la clave {error}") from error
