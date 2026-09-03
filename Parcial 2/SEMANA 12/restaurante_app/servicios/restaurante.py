from __future__ import annotations

from typing import Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class Restaurante:
    """
    Administra colecciones y reglas de negocio del restaurante.

    Mantiene listas principales para almacenar, recorrer y persistir objetos,
    y utiliza índices en memoria (diccionarios) para optimizar búsquedas frecuentes.
    """

    def __init__(
        self,
        productos: list[Producto] | None = None,
        usuarios: list[Usuario] | None = None,
        ventas: list[Venta] | None = None,
    ) -> None:
        # Colecciones principales - se utilizan para almacenar, recorrer y persistir
        self._productos: list[Producto] = productos or []
        self._usuarios: list[Usuario] = usuarios or []
        self._ventas: list[Venta] = ventas or []

        # Índices auxiliares en memoria para optimizar búsquedas frecuentes
        # Diccionario: codigo -> Producto (búsquedas O(1) en lugar de O(n))
        self._indice_productos_por_codigo: dict[str, Producto] = {}

        # Diccionario: identificacion -> Usuario (búsquedas O(1) en lugar de O(n))
        self._indice_usuarios_por_id: dict[str, Usuario] = {}

        # Diccionario: usuario_id -> lista de Ventas (consultas O(1) en lugar de O(n))
        self._ventas_por_usuario: dict[str, list[Venta]] = {}

        # Reconstruir índices a partir de las colecciones cargadas
        self._reconstruir_indices()

    # ============================================================================
    # Métodos privados para mantener sincronizados los índices
    # ============================================================================

    def _reconstruir_indices(self) -> None:
        """Reconstruye todos los índices a partir de las colecciones principales.

        Se ejecuta al iniciar el programa para sincronizar los índices con los datos
        cargados desde JSON.
        """
        # Limpiar índices existentes
        self._indice_productos_por_codigo.clear()
        self._indice_usuarios_por_id.clear()
        self._ventas_por_usuario.clear()

        # Reconstruir índice de productos
        for producto in self._productos:
            self._indice_productos_por_codigo[producto.codigo] = producto

        # Reconstruir índice de usuarios
        for usuario in self._usuarios:
            self._indice_usuarios_por_id[usuario.identificacion] = usuario

        # Reconstruir índice de ventas por usuario
        for venta in self._ventas:
            if venta.usuario_id not in self._ventas_por_usuario:
                self._ventas_por_usuario[venta.usuario_id] = []
            self._ventas_por_usuario[venta.usuario_id].append(venta)

    def _actualizar_indice_producto(self, producto: Producto) -> None:
        """Agrega o actualiza un producto en el índice de códigos."""
        self._indice_productos_por_codigo[producto.codigo] = producto

    def _eliminar_indice_producto(self, codigo: str) -> None:
        """Elimina un producto del índice de códigos."""
        self._indice_productos_por_codigo.pop(codigo, None)

    def _actualizar_indice_usuario(self, usuario: Usuario) -> None:
        """Agrega o actualiza un usuario en el índice de identificaciones."""
        self._indice_usuarios_por_id[usuario.identificacion] = usuario

    def _eliminar_indice_usuario(self, identificacion: str) -> None:
        """Elimina un usuario del índice de identificaciones."""
        self._indice_usuarios_por_id.pop(identificacion, None)

    def _actualizar_indice_venta(self, venta: Venta) -> None:
        """Agrega una venta al índice de ventas por usuario."""
        if venta.usuario_id not in self._ventas_por_usuario:
            self._ventas_por_usuario[venta.usuario_id] = []
        self._ventas_por_usuario[venta.usuario_id].append(venta)

    # ============================================================================
    # Métodos para gestionar productos (con índices)
    # ============================================================================

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un nuevo producto en el sistema.

        Valida que no exista un producto con el mismo código antes de agregar.
        Mantiene el índice sincronizado.
        """
        if self.buscar_producto_por_codigo(producto.codigo) is not None:
            raise ValueError(f"Codigo de producto duplicado: {producto.codigo}")

        self._productos.append(producto)
        self._actualizar_indice_producto(producto)

    def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
        """Busca un producto utilizando el índice (O(1) en lugar de O(n)).

        Devuelve el producto si existe, None en caso contrario.
        """
        return self._indice_productos_por_codigo.get(codigo)

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> bool:
        """Actualiza los datos de un producto existente.

        El índice no requiere cambios si la búsqueda se hace por código
        y el código no cambia.
        """
        producto = self.buscar_producto_por_codigo(codigo)
        if producto is None:
            return False

        if nombre is not None:
            if not nombre.strip():
                raise ValueError("El nombre del producto no puede estar vacio.")
            producto.nombre = nombre.strip()
        if categoria is not None:
            if not categoria.strip():
                raise ValueError("La categoria del producto no puede estar vacia.")
            producto.categoria = categoria.strip()
        if precio is not None:
            if float(precio) < 0:
                raise ValueError("El precio del producto no puede ser negativo.")
            producto.precio = float(precio)
        if stock is not None:
            if int(stock) < 0:
                raise ValueError("El stock del producto no puede ser negativo.")
            producto.stock = int(stock)

        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto del sistema.

        Busca en la lista principal y elimina del índice.
        """
        for indice, producto in enumerate(self._productos):
            if producto.codigo == codigo:
                self._productos.pop(indice)
                self._eliminar_indice_producto(codigo)
                return True
        return False

    def listar_productos(self) -> list[str]:
        """Retorna una lista formateada de todos los productos."""
        return [producto.mostrar_informacion() for producto in self._productos]

    def obtener_categorias_unicas(self) -> set[str]:
        """Retorna las categorías únicas de todos los productos."""
        return {producto.categoria for producto in self._productos}

    # ============================================================================
    # Métodos para gestionar usuarios (con índices)
    # ============================================================================

    def registrar_usuario(self, usuario: Usuario) -> None:
        """Registra un nuevo usuario en el sistema.

        Valida que no exista un usuario con la misma identificación antes de agregar.
        Mantiene el índice sincronizado.
        """
        if self.buscar_usuario_por_identificacion(usuario.identificacion) is not None:
            raise ValueError(f"Identificacion de usuario duplicada: {usuario.identificacion}")

        self._usuarios.append(usuario)
        self._actualizar_indice_usuario(usuario)

    def buscar_usuario_por_identificacion(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario utilizando el índice (O(1) en lugar de O(n)).

        Devuelve el usuario si existe, None en caso contrario.
        """
        return self._indice_usuarios_por_id.get(identificacion)

    def eliminar_usuario(self, identificacion: str) -> bool:
        """Elimina un usuario del sistema.

        Busca en la lista principal y elimina del índice.
        """
        for indice, usuario in enumerate(self._usuarios):
            if usuario.identificacion == identificacion:
                self._usuarios.pop(indice)
                self._eliminar_indice_usuario(identificacion)
                return True
        return False

    def listar_usuarios(self) -> list[str]:
        """Retorna una lista formateada de todos los usuarios."""
        return [usuario.mostrar_informacion() for usuario in self._usuarios]

    # ============================================================================
    # Métodos para gestionar ventas (con índices por usuario)
    # ============================================================================

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int,
    ) -> bool:
        """Registra una venta si el usuario, producto y stock existen.

        Utiliza los índices para búsquedas rápidas.
        Mantiene la lista de ventas sincronizada con el índice de ventas por usuario.
        """
        usuario = self.buscar_usuario_por_identificacion(identificacion_usuario)
        producto = self.buscar_producto_por_codigo(codigo_producto)

        if usuario is None or producto is None:
            return False
        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        self._actualizar_indice_venta(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """Consulta las ventas de un usuario utilizando el índice (O(1) en lugar de O(n)).

        Retorna una lista de ventas (o lista vacía si no hay ventas).
        """
        return self._ventas_por_usuario.get(identificacion_usuario, [])

    def describir_venta(self, venta: Venta) -> str:
        """Retorna una descripción legible de una venta."""
        producto = self.buscar_producto_por_codigo(venta.producto_codigo)
        nombre_producto = producto.nombre if producto is not None else "Producto no encontrado"
        return (
            f"Usuario: {venta.usuario_id} | Producto: {venta.producto_codigo} - "
            f"{nombre_producto} | Cantidad: {venta.cantidad}"
        )

    # ============================================================================
    # Métodos de consulta general
    # ============================================================================

    def contar_productos(self) -> int:
        """Retorna la cantidad de productos registrados."""
        return len(self._productos)

    def contar_usuarios(self) -> int:
        """Retorna la cantidad de usuarios registrados."""
        return len(self._usuarios)

    def contar_ventas(self) -> int:
        """Retorna la cantidad de ventas registradas."""
        return len(self._ventas)

    # ============================================================================
    # Métodos para obtener colecciones (usadas para persistencia)
    # ============================================================================

    def obtener_productos(self) -> list[Producto]:
        """Retorna una copia de la lista de productos para persistencia."""
        return list(self._productos)

    def obtener_usuarios(self) -> list[Usuario]:
        """Retorna una copia de la lista de usuarios para persistencia."""
        return list(self._usuarios)

    def obtener_ventas(self) -> list[Venta]:
        """Retorna una copia de la lista de ventas para persistencia."""
        return list(self._ventas)

    # ============================================================================
    # Métodos para cargar datos iniciales (usados al iniciar desde JSON)
    # ============================================================================

    def cargar_productos_iniciales(self, productos: list[Producto]) -> None:
        """Carga los productos desde JSON y reconstruye los índices."""
        self._productos = productos
        self._reconstruir_indices()

    def cargar_usuarios_iniciales(self, usuarios: list[Usuario]) -> None:
        """Carga los usuarios desde JSON y reconstruye los índices."""
        self._usuarios = usuarios
        self._reconstruir_indices()

    def cargar_ventas_iniciales(self, ventas: list[Venta]) -> None:
        """Carga las ventas desde JSON y reconstruye los índices."""
        self._ventas = ventas
        self._reconstruir_indices()

    # ============================================================================
    # Métodos de información sobre los índices (para debugging)
    # ============================================================================

    def obtener_estado_indices(self) -> dict:
        """Retorna información sobre el estado de los índices.

        Útil para verificar que los índices estén sincronizados con las colecciones.
        """
        return {
            "productos_en_lista": len(self._productos),
            "productos_en_indice": len(self._indice_productos_por_codigo),
            "usuarios_en_lista": len(self._usuarios),
            "usuarios_en_indice": len(self._indice_usuarios_por_id),
            "ventas_totales": len(self._ventas),
            "usuarios_con_ventas": len(self._ventas_por_usuario),
        }

