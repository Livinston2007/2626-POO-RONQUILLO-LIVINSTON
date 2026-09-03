# Guía Técnica: Optimizaciones mediante Colecciones (Semana 12)

## 1. Problema Identificado

El sistema original (Semana 11) realizaba búsquedas lineales (O(n)) en las siguientes operaciones:

```python
# Búsqueda O(n) - recorre todos los productos
def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
    for producto in self._productos:
        if producto.codigo == codigo:
            return producto
    return None
```

Esto se repetía en:
- Registrar producto (validar duplicados)
- Buscar producto
- Actualizar producto
- Eliminar producto
- Procesar venta

**Con 1000+ productos, esto generaba miles de iteraciones innecesarias.**

## 2. Solución: Índices en Memoria

Se agregaron diccionarios auxiliares que actúan como "índices" para búsquedas O(1):

```python
# Índice: código → Producto
self._indice_productos_por_codigo: dict[str, Producto] = {}

# Búsqueda O(1) - acceso directo al diccionario
def buscar_producto_por_codigo(self, codigo: str) -> Optional[Producto]:
    return self._indice_productos_por_codigo.get(codigo)
```

### Estructura de Datos Agregada

```python
class Restaurante:
    # Colecciones principales (listas)
    self._productos: list[Producto]        # O(n) para búsqueda, O(1) para añadir
    self._usuarios: list[Usuario]          # O(n) para búsqueda, O(1) para añadir
    self._ventas: list[Venta]              # O(n) para búsqueda, O(1) para añadir
    
    # Índices auxiliares (diccionarios)
    self._indice_productos_por_codigo: dict[str, Producto]      # O(1) búsqueda
    self._indice_usuarios_por_id: dict[str, Usuario]            # O(1) búsqueda
    self._ventas_por_usuario: dict[str, list[Venta]]            # O(1) consulta
```

## 3. Mejoras de Rendimiento

### 3.1 Búsqueda de Productos

**Antes (O(n)):**
```python
for producto in self._productos:
    if producto.codigo == codigo:
        return producto
return None
```

**Después (O(1)):**
```python
return self._indice_productos_por_codigo.get(codigo)
```

**Impacto:**
- 100 productos: 50 iteraciones promedio → 0 iteraciones
- 1000 productos: 500 iteraciones promedio → 0 iteraciones
- 10000 productos: 5000 iteraciones promedio → 0 iteraciones

### 3.2 Validación de Duplicados

**Antes (O(n)):**
```python
def registrar_producto(self, producto: Producto) -> None:
    if self.buscar_producto_por_codigo(producto.codigo) is not None:  # O(n)
        raise ValueError(...)
    self._productos.append(producto)
```

**Después (O(1)):**
```python
def registrar_producto(self, producto: Producto) -> None:
    if self.buscar_producto_por_codigo(producto.codigo) is not None:  # O(1)
        raise ValueError(...)
    self._productos.append(producto)
    self._actualizar_indice_producto(producto)  # O(1)
```

### 3.3 Consulta de Ventas por Usuario

**Antes (O(n)):**
```python
def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
    ventas_usuario: list[Venta] = []
    for venta in self._ventas:  # Recorre TODAS las ventas
        if venta.usuario_id == identificacion_usuario:
            ventas_usuario.append(venta)
    return ventas_usuario
```

**Problema con 10000 ventas:** Se recorren 10000 items cada vez que se consulta.

**Después (O(1) acceso, O(m) iteración):**
```python
def consultar_ventas_por_usuario(self, identificacion_usuario: str) -> list[Venta]:
    return self._ventas_por_usuario.get(identificacion_usuario, [])  # O(1) acceso
    # O(m) solo para las ventas del usuario, no todas
```

**Impacto:**
- 10000 ventas, 100 por usuario: 5000 iteraciones promedio → 0 iteraciones (acceso directo)
- Iteración de las ventas del usuario es mucho más rápida

## 4. Sincronización de Índices

### 4.1 Reconstrucción Inicial

Al iniciar, se cargan datos desde JSON y se reconstruyen todos los índices:

```python
def __init__(self, productos, usuarios, ventas):
    self._productos = productos or []
    self._usuarios = usuarios or []
    self._ventas = ventas or []
    
    # Inicializar índices vacíos
    self._indice_productos_por_codigo = {}
    self._indice_usuarios_por_id = {}
    self._ventas_por_usuario = {}
    
    # Reconstruir índices desde colecciones
    self._reconstruir_indices()
```

### 4.2 Mantener Sincronización

Cada operación que modifica datos también actualiza los índices:

```python
def registrar_producto(self, producto: Producto) -> None:
    # Validar y agregar a lista
    if self.buscar_producto_por_codigo(producto.codigo) is not None:
        raise ValueError(...)
    self._productos.append(producto)
    
    # Actualizar índice
    self._actualizar_indice_producto(producto)  # O(1)
```

### 4.3 Operaciones Atómicas

Para garantizar consistencia, las operaciones son atómicas:

```python
def vender_producto(self, codigo, usuario_id, cantidad):
    usuario = self.buscar_usuario_por_identificacion(usuario_id)  # O(1)
    producto = self.buscar_producto_por_codigo(codigo)             # O(1)
    
    if usuario is None or producto is None:
        return False
    
    # Crear venta y actualizar índices una sola vez
    venta = Venta(usuario.identificacion, producto.codigo, cantidad)
    self._ventas.append(venta)
    self._actualizar_indice_venta(venta)  # O(1)
    producto.vender(cantidad)              # Descuenta stock
    return True
```

## 5. Matriz de Operaciones

| Operación | Antes | Después | Componentes |
|-----------|-------|---------|------------|
| Buscar producto | O(n) | O(1) | indice_productos_por_codigo |
| Buscar usuario | O(n) | O(1) | indice_usuarios_por_id |
| Registrar producto | O(n) | O(1) | indice_productos_por_codigo |
| Registrar usuario | O(n) | O(1) | indice_usuarios_por_id |
| Eliminar producto | O(n) | O(1) | indice_productos_por_codigo |
| Eliminar usuario | O(n) | O(1) | indice_usuarios_por_id |
| Consultar ventas usuario | O(n) | O(1) acceso | ventas_por_usuario |
| Listar productos | O(n) | O(n) | _productos |
| Listar usuarios | O(n) | O(n) | _usuarios |
| Listar ventas | O(n) | O(n) | _ventas |

## 6. Complejidad Espacial

### Costo de Memoria

```
Colecciones principales:
- _productos: n * tamaño(Producto)
- _usuarios: m * tamaño(Usuario)
- _ventas: v * tamaño(Venta)

Índices auxiliares:
- _indice_productos_por_codigo: n * (tamaño(string) + referencia)
- _indice_usuarios_por_id: m * (tamaño(string) + referencia)
- _ventas_por_usuario: m * (tamaño(string) + lista de referencias)

Total: ~1.5x a 2x memoria original
```

**Análisis:** La redundancia es aceptable porque:
- Los diccionarios solo almacenan referencias, no copias
- El rendimiento O(1) compensa el costo de memoria
- Con datos típicos (miles de registros), el overhead es insignificante

## 7. Casos de Uso Comunes

### Caso 1: Proceso de Venta (3 búsquedas)

```python
# Antes: 3 búsquedas O(n)
usuario = self.buscar_usuario_por_identificacion(id)      # O(n)
producto = self.buscar_producto_por_codigo(codigo)        # O(n)
if producto and usuario:
    venta = Venta(...)
    self._ventas.append(venta)

# Después: 3 búsquedas O(1) + 1 actualización índice
usuario = self.buscar_usuario_por_identificacion(id)      # O(1)
producto = self.buscar_producto_por_codigo(codigo)        # O(1)
if producto and usuario:
    venta = Venta(...)
    self._ventas.append(venta)
    self._actualizar_indice_venta(venta)                 # O(1)
```

### Caso 2: Consulta de Historial de Usuario

```python
# Antes: recorre todas las ventas
ventas = []
for venta in self._ventas:  # O(n) - 10000 iteraciones
    if venta.usuario_id == user_id:
        ventas.append(venta)

# Después: acceso directo
ventas = self._ventas_por_usuario.get(user_id, [])  # O(1)
```

### Caso 3: Validación de Producto Existente

```python
# Antes: O(n) búsqueda
if self.buscar_producto_por_codigo("P001") is None:  # O(n)
    crear_producto(...)

# Después: O(1) búsqueda
if self.buscar_producto_por_codigo("P001") is None:  # O(1)
    crear_producto(...)
```

## 8. Verificación de Sincronización

Para verificar que los índices están sincronizados:

```python
estado = restaurante.obtener_estado_indices()

assert estado['productos_en_lista'] == estado['productos_en_indice']
assert estado['usuarios_en_lista'] == estado['usuarios_en_indice']

# Si están iguales, índices sincronizados ✓
# Si no son iguales, hay un problema ✗
```

## 9. Escalabilidad

### Con 1000 productos:

**Operación:** Buscar producto "P0500"

**Antes (O(n)):**
- Promedio: 500 comparaciones
- Peor caso: 1000 comparaciones

**Después (O(1)):**
- Siempre: 1 acceso al diccionario

**Mejora:** 500-1000x más rápido

### Con 10000 ventas, 100 usuarios:

**Operación:** Consultar ventas del usuario "U0050"

**Antes (O(n)):**
- 10000 comparaciones

**Después (O(1)):**
- 1 acceso al diccionario
- Luego iterar ~100 ventas del usuario

**Mejora:** 100x más rápido para acceso

## 10. Conclusión

Los índices en memoria (diccionarios) transforman operaciones frecuentes de O(n) a O(1), lo que es crítico para:

- **Registros grandes:** 1000+ usuarios/productos
- **Operaciones frecuentes:** Búsquedas en cada transacción
- **Experiencia del usuario:** Respuesta instantánea en búsquedas
- **Escalabilidad:** Permite crecer sin degradación de rendimiento

**Trade-off:** Un poco más de complejidad de código + ~50% más de memoria = 500-1000x mejora de rendimiento en búsquedas.

