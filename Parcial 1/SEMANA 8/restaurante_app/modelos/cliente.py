from __future__ import annotations

class Cliente:
    """Representa a un cliente registrado."""
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    def mostrar_informacion(self) -> str:
        return f"[Cliente] ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
