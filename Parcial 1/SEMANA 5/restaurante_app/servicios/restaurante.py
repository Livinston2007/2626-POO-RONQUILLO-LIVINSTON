"""
Clase Restaurante: Administra los productos, clientes y pedidos del restaurante.
Esta es la clase principal del servicio que coordina todas las operaciones.
"""

from modelos.producto import Producto
from modelos.cliente import Cliente
from modelos.pedido import Pedido


class Restaurante:
    """Administra las operaciones principales del sistema de restaurante."""
    
    def __init__(self, nombre):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre: Nombre del restaurante
        """
        self.nombre = nombre
        self.productos_disponibles = []
        self.clientes_registrados = []
        self.pedidos_realizados = []
    
    # ===== MÉTODOS PARA GESTIONAR PRODUCTOS =====
    def registrar_producto(self, nombre, descripcion, precio, categoria):
        """
        Registra un nuevo producto en el restaurante.
        
        Args:
            nombre: Nombre del producto
            descripcion: Descripción del producto
            precio: Precio del producto
            categoria: Categoría del producto
        
        Returns:
            El objeto Producto creado
        """
        producto = Producto(nombre, descripcion, precio, categoria)
        self.productos_disponibles.append(producto)
        return producto
    
    def obtener_producto(self, producto_id):
        """Obtiene un producto por su ID."""
        for producto in self.productos_disponibles:
            if producto.id == producto_id:
                return producto
        return None
    
    def listar_productos(self):
        """Retorna la lista de todos los productos disponibles."""
        return self.productos_disponibles
    
    # ===== MÉTODOS PARA GESTIONAR CLIENTES =====
    def registrar_cliente(self, nombre, email, telefono):
        """
        Registra un nuevo cliente en el restaurante.
        
        Args:
            nombre: Nombre completo del cliente
            email: Correo electrónico del cliente
            telefono: Número de teléfono del cliente
        
        Returns:
            El objeto Cliente creado
        """
        cliente = Cliente(nombre, email, telefono)
        self.clientes_registrados.append(cliente)
        return cliente
    
    def obtener_cliente(self, cliente_id):
        """Obtiene un cliente por su ID."""
        for cliente in self.clientes_registrados:
            if cliente.id == cliente_id:
                return cliente
        return None
    
    def listar_clientes(self):
        """Retorna la lista de todos los clientes registrados."""
        return self.clientes_registrados
    
    # ===== MÉTODOS PARA GESTIONAR PEDIDOS =====
    def crear_pedido(self, cliente):
        """
        Crea un nuevo pedido para un cliente.
        
        Args:
            cliente: Objeto Cliente para el cual se crea el pedido
        
        Returns:
            El objeto Pedido creado
        """
        pedido = Pedido(cliente)
        self.pedidos_realizados.append(pedido)
        return pedido
    
    def obtener_pedido(self, pedido_id):
        """Obtiene un pedido por su ID."""
        for pedido in self.pedidos_realizados:
            if pedido.id == pedido_id:
                return pedido
        return None
    
    def listar_pedidos(self):
        """Retorna la lista de todos los pedidos realizados."""
        return self.pedidos_realizados
    
    def listar_pedidos_por_estado(self, estado):
        """Retorna los pedidos filtrados por estado."""
        return [p for p in self.pedidos_realizados if p.estado == estado]
    
    # ===== MÉTODOS INFORMATIVOS =====
    def mostrar_informacion(self):
        """Muestra la información general del restaurante."""
        info = f"""
{'='*60}
INFORMACIÓN DEL RESTAURANTE: {self.nombre}
{'='*60}
Productos disponibles: {len(self.productos_disponibles)}
Clientes registrados: {len(self.clientes_registrados)}
Pedidos realizados: {len(self.pedidos_realizados)}
{'='*60}
        """
        return info
    
    def mostrar_menu(self):
        """Muestra el menú disponible del restaurante."""
        if not self.productos_disponibles:
            return "El restaurante no tiene productos disponibles."
        
        menu = "\n" + "="*60 + "\n"
        menu += f"MENÚ DE {self.nombre.upper()}\n"
        menu += "="*60 + "\n"
        
        # Agrupar productos por categoría
        categorias = {}
        for producto in self.productos_disponibles:
            if producto.categoria not in categorias:
                categorias[producto.categoria] = []
            categorias[producto.categoria].append(producto)
        
        for categoria in categorias:
            menu += f"\n{categoria.upper()}:\n"
            for producto in categorias[categoria]:
                menu += f"  ID: {producto.id} | {producto} | {producto.descripcion}\n"
        
        menu += "="*60 + "\n"
        return menu
    
    def mostrar_clientes(self):
        """Muestra todos los clientes registrados."""
        if not self.clientes_registrados:
            return "No hay clientes registrados."
        
        clientes_info = "\n" + "="*60 + "\n"
        clientes_info += "CLIENTES REGISTRADOS\n"
        clientes_info += "="*60 + "\n"
        
        for cliente in self.clientes_registrados:
            info = cliente.obtener_informacion()
            clientes_info += f"\nID: {info['id']} | {info['nombre']}\n"
            clientes_info += f"  Email: {info['email']}\n"
            clientes_info += f"  Teléfono: {info['telefono']}\n"
            clientes_info += f"  Registrado: {info['fecha_registro']}\n"
        
        clientes_info += "="*60 + "\n"
        return clientes_info
    
    def mostrar_pedidos(self):
        """Muestra todos los pedidos realizados."""
        if not self.pedidos_realizados:
            return "No hay pedidos registrados."
        
        pedidos_info = "\n" + "="*60 + "\n"
        pedidos_info += "PEDIDOS REALIZADOS\n"
        pedidos_info += "="*60 + "\n"
        
        for pedido in self.pedidos_realizados:
            pedidos_info += f"\n{pedido}\n"
            pedidos_info += f"Productos:\n{pedido.listar_productos()}\n"
        
        pedidos_info += "="*60 + "\n"
        return pedidos_info
    
    def obtener_ingresos_totales(self):
        """Calcula los ingresos totales de los pedidos entregados."""
        entregados = [p for p in self.pedidos_realizados if p.estado == 'entregado']
        return sum(p.total for p in entregados)
    
    def __str__(self):
        """Representación en texto del restaurante."""
        return (f"Restaurante: {self.nombre} | "
                f"Productos: {len(self.productos_disponibles)} | "
                f"Clientes: {len(self.clientes_registrados)} | "
                f"Pedidos: {len(self.pedidos_realizados)}")
