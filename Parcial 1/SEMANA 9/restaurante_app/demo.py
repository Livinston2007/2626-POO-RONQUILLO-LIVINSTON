"""Demostración interactiva del sistema de restaurante."""

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def demo_interactiva():
    """Demuestra todas las funcionalidades del sistema de forma interactiva."""
    serv = Restaurante()
    
    print("\n" + "=" * 60)
    print("DEMOSTRACIÓN INTERACTIVA DEL SISTEMA DE RESTAURANTE")
    print("=" * 60)
    
    # Scenario 1: Registrar algunos productos iniciales
    print("\n[PASO 1] Registrando productos iniciales...")
    productos_iniciales = [
        Producto("BUR001", "Hamburguesa Simple", "Comidas Rápidas", 8.99),
        Producto("BUR002", "Hamburguesa Doble", "Comidas Rápidas", 11.99),
        Producto("PZA001", "Pizza Margarita", "Pizzas", 14.50),
        Producto("PZA002", "Pizza Pepperoni", "Pizzas", 15.50),
        Producto("BEB001", "Coca Cola 350ml", "Bebidas", 2.50),
        Producto("BEB002", "Jugo Natural", "Bebidas", 4.00),
        Producto("POS001", "Helado", "Postres", 5.50),
    ]
    
    for prod in productos_iniciales:
        serv.registrar_producto(prod)
        print(f"  ✓ {prod.nombre} - ${prod.precio:.2f}")
    
    # Scenario 2: Listar productos
    print("\n[PASO 2] Listando todos los productos registrados:")
    print("-" * 60)
    for info in serv.listar_productos():
        print(f"  {info}")
    print(f"\nTotal: {serv.contar_productos()} productos\n")
    
    # Scenario 3: Buscar un producto específico
    print("[PASO 3] Buscando producto específico (PZA001):")
    producto = serv.buscar_producto_por_codigo("PZA001")
    if producto:
        print(f"  ✓ Encontrado: {producto.mostrar_informacion()}\n")
    
    # Scenario 4: Actualizar un producto
    print("[PASO 4] Actualizando precio de Hamburguesa Simple (BUR001):")
    print(f"  Precio anterior: $8.99")
    serv.actualizar_producto("BUR001", precio=9.99)
    producto_actualizado = serv.buscar_producto_por_codigo("BUR001")
    print(f"  Precio nuevo: ${producto_actualizado.precio:.2f}")
    print(f"  ✓ Producto actualizado\n")
    
    # Scenario 5: Mostrar categorías únicas
    print("[PASO 5] Mostrando categorías de productos:")
    categorias = serv.obtener_categorias_unicas()
    print(f"  Total de categorías: {len(categorias)}")
    for categoria in sorted(categorias):
        print(f"    • {categoria}")
    print()
    
    # Scenario 6: Eliminar un producto
    print("[PASO 6] Eliminando producto (POS001):")
    producto_a_eliminar = serv.buscar_producto_por_codigo("POS001")
    print(f"  A eliminar: {producto_a_eliminar.mostrar_informacion()}")
    serv.eliminar_producto("POS001")
    print(f"  ✓ Producto eliminado")
    print(f"  Productos restantes: {serv.contar_productos()}\n")
    
    # Scenario 7: Registrar usuarios
    print("[PASO 7] Registrando usuarios:")
    usuarios_iniciales = [
        Usuario("12345678", "Juan Martínez", "juan.martinez@email.com"),
        Usuario("87654321", "María González", "maria.gonzalez@email.com"),
        Usuario("55555555", "Carlos Rodríguez", "carlos.rodriguez@email.com"),
        Usuario("66666666", "Ana López", "ana.lopez@email.com"),
    ]
    
    for user in usuarios_iniciales:
        serv.registrar_usuario(user)
        print(f"  ✓ {user.nombre}")
    
    # Scenario 8: Listar usuarios
    print(f"\n[PASO 8] Listando usuarios ({serv.contar_usuarios()}):")
    print("-" * 60)
    for info in serv.listar_usuarios():
        print(f"  {info}")
    print()
    
    # Scenario 9: Intentar registrar productos duplicados
    print("[PASO 9] Intentando registrar producto con código duplicado:")
    try:
        producto_dup = Producto("BUR001", "Producto Duplicado", "Test", 10.00)
        serv.registrar_producto(producto_dup)
        print("  ✗ Se permitió código duplicado (ERROR)")
    except ValueError as e:
        print(f"  ✓ Validación correcta: {e}\n")
    
    # Scenario 10: Intentar registrar usuario con identificación duplicada
    print("[PASO 10] Intentando registrar usuario con ID duplicada:")
    try:
        usuario_dup = Usuario("12345678", "Usuario Duplicado", "duplicado@email.com")
        serv.registrar_usuario(usuario_dup)
        print("  ✗ Se permitió ID duplicada (ERROR)")
    except ValueError as e:
        print(f"  ✓ Validación correcta: {e}\n")
    
    # Final Summary
    print("=" * 60)
    print("RESUMEN FINAL DEL SISTEMA")
    print("=" * 60)
    print(f"Productos registrados: {serv.contar_productos()}")
    print(f"Usuarios registrados: {serv.contar_usuarios()}")
    print(f"Categorías disponibles: {len(serv.obtener_categorias_unicas())}")
    
    print("\nESTRUCTURAS DE DATOS UTILIZADAS:")
    print("  1. LISTA (list) - Administra colecciones de productos y usuarios")
    print("  2. TUPLA (tuple) - Define opciones estables del menú")
    print("  3. DICCIONARIO (dict) - Mapea opciones del menú a funciones")
    print("  4. CONJUNTO (set) - Obtiene categorías únicas sin duplicados")
    
    print("\nOPERACIONES CRUD COMPLETADAS:")
    print("  ✓ CREATE - Registrar productos y usuarios")
    print("  ✓ READ - Buscar y listar productos y usuarios")
    print("  ✓ UPDATE - Actualizar datos de productos")
    print("  ✓ DELETE - Eliminar productos")
    
    print("\nVALIDACIONES IMPLEMENTADAS:")
    print("  ✓ Códigos de productos únicos")
    print("  ✓ Identificaciones de usuarios únicas")
    print("  ✓ Campos no vacíos")
    print("  ✓ Precios no negativos")
    print("  ✓ Entrada numérica válida")
    
    print("\n" + "=" * 60)
    print("¡DEMOSTRACIÓN COMPLETADA EXITOSAMENTE!")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    demo_interactiva()
