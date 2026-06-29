# Módulo principal - Punto de arranque del sistema de gestión de restaurante

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante

# Crear instancia del restaurante
print("=" * 70)
print("SISTEMA DE GESTIÓN DE RESTAURANTE")
print("=" * 70)

restaurante = Restaurante("Sabores del Mundo", "Calle Principal 123")

# Registrar productos en el menú
print("\n[1] Registrando productos en el sistema...")
producto1 = Producto(1, "Hamburguesa", "Plato", 12.50)
producto2 = Producto(2, "Pizza Margarita", "Plato", 15.00)
producto3 = Producto(3, "Jugo Natural", "Bebida", 5.00)
producto4 = Producto(4, "Ensalada César", "Plato", 10.00)
producto5 = Producto(5, "Refresco", "Bebida", 3.50)
producto6 = Producto(6, "Tiramisú", "Postre", 8.00)

restaurante.registrar_producto(producto1)
restaurante.registrar_producto(producto2)
restaurante.registrar_producto(producto3)
restaurante.registrar_producto(producto4)
restaurante.registrar_producto(producto5)
restaurante.registrar_producto(producto6)

print(f"✓ {restaurante.obtener_cantidad_productos()} productos registrados")

# Registrar clientes
print("\n[2] Registrando clientes en el sistema...")
cliente1 = Cliente(101, "Juan Pérez", "juan.perez@email.com", "555-1001")
cliente2 = Cliente(102, "María García", "maria.garcia@email.com", "555-1002")
cliente3 = Cliente(103, "Carlos López", "carlos.lopez@email.com", "555-1003")

restaurante.registrar_cliente(cliente1)
restaurante.registrar_cliente(cliente2)
restaurante.registrar_cliente(cliente3)

print(f"✓ {restaurante.obtener_cantidad_clientes()} clientes registrados")

# Realizar algunos pedidos
print("\n[3] Procesando pedidos...")
pedido1 = restaurante.realizar_pedido(101, "Hamburguesa", 2)
if pedido1:
    print(f"✓ Pedido registrado: {pedido1['producto']} x {pedido1['cantidad']} - Total: ${pedido1['total']:.2f}")

pedido2 = restaurante.realizar_pedido(102, "Pizza Margarita", 1)
if pedido2:
    print(f"✓ Pedido registrado: {pedido2['producto']} x {pedido2['cantidad']} - Total: ${pedido2['total']:.2f}")

pedido3 = restaurante.realizar_pedido(102, "Jugo Natural", 3)
if pedido3:
    print(f"✓ Pedido registrado: {pedido3['producto']} x {pedido3['cantidad']} - Total: ${pedido3['total']:.2f}")

pedido4 = restaurante.realizar_pedido(103, "Tiramisú", 2)
if pedido4:
    print(f"✓ Pedido registrado: {pedido4['producto']} x {pedido4['cantidad']} - Total: ${pedido4['total']:.2f}")

# Mostrar información del restaurante
print("\n" + "=" * 70)
print("INFORMACIÓN DEL RESTAURANTE")
print("=" * 70)
info_rest = restaurante.obtener_informacion_restaurante()
print(f"Nombre: {info_rest['nombre']}")
print(f"Ubicación: {info_rest['ubicacion']}")
print(f"Productos en catálogo: {info_rest['productos_registrados']}")
print(f"Clientes registrados: {info_rest['clientes_registrados']}")
print(f"Total de ventas: {info_rest['total_ventas']}")

# Mostrar catálogo de productos
print("\n" + "=" * 70)
print("CATÁLOGO DE PRODUCTOS")
print("=" * 70)
for producto in restaurante.listar_productos():
    print(f"  • {producto}")

# Mostrar información de clientes y sus pedidos
print("\n" + "=" * 70)
print("INFORMACIÓN DE CLIENTES")
print("=" * 70)
for cliente in restaurante.listar_clientes():
    print(f"\n{cliente}")
    info_cliente = cliente.obtener_informacion()
    print(f"  Pedidos realizados: {info_cliente['pedidos_realizados']}")
    
    if cliente.obtener_cantidad_pedidos() > 0:
        print(f"  Detalle de pedidos:")
        for pedido in cliente.pedidos:
            print(f"    - {pedido['producto']} x {pedido['cantidad']} = ${pedido['total']:.2f}")

print("\n" + "=" * 70)
print("FIN DEL PROGRAMA")
print("=" * 70)
