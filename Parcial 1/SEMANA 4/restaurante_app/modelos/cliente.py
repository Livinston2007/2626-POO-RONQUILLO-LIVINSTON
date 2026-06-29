# Módulo que define la clase Cliente
# Representa un cliente que realiza pedidos en el restaurante

class Cliente:
    """Clase que representa un cliente del restaurante."""
    
    def __init__(self, id_cliente, nombre, correo, telefono):
        """
        Inicializa un nuevo cliente.
        
        Args:
            id_cliente (int): Identificador único del cliente
            nombre (str): Nombre completo del cliente
            correo (str): Correo electrónico del cliente
            telefono (str): Número de teléfono del cliente
        """
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.pedidos = []  # Lista para almacenar los pedidos del cliente
    
    def agregar_pedido(self, pedido):
        """
        Registra un pedido realizado por el cliente.
        
        Args:
            pedido (dict): Diccionario con información del pedido
        """
        self.pedidos.append(pedido)
    
    def obtener_cantidad_pedidos(self):
        """Retorna la cantidad de pedidos realizados por el cliente."""
        return len(self.pedidos)
    
    def obtener_informacion(self):
        """Retorna la información del cliente como diccionario."""
        return {
            'id': self.id_cliente,
            'nombre': self.nombre,
            'correo': self.correo,
            'telefono': self.telefono,
            'pedidos_realizados': self.obtener_cantidad_pedidos()
        }
    
    def __str__(self):
        """Representación en texto del cliente."""
        return f"{self.nombre} (ID: {self.id_cliente}) - {self.correo} - {self.telefono}"
