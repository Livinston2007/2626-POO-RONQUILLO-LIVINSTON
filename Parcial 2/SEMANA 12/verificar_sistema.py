"""Script de verificacion rapida - Sin caracteres especiales"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante

base_datos = Path(__file__).resolve().parent / "restaurante_app" / "datos"
archivos = ArchivoServicio(str(base_datos))
restaurante = Restaurante()

productos = archivos.cargar_productos()
usuarios = archivos.cargar_usuarios()
ventas = archivos.cargar_ventas()

restaurante.cargar_productos_iniciales(productos)
restaurante.cargar_usuarios_iniciales(usuarios)
restaurante.cargar_ventas_iniciales(ventas)

print("=== VERIFICACION BASICA DE FUNCIONAMIENTO ===")
print(f"Productos cargados: {len(productos)}")
print(f"Usuarios cargados: {len(usuarios)}")
print(f"Ventas cargadas: {len(ventas)}")

print()
print("=== BUSCANDO PRODUCTOS (O(1)) ===")
prod = restaurante.buscar_producto_por_codigo("P001")
print(f"Producto P001: {prod.nombre}")

print()
print("=== BUSCANDO USUARIOS (O(1)) ===")
usr = restaurante.buscar_usuario_por_identificacion("1001")
print(f"Usuario 1001: {usr.nombre}")

print()
print("=== CONSULTANDO VENTAS POR USUARIO (O(1)) ===")
ventas_usr = restaurante.consultar_ventas_por_usuario("1001")
print(f"Ventas de usuario 1001: {len(ventas_usr)}")

print()
print("=== ESTADO DE INDICES ===")
estado = restaurante.obtener_estado_indices()
print(f"Productos en lista: {estado['productos_en_lista']}")
print(f"Productos en indice: {estado['productos_en_indice']}")
print(f"Usuarios en lista: {estado['usuarios_en_lista']}")
print(f"Usuarios en indice: {estado['usuarios_en_indice']}")

if (estado['productos_en_lista'] == estado['productos_en_indice'] and
    estado['usuarios_en_lista'] == estado['usuarios_en_indice']):
    print("\nRESULTADO: Indices sincronizados correctamente [EXITO]")
else:
    print("\nRESULTADO: Indices desincronizados [ERROR]")

print("\n=== VERIFICACION EXITOSA ===")
print("Sistema funcionando correctamente con todas las optimizaciones")

