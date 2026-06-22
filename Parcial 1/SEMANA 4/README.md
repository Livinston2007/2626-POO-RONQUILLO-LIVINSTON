# Sistema de Gestión de Restaurante

## Descripción
Sistema básico de gestión de restaurante desarrollado en Python utilizando Programación Orientada a Objetos (POO). Demuestra organización modular del código, separación de responsabilidades e importaciones entre archivos.

## Estructura del Proyecto

```
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py       # Clase Producto
│   ├── cliente.py         # Clase Cliente
│   └── pedido.py          # Clase Pedido
├── servicios/
│   ├── __init__.py
│   └── restaurante.py     # Clase Restaurante (servicio principal)
└── main.py                # Punto de entrada - demostración del sistema
```

## Clases Implementadas

### 1. **Producto** (`modelos/producto.py`)
Representa un plato, bebida o producto disponible en el restaurante.

**Atributos:**
- `id`: Identificador único (autogenerado)
- `nombre`: Nombre del producto
- `descripcion`: Descripción del producto
- `precio`: Precio en unidades monetarias
- `categoria`: Categoría (plato, bebida, postre)

**Métodos:**
- `obtener_informacion()`: Retorna información del producto como diccionario
- `validar_precio()`: Valida que el precio sea un número positivo
- `actualizar_precio(nuevo_precio)`: Actualiza el precio del producto
- `__str__()`: Representación en texto del producto

### 2. **Cliente** (`modelos/cliente.py`)
Representa una persona que realiza o consume un pedido.

**Atributos:**
- `id`: Identificador único (autogenerado)
- `nombre`: Nombre completo del cliente
- `email`: Correo electrónico
- `telefono`: Número de teléfono
- `fecha_registro`: Fecha y hora de registro (timestamp)

**Métodos:**
- `obtener_informacion()`: Retorna información del cliente como diccionario
- `actualizar_contacto(email=None, telefono=None)`: Actualiza datos de contacto
- `validar_email()`: Valida formato básico del email
- `__str__()`: Representación en texto del cliente

### 3. **Pedido** (`modelos/pedido.py`)
Representa un pedido realizado por un cliente.

**Atributos:**
- `id`: Identificador único (autogenerado)
- `cliente`: Referencia al objeto Cliente
- `productos`: Lista de productos en el pedido
- `estado`: Estado del pedido (pendiente, preparación, listo, entregado, cancelado)
- `fecha_creacion`: Fecha y hora de creación del pedido
- `total`: Total del pedido (calculado automáticamente)

**Métodos:**
- `agregar_producto(producto, cantidad=1)`: Agrega un producto al pedido
- `cambiar_estado(nuevo_estado)`: Cambia el estado del pedido
- `obtener_resumen()`: Retorna resumen del pedido
- `listar_productos()`: Retorna detalles de todos los productos
- `__str__()`: Representación en texto del pedido

### 4. **Restaurante** (`servicios/restaurante.py`)
Administra productos, clientes y pedidos del restaurante.

**Atributos:**
- `nombre`: Nombre del restaurante
- `productos_disponibles`: Lista de productos registrados
- `clientes_registrados`: Lista de clientes registrados
- `pedidos_realizados`: Lista de pedidos realizados

**Métodos principales:**
- **Gestión de Productos:**
  - `registrar_producto(nombre, descripcion, precio, categoria)`
  - `obtener_producto(producto_id)`
  - `listar_productos()`

- **Gestión de Clientes:**
  - `registrar_cliente(nombre, email, telefono)`
  - `obtener_cliente(cliente_id)`
  - `listar_clientes()`

- **Gestión de Pedidos:**
  - `crear_pedido(cliente)`
  - `obtener_pedido(pedido_id)`
  - `listar_pedidos()`
  - `listar_pedidos_por_estado(estado)`

- **Métodos Informativos:**
  - `mostrar_informacion()`: Información general del restaurante
  - `mostrar_menu()`: Menú organizado por categoría
  - `mostrar_clientes()`: Lista de clientes registrados
  - `mostrar_pedidos()`: Lista de pedidos realizados
  - `obtener_ingresos_totales()`: Calcula ingresos de pedidos entregados

## Ejecución

Para ejecutar el programa:

```bash
cd restaurante_app
python main.py
```

## Características Demostrativas en main.py

El archivo `main.py` demuestra:

1. **Creación de instancia del restaurante**
2. **Registro de 8 productos** distribuidos en 3 categorías:
   - Platos principales: Filete, Pechuga, Salmón
   - Bebidas: Jugo, Refresco, Vino
   - Postres: Tiramisú, Helado
3. **Registro de 3 clientes** con información de contacto
4. **Creación de 3 pedidos** con productos y estados diferentes
5. **Demostración de métodos** de cada clase
6. **Análisis de datos** (pedidos por estado, ingresos totales)
7. **Visualización organizada** de menú, clientes y pedidos

## Requisitos Cumplidos

✅ Estructura modular en carpetas (modelos/ y servicios/)
✅ Implementación de clases con constructores `__init__`
✅ Atributos pertinentes para cada clase
✅ Métodos para obtener y gestionar información
✅ Implementación de `__str__()` en clases principales
✅ Importaciones correctas entre archivos
✅ Creación de objetos en main.py
✅ Demostración completa de funcionalidades
✅ Comentarios explicativos en código

## Notas de Diseño

- Los IDs se generan automáticamente usando contadores de clase
- Los precios se validan para asegurar valores positivos
- El estado de los pedidos está limitado a valores predefinidos
- El total del pedido se calcula automáticamente al agregar productos
- El menú se organiza por categoría para mejor presentación
- Los ingresos se calculan solo de pedidos entregados
