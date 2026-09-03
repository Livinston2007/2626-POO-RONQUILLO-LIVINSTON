from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        stock: int,
    ) -> None:
        if not codigo.strip():
            raise ValueError("El codigo del producto no puede estar vacio.")
        if not nombre.strip():
            raise ValueError("El nombre del producto no puede estar vacio.")
        if not categoria.strip():
            raise ValueError("La categoria del producto no puede estar vacia.")
        if float(precio) < 0:
            raise ValueError("El precio del producto no puede ser negativo.")
        if int(stock) < 0:
            raise ValueError("El stock del producto no puede ser negativo.")

        self.codigo: str = codigo.strip()
        self.nombre: str = nombre.strip()
        self.categoria: str = categoria.strip()
        self.precio: float = float(precio)
        self.stock: int = int(stock)

    def vender(self, cantidad: int) -> None:
        if cantidad <= 0:
            raise ValueError("La cantidad vendida debe ser mayor que cero.")
        if cantidad > self.stock:
            raise ValueError("No hay stock suficiente para vender esa cantidad.")

        self.stock -= cantidad

    def mostrar_informacion(self) -> str:
        return (
            f"[Producto] Codigo: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoria: {self.categoria} | Precio: ${self.precio:.2f} | "
            f"Stock: {self.stock}"
        )

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> Producto:
        try:
            return Producto(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=datos["precio"],
                stock=datos["stock"],
            )
        except KeyError as error:
            raise KeyError(f"Producto incompleto: falta la clave {error}") from error

