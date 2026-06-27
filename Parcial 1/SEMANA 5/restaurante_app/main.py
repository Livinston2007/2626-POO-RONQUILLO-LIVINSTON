"""
Archivo main.py - Punto de arranque del sistema de gestión de restaurante.
Este archivo demuestra el funcionamiento del sistema creando objetos,
registrando información y ejecutando operaciones principales.
"""

from servicios.restaurante import Restaurante


def main():
    """Función principal que demuestra el funcionamiento del sistema."""
    
    # ===== CREAR INSTANCIA DEL RESTAURANTE =====
    restaurante = Restaurante("Don Roberto's Grill")
    print(restaurante.mostrar_informacion())
    
    # ===== REGISTRAR PRODUCTOS =====
    print("\n--- REGISTRANDO PRODUCTOS ---\n")
    
    # Platos principales
    restaurante.registrar_producto(
        "Filete de Res",
        "Filete premium acompañado de papas al horno",
        25.50,
        "plato"
    )
    restaurante.registrar_producto(
        "Pechuga de Pollo",
        "Pechuga a la parrilla con vegetales frescos",
        18.00,
        "plato"
    )
    restaurante.registrar_producto(
        "Salmón a la Mantequilla",
        "Salmón fresco con salsa de mantequilla y limón",
        28.00,
        "plato"
    )
    
    # Bebidas
    restaurante.registrar_producto(
        "Jugo Natural de Naranja",
        "Jugo fresco recién exprimido",
        4.50,
        "bebida"
    )
    restaurante.registrar_producto(
        "Refresco Cola",
        "Bebida gaseosa en vaso con hielo",
        3.00,
        "bebida"
    )
    restaurante.registrar_producto(
        "Vino Tinto Reserva",
        "Vino tinto de excelente cosecha",
        12.00,
        "bebida"
    )
    
    # Postres
    restaurante.registrar_producto(
        "Tiramisú",
        "Postre italiano tradicional con capas de mascarpone",
        7.50,
        "postre"
    )
    restaurante.registrar_producto(
        "Helado de Chocolate",
        "Helado artesanal de chocolate oscuro",
        5.00,
        "postre"
    )
    
    # Mostrar menú
    print(restaurante.mostrar_menu())
    
    # ===== REGISTRAR CLIENTES =====
    print("\n--- REGISTRANDO CLIENTES ---\n")
    
    cliente1 = restaurante.registrar_cliente(
        "Carlos Martínez",
        "carlos.martinez@email.com",
        "+34-912345678"
    )
    print(f"[OK] Cliente registrado: {cliente1}")
    
    cliente2 = restaurante.registrar_cliente(
        "María González",
        "maria.gonzalez@email.com",
        "+34-987654321"
    )
    print(f"[OK] Cliente registrado: {cliente2}")
    
    cliente3 = restaurante.registrar_cliente(
        "Juan Rodríguez",
        "juan.rodriguez@email.com",
        "+34-555888999"
    )
    print(f"[OK] Cliente registrado: {cliente3}")
    
    # Mostrar lista de clientes
    print(restaurante.mostrar_clientes())
    
    # ===== CREAR Y GESTIONAR PEDIDOS =====
    print("\n--- CREANDO PEDIDOS ---\n")
    
    # Pedido 1: Carlos Martínez
    pedido1 = restaurante.crear_pedido(cliente1)
    pedido1.agregar_producto(restaurante.obtener_producto(1), 1)  # Filete
    pedido1.agregar_producto(restaurante.obtener_producto(4), 2)  # Jugos
    pedido1.agregar_producto(restaurante.obtener_producto(7), 1)  # Tiramisú
    pedido1.cambiar_estado("preparación")
    print(f"[OK] {pedido1}")
    
    # Pedido 2: María González
    pedido2 = restaurante.crear_pedido(cliente2)
    pedido2.agregar_producto(restaurante.obtener_producto(2), 1)  # Pechuga
    pedido2.agregar_producto(restaurante.obtener_producto(6), 1)  # Vino
    pedido2.agregar_producto(restaurante.obtener_producto(8), 1)  # Helado
    pedido2.cambiar_estado("listo")
    print(f"[OK] {pedido2}")
    
    # Pedido 3: Juan Rodríguez
    pedido3 = restaurante.crear_pedido(cliente3)
    pedido3.agregar_producto(restaurante.obtener_producto(3), 1)  # Salmón
    pedido3.agregar_producto(restaurante.obtener_producto(5), 1)  # Refresco
    pedido3.cambiar_estado("entregado")
    print(f"[OK] {pedido3}")
    
    # Mostrar todos los pedidos
    print(restaurante.mostrar_pedidos())
    
    # ===== ANÁLISIS DE PEDIDOS POR ESTADO =====
    print("\n--- ANÁLISIS DE PEDIDOS ---\n")
    
    estados = ['pendiente', 'preparación', 'listo', 'entregado', 'cancelado']
    for estado in estados:
        pedidos_estado = restaurante.listar_pedidos_por_estado(estado)
        cantidad = len(pedidos_estado)
        print(f"Pedidos en estado '{estado}': {cantidad}")
    
    # ===== INFORMACIÓN FINANCIERA =====
    print("\n" + "="*60)
    ingresos = restaurante.obtener_ingresos_totales()
    print(f"INGRESOS TOTALES (Pedidos Entregados): ${ingresos:.2f}")
    print("="*60)
    
    # ===== DEMOSTRACIÓN DE MÉTODOS DE CLASES INDIVIDUALES =====
    print("\n--- DEMOSTRACIÓN DE MÉTODOS INDIVIDUALES ---\n")
    
    # Información detallada de un cliente
    print("Información detallada del cliente Carlos Martínez:")
    info_cliente = cliente1.obtener_informacion()
    for clave, valor in info_cliente.items():
        print(f"  {clave}: {valor}")
    
    # Actualizar contacto del cliente
    print("\nActualizando contacto de María González...")
    cliente2.actualizar_contacto(
        email="maria.nueva@email.com",
        telefono="+34-666777888"
    )
    print(f"  Nuevo email: {cliente2.email}")
    print(f"  Nuevo teléfono: {cliente2.telefono}")
    
    # Información detallada de un producto
    print("\nInformación detallada del producto ID 1:")
    producto = restaurante.obtener_producto(1)
    info_producto = producto.obtener_informacion()
    for clave, valor in info_producto.items():
        print(f"  {clave}: {valor}")
    
    # Validación de precio del producto
    print(f"  ¿Precio válido?: {producto.validar_precio()}")
    
    # Información resumida del pedido
    print("\nResumen del Pedido 1:")
    resumen = pedido1.obtener_resumen()
    for clave, valor in resumen.items():
        print(f"  {clave}: {valor}")
    
    # ===== RESUMEN FINAL =====
    print("\n" + "="*60)
    print(f"RESUMEN FINAL: {restaurante}")
    print("="*60)
    print("\n¡Sistema de restaurante ejecutado correctamente!")


if __name__ == "__main__":
    main()
