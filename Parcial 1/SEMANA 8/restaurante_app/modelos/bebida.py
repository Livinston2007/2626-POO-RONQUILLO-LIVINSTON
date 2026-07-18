from __future__ import annotations
from .producto import Producto

class Bebida(Producto):
    """Especialización de Producto para bebidas."""
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamano: str, envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamano: str = tamano
        self.envase: str = envase

    def mostrar_informacion(self) -> str:
        base = super().mostrar_informacion()
        return f"{base} | Tamaño: {self.tamano} | Envase: {self.envase}"
