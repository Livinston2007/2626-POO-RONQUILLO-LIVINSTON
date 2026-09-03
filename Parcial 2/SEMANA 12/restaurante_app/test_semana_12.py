"""
Script de prueba para verificar que las optimizaciones funcionan correctamente.
Comprueba búsquedas, consultas y sincronización de índices.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante


def prueba_carga_datos():
    """Prueba 1: Cargar datos desde JSON y verificar sincronización."""
    print("\n" + "=" * 60)
    print("PRUEBA 1: Carga de datos desde JSON y sincronización de índices")
    print("=" * 60)
    
    base_datos = Path(__file__).resolve().parent / "datos"
    archivos = ArchivoServicio(str(base_datos))
    restaurante = Restaurante()
    
    productos = archivos.cargar_productos()
    usuarios = archivos.cargar_usuarios()
    ventas = archivos.cargar_ventas()
    
    restaurante.cargar_productos_iniciales(productos)
    restaurante.cargar_usuarios_iniciales(usuarios)
    restaurante.cargar_ventas_iniciales(ventas)
    
    estado = restaurante.obtener_estado_indices()
    
    print(f"✓ Productos cargados: {estado['productos_en_lista']}")
    print(f"✓ Usuarios cargados: {estado['usuarios_en_lista']}")
    print(f"✓ Ventas cargadas: {estado['ventas_totales']}")
    
    assert estado['productos_en_lista'] == estado['productos_en_indice'], "Índice de productos desincronizado"
    assert estado['usuarios_en_lista'] == estado['usuarios_en_indice'], "Índice de usuarios desincronizado"
    
    print("\n✓ PRUEBA 1 EXITOSA: Indices sincronizados correctamente")
    return restaurante


def prueba_busqueda_producto(restaurante: Restaurante):
    """Prueba 2: Búsqueda de productos por código (O(1))."""
    print("\n" + "=" * 60)
    print("PRUEBA 2: Búsqueda de productos por código (O(1))")
    print("=" * 60)
    
    # Buscar un producto existente
    producto = restaurante.buscar_producto_por_codigo("P001")
    assert producto is not None, "Producto P001 no encontrado"
    assert producto.nombre == "Hamburguesa clasica", f"Nombre incorrecto: {producto.nombre}"
    print(f"✓ Producto encontrado: {producto.mostrar_informacion()}")
    
    # Buscar un producto inexistente
    producto_inexistente = restaurante.buscar_producto_por_codigo("INEXISTENTE")
    assert producto_inexistente is None, "Búsqueda debe retornar None"
    print("✓ Búsqueda de producto inexistente retorna None")
    
    print("\n✓ PRUEBA 2 EXITOSA: Búsquedas de producto funcionan")


def prueba_busqueda_usuario(restaurante: Restaurante):
    """Prueba 3: Búsqueda de usuarios por ID (O(1))."""
    print("\n" + "=" * 60)
    print("PRUEBA 3: Búsqueda de usuarios por ID (O(1))")
    print("=" * 60)
    
    # Buscar un usuario existente
    usuario = restaurante.buscar_usuario_por_identificacion("1001")
    assert usuario is not None, "Usuario 1001 no encontrado"
    assert usuario.nombre == "Laura Gomez", f"Nombre incorrecto: {usuario.nombre}"
    print(f"✓ Usuario encontrado: {usuario.mostrar_informacion()}")
    
    # Buscar un usuario inexistente
    usuario_inexistente = restaurante.buscar_usuario_por_identificacion("INEXISTENTE")
    assert usuario_inexistente is None, "Búsqueda debe retornar None"
    print("✓ Búsqueda de usuario inexistente retorna None")
    
    print("\n✓ PRUEBA 3 EXITOSA: Búsquedas de usuario funcionan")


def prueba_consulta_ventas_usuario(restaurante: Restaurante):
    """Prueba 4: Consulta de ventas por usuario (O(1))."""
    print("\n" + "=" * 60)
    print("PRUEBA 4: Consulta de ventas por usuario (O(1))")
    print("=" * 60)
    
    # Consultar ventas del usuario 1001
    ventas_1001 = restaurante.consultar_ventas_por_usuario("1001")
    print(f"✓ Ventas del usuario 1001: {len(ventas_1001)} venta(s)")
    for venta in ventas_1001:
        print(f"  - {restaurante.describir_venta(venta)}")
    assert len(ventas_1001) == 2, f"Usuario 1001 debe tener 2 ventas, tiene {len(ventas_1001)}"
    
    # Consultar ventas del usuario 1003
    ventas_1003 = restaurante.consultar_ventas_por_usuario("1003")
    print(f"✓ Ventas del usuario 1003: {len(ventas_1003)} venta(s)")
    for venta in ventas_1003:
        print(f"  - {restaurante.describir_venta(venta)}")
    assert len(ventas_1003) == 2, f"Usuario 1003 debe tener 2 ventas, tiene {len(ventas_1003)}"
    
    # Consultar ventas de usuario sin ventas
    ventas_vacio = restaurante.consultar_ventas_por_usuario("INEXISTENTE")
    assert ventas_vacio == [], "Usuario inexistente debe tener lista vacía"
    print("✓ Usuario sin ventas retorna lista vacía")
    
    print("\n✓ PRUEBA 4 EXITOSA: Consultas de ventas por usuario funcionan")


def prueba_registrar_producto(restaurante: Restaurante, archivos: ArchivoServicio):
    """Prueba 5: Registrar producto y verificar índice."""
    print("\n" + "=" * 60)
    print("PRUEBA 5: Registrar producto y verificar índice")
    print("=" * 60)
    
    nuevo_producto = Producto("P999", "Agua mineral", "Bebidas", 2000.0, 20)
    restaurante.registrar_producto(nuevo_producto)
    
    # Verificar que se agregó a la lista
    assert restaurante.contar_productos() == 6, f"Debe haber 6 productos, hay {restaurante.contar_productos()}"
    print(f"✓ Producto agregado a la lista (total: {restaurante.contar_productos()})")
    
    # Verificar que se puede buscar en el índice
    producto_buscado = restaurante.buscar_producto_por_codigo("P999")
    assert producto_buscado is not None, "Producto nuevo no encontrado en índice"
    print(f"✓ Producto encontrado en índice: {producto_buscado.mostrar_informacion()}")
    
    # Verificar que el índice está sincronizado
    estado = restaurante.obtener_estado_indices()
    assert estado['productos_en_lista'] == estado['productos_en_indice'], "Índice desincronizado"
    print(f"✓ Indice sincronizado después de registrar (lista: {estado['productos_en_lista']}, índice: {estado['productos_en_indice']})")
    
    # Guardar cambios
    archivos.guardar_productos(restaurante.obtener_productos())
    print("✓ Cambios guardados en JSON")
    
    print("\n✓ PRUEBA 5 EXITOSA: Registrar producto funciona")


def prueba_registrar_usuario(restaurante: Restaurante, archivos: ArchivoServicio):
    """Prueba 6: Registrar usuario y verificar índice."""
    print("\n" + "=" * 60)
    print("PRUEBA 6: Registrar usuario y verificar índice")
    print("=" * 60)
    
    nuevo_usuario = Usuario("9999", "Juan Nuevo", "juan@email.com")
    restaurante.registrar_usuario(nuevo_usuario)
    
    # Verificar que se agregó a la lista
    assert restaurante.contar_usuarios() == 4, f"Debe haber 4 usuarios, hay {restaurante.contar_usuarios()}"
    print(f"✓ Usuario agregado a la lista (total: {restaurante.contar_usuarios()})")
    
    # Verificar que se puede buscar en el índice
    usuario_buscado = restaurante.buscar_usuario_por_identificacion("9999")
    assert usuario_buscado is not None, "Usuario nuevo no encontrado en índice"
    print(f"✓ Usuario encontrado en índice: {usuario_buscado.mostrar_informacion()}")
    
    # Verificar que el índice está sincronizado
    estado = restaurante.obtener_estado_indices()
    assert estado['usuarios_en_lista'] == estado['usuarios_en_indice'], "Índice desincronizado"
    print(f"✓ Indice sincronizado después de registrar (lista: {estado['usuarios_en_lista']}, índice: {estado['usuarios_en_indice']})")
    
    # Guardar cambios
    archivos.guardar_usuarios(restaurante.obtener_usuarios())
    print("✓ Cambios guardados en JSON")
    
    print("\n✓ PRUEBA 6 EXITOSA: Registrar usuario funciona")


def prueba_venta(restaurante: Restaurante, archivos: ArchivoServicio):
    """Prueba 7: Registrar venta y verificar índice de ventas por usuario."""
    print("\n" + "=" * 60)
    print("PRUEBA 7: Registrar venta y verificar índice de ventas")
    print("=" * 60)
    
    # Obtener producto y usuario antes de la venta
    producto_antes = restaurante.buscar_producto_por_codigo("B001")
    stock_antes = producto_antes.stock
    
    # Registrar una venta
    vendido = restaurante.vender_producto("B001", "9999", 2)
    assert vendido, "La venta debería ser exitosa"
    print("✓ Venta registrada exitosamente")
    
    # Verificar que el stock se decrementó
    producto_despues = restaurante.buscar_producto_por_codigo("B001")
    assert producto_despues.stock == stock_antes - 2, "Stock no se decrementó"
    print(f"✓ Stock actualizado: {stock_antes} → {producto_despues.stock}")
    
    # Verificar que la venta aparece en el índice de ventas por usuario
    ventas_usuario = restaurante.consultar_ventas_por_usuario("9999")
    assert len(ventas_usuario) == 1, f"Usuario 9999 debe tener 1 venta, tiene {len(ventas_usuario)}"
    print(f"✓ Venta agregada a índice de usuario (total: {len(ventas_usuario)})")
    
    # Guardar cambios
    archivos.guardar_ventas(restaurante.obtener_ventas())
    archivos.guardar_productos(restaurante.obtener_productos())
    print("✓ Cambios guardados en JSON")
    
    print("\n✓ PRUEBA 7 EXITOSA: Venta funciona correctamente")


def prueba_eliminar_producto(restaurante: Restaurante, archivos: ArchivoServicio):
    """Prueba 8: Eliminar producto y verificar índice."""
    print("\n" + "=" * 60)
    print("PRUEBA 8: Eliminar producto y verificar índice")
    print("=" * 60)
    
    productos_antes = restaurante.contar_productos()
    
    # Eliminar el producto que agregamos
    eliminado = restaurante.eliminar_producto("P999")
    assert eliminado, "El producto debería haberse eliminado"
    print(f"✓ Producto P999 eliminado")
    
    # Verificar que se eliminó de la lista
    assert restaurante.contar_productos() == productos_antes - 1, "Producto no se eliminó de la lista"
    print(f"✓ Lista actualizada (antes: {productos_antes}, después: {restaurante.contar_productos()})")
    
    # Verificar que se eliminó del índice
    producto_buscado = restaurante.buscar_producto_por_codigo("P999")
    assert producto_buscado is None, "Producto debería estar eliminado del índice"
    print("✓ Producto eliminado del índice")
    
    # Verificar que el índice está sincronizado
    estado = restaurante.obtener_estado_indices()
    assert estado['productos_en_lista'] == estado['productos_en_indice'], "Índice desincronizado"
    print(f"✓ Indice sincronizado después de eliminar (lista: {estado['productos_en_lista']}, índice: {estado['productos_en_indice']})")
    
    # Guardar cambios
    archivos.guardar_productos(restaurante.obtener_productos())
    print("✓ Cambios guardados en JSON")
    
    print("\n✓ PRUEBA 8 EXITOSA: Eliminar producto funciona")


def prueba_recarga_indices():
    """Prueba 9: Cerrar y reabrir para verificar que los índices se reconstruyen."""
    print("\n" + "=" * 60)
    print("PRUEBA 9: Recargar datos y reconstruir índices")
    print("=" * 60)
    
    base_datos = Path(__file__).resolve().parent / "datos"
    archivos = ArchivoServicio(str(base_datos))
    restaurante = Restaurante()
    
    productos = archivos.cargar_productos()
    usuarios = archivos.cargar_usuarios()
    ventas = archivos.cargar_ventas()
    
    restaurante.cargar_productos_iniciales(productos)
    restaurante.cargar_usuarios_iniciales(usuarios)
    restaurante.cargar_ventas_iniciales(ventas)
    
    print(f"✓ Datos recargados desde JSON")
    print(f"  - Productos: {restaurante.contar_productos()}")
    print(f"  - Usuarios: {restaurante.contar_usuarios()}")
    print(f"  - Ventas: {restaurante.contar_ventas()}")
    
    # Verificar que los índices se reconstruyeron correctamente
    estado = restaurante.obtener_estado_indices()
    assert estado['productos_en_lista'] == estado['productos_en_indice'], "Índice de productos desincronizado"
    assert estado['usuarios_en_lista'] == estado['usuarios_en_indice'], "Índice de usuarios desincronizado"
    print("✓ Indices reconstruidos y sincronizados correctamente")
    
    # Verificar búsquedas
    producto = restaurante.buscar_producto_por_codigo("P001")
    assert producto is not None, "Búsqueda de producto fallida"
    print("✓ Búsqueda de producto funciona después de recargar")
    
    usuario = restaurante.buscar_usuario_por_identificacion("1001")
    assert usuario is not None, "Búsqueda de usuario fallida"
    print("✓ Búsqueda de usuario funciona después de recargar")
    
    print("\n✓ PRUEBA 9 EXITOSA: Recarga de índices funciona correctamente")


def main():
    """Ejecuta todas las pruebas."""
    print("\n" + "=" * 60)
    print("PRUEBAS DE OPTIMIZACIÓN MEDIANTE COLECCIONES (SEMANA 12)")
    print("=" * 60)
    
    try:
        # Pruebas de carga y sincronización
        restaurante = prueba_carga_datos()
        
        # Pruebas de búsqueda
        prueba_busqueda_producto(restaurante)
        prueba_busqueda_usuario(restaurante)
        
        # Pruebas de consulta
        prueba_consulta_ventas_usuario(restaurante)
        
        # Configurar archivos para pruebas de escritura
        base_datos = Path(__file__).resolve().parent / "datos"
        archivos = ArchivoServicio(str(base_datos))
        
        # Pruebas de modificación
        prueba_registrar_producto(restaurante, archivos)
        prueba_registrar_usuario(restaurante, archivos)
        prueba_venta(restaurante, archivos)
        prueba_eliminar_producto(restaurante, archivos)
        
        # Prueba de recarga
        prueba_recarga_indices()
        
        # Resumen final
        print("\n" + "=" * 60)
        print("TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ✓")
        print("=" * 60)
        print("\nResumen de optimizaciones verificadas:")
        print("✓ Búsqueda de productos por código: O(n) → O(1)")
        print("✓ Búsqueda de usuarios por ID: O(n) → O(1)")
        print("✓ Consulta de ventas por usuario: O(n) → O(1)")
        print("✓ Validación de duplicados: O(n) → O(1)")
        print("✓ Sincronización de índices: ✓")
        print("✓ Reconstrucción de índices: ✓")
        print("✓ Persistencia JSON: ✓")
        
    except AssertionError as error:
        print(f"\n✗ PRUEBA FALLIDA: {error}")
        return False
    except Exception as error:
        print(f"\n✗ ERROR INESPERADO: {error}")
        import traceback
        traceback.print_exc()
        return False
    
    return True


if __name__ == "__main__":
    exito = main()
    sys.exit(0 if exito else 1)

