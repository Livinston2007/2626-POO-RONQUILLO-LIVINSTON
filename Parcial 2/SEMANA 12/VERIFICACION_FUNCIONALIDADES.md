# Verificación de Funcionalidades - Semana 12

Esta guía reproduce todas las pruebas manuales requeridas para verificar que el sistema funciona correctamente.

## Comprobación Mínima de Funcionamiento

### Paso 1: Ejecutar main.py y verificar carga

```bash
python restaurante_app/main.py
```

**Esperado:**
```
Datos cargados: 5 producto(s), 3 usuario(s), 5 venta(s).
```

✓ **Verificado:** El sistema carga datos desde JSON correctamente

---

### Paso 2: Registrar o cargar usuarios, productos y ventas existentes

Ya están cargados desde JSON, pero podemos verificar:

**Opción 5: Listar productos**
```
Seleccione una opcion: 5
--- Productos registrados ---
[Producto] Codigo: P001 | Nombre: Hamburguesa clasica | Categoria: Comidas | Precio: $15000.00 | Stock: 8
[Producto] Codigo: P002 | Nombre: Pizza personal | Categoria: Comidas | Precio: $18000.00 | Stock: 5
[Producto] Codigo: B001 | Nombre: Limonada natural | Categoria: Bebidas | Precio: $5000.00 | Stock: 10
[Producto] Codigo: B002 | Nombre: Gaseosa | Categoria: Bebidas | Precio: $4500.00 | Stock: 11
[Producto] Codigo: D001 | Nombre: Brownie | Categoria: Postres | Precio: $7000.00 | Stock: 6
Total: 5 productos
```

✓ **Verificado:** Los 5 productos se cargaron correctamente

**Opción 7: Listar usuarios**
```
Seleccione una opcion: 7
--- Usuarios registrados ---
[Usuario] ID: 1001 | Nombre: Laura Gomez | Correo: laura.gomez@email.com
[Usuario] ID: 1002 | Nombre: Carlos Ruiz | Correo: carlos.ruiz@email.com
[Usuario] ID: 1003 | Nombre: Ana Torres | Correo: ana.torres@email.com
Total: 3 usuarios
```

✓ **Verificado:** Los 3 usuarios se cargaron correctamente

---

### Paso 3: Comprobación de búsqueda de un producto mediante su código

**Opción 2: Buscar producto**
```
Seleccione una opcion: 2
--- Buscar producto ---
Codigo del producto: P001
[Producto] Codigo: P001 | Nombre: Hamburguesa clasica | Categoria: Comidas | Precio: $15000.00 | Stock: 8
```

✓ **Verificado:** Búsqueda de producto funciona (O(1) usando índice)

**Prueba adicional - producto no existe:**
```
Seleccione una opcion: 2
--- Buscar producto ---
Codigo del producto: INEXISTENTE
Producto no encontrado.
```

✓ **Verificado:** Manejo de producto no encontrado correcto

---

### Paso 4: Comprobación de búsqueda de un usuario mediante su identificación

**Opción 6: Registrar usuario - Búsqueda implícita**
```
Seleccione una opcion: 6
--- Registrar usuario ---
Identificacion: 1001
...
No se pudo registrar el usuario: Identificacion de usuario duplicada: 1001
```

✓ **Verificado:** Búsqueda de usuario funciona (O(1) usando índice), detecta duplicados

**Buscar un usuario nuevo:**
```
Seleccione una opcion: 6
--- Registrar usuario ---
Identificacion: 1999
Nombre: Juan Perez
Correo: juan@email.com
Usuario registrado correctamente.
```

✓ **Verificado:** Registro de usuario nuevo funciona e índice se actualiza

---

### Paso 5: Consulte las ventas relacionadas con un usuario

**Opción 9: Consultar ventas por usuario**
```
Seleccione una opcion: 9
--- Consultar ventas por usuario ---
Identificacion del usuario: 1001
Usuario: 1001 | Producto: P001 - Hamburguesa clasica | Cantidad: 2
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 1
Total de ventas encontradas: 2
```

✓ **Verificado:** Consulta de ventas funciona (O(1) acceso al diccionario de ventas)

**Prueba con usuario sin ventas:**
```
Seleccione una opcion: 9
--- Consultar ventas por usuario ---
Identificacion del usuario: 1999
No hay ventas registradas para ese usuario.
```

✓ **Verificado:** Manejo correcto de usuario sin ventas

---

### Paso 6: Realice una venta y confirme que el stock se actualice correctamente

**Opción 8: Vender producto**
```
Seleccione una opcion: 8
--- Vender producto ---
Identificacion del usuario: 1001
Codigo del producto: B001
Cantidad a vender: 2
Venta registrada correctamente.
```

✓ **Verificado:** Venta registrada

**Verificar stock actualizado - Opción 2:**
```
Seleccione una opcion: 2
--- Buscar producto ---
Codigo del producto: B001
[Producto] Codigo: B001 | Nombre: Limonada natural | Categoria: Bebidas | Precio: $5000.00 | Stock: 8
```

Stock antes: 10, Stock después: 8 (se vendieron 2)

✓ **Verificado:** Stock se decrementó correctamente de 10 a 8

**Verificar venta agregada - Opción 9:**
```
Seleccione una opcion: 9
--- Consultar ventas por usuario ---
Identificacion del usuario: 1001
Usuario: 1001 | Producto: P001 - Hamburguesa clasica | Cantidad: 2
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 1
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 2  ← NUEVA
Total de ventas encontradas: 3
```

✓ **Verificado:** Venta agregada al índice de ventas por usuario (O(1) actualización)

---

### Paso 7: Verifique que los índices auxiliares permanezcan coherentes

**Opción 11: Ver estado de índices**
```
Seleccione una opcion: 11
--- Estado de los indices (diagnostico) ---
Productos en lista: 5
Productos en indice: 5
Usuarios en lista: 4
Usuarios en indice: 4
Ventas totales: 6
Usuarios con ventas: 3

✓ Los indices estan sincronizados correctamente.
```

✓ **Verificado:** 
- Productos en lista == Productos en índice ✓
- Usuarios en lista == Usuarios en índice ✓
- Los índices están correctamente sincronizados ✓

---

### Paso 8: Cierre y vuelva a ejecutar el programa

**Cerrar:**
```
Seleccione una opcion: 0
Hasta luego.
```

**Ejecutar nuevamente:**
```
python restaurante_app/main.py
```

**Esperado:**
```
Datos cargados: 5 producto(s), 4 usuario(s), 6 venta(s).
```

✓ **Verificado:** Datos persistidos en JSON correctamente

**Verificar datos cargados - Opción 9:**
```
Seleccione una opcion: 9
--- Consultar ventas por usuario ---
Identificacion del usuario: 1001
Usuario: 1001 | Producto: P001 - Hamburguesa clasica | Cantidad: 2
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 1
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 2
Total de ventas encontradas: 3
```

✓ **Verificado:** Las ventas se recuperan correctamente desde JSON

**Verificar índices reconstruidos - Opción 11:**
```
Seleccione una opcion: 11
--- Estado de los indices (diagnostico) ---
Productos en lista: 5
Productos en indice: 5
Usuarios en lista: 4
Usuarios en indice: 4
Ventas totales: 6
Usuarios con ventas: 3

✓ Los indices estan sincronizados correctamente.
```

✓ **Verificado:** Los índices se reconstruyeron correctamente desde JSON

---

## Resumen de Pruebas Manuales

| Prueba | Resultado | Observación |
|--------|-----------|-------------|
| 1. Ejecutar main.py | ✓ EXITOSA | Carga correcta desde JSON |
| 2. Productos cargados | ✓ EXITOSA | 5 productos validados |
| 3. Usuarios cargados | ✓ EXITOSA | 3 usuarios validados |
| 4. Búsqueda producto | ✓ EXITOSA | O(1) usando índice |
| 5. Búsqueda usuario | ✓ EXITOSA | O(1) usando índice |
| 6. Consulta ventas usuario | ✓ EXITOSA | O(1) acceso al diccionario |
| 7. Registrar usuario | ✓ EXITOSA | Índice actualizado |
| 8. Realizar venta | ✓ EXITOSA | Stock decrementado, venta indexada |
| 9. Índices sincronizados | ✓ EXITOSA | Diagnóstico valida sincronización |
| 10. Cierre y recarga | ✓ EXITOSA | Persistencia JSON correcta |
| 11. Reconstrucción índices | ✓ EXITOSA | Índices reconstruidos correctamente |

---

## Pruebas Ejecutables Automáticas

Para ejecutar todas las pruebas de forma automática:

```bash
python restaurante_app/test_semana_12.py
```

**Resultado esperado:**
```
============================================================
TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ✓
============================================================

Resumen de optimizaciones verificadas:
✓ Búsqueda de productos por código: O(n) → O(1)
✓ Búsqueda de usuarios por ID: O(n) → O(1)
✓ Consulta de ventas por usuario: O(n) → O(1)
✓ Validación de duplicados: O(n) → O(1)
✓ Sincronización de índices: ✓
✓ Reconstrucción de índices: ✓
✓ Persistencia JSON: ✓
```

---

## Verificación de Archivos Generados

### Estructura Final

```
SEMANA 12/
├── restaurante_app/
│   ├── __init__.py
│   ├── main.py                          ← Menú interactivo
│   ├── test_semana_12.py               ← Pruebas automáticas
│   ├── README.md                        ← Documentación principal
│   ├── datos/
│   │   ├── productos.json
│   │   ├── usuarios.json
│   │   └── ventas.json
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── usuario.py
│   │   └── venta.py
│   └── servicios/
│       ├── __init__.py
│       ├── archivo_servicio.py         ← Persistencia JSON
│       └── restaurante.py              ← Lógica + Índices
├── GUIA_TECNICA.md                      ← Análisis detallado
├── INICIO_RAPIDO.md                     ← Guía de uso
└── COMPARATIVA_S11_S12.md              ← Cambios realizados
```

✓ Todos los archivos creados correctamente

### Verificación de Contenido

**main.py:**
- ✓ Opción 1-10: Funcionalidades de Semana 11
- ✓ Opción 11: Nueva funcionalidad de diagnóstico
- ✓ Carga automática de datos JSON

**restaurante.py:**
- ✓ Índices privados (_indice_*)
- ✓ Métodos de sincronización (_actualizar_*, _reconstruir_*)
- ✓ Método de diagnóstico (obtener_estado_indices)
- ✓ Docstrings detallados

**Archivos JSON:**
- ✓ productos.json: 5 productos, estructura correcta
- ✓ usuarios.json: 3 usuarios, estructura correcta
- ✓ ventas.json: 5 ventas iniciales, estructura correcta

---

## Optimizaciones Verificadas

### 1. Búsquedas O(1)
```python
# Antes: recorría lista completa
for producto in self._productos:
    if producto.codigo == codigo:

# Después: acceso directo al diccionario
_indice_productos_por_codigo.get(codigo)
```
✓ Verificado en Paso 3 y 4

### 2. Consultas de Ventas O(1)
```python
# Antes: recorría todas las ventas
for venta in self._ventas:
    if venta.usuario_id == usuario_id:

# Después: acceso directo al diccionario de usuario
_ventas_por_usuario.get(usuario_id, [])
```
✓ Verificado en Paso 5

### 3. Sincronización de Índices
```python
# Mantiene índices actualizados con cada operación
def registrar_producto(self, producto):
    self._productos.append(producto)
    self._actualizar_indice_producto(producto)
```
✓ Verificado en Paso 7

### 4. Reconstrucción de Índices
```python
# Al cargar desde JSON, reconstruye índices
def cargar_productos_iniciales(self, productos):
    self._productos = productos
    self._reconstruir_indices()
```
✓ Verificado en Paso 8

---

## Criterios de Aceptación

- [x] Ejecutar main.py y comprobación de funcionalidades de Semana 11
- [x] Registrar o cargar usuarios, productos y ventas existentes
- [x] Comprobación de búsqueda de producto mediante código (O(1))
- [x] Comprobación de búsqueda de usuario mediante identificación (O(1))
- [x] Consulta de ventas relacionadas con un usuario (O(1))
- [x] Realizar venta y confirmar actualización de stock
- [x] Verificación de sincronización de índices auxiliares
- [x] Cierre y reapertura del programa con recuperación de datos JSON
- [x] Reconstrucción de índices al iniciar

**RESULTADO FINAL: ✓ TODOS LOS CRITERIOS CUMPLIDOS**

---

## Notas Importantes

1. **Archivos JSON:** Se actualizan automáticamente después de cada operación
2. **Índices:** No se guardan en JSON (se reconstruyen al iniciar)
3. **Performance:** Las pruebas automáticas verifican cambios O(n) → O(1)
4. **Diagnóstico:** Opción 11 muestra el estado de sincronización en cualquier momento


