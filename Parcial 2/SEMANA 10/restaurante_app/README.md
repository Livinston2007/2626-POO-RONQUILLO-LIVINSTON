# Sistema de Restaurante - SEMANA 10
## Persistencia de Productos mediante JSON

### Descripción General
Continuación del proyecto `restaurante_app` de semanas anteriores. Esta versión incorpora **persistencia de productos** mediante un archivo JSON. Los productos se guardan automáticamente cuando se registran, actualizan o eliminan, y se cargan al iniciar la aplicación.

### Mejoras Implementadas en SEMANA 10

#### 1. Persistencia Real con JSON
- **Archivo de almacenamiento**: `datos/productos.json`
- **Formato**: Lista de diccionarios en JSON (UTF-8)
- **Actualización automática**: El archivo se actualiza después de cada operación que modifique la colección
- **Carga al iniciar**: Los productos se cargan automáticamente cuando se ejecuta `main.py`

#### 2. Nueva Clase: `ArchivoServicio`
Ubicación: `servicios/archivo_servicio.py`

Responsabilidades:
- **`cargar_productos()`**: Lee el archivo JSON y convierte cada registro a un objeto `Producto`
  - Retorna lista vacía si el archivo no existe
  - Maneja errores de formato JSON
  - Omite registros inválidos sin detener la aplicación
  
- **`guardar_productos(productos)`**: Convierte objetos `Producto` a diccionarios y escribe en JSON
  - Crea el directorio `datos/` si no existe
  - Utiliza UTF-8 para encoding
  - Formatea el JSON con indentación para legibilidad

#### 3. Mejoras a la Clase `Producto`
Ubicación: `modelos/producto.py`

Nuevos métodos de serialización:
- **`a_diccionario()`**: Convierte el objeto a un diccionario compatible con JSON
  ```python
  producto.a_diccionario()
  # Retorna: {"codigo": "...", "nombre": "...", "categoria": "...", "precio": ...}
  ```

- **`desde_diccionario(datos)` (método estático)**: Crea un `Producto` desde un diccionario
  ```python
  producto = Producto.desde_diccionario(dict_data)
  # Valida que todas las claves necesarias estén presentes
  ```

#### 4. Mejoras al Servicio `Restaurante`
Ubicación: `servicios/restaurante.py`

Nuevos métodos:
- **`obtener_productos()`**: Retorna la lista interna de productos (para persistencia)
- **`cargar_productos_iniciales(productos)`**: Carga una lista de productos al iniciar

#### 5. Integración en `main.py`
- **Carga al iniciar**: Se crea `ArchivoServicio`, se cargan productos y se asignan al servicio `Restaurante`
- **Guardado automático**:
  - Después de registrar un producto
  - Después de actualizar un producto
  - Después de eliminar un producto
- **Funciones actualizadas**:
  - `registrar_producto(serv, archivo_serv)`
  - `actualizar_producto(serv, archivo_serv)`
  - `eliminar_producto(serv, archivo_serv)`

### Manejo de Excepciones

El sistema controla específicamente las siguientes excepciones:

| Excepción | Situación | Comportamiento |
|-----------|-----------|-----------------|
| `FileNotFoundError` | Archivo `productos.json` no existe | Inicia con colección vacía, crea archivo en primer guardado |
| `json.JSONDecodeError` | Contenido JSON inválido | Muestra error y permite continuar (no usa archivo corrupto) |
| `PermissionError` | Sin permisos lectura/escritura | Informa error pero permite usar aplicación en memoria |
| `KeyError` | Registro incompleto en JSON | Omite ese registro, continúa con los demás |
| `ValueError` | Datos inválidos al deserializar | Captura el error y lo reporta al usuario |

Todas las excepciones se reportan al usuario de forma clara. No se utiliza `except: pass` para ocultar errores.

### Flujo de Carga (Inicio de Aplicación)

```
main.py se ejecuta
    ↓
Se crea ArchivoServicio con ruta "datos/productos.json"
    ↓
Se crea Restaurante (vacío)
    ↓
archivo_serv.cargar_productos()
    ├─ Intenta leer datos/productos.json
    ├─ Si no existe: retorna [] (lista vacía)
    ├─ Si JSON inválido: muestra error, retorna []
    └─ Si OK: convierte cada item a Producto
    ↓
serv.cargar_productos_iniciales(productos)
    ├─ Asigna la lista cargada a _productos
    └─ Muestra cantidad de productos cargados
    ↓
Menú interactivo listo
```

### Flujo de Guardado (Operación Modificadora)

```
Usuario selecciona opción (1, 3 ó 4)
    ↓
Se ejecuta operación en serv.Restaurante (registrar, actualizar, eliminar)
    ↓
Si la operación fue exitosa:
    ├─ archivo_serv.guardar_productos(serv.obtener_productos())
    └─ Se escribe el estado actualizado en datos/productos.json
    ↓
Se confirma al usuario
```

### Estructura del Proyecto

```
restaurante_app/
├── datos/
│   └── productos.json          # Archivo de persistencia (creado automáticamente)
├── modelos/
│   ├── __init__.py
│   ├── producto.py             # Mejorado: con serialización
│   └── usuario.py              # Sin cambios (no persiste en SEMANA 10)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py     # NUEVO: maneja JSON
│   └── restaurante.py          # Mejorado: nuevos getters
├── main.py                     # Mejorado: integra persistencia
├── demo.py                     # Sin cambios
├── test_sistema.py             # Sin cambios
└── README.md                   # Este archivo
```

### Cómo Usar

#### Ejecución Básica
```bash
python main.py
```

La aplicación se iniciará cargando automáticamente los productos almacenados.

#### Verificación de Persistencia
1. Ejecutar el programa: `python main.py`
2. Registrar productos (opción 1)
3. Verificar que `datos/productos.json` contiene los registros
4. Cerrar el programa (opción 9)
5. Ejecutar nuevamente: `python main.py`
6. Los productos anteriores deberían aparecer al listar (opción 5)

#### Visualizar el Archivo JSON
```bash
# Linux/Mac
cat datos/productos.json

# Windows (PowerShell)
Get-Content datos/productos.json

# O simplemente abrirlo en un editor de texto
```

### Ejemplo de `datos/productos.json`

```json
[
  {
    "codigo": "P001",
    "nombre": "Hamburguesa",
    "categoria": "Platos Fuertes",
    "precio": 12.5
  },
  {
    "codigo": "P002",
    "nombre": "Ensalada Cesar",
    "categoria": "Ensaladas",
    "precio": 8.99
  }
]
```

### Validaciones Mantenidas

- Código de producto único (no se pueden duplicar)
- Nombre, categoría y código no pueden estar vacíos
- Precio no puede ser negativo
- Tipos de datos respetados en JSON

### Validaciones Nuevas

- Estructura JSON debe ser una lista
- Cada registro en JSON debe tener: `codigo`, `nombre`, `categoria`, `precio`
- Valores se convierten al tipo correcto (precio como float)

### Consideraciones Técnicas

- **Codificación**: UTF-8 en todas las operaciones de archivo
- **Indentación JSON**: 2 espacios para legibilidad
- **Caracteres especiales**: Soportados en nombre y categoría (no se usa ASCII)
- **Rutas**: Relativas al directorio de ejecución de `main.py`
- **Concurrencia**: No soportada (archivo se escribe cada operación)

### Limitaciones (Intencionales para SEMANA 10)

- Solo se persisten productos (usuarios quedan en memoria)
- No hay versionado o historial de cambios
- No hay respaldo automático del archivo
- No hay validación de integridad posterior a cargar

### Trabajo Futuro (SEMANAS POSTERIORES)

- Persistencia de usuarios
- Persistencia de pedidos/transacciones
- Base de datos SQL
- API REST
- Interfaz gráfica

### Archivos Modificados desde SEMANA 9

- `modelos/producto.py` - Agregados métodos de serialización
- `servicios/restaurante.py` - Agregados getters y setter de carga inicial
- `main.py` - Integración completa de persistencia
- `README.md` - Este documento

### Archivos Nuevos

- `servicios/archivo_servicio.py` - Nuevo servicio de persistencia
- `datos/productos.json` - Archivo de almacenamiento (generado automáticamente)

### Notas de Desarrollo

- El sistema continúa trabajando con objetos `Producto` (no convierte todo a diccionarios)
- `ArchivoServicio` solo maneja lectura/escritura de archivo
- `Restaurante` mantiene la lógica de negocio
- `main.py` coordina cuándo cargar y guardar
- Separación clara de responsabilidades

---

**Versión**: SEMANA 10  
**Autor**: Estudiante de POO  
**Fecha**: 2026  
**Estado**: Implementación completada con persistencia JSON
