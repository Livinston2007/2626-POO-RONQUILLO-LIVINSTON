from __future__ import annotations


class Producto:
    """Representa un producto del restaurante."""
    
    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        if float(precio) < 0:
            raise ValueError(f"El precio no puede ser negativo: {precio}")
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
