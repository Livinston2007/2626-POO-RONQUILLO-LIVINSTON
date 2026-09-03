"""
Script de demostración interactivo que muestra todas las características
de la Semana 12: Optimización de Búsquedas mediante Colecciones.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante


def limpiar_pantalla():
    """Limpia la pantalla."""
    print("\n" + "=" * 70 + "\n")


def demo_1_carga_inicial():
    """Demo 1: Carga de datos iniciales y verificación de índices."""
    limpiar_pantalla()
    print("DEMO 1: CARGA DE DATOS INICIALES Y SINCRONIZACIÓN DE ÍNDICES")
    print("=" * 70)

    base_datos = Path(__file__).resolve().parent / "datos"
    archivos = ArchivoServicio(str(base_datos))
    restaurante = Restaurante()

    print("\n📂 Cargando datos desde JSON...")
    productos = archivos.cargar_productos()
    usuarios = archivos.cargar_usuarios()
    ventas = archivos.cargar_ventas()

    restaurante.cargar_productos_iniciales(productos)
    restaurante.cargar_usuarios_iniciales(usuarios)
    restaurante.cargar_ventas_iniciales(ventas)

    print(f"   ✓ {len(productos)} productos cargados")
    print(f"   ✓ {len(usuarios)} usuarios cargados")
    print(f"   ✓ {len(ventas)} ventas cargadas")

    print("\n🔍 Verificando sincronización de índices...")
    estado = restaurante.obtener_estado_indices()
    print(f"   Productos (lista/índice): {estado['productos_en_lista']}/{estado['productos_en_indice']}")
    print(f"   Usuarios (lista/índice): {estado['usuarios_en_lista']}/{estado['usuarios_en_indice']}")
    print(f"   Ventas totales: {estado['ventas_totales']}")
    print(f"   Usuarios con ventas: {estado['usuarios_con_ventas']}")

    if (estado['productos_en_lista'] == estado['productos_en_indice'] and
        estado['usuarios_en_lista'] == estado['usuarios_en_indice']):
        print("\n✅ Índices sincronizados correctamente")
    else:
        print("\n❌ Advertencia: Índices desincronizados")

    return restaurante, archivos


def demo_2_busqueda_productos(restaurante):
    """Demo 2: Búsqueda optimizada de productos (O(1))."""
    limpiar_pantalla()
    print("DEMO 2: BÚSQUEDA DE PRODUCTOS OPTIMIZADA (O(1))")
    print("=" * 70)

    print("\n🔍 Buscando productos por código usando ÍNDICE (O(1))...\n")

    codigos = ["P001", "B002", "D001", "INEXISTENTE"]

    for codigo in codigos:
        producto = restaurante.buscar_producto_por_codigo(codigo)
        if producto:
            print(f"   ✓ {producto.mostrar_informacion()}")
        else:
            print(f"   ✗ {codigo} - Producto no encontrado")

    print("\n💡 Nota: Estas búsquedas son O(1) - acceso directo al diccionario")
    print("   Antes (Semana 11) eran O(n) - recorrían toda la lista")


def demo_3_busqueda_usuarios(restaurante):
    """Demo 3: Búsqueda optimizada de usuarios (O(1))."""
    limpiar_pantalla()
    print("DEMO 3: BÚSQUEDA DE USUARIOS OPTIMIZADA (O(1))")
    print("=" * 70)

    print("\n🔍 Buscando usuarios por ID usando ÍNDICE (O(1))...\n")

    ids = ["1001", "1002", "1003", "INEXISTENTE"]

    for usuario_id in ids:
        usuario = restaurante.buscar_usuario_por_identificacion(usuario_id)
        if usuario:
            print(f"   ✓ {usuario.mostrar_informacion()}")
        else:
            print(f"   ✗ {usuario_id} - Usuario no encontrado")

    print("\n💡 Nota: Estas búsquedas son O(1) - acceso directo al diccionario")


def demo_4_consulta_ventas(restaurante):
    """Demo 4: Consulta optimizada de ventas por usuario (O(1))."""
    limpiar_pantalla()
    print("DEMO 4: CONSULTA DE VENTAS POR USUARIO OPTIMIZADA (O(1))")
    print("=" * 70)

    print("\n📊 Consultando ventas de cada usuario usando ÍNDICE (O(1))...\n")

    usuarios_ids = ["1001", "1002", "1003"]

    for usuario_id in usuarios_ids:
        ventas = restaurante.consultar_ventas_por_usuario(usuario_id)
        usuario = restaurante.buscar_usuario_por_identificacion(usuario_id)

        print(f"   Usuario: {usuario.nombre} (ID: {usuario_id})")
        if ventas:
            for venta in ventas:
                desc = restaurante.describir_venta(venta)
                print(f"      - {desc}")
            print(f"      → Total: {len(ventas)} venta(s)")
        else:
            print(f"      → Sin ventas")
        print()

    print("💡 Nota: Acceso O(1) al diccionario de ventas por usuario")
    print("   Antes (Semana 11) recorría TODAS las ventas cada vez (O(n))")


def demo_5_registrar_producto(restaurante, archivos):
    """Demo 5: Registrar producto y verificar índice."""
    limpiar_pantalla()
    print("DEMO 5: REGISTRAR PRODUCTO Y VERIFICAR ÍNDICE")
    print("=" * 70)

    print("\n✍️  Registrando nuevo producto...\n")

    nuevo_producto = Producto("S001", "Sandwich Especial", "Comidas", 14000.0, 25)
    restaurante.registrar_producto(nuevo_producto)

    print(f"   ✓ Producto registrado: {nuevo_producto.mostrar_informacion()}")

    print("\n🔍 Verificando que se puede buscar inmediatamente...\n")

    producto_buscado = restaurante.buscar_producto_por_codigo("S001")

    if producto_buscado:
        print(f"   ✓ Búsqueda exitosa (O(1)): {producto_buscado.mostrar_informacion()}")

    print("\n📊 Verificando sincronización de índice...\n")

    estado = restaurante.obtener_estado_indices()
    print(f"   Productos en lista: {estado['productos_en_lista']}")
    print(f"   Productos en índice: {estado['productos_en_indice']}")

    if estado['productos_en_lista'] == estado['productos_en_indice']:
        print("   ✓ Índice sincronizado")

    archivos.guardar_productos(restaurante.obtener_productos())


def demo_6_venta_completa(restaurante, archivos):
    """Demo 6: Procesar una venta completa."""
    limpiar_pantalla()
    print("DEMO 6: PROCESAR VENTA COMPLETA (MÚLTIPLES BÚSQUEDAS O(1))")
    print("=" * 70)

    print("\n💳 Procesando venta...")
    print("   Usuario: 1001")
    print("   Producto: S001 (Sandwich Especial)")
    print("   Cantidad: 3")

    usuario_antes = restaurante.buscar_usuario_por_identificacion("1001")
    producto_antes = restaurante.buscar_producto_por_codigo("S001")
    ventas_antes = restaurante.consultar_ventas_por_usuario("1001")

    print(f"\n📊 ANTES:")
    print(f"   Producto S001 - Stock: {producto_antes.stock}")
    print(f"   Usuario 1001 - Ventas: {len(ventas_antes)}")

    # Realizar venta
    print(f"\n⏳ Realizando venta...")
    exito = restaurante.vender_producto("S001", "1001", 3)

    if exito:
        print("   ✓ Venta registrada exitosamente")

        usuario_despues = restaurante.buscar_usuario_por_identificacion("1001")
        producto_despues = restaurante.buscar_producto_por_codigo("S001")
        ventas_despues = restaurante.consultar_ventas_por_usuario("1001")

        print(f"\n📊 DESPUÉS:")
        print(f"   Producto S001 - Stock: {producto_despues.stock} (decrementado)")
        print(f"   Usuario 1001 - Ventas: {len(ventas_despues)} (incrementado)")

        print(f"\n💡 Nota: Todas estas búsquedas fueron O(1):")
        print(f"   - Búsqueda de usuario (1 acceso al índice)")
        print(f"   - Búsqueda de producto (1 acceso al índice)")
        print(f"   - Actualización de ventas (1 acceso al índice)")
        print(f"   - Consulta de ventas del usuario (1 acceso al índice)")

        archivos.guardar_ventas(restaurante.obtener_ventas())
        archivos.guardar_productos(restaurante.obtener_productos())
    else:
        print("   ✗ Venta rechazada")


def demo_7_diagnostico_final(restaurante):
    """Demo 7: Diagnóstico final de índices."""
    limpiar_pantalla()
    print("DEMO 7: DIAGNÓSTICO FINAL DE ÍNDICES")
    print("=" * 70)

    print("\n🔧 Estado completo del sistema:\n")

    estado = restaurante.obtener_estado_indices()

    print(f"   Productos:")
    print(f"      En lista: {estado['productos_en_lista']}")
    print(f"      En índice: {estado['productos_en_indice']}")

    print(f"\n   Usuarios:")
    print(f"      En lista: {estado['usuarios_en_lista']}")
    print(f"      En índice: {estado['usuarios_en_indice']}")

    print(f"\n   Ventas:")
    print(f"      Total: {estado['ventas_totales']}")
    print(f"      Usuarios con ventas: {estado['usuarios_con_ventas']}")

    # Validar sincronización
    sincronizado = (
        estado['productos_en_lista'] == estado['productos_en_indice'] and
        estado['usuarios_en_lista'] == estado['usuarios_en_indice']
    )

    print(f"\n   Sincronización:")
    if sincronizado:
        print(f"      ✅ SINCRONIZADO - Todos los índices están coherentes")
    else:
        print(f"      ❌ DESINCRONIZADO - Hay inconsistencias")

    print("\n💡 Resumen de mejoras de Semana 12:")
    print("   ✓ Búsquedas de productos: O(n) → O(1)")
    print("   ✓ Búsquedas de usuarios: O(n) → O(1)")
    print("   ✓ Consultas de ventas: O(n) → O(1)")
    print("   ✓ Validaciones de duplicados: O(n) → O(1)")
    print("   ✓ Sincronización automática de índices")
    print("   ✓ Reconstrucción al iniciar")


def main():
    """Ejecuta todas las demostraciones."""
    print("\n" + "=" * 70)
    print("  DEMOSTRACIÓN COMPLETA: SEMANA 12")
    print("  Optimización de Búsquedas mediante Colecciones")
    print("=" * 70)

    try:
        # Demo 1: Carga inicial
        restaurante, archivos = demo_1_carga_inicial()

        input("\n[Presiona ENTER para continuar...]")

        # Demo 2: Búsqueda de productos
        demo_2_busqueda_productos(restaurante)
        input("\n[Presiona ENTER para continuar...]")

        # Demo 3: Búsqueda de usuarios
        demo_3_busqueda_usuarios(restaurante)
        input("\n[Presiona ENTER para continuar...]")

        # Demo 4: Consulta de ventas
        demo_4_consulta_ventas(restaurante)
        input("\n[Presiona ENTER para continuar...]")

        # Demo 5: Registrar producto
        demo_5_registrar_producto(restaurante, archivos)
        input("\n[Presiona ENTER para continuar...]")

        # Demo 6: Venta completa
        demo_6_venta_completa(restaurante, archivos)
        input("\n[Presiona ENTER para continuar...]")

        # Demo 7: Diagnóstico
        demo_7_diagnostico_final(restaurante)

        limpiar_pantalla()
        print("✅ DEMOSTRACIÓN COMPLETADA EXITOSAMENTE")
        print("=" * 70)
        print("\nPara usar el programa interactivo:")
        print("   python restaurante_app/main.py")
        print("\nPara ejecutar pruebas automáticas:")
        print("   python restaurante_app/test_semana_12.py")
        print("\n" + "=" * 70 + "\n")

    except Exception as error:
        print(f"\n❌ Error: {error}")
        import traceback
        traceback.print_exc()
        return False

    return True


if __name__ == "__main__":
    exito = main()
    sys.exit(0 if exito else 1)

