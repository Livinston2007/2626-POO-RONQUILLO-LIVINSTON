"""
Modelo Cliente usando dataclass
"""
from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa un cliente del restaurante.

    Atributos:
        id_cliente: identificador único del cliente (int o str)
        nombre: nombre completo
        correo: correo electrónico
    """
    id_cliente: str
    nombre: str
    correo: str

    def __post_init__(self):
        # Normalizar algunos campos
        self.id_cliente = str(self.id_cliente).strip()
        self.nombre = (self.nombre or "").strip()
        self.correo = (self.correo or "").strip()

    def __repr__(self):
        return f"Cliente(id_cliente={self.id_cliente!r}, nombre={self.nombre!r}, correo={self.correo!r})"

    def mostrar_informacion(self) -> str:
        return f"ID: {self.id_cliente} | Nombre: {self.nombre} | Correo: {self.correo}"

