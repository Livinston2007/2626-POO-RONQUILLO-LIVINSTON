from __future__ import annotations
import json
from pathlib import Path
from typing import List, Dict, Any
from restaurante_app.modelos.producto import Producto


class ArchivoServicio:
    """Servicio responsable de la persistencia de productos en archivo JSON."""
    
    def __init__(self, ruta_archivo: str = "datos/productos.json") -> None:
        """
        Inicializa el servicio de archivo.
        
        Args:
            ruta_archivo: Ruta del archivo JSON (relativa a la ejecución de main.py)
        """
        self.ruta_archivo: str = ruta_archivo
        self.ruta_path: Path = Path(ruta_archivo)
    
    def cargar_productos(self) -> List[Producto]:
        """
        Carga los productos desde el archivo JSON.
        
        Returns:
            Lista de objetos Producto cargados desde el archivo.
            Si el archivo no existe, retorna una lista vacía.
        
        Raises:
            FileNotFoundError: Si el archivo no existe (manejado internamente).
            json.JSONDecodeError: Si el archivo contiene JSON inválido.
            PermissionError: Si no hay permisos de lectura.
            ValueError: Si un registro en JSON es inválido.
        """
        try:
            with open(self.ruta_path, 'r', encoding='utf-8') as archivo:
                datos = json.load(archivo)
        except FileNotFoundError:
            print(f"ℹ Archivo {self.ruta_archivo} no encontrado. Iniciando con colección vacía.\n")
            return []
        except json.JSONDecodeError as e:
            print(f"✗ Error: El archivo {self.ruta_archivo} contiene JSON inválido: {e}\n")
            raise
        except PermissionError:
            print(f"✗ Error: Permisos insuficientes para leer {self.ruta_archivo}\n")
            raise
        
        # Validar que es una lista
        if not isinstance(datos, list):
            print(f"✗ Error: El archivo JSON debe contener una lista de productos.\n")
            raise ValueError("Estructura JSON inválida: se esperaba una lista")
        
        # Convertir cada diccionario a objeto Producto
        productos: List[Producto] = []
        for i, item in enumerate(datos):
            try:
                producto = Producto.desde_diccionario(item)
                productos.append(producto)
            except (ValueError, TypeError) as e:
                print(f"✗ Advertencia: Producto en posición {i} no puede ser cargado ({e}). Se omite.\n")
                continue
        
        return productos
    
    def guardar_productos(self, productos: List[Producto]) -> None:
        """
        Guarda la lista de productos en el archivo JSON.
        
        Args:
            productos: Lista de objetos Producto a guardar.
        
        Raises:
            PermissionError: Si no hay permisos de escritura.
        """
        try:
            # Crear directorio si no existe
            self.ruta_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Convertir objetos a diccionarios
            datos: List[Dict[str, Any]] = [p.a_diccionario() for p in productos]
            
            # Guardar en JSON
            with open(self.ruta_path, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError:
            print(f"✗ Error: Permisos insuficientes para escribir en {self.ruta_archivo}\n")
            raise
