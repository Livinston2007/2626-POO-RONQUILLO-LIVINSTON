from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, TypeVar

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta

T = TypeVar("T")


class ArchivoServicio:
    """Centraliza la lectura y escritura JSON de productos, usuarios y ventas."""

    def __init__(self, carpeta_datos: str = "datos") -> None:
        self.carpeta_datos = Path(carpeta_datos)
        self.ruta_productos = self.carpeta_datos / "productos.json"
        self.ruta_usuarios = self.carpeta_datos / "usuarios.json"
        self.ruta_ventas = self.carpeta_datos / "ventas.json"

    def cargar_productos(self) -> list[Producto]:
        return self._cargar_lista(self.ruta_productos, Producto.desde_diccionario)

    def cargar_usuarios(self) -> list[Usuario]:
        return self._cargar_lista(self.ruta_usuarios, Usuario.desde_diccionario)

    def cargar_ventas(self) -> list[Venta]:
        return self._cargar_lista(self.ruta_ventas, Venta.desde_diccionario)

    def guardar_productos(self, productos: list[Producto]) -> None:
        self._guardar_lista(self.ruta_productos, [producto.a_diccionario() for producto in productos])

    def guardar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._guardar_lista(self.ruta_usuarios, [usuario.a_diccionario() for usuario in usuarios])

    def guardar_ventas(self, ventas: list[Venta]) -> None:
        self._guardar_lista(self.ruta_ventas, [venta.a_diccionario() for venta in ventas])

    def _cargar_lista(self, ruta: Path, constructor: Callable[[dict[str, Any]], T]) -> list[T]:
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"Archivo {ruta} no encontrado. Se inicia con una coleccion vacia.")
            return []
        except json.JSONDecodeError as error:
            print(f"El archivo {ruta} contiene JSON invalido: {error}")
            return []
        except PermissionError:
            print(f"No hay permisos para leer el archivo {ruta}.")
            raise

        if not isinstance(datos, list):
            raise ValueError(f"El archivo {ruta} debe contener una lista JSON.")

        objetos: list[T] = []
        for indice, item in enumerate(datos):
            try:
                if not isinstance(item, dict):
                    raise ValueError("El registro debe ser un diccionario.")
                objetos.append(constructor(item))
            except (KeyError, ValueError, TypeError) as error:
                print(f"Registro {indice} omitido en {ruta}: {error}")
        return objetos

    def _guardar_lista(self, ruta: Path, datos: list[dict[str, Any]]) -> None:
        try:
            ruta.parent.mkdir(parents=True, exist_ok=True)
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError:
            print(f"No hay permisos para escribir el archivo {ruta}.")
            raise
