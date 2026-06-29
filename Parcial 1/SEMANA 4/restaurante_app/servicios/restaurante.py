# Módulo que define la clase Restaurante
# Gestiona los productos y clientes del sistema

class Restaurante:
    """Clase que administra las operaciones principales del restaurante."""
    
    def __init__(self, nombre, ubicacion):
        """
        Inicializa un nuevo restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
            ubicacion (str): Ubicación o dirección del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []  # Lista para almacenar productos
        self.clientes = []   # Lista para almacenar clientes
        self.total_ventas = 0.0  # Acumulador de ventas
    
    def registrar_producto(self, producto):
        """
        Añade un producto al catálogo del restaurante.
        
        Args:
            producto (Producto): Objeto de la clase Producto
        """
        self.productos.append(producto)
    
    def registrar_cliente(self, cliente):
        """
        Registra un nuevo cliente en el sistema.
        
        Args:
            cliente (Cliente): Objeto de la clase Cliente
        """
        self.clientes.append(cliente)
    
    def buscar_producto_por_nombre(self, nombre):
        """
        Busca un producto por su nombre.
        
        Args:
            nombre (str): Nombre del producto a buscar
            
        Returns:
            Producto: El producto encontrado o None
        """
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
    
    def buscar_cliente_por_id(self, id_cliente):
        """
        Busca un cliente por su ID.
        
        Args:
            id_cliente (int): ID del cliente a buscar
            
        Returns:
            Cliente: El cliente encontrado o None
        """
        for cliente in self.clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def realizar_pedido(self, id_cliente, nombre_producto, cantidad):
        """
        Registra un pedido de un cliente.
        
        Args:
            id_cliente (int): ID del cliente
            nombre_producto (str): Nombre del producto a pedir
            cantidad (int): Cantidad de productos
            
        Returns:
            dict: Información del pedido realizado o None si hay error
        """
        cliente = self.buscar_cliente_por_id(id_cliente)
        if cliente is None:
            return None
        
        producto = self.buscar_producto_por_nombre(nombre_producto)
        if producto is None or not producto.disponible:
            return None
        
        total_pedido = producto.precio * cantidad
        self.total_ventas += total_pedido
        
        pedido = {
            'producto': nombre_producto,
            'cantidad': cantidad,
            'precio_unitario': producto.precio,
            'total': total_pedido
        }
        
        cliente.agregar_pedido(pedido)
        return pedido
    
    def obtener_cantidad_productos(self):
        """Retorna la cantidad de productos disponibles."""
        return len(self.productos)
    
    def obtener_cantidad_clientes(self):
        """Retorna la cantidad de clientes registrados."""
        return len(self.clientes)
    
    def listar_productos(self):
        """Retorna una lista de todos los productos."""
        return self.productos
    
    def listar_clientes(self):
        """Retorna una lista de todos los clientes."""
        return self.clientes
    
    def obtener_informacion_restaurante(self):
        """Retorna información general del restaurante."""
        return {
            'nombre': self.nombre,
            'ubicacion': self.ubicacion,
            'productos_registrados': self.obtener_cantidad_productos(),
            'clientes_registrados': self.obtener_cantidad_clientes(),
            'total_ventas': f"${self.total_ventas:.2f}"
        }
