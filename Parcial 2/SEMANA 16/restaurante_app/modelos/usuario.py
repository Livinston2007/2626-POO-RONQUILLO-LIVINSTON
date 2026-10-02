from __future__ import annotations

from typing import Any


class Usuario:
    """Representa a un usuario autorizado para acceder a la aplicación."""

    ROLES_PERMITIDOS = ("Administrador", "Empleado", "Cliente")

    def __init__(
        self,
        usuario: str,
        nombre: str,
        contrasena: str,
        identificacion: str | None = None,
        rol: str = "Cliente",
    ) -> None:
        if not usuario.strip():
            raise ValueError("El usuario no puede estar vacío.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not contrasena.strip():
            raise ValueError("La contraseña no puede estar vacía.")

        identificacion_normalizada = (identificacion or usuario).strip()
        if not identificacion_normalizada:
            raise ValueError("La identificación del usuario no puede estar vacía.")

        self.usuario: str = usuario.strip()
        self.nombre: str = nombre.strip()
        self.contrasena: str = contrasena.strip()
        self.identificacion: str = identificacion_normalizada
        self.rol: str = self._normalizar_rol(rol)

    @staticmethod
    def _normalizar_rol(rol: str | None) -> str:
        valor = (rol or "Cliente").strip()
        texto = valor.lower()
        if texto in {"admin", "administrador"}:
            return "Administrador"
        if texto in {"empleado", "employee"}:
            return "Empleado"
        if texto in {"cliente", "client", "usuario"}:
            return "Cliente"
        raise ValueError(f"El rol {rol} no es válido. Roles permitidos: {', '.join(Usuario.ROLES_PERMITIDOS)}")

    def mostrar_informacion(self) -> str:
        return f"Identificación: {self.identificacion} | Usuario: {self.usuario} | Nombre: {self.nombre} | Rol: {self.rol}"

    def a_diccionario(self) -> dict[str, Any]:
        return {
            "identificacion": self.identificacion,
            "usuario": self.usuario,
            "nombre": self.nombre,
            "contrasena": self.contrasena,
            "rol": self.rol,
        }

    @staticmethod
    def desde_diccionario(datos: dict[str, Any]) -> "Usuario":
        try:
            identificacion = datos.get("identificacion") or datos.get("usuario")
            rol = datos.get("rol", "Cliente")
            return Usuario(
                usuario=datos["usuario"],
                nombre=datos["nombre"],
                contrasena=datos["contrasena"],
                identificacion=identificacion,
                rol=rol,
            )
        except KeyError as error:
            raise KeyError(f"Usuario incompleto: falta la clave {error}") from error
