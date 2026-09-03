from __future__ import annotations
from typing import List, Optional, Set
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class Restaurante:
    """Servicio que administra las colecciones de productos y usuarios del restaurante."""
    
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []
    
    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto si su código no está duplicado."""
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"Código de producto duplicado: {producto.codigo}")
        self._productos.append(producto)
    
    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código. Retorna el producto o None si no existe."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None
    
    def actualizar_producto(self, codigo: str, nombre: str = None, 
                          categoria: str = None, precio: float = None) -> bool:
        """Actualiza los datos de un producto. Retorna True si fue exitoso, False si no existe."""
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False
        
        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            try:
                precio_float = float(precio)
                if precio_float < 0:
                    raise ValueError("El precio no puede ser negativo")
                producto.precio = precio_float
            except ValueError as e:
                raise ValueError(f"Precio inválido: {e}")
        
        return True
    
    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código. Retorna True si fue exitoso, False si no existe."""
        for i, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                self._productos.pop(i)
                return True
        return False
    
    def listar_productos(self) -> List[str]:
        """Devuelve la información de todos los productos como lista de strings."""
        return [p.mostrar_informacion() for p in self._productos]
    
    def obtener_categorias_unicas(self) -> Set[str]:
        """Retorna un conjunto con las categorías únicas de los productos registrados."""
        return {p.categoria for p in self._productos}
    
    def registrar_usuario(self, usuario: Usuario) -> None:
        """Registra un usuario si su identificación no está duplicada."""
        if any(u.identificacion == usuario.identificacion for u in self._usuarios):
            raise ValueError(f"Identificación de usuario duplicada: {usuario.identificacion}")
        self._usuarios.append(usuario)
    
    def buscar_usuario_por_identificacion(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación. Retorna el usuario o None si no existe."""
        for usuario in self._usuarios:
            if usuario.identificacion == identificacion:
                return usuario
        return None
    
    def listar_usuarios(self) -> List[str]:
        """Devuelve la información de todos los usuarios como lista de strings."""
        return [u.mostrar_informacion() for u in self._usuarios]
    
    def contar_productos(self) -> int:
        """Retorna la cantidad de productos registrados."""
        return len(self._productos)
    
    def contar_usuarios(self) -> int:
        """Retorna la cantidad de usuarios registrados."""
        return len(self._usuarios)
