# Módulo que define la clase Producto
# Representa un producto disponible en el restaurante (platos, bebidas, postres)

class Producto:
    """Clase que representa un producto del restaurante."""
    
    def __init__(self, id_producto, nombre, tipo, precio):
        """
        Inicializa un nuevo producto.
        
        Args:
            id_producto (int): Identificador único del producto
            nombre (str): Nombre del producto
            tipo (str): Tipo de producto (plato, bebida, postre)
            precio (float): Precio del producto
        """
        self.id_producto = id_producto
        self.nombre = nombre
        self.tipo = tipo
        self.precio = precio
        self.disponible = True
    
    def obtener_precio(self):
        """Retorna el precio del producto."""
        return self.precio
    
    def establecer_disponibilidad(self, disponible):
        """Actualiza la disponibilidad del producto."""
        self.disponible = disponible
    
    def obtener_informacion(self):
        """Retorna la información del producto como diccionario."""
        return {
            'id': self.id_producto,
            'nombre': self.nombre,
            'tipo': self.tipo,
            'precio': f"${self.precio:.2f}",
            'disponible': "Sí" if self.disponible else "No"
        }
    
    def __str__(self):
        """Representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"{self.nombre} ({self.tipo}) - ${self.precio:.2f} - {estado}"
