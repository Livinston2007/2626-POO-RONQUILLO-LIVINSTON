"""
Clase Producto: Representa un plato, bebida o producto disponible en el restaurante.
"""


class Producto:
    """Representa un producto del restaurante con sus características."""
    
    # Contador de clase para generar IDs únicos
    contador_id = 1
    
    def __init__(self, nombre, descripcion, precio, categoria):
        """
        Constructor de la clase Producto.
        
        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            categoria: Categoría (plato/bebida/postre)
        """
        self.id = Producto.contador_id
        Producto.contador_id += 1
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.categoria = categoria
    
    def obtener_informacion(self):
        """Retorna la información del producto como diccionario."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'precio': f"${self.precio:.2f}",
            'categoria': self.categoria
        }
    
    def validar_precio(self):
        """Valida que el precio sea un número positivo."""
        return isinstance(self.precio, (int, float)) and self.precio > 0
    
    def actualizar_precio(self, nuevo_precio):
        """Actualiza el precio del producto si es válido."""
        if nuevo_precio > 0:
            self.precio = nuevo_precio
            return True
        return False
    
    def __str__(self):
        """Representación en texto del producto."""
        return f"{self.nombre} ({self.categoria}) - ${self.precio:.2f}"
