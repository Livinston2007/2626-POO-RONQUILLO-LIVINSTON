from __future__ import annotations
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


def solicitar_numero(prompt: str) -> float:
    """Solicita un número al usuario hasta que ingrese un valor válido."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Ingrese un número válido.\n")


def registrar_producto(serv: Restaurante, archivo_serv: ArchivoServicio) -> None:
    """Solicita datos y registra un nuevo producto."""
    print("\n--- Registrar Producto ---")
    codigo = input("Código del producto: ").strip()
    
    if not codigo:
        print("Error: El código no puede estar vacío.\n")
        return
    
    nombre = input("Nombre del producto: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.\n")
        return
    
    categoria = input("Categoría: ").strip()
    if not categoria:
        print("Error: La categoría no puede estar vacía.\n")
        return
    
    precio = solicitar_numero("Precio: $")
    if precio < 0:
        print("Error: El precio no puede ser negativo.\n")
        return
    
    producto = Producto(codigo, nombre, categoria, precio)
    try:
        serv.registrar_producto(producto)
        archivo_serv.guardar_productos(serv.obtener_productos())
        print(f"✓ Producto '{nombre}' registrado correctamente.\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")
    except Exception as e:
        print(f"✗ Error al guardar: {e}\n")


def buscar_producto(serv: Restaurante) -> None:
    """Busca un producto por su código."""
    print("\n--- Buscar Producto ---")
    codigo = input("Código del producto a buscar: ").strip()
    
    if not codigo:
        print("Error: El código no puede estar vacío.\n")
        return
    
    producto = serv.buscar_producto_por_codigo(codigo)
    if producto:
        print(f"\n{producto.mostrar_informacion()}\n")
    else:
        print(f"✗ No se encontró producto con código '{codigo}'.\n")


def actualizar_producto(serv: Restaurante, archivo_serv: ArchivoServicio) -> None:
    """Actualiza los datos de un producto existente."""
    print("\n--- Actualizar Producto ---")
    codigo = input("Código del producto a actualizar: ").strip()
    
    if not codigo:
        print("Error: El código no puede estar vacío.\n")
        return
    
    producto = serv.buscar_producto_por_codigo(codigo)
    if not producto:
        print(f"✗ No se encontró producto con código '{codigo}'.\n")
        return
    
    print(f"\nProducto encontrado: {producto.mostrar_informacion()}")
    print("Ingrese los nuevos datos (deje en blanco para mantener el actual):")
    
    nuevo_nombre = input("Nuevo nombre (actual: " + producto.nombre + "): ").strip()
    nueva_categoria = input("Nueva categoría (actual: " + producto.categoria + "): ").strip()
    nuevo_precio_str = input("Nuevo precio (actual: $" + f"{producto.precio:.2f}" + "): ").strip()
    
    nuevo_precio = None
    if nuevo_precio_str:
        try:
            nuevo_precio = float(nuevo_precio_str)
            if nuevo_precio < 0:
                print("Error: El precio no puede ser negativo.\n")
                return
        except ValueError:
            print("Error: Ingrese un precio válido.\n")
            return
    
    if serv.actualizar_producto(codigo, nuevo_nombre if nuevo_nombre else None,
                               nueva_categoria if nueva_categoria else None, nuevo_precio):
        archivo_serv.guardar_productos(serv.obtener_productos())
        print("✓ Producto actualizado correctamente.\n")
    else:
        print("✗ Error al actualizar el producto.\n")


def eliminar_producto(serv: Restaurante, archivo_serv: ArchivoServicio) -> None:
    """Elimina un producto por su código."""
    print("\n--- Eliminar Producto ---")
    codigo = input("Código del producto a eliminar: ").strip()
    
    if not codigo:
        print("Error: El código no puede estar vacío.\n")
        return
    
    producto = serv.buscar_producto_por_codigo(codigo)
    if not producto:
        print(f"✗ No se encontró producto con código '{codigo}'.\n")
        return
    
    print(f"Producto a eliminar: {producto.mostrar_informacion()}")
    confirmacion = input("¿Desea eliminar este producto? (s/n): ").strip().lower()
    
    if confirmacion == 's':
        if serv.eliminar_producto(codigo):
            archivo_serv.guardar_productos(serv.obtener_productos())
            print("✓ Producto eliminado correctamente.\n")
        else:
            print("✗ Error al eliminar el producto.\n")
    else:
        print("Operación cancelada.\n")


def listar_productos(serv: Restaurante) -> None:
    """Lista todos los productos registrados."""
    print("\n--- Listar Productos ---")
    productos = serv.listar_productos()
    
    if not productos:
        print("No hay productos registrados.\n")
        return
    
    print(f"\nTotal de productos: {serv.contar_productos()}\n")
    for info in productos:
        print(info)
    print()


def mostrar_categorias(serv: Restaurante) -> None:
    """Muestra las categorías únicas de los productos registrados."""
    print("\n--- Categorías de Productos ---")
    categorias = serv.obtener_categorias_unicas()
    
    if not categorias:
        print("No hay categorías registradas (no hay productos).\n")
        return
    
    print(f"\nCategorías únicas ({len(categorias)}):\n")
    for categoria in sorted(categorias):
        print(f"  • {categoria}")
    print()


def registrar_usuario(serv: Restaurante) -> None:
    """Solicita datos y registra un nuevo usuario."""
    print("\n--- Registrar Usuario ---")
    identificacion = input("Identificación del usuario: ").strip()
    
    if not identificacion:
        print("Error: La identificación no puede estar vacía.\n")
        return
    
    nombre = input("Nombre del usuario: ").strip()
    if not nombre:
        print("Error: El nombre no puede estar vacío.\n")
        return
    
    correo = input("Correo del usuario: ").strip()
    if not correo:
        print("Error: El correo no puede estar vacío.\n")
        return
    
    usuario = Usuario(identificacion, nombre, correo)
    try:
        serv.registrar_usuario(usuario)
        print(f"✓ Usuario '{nombre}' registrado correctamente.\n")
    except ValueError as e:
        print(f"✗ Error: {e}\n")


def listar_usuarios(serv: Restaurante) -> None:
    """Lista todos los usuarios registrados."""
    print("\n--- Listar Usuarios ---")
    usuarios = serv.listar_usuarios()
    
    if not usuarios:
        print("No hay usuarios registrados.\n")
        return
    
    print(f"\nTotal de usuarios: {serv.contar_usuarios()}\n")
    for info in usuarios:
        print(info)
    print()


def menu() -> None:
    """Ejecuta el menú interactivo del sistema de restaurante."""
    archivo_serv = ArchivoServicio("datos/productos.json")
    serv = Restaurante()
    
    # Cargar productos almacenados al iniciar
    try:
        productos_cargados = archivo_serv.cargar_productos()
        serv.cargar_productos_iniciales(productos_cargados)
        if productos_cargados:
            print(f"✓ Se cargaron {len(productos_cargados)} producto(s) desde el archivo.\n")
    except Exception as e:
        print(f"✗ Error al cargar productos: {e}\n")
    
    opciones_productos: tuple = ("1", "2", "3", "4", "5", "8")
    opciones_usuarios: tuple = ("6", "7")
    
    opciones_dict: dict = {
        "1": lambda: registrar_producto(serv, archivo_serv),
        "2": lambda: buscar_producto(serv),
        "3": lambda: actualizar_producto(serv, archivo_serv),
        "4": lambda: eliminar_producto(serv, archivo_serv),
        "5": lambda: listar_productos(serv),
        "6": lambda: registrar_usuario(serv),
        "7": lambda: listar_usuarios(serv),
        "8": lambda: mostrar_categorias(serv),
    }
    
    while True:
        print("\n" + "="*40)
        print("        SISTEMA DE RESTAURANTE")
        print("="*40)
        print("1. Registrar producto")
        print("2. Buscar producto")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Listar productos")
        print("-"*40)
        print("6. Registrar usuario")
        print("7. Listar usuarios")
        print("-"*40)
        print("8. Mostrar categorías")
        print("9. Salir")
        print("="*40)
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "9":
            print("\n¡Hasta luego!\n")
            break
        
        if opcion not in opciones_productos and opcion not in opciones_usuarios and opcion != "8":
            print("✗ Opción no válida. Intente nuevamente.\n")
            continue
        
        accion = opciones_dict.get(opcion)
        if accion:
            try:
                accion()
            except Exception as e:
                print(f"✗ Error inesperado: {e}\n")
        else:
            print("✗ Opción no disponible.\n")


if __name__ == "__main__":
    menu()
