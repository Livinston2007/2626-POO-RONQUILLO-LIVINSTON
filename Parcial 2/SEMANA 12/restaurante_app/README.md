# Sistema de Restaurante - Semana 12: Optimización de Búsquedas mediante Colecciones

## Descripción General

Esta versión continúa del proyecto de restaurante de la Semana 11, enfocándose en optimizar las búsquedas, consultas y validaciones mediante el uso estratégico de colecciones en Python. Se mantienen las listas principales para almacenar, recorrer y persistir datos, mientras se agregan índices auxiliares (diccionarios) para mejorar el rendimiento de operaciones frecuentes.

## Mejoras Principales (Semana 12)

### 1. Índices de Productos por Código
- **Estructura**: Diccionario `_indice_productos_por_codigo: dict[str, Producto]`
- **Mejora**: Búsqueda de O(n) a O(1)
- **Operaciones optimizadas**:
  - `buscar_producto_por_codigo()` - antes recorría toda la lista
  - `registrar_producto()` - validación de duplicados es ahora O(1)
  - `actualizar_producto()` - búsqueda inicial es O(1)
  - `eliminar_producto()` - búsqueda es O(1)

### 2. Índices de Usuarios por Identificación
- **Estructura**: Diccionario `_indice_usuarios_por_id: dict[str, Usuario]`
- **Mejora**: Búsqueda de O(n) a O(1)
- **Operaciones optimizadas**:
  - `buscar_usuario_por_identificacion()` - antes recorría toda la lista
  - `registrar_usuario()` - validación de duplicados es ahora O(1)
  - `eliminar_usuario()` - búsqueda es O(1)

### 3. Índice de Ventas por Usuario
- **Estructura**: Diccionario `_ventas_por_usuario: dict[str, list[Venta]]`
- **Mejora**: Consulta de O(n) a O(1)
- **Operaciones optimizadas**:
  - `consultar_ventas_por_usuario()` - antes recorría toda la lista de ventas cada vez
  - Ahora acceso directo a las ventas del usuario en O(1)

### 4. Categorías (Set)
- **Estructura**: Generado dinámicamente mediante `{producto.categoria for producto in self._productos}`
- **Nota**: Se mantiene como cálculo dinámico porque cambia con la actualización de productos

## Arquitectura de Colecciones

### Colecciones Principales (Listas)
Se mantienen para su propósito original:
- **`_productos: list[Producto]`** - Almacenar, recorrer y persistir productos
- **`_usuarios: list[Usuario]`** - Almacenar, recorrer y persistir usuarios
- **`_ventas: list[Venta]`** - Almacenar, recorrer y persistir ventas

### Estructuras Auxiliares (Índices)
Se crean y actualizan para optimizar búsquedas:
- **`_indice_productos_por_codigo: dict[str, Producto]`** - Búsqueda rápida por código
- **`_indice_usuarios_por_id: dict[str, Usuario]`** - Búsqueda rápida por ID
- **`_ventas_por_usuario: dict[str, list[Venta]]`** - Consulta rápida de ventas por usuario

## Sincronización de Índices

### Métodos Privados de Mantenimiento
- `_reconstruir_indices()` - Se ejecuta al cargar datos desde JSON para sincronizar índices
- `_actualizar_indice_producto(producto)` - Agrega o actualiza un producto en el índice
- `_eliminar_indice_producto(codigo)` - Elimina un producto del índice
- `_actualizar_indice_usuario(usuario)` - Agrega o actualiza un usuario en el índice
- `_eliminar_indice_usuario(identificacion)` - Elimina un usuario del índice
- `_actualizar_indice_venta(venta)` - Agrega una venta al índice por usuario

### Casos de Sincronización
1. **Al registrar**: Índice se actualiza cuando se agrega un nuevo objeto
2. **Al eliminar**: Índice se actualiza cuando se elimina un objeto
3. **Al cargar (JSON)**: Se reconstruyen todos los índices a partir de las listas cargadas
4. **Al actualizar**: Los cambios en propiedades no requieren cambios en índices (mismo objeto)

## Flujo de Inicialización

```
1. Crear instancia de Restaurante()
   ↓
2. Listas principales se inicializan vacías
   ↓
3. Índices se inicializan vacíos
   ↓
4. Desde main.py:
   - Cargar JSON → obtener listas
   - cargar_productos_iniciales() → actualiza _productos y reconstruye índices
   - cargar_usuarios_iniciales() → actualiza _usuarios y reconstruye índices
   - cargar_ventas_iniciales() → actualiza _ventas y reconstruye índices
   ↓
5. Sistema listo con índices sincronizados
```

## Comparativa de Rendimiento

| Operación | Antes (Semana 11) | Después (Semana 12) | Mejora |
|-----------|-------------------|-------------------|--------|
| Buscar producto por código | O(n) | O(1) | Lineal → Constante |
| Buscar usuario por ID | O(n) | O(1) | Lineal → Constante |
| Registrar producto (validar duplicado) | O(n) | O(1) | Lineal → Constante |
| Registrar usuario (validar duplicado) | O(n) | O(1) | Lineal → Constante |
| Consultar ventas por usuario | O(n) | O(1)* | Lineal → Constante |

*O(1) para el acceso; O(m) para iterar las ventas del usuario (m = ventas del usuario)

## Funcionalidades Mantenidas

✓ Registrar, buscar, actualizar y eliminar productos
✓ Registrar, buscar y listar usuarios
✓ Registrar ventas y descontar de stock
✓ Consultar ventas por usuario
✓ Persistencia JSON (productos, usuarios, ventas)
✓ Validaciones de negocio
✓ Cálculo de categorías únicas

## Funcionalidades Agregadas

✓ Opción de menú para ver estado de índices (diagnóstico)
✓ Verificación de sincronización de índices
✓ Método `obtener_estado_indices()` para debugging

## Estructura de Archivos

```
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── __init__.py
├── main.py
└── README.md
```

## Cómo Usar la Aplicación

### Iniciar el programa
```bash
python main.py
```

### Menú de opciones
1. **Registrar producto** - Crea un nuevo producto (búsqueda de duplicados en O(1))
2. **Buscar producto** - Busca por código usando índice (O(1))
3. **Actualizar producto** - Modifica propiedades del producto
4. **Eliminar producto** - Borra un producto y su entrada del índice
5. **Listar productos** - Muestra todos los productos
6. **Registrar usuario** - Crea un nuevo usuario (búsqueda de duplicados en O(1))
7. **Listar usuarios** - Muestra todos los usuarios
8. **Vender producto** - Registra una venta (utiliza índices para búsquedas)
9. **Consultar ventas por usuario** - Ve las ventas del usuario usando índice (O(1))
10. **Mostrar categorías** - Muestra categorías únicas
11. **Ver estado de índices** - Verifica sincronización de índices (para debugging)

## Comprobación de Funcionamiento

### Verificar búsquedas optimizadas
1. Registrar varios productos
2. Buscar un producto por código → usa índice (O(1))
3. Actualizar un producto → busca por código mediante índice
4. Eliminar un producto → busca y elimina del índice

### Verificar búsquedas de usuarios
1. Registrar varios usuarios
2. Búsquedas de usuarios usan el índice `_indice_usuarios_por_id`
3. Ventas validan usuario mediante índice

### Verificar consultas de ventas
1. Registrar usuarios y productos
2. Crear varias ventas para un usuario
3. Consultar ventas por usuario → acceso O(1) al diccionario de ventas
4. Las ventas se agrupan automáticamente en `_ventas_por_usuario`

### Verificar sincronización
1. Ejecutar opción 11 para ver estado de índices
2. Verificar que `productos_en_lista == productos_en_indice`
3. Verificar que `usuarios_en_lista == usuarios_en_indice`
4. Debería mostrar "✓ Los indices estan sincronizados correctamente."

### Verificar persistencia
1. Registrar datos
2. Cerrar el programa
3. Volver a ejecutar
4. Verificar que los datos se cargan correctamente
5. Los índices se reconstruyen automáticamente desde JSON

## Decisiones de Diseño

### ¿Por qué mantener listas principales?
- **Persistencia**: Necesarias para guardar en JSON
- **Recorrido**: Requeridas para listar y iterar sobre todos los objetos
- **Integridad**: Facilita auditoría y consistencia de datos
- **Simplicidad**: Evita complejidad con solo diccionarios

### ¿Por qué agregar índices?
- **Rendimiento**: Las búsquedas frecuentes pasan de O(n) a O(1)
- **Validaciones**: Verificar duplicados se vuelve constante
- **Escalabilidad**: Con mil usuarios/productos, la diferencia es significativa
- **Precisión**: Permiten consultas más específicas (consultas por usuario)

### ¿Por qué no usar solo diccionarios?
- Perderías el orden de inser
ción (importante en historiales de ventas)
- Recorrer todos los elementos sería O(n) en lugar de O(1) con lista
- Persistencia JSON requiere orden
- La redundancia es mínima en términos de memoria

## Notas Técnicas

- Los índices se reconstruyen al cargar datos iniciales para garantizar sincronización
- Cuando se actualiza un producto, no es necesario cambiar el índice (mismo objeto, mismo código)
- El diccionario de ventas por usuario es el más crítico para rendimiento, ya que evita O(n) en cada consulta
- El sistema es thread-safe para operaciones de lectura pero no para escritura concurrente

## Próximas Mejoras Posibles (Fuera de Scope)

- Agregar índices secundarios (próductos por categoría)
- Implementar caché de categorías
- Agregar transacciones (rollback en caso de error)
- Sincronización con base de datos
- Validación de duplicados en correos de usuarios
- Índice de productos por precio u otros atributos

## Conclusión

La Semana 12 demuestra cómo estructuras de datos auxiliares (diccionarios e índices) pueden mejorar significativamente el rendimiento de búsquedas sin comprometer la integridad, persistencia o claridad del código. El sistema mantiene las ventajas de las listas (persistencia, orden, recorrido) mientras agrega la velocidad de los diccionarios para operaciones críticas.

