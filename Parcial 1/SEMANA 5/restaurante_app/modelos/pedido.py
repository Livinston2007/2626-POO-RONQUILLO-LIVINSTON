"""
Clase Pedido: Representa un pedido realizado por un cliente en el restaurante.
"""

from datetime import datetime


class Pedido:
    """Representa un pedido del restaurante."""
    
    # Contador de clase para generar IDs únicos
    contador_id = 1
    
    # Estados posibles de un pedido
    ESTADOS_VALIDOS = ['pendiente', 'preparación', 'listo', 'entregado', 'cancelado']
    
    def __init__(self, cliente):
        """
        Constructor de la clase Pedido.
        
        Args:
            cliente: Objeto Cliente asociado al pedido
        """
        self.id = Pedido.contador_id
        Pedido.contador_id += 1
        self.cliente = cliente
        self.productos = []
        self.estado = 'pendiente'
        self.fecha_creacion = datetime.now()
        self.total = 0.0
    
    def agregar_producto(self, producto, cantidad=1):
        """
        Agrega un producto al pedido.
        
        Args:
            producto: Objeto Producto a agregar
            cantidad: Cantidad del producto
        """
        self.productos.append({
            'producto': producto,
            'cantidad': cantidad
        })
        self._calcular_total()
    
    def _calcular_total(self):
        """Calcula el total del pedido."""
        self.total = sum(item['producto'].precio * item['cantidad'] 
                        for item in self.productos)
    
    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del pedido si es válido."""
        if nuevo_estado in self.ESTADOS_VALIDOS:
            self.estado = nuevo_estado
            return True
        return False
    
    def obtener_resumen(self):
        """Retorna un resumen del pedido."""
        resumen = {
            'id': self.id,
            'cliente': self.cliente.nombre,
            'estado': self.estado,
            'fecha': self.fecha_creacion.strftime('%Y-%m-%d %H:%M:%S'),
            'total': f"${self.total:.2f}",
            'cantidad_items': len(self.productos)
        }
        return resumen
    
    def listar_productos(self):
        """Retorna la lista de productos del pedido con detalles."""
        if not self.productos:
            return "El pedido no contiene productos."
        
        detalles = []
        for i, item in enumerate(self.productos, 1):
            producto = item['producto']
            cantidad = item['cantidad']
            subtotal = producto.precio * cantidad
            detalles.append(
                f"  {i}. {producto.nombre} x{cantidad} = ${subtotal:.2f}"
            )
        return "\n".join(detalles)
    
    def __str__(self):
        """Representación en texto del pedido."""
        return (f"Pedido #{self.id} - Cliente: {self.cliente.nombre} | "
                f"Estado: {self.estado} | Total: ${self.total:.2f}")
