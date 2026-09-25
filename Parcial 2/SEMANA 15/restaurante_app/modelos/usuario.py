from __future__ import annotations

from typing import Any


class Usuario:
    """Representa a un usuario autorizado para acceder a la aplicación."""

    def __init__(self, usuario: str, nombre: str, contrasena: str) -> None:
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía.")

        self.usuario: str = usuario.strip()
        self.nombre: str = nombre.strip()
        self.contrasena: str = contrasena.strip()

    def mostrar_informacion(self) -> str:
        return f"Usuario: {self.usuario} | Nombre: {self.nombre}"

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "usuario": self.usuario,
            "nombre": self.nombre,
            "contrasena": self.contrasena,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> "Usuario":
        try:
            return Usuario(
                usuario=datos["usuario"],
                nombre=datos["nombre"],
                contrasena=datos["contrasena"],
            )
        except KeyError as error:
            raise KeyError(f"Usuario incompleto: falta la clave {error}") from error
