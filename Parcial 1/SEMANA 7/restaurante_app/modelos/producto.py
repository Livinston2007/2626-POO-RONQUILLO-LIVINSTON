"""
Modelo Producto
Implementa constructor tradicional y propiedades con getters/setters
"""

class Producto:
    """Clase que representa un producto del restaurante.

    Atributos:
        _nombre (str)
        _categoria (str)
        _precio (float)
        _disponible (bool)
    """

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        # Usamos setters para validar
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    # nombre
    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor

    # categoria
    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        valor = (valor or "").strip()
        if not valor:
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor

    # precio
    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        try:
            precio = float(valor)
        except (TypeError, ValueError):
            raise ValueError("El precio debe ser un número mayor que cero.")
        if precio <= 0:
            raise ValueError("El precio del producto debe ser mayor que cero.")
        self._precio = precio

    # disponible
    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> str:
        """Retorna una representación legible del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Nombre: {self.nombre} | Categoría: {self.categoria} | Precio: S/ {self.precio:.2f} | {estado}"

    def __repr__(self):
        return f"Producto(nombre={self.nombre!r}, categoria={self.categoria!r}, precio={self.precio!r}, disponible={self.disponible!r})"

