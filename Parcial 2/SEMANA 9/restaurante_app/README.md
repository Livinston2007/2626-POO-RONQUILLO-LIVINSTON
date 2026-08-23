# Sistema de Restaurante - Semana 9

## Descripción General

El sistema de restaurante es una aplicación de consola que administra productos y usuarios de un restaurante. Esta es la versión de **Semana 9**, que representa una evolución significativa desde las semanas anteriores, incorporando estructuras de datos fundamentales de Python para la administración eficiente de colecciones de objetos.

## Mejoras Principales - Semana 9

### Refactorización de Usuarios
- Renombrado `Cliente` → `Usuario` para representar de forma más general a las personas registradas en el sistema
- Esto permite una evolución posterior hacia diferentes tipos de usuarios (clientes, empleados, administradores) sin necesidad de modificar la arquitectura actual

### Operaciones CRUD Completas para Productos
- **Crear**: Registrar un nuevo producto
- **Leer**: Buscar por código y listar todos
- **Actualizar**: Modificar datos de un producto existente
- **Eliminar**: Remover un producto del sistema

### Uso Funcional de Estructuras de Datos

El proyecto implementa de manera integral las cuatro estructuras de datos fundamentales de Python:

#### 1. **Lista (list)**
```python
# En Restaurante.py
self._productos: List[Producto] = []
self._usuarios: List[Usuario] = []
```
- Administran colecciones dinámicas de productos y usuarios
- Permiten operaciones de búsqueda, modificación y eliminación
- Se utiliza para mantener un registro persistente (en tiempo de ejecución) de entidades

#### 2. **Tupla (tuple)**
```python
# En main.py
opciones_tuple: tuple = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
```
- Representa las opciones disponibles del menú principal
- Información inmutable que debe mantenerse estable durante la ejecución
- Se utiliza para validar que la opción ingresada sea válida

#### 3. **Diccionario (dict)**
```python
# En main.py
opciones_dict: dict = {
    "1": registrar_producto,
    "2": buscar_producto,
    "3": actualizar_producto,
    # ... más opciones
}
```
- Establece una relación clara entre la opción del menú y la función a ejecutar
- Permite una implementación elegante y eficiente del despachador de comandos
- Facilita el mantenimiento y extensión del menú

#### 4. **Conjunto (set)**
```python
# En Restaurante.py
def obtener_categorias_unicas(self) -> Set[str]:
    return {p.categoria for p in self._productos}
```
- Obtiene automáticamente las categorías únicas sin duplicados
- Se utiliza en la opción "Mostrar categorías" del menú
- Permite análisis rápido de las categorías disponibles

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Clase Producto
│   └── usuario.py        # Clase Usuario (antes Cliente)
├── servicios/
│   ├── __init__.py
│   └── restaurante.py    # Servicio Restaurante (CRUD y administración)
├── main.py               # Punto de arranque y menú interactivo
└── README.md             # Este archivo
```

## Descripción de Componentes

### modelos/producto.py
Define la clase `Producto` con los siguientes atributos:
- `codigo` (str): Identificador único del producto
- `nombre` (str): Nombre descriptivo del producto
- `categoria` (str): Categoría a la que pertenece (p. ej., "Bebidas", "Comidas")
- `precio` (float): Precio unitario del producto

**Método principal**:
- `mostrar_informacion()`: Retorna una representación legible del producto

### modelos/usuario.py
Define la clase `Usuario` con los siguientes atributos:
- `identificacion` (str): Identificador único del usuario (cédula, pasaporte, etc.)
- `nombre` (str): Nombre completo del usuario
- `correo` (str): Correo electrónico de contacto

**Método principal**:
- `mostrar_informacion()`: Retorna una representación legible de los datos del usuario

### servicios/restaurante.py
Define la clase `Restaurante` que actúa como servicio de administración del sistema.

**Métodos para Productos**:
- `registrar_producto(producto)`: Registra un nuevo producto (valida códigos duplicados)
- `buscar_producto_por_codigo(codigo)`: Busca un producto específico
- `actualizar_producto(codigo, nombre, categoria, precio)`: Modifica los datos de un producto
- `eliminar_producto(codigo)`: Elimina un producto del sistema
- `listar_productos()`: Retorna información de todos los productos
- `obtener_categorias_unicas()`: Retorna un conjunto con las categorías únicas
- `contar_productos()`: Retorna la cantidad de productos registrados

**Métodos para Usuarios**:
- `registrar_usuario(usuario)`: Registra un nuevo usuario (valida identificaciones duplicadas)
- `buscar_usuario_por_identificacion(identificacion)`: Busca un usuario específico
- `listar_usuarios()`: Retorna información de todos los usuarios
- `contar_usuarios()`: Retorna la cantidad de usuarios registrados

**Validaciones**:
- Previene códigos de productos duplicados
- Previene identificaciones de usuarios duplicadas
- Utiliza búsqueda eficiente mediante listas internas

### main.py
Punto de arranque del sistema que implementa:

**Funciones Auxiliares**:
- `solicitar_numero(prompt)`: Valida entrada numérica del usuario

**Funciones de Operación** (cada una solicita datos y usa el servicio):
- `registrar_producto()`: Registra un nuevo producto con validaciones
- `buscar_producto()`: Busca un producto por código
- `actualizar_producto()`: Modifica datos de un producto existente
- `eliminar_producto()`: Elimina un producto con confirmación
- `listar_productos()`: Muestra todos los productos registrados
- `registrar_usuario()`: Registra un nuevo usuario con validaciones
- `listar_usuarios()`: Muestra todos los usuarios registrados
- `mostrar_categorias()`: Muestra las categorías únicas de productos

**Función Menu**:
- `menu()`: Implementa el bucle principal de interacción
- Utiliza **tupla** para validar opciones válidas
- Utiliza **diccionario** para despachar comandos a funciones
- Maneja excepciones para evitar que errores detengan el programa
- Mantiene el programa en ejecución hasta que el usuario seleccione "Salir"

## Menú Interactivo

```
========================================
        SISTEMA DE RESTAURANTE
========================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
----------------------------------------
6. Registrar usuario
7. Listar usuarios
----------------------------------------
8. Mostrar categorías
9. Salir
========================================
```

## Flujo de Ejecución

1. **Inicio**: El usuario ejecuta `main.py`
2. **Menú**: Se muestra el menú interactivo
3. **Selección**: El usuario ingresa una opción (1-9)
4. **Validación**: Se valida que la opción sea válida
5. **Solicitud de Datos**: Se solicitan los datos necesarios según la opción
6. **Validaciones**: Se validan los datos ingresados
7. **Procesamiento**: Se utiliza el servicio `Restaurante` para procesar la operación
8. **Resultado**: Se muestra el resultado de la operación
9. **Iteración**: Se vuelve al menú a menos que se seleccione "Salir"

## Validaciones Implementadas

- ✓ Códigos de productos únicos
- ✓ Identificaciones de usuarios únicas
- ✓ Campos no vacíos (código, nombre, categoría, precio, etc.)
- ✓ Precios no negativos
- ✓ Entrada numérica válida (para precios)
- ✓ Búsqueda de productos antes de actualizar/eliminar
- ✓ Confirmación antes de eliminar
- ✓ Manejo de excepciones en operaciones críticas

## Anotaciones de Tipos

Todo el código utiliza anotaciones de tipos de Python (type hints) para:
- Mejorar la legibilidad del código
- Facilitar el mantenimiento
- Permitir detección de errores en tiempo de desarrollo
- Documentar el propósito de cada variable y función

Ejemplo:
```python
def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
    """Busca un producto por su código."""
```

## Separación de Responsabilidades

- **Modelos** (`modelos/`): Contienen las entidades del sistema (Producto, Usuario)
- **Servicios** (`servicios/`): Contienen la lógica de administración de colecciones (Restaurante)
- **Main** (`main.py`): Coordina la interacción con el usuario y utiliza el servicio

Esta arquitectura asegura que:
- El servicio nunca es modificado directamente desde `main.py`
- Las operaciones de administración de colecciones están centralizadas
- El código es fácil de mantener y extender

## Ejecución del Programa

```bash
python main.py
```

Asegúrese de:
1. Estar en el directorio `restaurante_app/`
2. Tener Python 3.7+ instalado
3. Que los archivos `__init__.py` estén presentes en los directorios `modelos/` y `servicios/`

## Ejemplos de Uso

### Registrar un Producto
```
Seleccione una opción: 1
--- Registrar Producto ---
Código del producto: P001
Nombre del producto: Hamburguesa
Categoría: Comidas
Precio: $12.50
✓ Producto 'Hamburguesa' registrado correctamente.
```

### Buscar un Producto
```
Seleccione una opción: 2
--- Buscar Producto ---
Código del producto a buscar: P001
[Producto] Código: P001 | Nombre: Hamburguesa | Categoría: Comidas | Precio: $12.50
```

### Mostrar Categorías
```
Seleccione una opción: 8
--- Categorías de Productos ---
Categorías únicas (2):
  • Bebidas
  • Comidas
```

## Restricciones Respetadas

✓ Continuación del proyecto `restaurante_app` (no nuevo proyecto)
✓ Uso funcional de las cuatro estructuras de datos
✓ Sin persistencia en archivos o bases de datos
✓ Sin interfaces gráficas
✓ Arquitectura modular mantenida
✓ Operaciones centralizadas en el servicio
✓ Validaciones y manejo de excepciones

## Evolución Futura

Este proyecto está diseñado para evolucionar en semanas posteriores hacia:
- Jerarquías avanzadas de usuarios (Cliente, Empleado, Administrador)
- Funcionalidades de pedidos y facturación
- Persistencia de datos en archivos o bases de datos
- Mejoras en la interfaz de usuario
- Reportes y análisis de datos

---

**Autor**: Ronquillo Livinston  
**Semana**: 9  
**Curso**: Programación Orientada a Objetos  
**Institución**: Universidad  
