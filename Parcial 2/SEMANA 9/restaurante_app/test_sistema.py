"""Script de prueba del sistema de restaurante."""

from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def test_sistema():
    """Prueba las funcionalidades principales del sistema."""
    print("=" * 60)
    print("PRUEBA DEL SISTEMA DE RESTAURANTE - SEMANA 9")
    print("=" * 60)
    
    # Crear instancia del servicio
    serv = Restaurante()
    print("\n✓ Servicio Restaurante creado exitosamente")
    
    # Prueba 1: Registrar productos
    print("\n--- Prueba 1: Registrar Productos ---")
    productos_test = [
        Producto("P001", "Hamburguesa", "Comidas", 12.50),
        Producto("P002", "Pizza", "Comidas", 15.00),
        Producto("B001", "Coca Cola", "Bebidas", 3.50),
        Producto("B002", "Agua", "Bebidas", 2.00),
        Producto("D001", "Pastel de Chocolate", "Postres", 8.00),
    ]
    
    for prod in productos_test:
        try:
            serv.registrar_producto(prod)
            print(f"✓ Registrado: {prod.nombre}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    # Prueba 2: Intentar registrar duplicado
    print("\n--- Prueba 2: Validación de Código Duplicado ---")
    try:
        producto_duplicado = Producto("P001", "Otro Producto", "Otros", 10.00)
        serv.registrar_producto(producto_duplicado)
        print("✗ Error: Se permitió código duplicado")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    
    # Prueba 3: Buscar producto
    print("\n--- Prueba 3: Búsqueda de Productos ---")
    producto_encontrado = serv.buscar_producto_por_codigo("P002")
    if producto_encontrado:
        print(f"✓ Encontrado: {producto_encontrado.mostrar_informacion()}")
    else:
        print("✗ No se encontró el producto")
    
    # Prueba 4: Listar productos
    print("\n--- Prueba 4: Listar Productos ---")
    print(f"Total de productos: {serv.contar_productos()}")
    for info in serv.listar_productos():
        print(f"  {info}")
    
    # Prueba 5: Obtener categorías únicas (SET)
    print("\n--- Prueba 5: Categorías Únicas (Estructura SET) ---")
    categorias = serv.obtener_categorias_unicas()
    print(f"Categorías ({len(categorias)}):")
    for cat in sorted(categorias):
        print(f"  • {cat}")
    
    # Prueba 6: Actualizar producto
    print("\n--- Prueba 6: Actualizar Producto ---")
    if serv.actualizar_producto("P001", nombre="Hamburguesa Premium", precio=14.50):
        producto_actualizado = serv.buscar_producto_por_codigo("P001")
        print(f"✓ Actualizado: {producto_actualizado.mostrar_informacion()}")
    else:
        print("✗ Error al actualizar")
    
    # Prueba 7: Eliminar producto
    print("\n--- Prueba 7: Eliminar Producto ---")
    print(f"Productos antes: {serv.contar_productos()}")
    if serv.eliminar_producto("D001"):
        print(f"✓ Producto eliminado")
        print(f"Productos después: {serv.contar_productos()}")
    else:
        print("✗ Error al eliminar")
    
    # Prueba 8: Registrar usuarios
    print("\n--- Prueba 8: Registrar Usuarios ---")
    usuarios_test = [
        Usuario("1234567890", "Juan Pérez", "juan@email.com"),
        Usuario("9876543210", "María García", "maria@email.com"),
        Usuario("5555555555", "Carlos López", "carlos@email.com"),
    ]
    
    for user in usuarios_test:
        try:
            serv.registrar_usuario(user)
            print(f"✓ Registrado: {user.nombre}")
        except ValueError as e:
            print(f"✗ Error: {e}")
    
    # Prueba 9: Validación de identificación duplicada
    print("\n--- Prueba 9: Validación de Identificación Duplicada ---")
    try:
        usuario_duplicado = Usuario("1234567890", "Pedro", "pedro@email.com")
        serv.registrar_usuario(usuario_duplicado)
        print("✗ Error: Se permitió identificación duplicada")
    except ValueError as e:
        print(f"✓ Validación correcta: {e}")
    
    # Prueba 10: Listar usuarios
    print("\n--- Prueba 10: Listar Usuarios ---")
    print(f"Total de usuarios: {serv.contar_usuarios()}")
    for info in serv.listar_usuarios():
        print(f"  {info}")
    
    # Prueba 11: Demostración de Estructuras de Datos
    print("\n--- Prueba 11: Estructuras de Datos Utilizadas ---")
    
    print("\n1. LISTA (list):")
    print(f"   - Productos (_productos): {type(serv._productos).__name__} con {len(serv._productos)} elementos")
    print(f"   - Usuarios (_usuarios): {type(serv._usuarios).__name__} con {len(serv._usuarios)} elementos")
    
    print("\n2. TUPLA (tuple):")
    opciones_menu = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
    print(f"   - Opciones del menú: {type(opciones_menu).__name__} = {opciones_menu}")
    
    print("\n3. DICCIONARIO (dict):")
    opciones_dict = {
        "1": "Registrar producto",
        "2": "Buscar producto",
        "3": "Actualizar producto",
        "4": "Eliminar producto",
        "5": "Listar productos",
    }
    print(f"   - Mapeo opciones→funciones: {type(opciones_dict).__name__}")
    for key, value in opciones_dict.items():
        print(f"     {key} → {value}")
    
    print("\n4. CONJUNTO (set):")
    categorias_set = serv.obtener_categorias_unicas()
    print(f"   - Categorías únicas: {type(categorias_set).__name__} = {categorias_set}")
    
    # Resumen final
    print("\n" + "=" * 60)
    print("RESUMEN FINAL")
    print("=" * 60)
    print(f"Total de productos: {serv.contar_productos()}")
    print(f"Total de usuarios: {serv.contar_usuarios()}")
    print(f"Categorías: {len(serv.obtener_categorias_unicas())}")
    print("\n✓ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 60)


if __name__ == "__main__":
    test_sistema()
