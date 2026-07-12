"""
Servicio Restaurante
Administra listas de productos y clientes con métodos para registrar, listar y buscar.
"""
from typing import List, Optional
from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """Servicio que administra productos y clientes."""

    def __init__(self):
        # listas internas
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    # Métodos para productos
    def registrar_producto(self, producto: Producto) -> None:
        # Evitar duplicados por nombre (caso-insensible)
        if self.buscar_producto(producto.nombre) is not None:
            raise ValueError(f"Ya existe un producto con nombre '{producto.nombre}'.")
        self._productos.append(producto)

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    def buscar_producto(self, nombre: str) -> Optional[Producto]:
        nombre = (nombre or "").strip().lower()
        for p in self._productos:
            if p.nombre.lower() == nombre:
                return p
        return None

    # Métodos para clientes
    def registrar_cliente(self, cliente: Cliente) -> None:
        # Evitar duplicados por id
        if self.buscar_cliente(cliente.id_cliente) is not None:
            raise ValueError(f"Ya existe un cliente con id '{cliente.id_cliente}'.")
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[Cliente]:
        return list(self._clientes)

    def buscar_cliente(self, id_cliente: str) -> Optional[Cliente]:
        id_cliente = str(id_cliente).strip()
        for c in self._clientes:
            if c.id_cliente == id_cliente:
                return c
        return None

    # Métodos didácticos: precargar datos de ejemplo
    def precargar_ejemplos(self) -> None:
        # Añadir algunos productos y clientes de ejemplo para facilitar la interacción
        ejemplos_productos = [
            Producto("Ceviche", "Mariscos", 25.0, True),
            Producto("Lomo Saltado", "Plato Principal", 30.0, True),
            Producto("Inca Kola", "Bebida", 5.0, True),
        ]
        ejemplos_clientes = [
            Cliente("1", "Ana Pérez", "ana.perez@example.com"),
            Cliente("2", "Carlos Ruiz", "c.ruiz@example.com"),
        ]

        for p in ejemplos_productos:
            try:
                self.registrar_producto(p)
            except ValueError:
                pass

        for c in ejemplos_clientes:
            try:
                self.registrar_cliente(c)
            except ValueError:
                pass

