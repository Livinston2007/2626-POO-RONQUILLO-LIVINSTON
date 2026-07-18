from __future__ import annotations
from typing import List
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.cliente import Cliente

class Restaurante:
    """Servicio que administra productos y clientes."""
    def __init__(self) -> None:
        self._productos: List[Producto] = []
        self._clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        """Registra un producto si su código no está duplicado."""
        if any(p.codigo == producto.codigo for p in self._productos):
            raise ValueError(f"Código de producto duplicado: {producto.codigo}")
        self._productos.append(producto)

    def listar_productos(self) -> List[str]:
        """Devuelve la información de todos los productos usando polimorfismo."""
        return [p.mostrar_informacion() for p in self._productos]

    def registrar_cliente(self, cliente: Cliente) -> None:
        """Registra un cliente si su identificación no está duplicada."""
        if any(c.identificacion == cliente.identificacion for c in self._clientes):
            raise ValueError(f"Identificación de cliente duplicada: {cliente.identificacion}")
        self._clientes.append(cliente)

    def listar_clientes(self) -> List[str]:
        return [c.mostrar_informacion() for c in self._clientes]
