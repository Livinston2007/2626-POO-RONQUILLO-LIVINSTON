from __future__ import annotations
from typing import Dict, Any


class Producto:
    """Representa un producto del restaurante."""
    
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = float(precio)
    
    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible del producto."""
        return (
            f"[Producto] Código: {self.codigo} | Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}"
        )
    
    def a_diccionario(self) -> Dict[str, Any]:
        """Convierte el objeto Producto a un diccionario para serialización JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": float(self.precio)
        }
    
    @staticmethod
    def desde_diccionario(datos: Dict[str, Any]) -> Producto:
        """Crea un objeto Producto a partir de un diccionario (deserialización JSON)."""
        try:
            codigo = datos["codigo"]
            nombre = datos["nombre"]
            categoria = datos["categoria"]
            precio = datos["precio"]
            return Producto(codigo, nombre, categoria, precio)
        except KeyError as e:
            raise ValueError(f"Producto incompleto en JSON: falta la clave {e}")
