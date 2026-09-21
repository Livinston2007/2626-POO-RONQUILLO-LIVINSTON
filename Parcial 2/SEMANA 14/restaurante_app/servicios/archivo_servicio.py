from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, TypeVar

try:
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.usuario import Usuario
except ImportError:  # pragma: no cover
    from modelos.producto import Producto
    from modelos.usuario import Usuario

T = TypeVar("T")


class ArchivoServicio:
    """Lee y guarda la información del restaurante en archivos JSON."""

    def __init__(self, carpeta_datos: str | Path | None = None) -> None:
        if carpeta_datos is None:
            base_dir = Path(__file__).resolve().parent.parent
            self.carpeta_datos = base_dir / "datos"
        else:
            self.carpeta_datos = Path(carpeta_datos)

        self.ruta_productos = self.carpeta_datos / "productos.json"
        self.ruta_usuarios = self.carpeta_datos / "usuarios.json"

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_lista(self.ruta_productos, Producto.desde_diccionario)

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_lista(self.ruta_usuarios, Usuario.desde_diccionario)

    def guardar_productos(self, productos: list[Producto]) -> None:
        self._guardar_lista(self.ruta_productos, [producto.a_diccionario() for producto in productos])

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._guardar_lista(self.ruta_usuarios, [usuario.a_diccionario() for usuario in usuarios])

    def _cargar_lista(self, ruta: Path, constructor: Callable[[dict[str, Any]], T]) -> list[T]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        if not isinstance(datos, list):
            raise ValueError(f"El archivo {ruta} debe contener una lista JSON.")

        objetos: list[T] = []
        for item in datos:
            if not isinstance(item, dict):
                continue
            try:
                objetos.append(constructor(item))
            except (KeyError, TypeError, ValueError):
                continue
        return objetos

    def _guardar_lista(self, ruta: Path, datos: list[dict[str, Any]]) -> None:
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)
