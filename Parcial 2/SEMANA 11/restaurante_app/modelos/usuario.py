from __future__ import annotations

from typing import Any


class Usuario:
    """Representa a una persona registrada que puede realizar compras."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        if not identificacion.strip():
            raise ValueError("La identificacion del usuario no puede estar vacia.")
        if not nombre.strip():
            raise ValueError("El nombre del usuario no puede estar vacio.")
        if not correo.strip():
            raise ValueError("El correo del usuario no puede estar vacio.")

        self.identificacion: str = identificacion.strip()
        self.nombre: str = nombre.strip()
        self.correo: str = correo.strip()

    def mostrar_informacion(self) -> str:
        return (
            f"[Usuario] ID: {self.identificacion} | "
            f"Nombre: {self.nombre} | Correo: {self.correo}"
        )

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> Usuario:
        try:
            return Usuario(
                identificacion=datos["identificacion"],
                nombre=datos["nombre"],
                correo=datos["correo"],
            )
        except KeyError as error:
            raise KeyError(f"Usuario incompleto: falta la clave {error}") from error
