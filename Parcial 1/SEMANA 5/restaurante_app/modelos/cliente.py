"""
Clase Cliente: Representa una persona que realiza o consume un pedido en el restaurante.
"""

from datetime import datetime


class Cliente:
    """Representa un cliente del restaurante."""
    
    # Contador de clase para generar IDs únicos
    contador_id = 1
    
    def __init__(self, nombre, email, telefono):
        """
        Constructor de la clase Cliente.
        
        Args:
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
        """
        self.id = Cliente.contador_id
        Cliente.contador_id += 1
        self.nombre = nombre
        self.email = email
        self.telefono = telefono
        self.fecha_registro = datetime.now()
    
    def obtener_informacion(self):
        """Retorna la información del cliente como diccionario."""
        return {
            'id': self.id,
            'nombre': self.nombre,
            'email': self.email,
            'telefono': self.telefono,
            'fecha_registro': self.fecha_registro.strftime('%Y-%m-%d %H:%M:%S')
        }
    
    def actualizar_contacto(self, email=None, telefono=None):
        """Actualiza los datos de contacto del cliente."""
        if email:
            self.email = email
        if telefono:
            self.telefono = telefono
        return True
    
    def validar_email(self):
        """Valida que el email contenga un formato básico válido."""
        return '@' in self.email and '.' in self.email
    
    def __str__(self):
        """Representación en texto del cliente."""
        return f"Cliente: {self.nombre} | Email: {self.email} | Tel: {self.telefono}"
