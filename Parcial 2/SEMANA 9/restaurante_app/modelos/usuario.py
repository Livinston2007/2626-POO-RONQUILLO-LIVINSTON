from __future__ import annotations


class Usuario:
    """Representa a un usuario (persona) registrado en el sistema."""
    
    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo
    
    def mostrar_informacion(self) -> str:
        """Devuelve una representación legible de la información del usuario."""
        return f"[Usuario] ID: {self.identificacion} | Nombre: {self.nombre} | Correo: {self.correo}"
