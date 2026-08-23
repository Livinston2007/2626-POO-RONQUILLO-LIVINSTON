"""Script de prueba automatizado para verificar la persistencia de productos."""
from __future__ import annotations
import json
import os
from pathlib import Path
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.modelos.producto import Producto


def test_serialización() -> None:
    """Prueba que los métodos de serialización funcionan correctamente."""
    print("\n" + "="*60)
    print("TEST 1: Serialización de Producto")
    print("="*60)
    
    # Crear un producto
    p = Producto("P001", "Hamburguesa", "Comida Rápida", 12.50)
    print(f"✓ Producto creado: {p.mostrar_informacion()}")
    
    # Convertir a diccionario
    dict_p = p.a_diccionario()
    print(f"✓ Convertido a diccionario: {dict_p}")
    
    # Convertir de vuelta
    p2 = Producto.desde_diccionario(dict_p)
    print(f"✓ Reconvertido desde diccionario: {p2.mostrar_informacion()}")
    
    # Verificar que son idénticos
    assert p.codigo == p2.codigo
    assert p.nombre == p2.nombre
    assert p.categoria == p2.categoria
    assert p.precio == p2.precio
    print("✓ Los datos se preservaron correctamente en la conversión")


def test_archivo_vacio() -> None:
    """Prueba que el servicio carga una lista vacía si el archivo no existe."""
    print("\n" + "="*60)
    print("TEST 2: Carga de archivo vacío/inexistente")
    print("="*60)
    
    # Usar ruta que no existe
    archivo_serv = ArchivoServicio("datos/test_inexistente.json")
    
    # Intentar cargar
    productos = archivo_serv.cargar_productos()
    print(f"✓ Cargados {len(productos)} productos (esperado: 0)")
    assert len(productos) == 0


def test_guardar_y_cargar() -> None:
    """Prueba que se pueden guardar y cargar productos."""
    print("\n" + "="*60)
    print("TEST 3: Guardar y cargar productos")
    print("="*60)
    
    ruta_test = "datos/test_persistencia.json"
    archivo_serv = ArchivoServicio(ruta_test)
    
    # Limpiar archivo si existe
    Path(ruta_test).unlink(missing_ok=True)
    
    # Crear algunos productos
    productos_original = [
        Producto("P001", "Hamburguesa", "Comida Rápida", 12.50),
        Producto("P002", "Ensalada", "Ensaladas", 8.99),
        Producto("P003", "Refresco", "Bebidas", 3.50),
    ]
    
    # Guardar
    archivo_serv.guardar_productos(productos_original)
    print(f"✓ Guardados {len(productos_original)} productos en {ruta_test}")
    
    # Verificar que el archivo existe y contiene JSON válido
    assert Path(ruta_test).exists(), "El archivo no fue creado"
    with open(ruta_test, 'r', encoding='utf-8') as f:
        datos = json.load(f)
    print(f"✓ Archivo JSON creado correctamente con {len(datos)} elementos")
    
    # Cargar de vuelta
    productos_cargados = archivo_serv.cargar_productos()
    print(f"✓ Cargados {len(productos_cargados)} productos")
    
    # Verificar que coinciden
    assert len(productos_cargados) == len(productos_original)
    for orig, cargado in zip(productos_original, productos_cargados):
        assert orig.codigo == cargado.codigo
        assert orig.nombre == cargado.nombre
        assert orig.categoria == cargado.categoria
        assert orig.precio == cargado.precio
    print("✓ Todos los productos se cargaron correctamente")
    
    # Limpiar
    Path(ruta_test).unlink(missing_ok=True)


def test_integracion_restaurante() -> None:
    """Prueba la integración completa con Restaurante."""
    print("\n" + "="*60)
    print("TEST 4: Integración con Restaurante")
    print("="*60)
    
    ruta_test = "datos/test_restaurante.json"
    Path(ruta_test).unlink(missing_ok=True)
    
    archivo_serv = ArchivoServicio(ruta_test)
    serv = Restaurante()
    
    # Registrar productos
    p1 = Producto("R001", "Pizza", "Platos Fuertes", 15.00)
    serv.registrar_producto(p1)
    print(f"✓ Registrado: {p1.mostrar_informacion()}")
    
    # Guardar
    archivo_serv.guardar_productos(serv.obtener_productos())
    print("✓ Guardado en archivo")
    
    # Crear nuevo restaurante y cargar
    serv2 = Restaurante()
    productos_cargados = archivo_serv.cargar_productos()
    serv2.cargar_productos_iniciales(productos_cargados)
    
    print(f"✓ Nuevo restaurante cargó {serv2.contar_productos()} producto(s)")
    
    # Buscar el producto
    p_buscado = serv2.buscar_producto_por_codigo("R001")
    assert p_buscado is not None
    assert p_buscado.nombre == "Pizza"
    print(f"✓ Producto encontrado y verificado: {p_buscado.mostrar_informacion()}")
    
    # Limpiar
    Path(ruta_test).unlink(missing_ok=True)


def test_actualización_y_eliminación() -> None:
    """Prueba que actualizar y eliminar actualiza el archivo."""
    print("\n" + "="*60)
    print("TEST 5: Actualización y eliminación con persistencia")
    print("="*60)
    
    ruta_test = "datos/test_operaciones.json"
    Path(ruta_test).unlink(missing_ok=True)
    
    archivo_serv = ArchivoServicio(ruta_test)
    serv = Restaurante()
    
    # Registrar
    p = Producto("O001", "Tacos", "Comida Mexicana", 6.50)
    serv.registrar_producto(p)
    archivo_serv.guardar_productos(serv.obtener_productos())
    print("✓ Producto registrado y guardado")
    
    # Actualizar
    serv.actualizar_producto("O001", nombre="Tacos al Pastor", precio=7.00)
    archivo_serv.guardar_productos(serv.obtener_productos())
    print("✓ Producto actualizado y guardado")
    
    # Cargar y verificar actualización
    serv2 = Restaurante()
    serv2.cargar_productos_iniciales(archivo_serv.cargar_productos())
    p_actualizado = serv2.buscar_producto_por_codigo("O001")
    assert p_actualizado.nombre == "Tacos al Pastor"
    assert p_actualizado.precio == 7.00
    print(f"✓ Actualización confirmada: {p_actualizado.mostrar_informacion()}")
    
    # Eliminar
    serv.eliminar_producto("O001")
    archivo_serv.guardar_productos(serv.obtener_productos())
    print("✓ Producto eliminado y guardado")
    
    # Cargar y verificar que se eliminó
    serv3 = Restaurante()
    serv3.cargar_productos_iniciales(archivo_serv.cargar_productos())
    assert serv3.contar_productos() == 0
    print(f"✓ Eliminación confirmada: {serv3.contar_productos()} productos")
    
    # Limpiar
    Path(ruta_test).unlink(missing_ok=True)


def test_manejo_errores_json() -> None:
    """Prueba que el sistema maneja errores JSON correctamente."""
    print("\n" + "="*60)
    print("TEST 6: Manejo de errores JSON")
    print("="*60)
    
    ruta_test = "datos/test_error.json"
    Path(ruta_test).parent.mkdir(parents=True, exist_ok=True)
    
    # Crear JSON inválido
    with open(ruta_test, 'w', encoding='utf-8') as f:
        f.write("{ esto no es JSON válido }")
    print("✓ Creado archivo JSON inválido")
    
    archivo_serv = ArchivoServicio(ruta_test)
    
    # Intentar cargar debe capturar el error
    try:
        productos = archivo_serv.cargar_productos()
        print(f"✗ ERROR: No se lanzó excepción (se retornaron {len(productos)} productos)")
    except Exception as e:
        print(f"✓ Excepción capturada correctamente: {type(e).__name__}")
    
    # Limpiar
    Path(ruta_test).unlink(missing_ok=True)


def main() -> None:
    """Ejecuta todos los tests."""
    print("\n" + "="*60)
    print("PRUEBAS DE PERSISTENCIA JSON - RESTAURANTE APP SEMANA 10")
    print("="*60)
    
    try:
        test_serialización()
        test_archivo_vacio()
        test_guardar_y_cargar()
        test_integracion_restaurante()
        test_actualización_y_eliminación()
        test_manejo_errores_json()
        
        print("\n" + "="*60)
        print("✓ TODAS LAS PRUEBAS PASARON EXITOSAMENTE")
        print("="*60 + "\n")
        
    except AssertionError as e:
        print(f"\n✗ PRUEBA FALLIDA: {e}\n")
    except Exception as e:
        print(f"\n✗ ERROR INESPERADO: {e}\n")


if __name__ == "__main__":
    main()
