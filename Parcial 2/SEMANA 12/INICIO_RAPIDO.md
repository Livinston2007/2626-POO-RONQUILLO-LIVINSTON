# Guía de Inicio Rápido (Semana 12)

## Instalación y Ejecución

### Requisitos
- Python 3.7+
- Sin dependencias externas requeridas

### Pasos para ejecutar

```bash
# 1. Navegar a la carpeta del proyecto
cd Parcial\ 2/SEMANA\ 12/

# 2. Ejecutar el programa principal
python restaurante_app/main.py

# 3. O ejecutar las pruebas
python restaurante_app/test_semana_12.py
```

## Flujo de Uso del Sistema

### Iniciar el Programa
```bash
python restaurante_app/main.py
```

El programa automáticamente:
1. Carga productos desde `datos/productos.json`
2. Carga usuarios desde `datos/usuarios.json`
3. Carga ventas desde `datos/ventas.json`
4. Reconstruye índices en memoria
5. Muestra el menú principal

### Menú Principal

```
============================================================
          SISTEMA DE RESTAURANTE
============================================================
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Vender producto
9. Consultar ventas por usuario
10. Mostrar categorias
11. Ver estado de indices (diagnostico)
0. Salir
============================================================
Seleccione una opcion:
```

## Operaciones Básicas

### 1. Registrar un Producto

```
Seleccione una opcion: 1
--- Registrar producto ---
Codigo: P003
Nombre: Ensalada Fresca
Categoria: Ensaladas
Precio: 12000
Stock disponible: 15

Producto registrado correctamente.
```

**Optimización:** La validación de código duplicado ahora es O(1) ✓

### 2. Buscar un Producto

```
Seleccione una opcion: 2
--- Buscar producto ---
Codigo del producto: P001
[Producto] Codigo: P001 | Nombre: Hamburguesa clasica | Categoria: Comidas | Precio: $15000.00 | Stock: 8
```

**Optimización:** Búsqueda O(1) en lugar de O(n) ✓

### 3. Registrar un Usuario

```
Seleccione una opcion: 6
--- Registrar usuario ---
Identificacion: 1004
Nombre: Maria Lopez
Correo: maria.lopez@email.com

Usuario registrado correctamente.
```

**Optimización:** Validación de duplicados O(1) ✓

### 4. Realizar una Venta

```
Seleccione una opcion: 8
--- Vender producto ---
Identificacion del usuario: 1001
Codigo del producto: P001
Cantidad a vender: 2

Venta registrada correctamente.
```

**Optimización:** Búsquedas O(1) + índice de ventas actualizado ✓

### 5. Consultar Ventas de un Usuario

```
Seleccione una opcion: 9
--- Consultar ventas por usuario ---
Identificacion del usuario: 1001
Usuario: 1001 | Producto: P001 - Hamburguesa clasica | Cantidad: 2
Usuario: 1001 | Producto: B001 - Limonada natural | Cantidad: 1
Total de ventas encontradas: 2
```

**Optimización:** Consulta O(1) del diccionario de ventas por usuario ✓

### 6. Ver Estado de Índices

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

**Diagnóstico:** Verifica que los índices no estén desincronizados ✓

## Archivos de Datos

### Estructura JSON

Los datos se almacenan en la carpeta `datos/`:

#### productos.json
```json
[
  {
    "codigo": "P001",
    "nombre": "Hamburguesa clasica",
    "categoria": "Comidas",
    "precio": 15000.0,
    "stock": 8
  }
]
```

#### usuarios.json
```json
[
  {
    "identificacion": "1001",
    "nombre": "Laura Gomez",
    "correo": "laura.gomez@email.com"
  }
]
```

#### ventas.json
```json
[
  {
    "usuario_id": "1001",
    "producto_codigo": "P001",
    "cantidad": 2
  }
]
```

### Actualización de Datos

Los datos se guardan automáticamente después de cada operación:
- Registrar/Actualizar/Eliminar producto → actualiza `productos.json`
- Registrar usuario → actualiza `usuarios.json`
- Realizar venta → actualiza `ventas.json` y `productos.json` (stock)

## Tipos de Datos

### Producto
- **Codigo:** Identificador único (string)
- **Nombre:** Nombre del producto
- **Categoria:** Categoría (ej: Comidas, Bebidas, Postres)
- **Precio:** Precio en pesos (float)
- **Stock:** Cantidad disponible (int)

### Usuario
- **Identificacion:** ID único del usuario (string)
- **Nombre:** Nombre completo
- **Correo:** Correo electrónico

### Venta
- **Usuario_id:** ID del usuario que compra
- **Producto_codigo:** Código del producto
- **Cantidad:** Cantidad vendida

## Ejemplos de Uso

### Ejemplo 1: Crear una Venta Completa

```bash
# 1. Registrar un nuevo usuario
Opción 6 → ID: 5000, Nombre: Pedro, Correo: pedro@email.com

# 2. Registrar un nuevo producto
Opción 1 → Código: A001, Nombre: Arepa, Categoría: Comidas, Precio: 8000, Stock: 50

# 3. Realizar la venta
Opción 8 → Usuario: 5000, Producto: A001, Cantidad: 3

# 4. Verificar ventas del usuario
Opción 9 → Usuario: 5000
```

### Ejemplo 2: Consultar Estado del Sistema

```bash
# Ver productos
Opción 5

# Ver usuarios
Opción 7

# Ver categorías
Opción 10

# Diagnóstico de índices
Opción 11
```

## Validaciones del Sistema

El sistema valida automáticamente:

### Al registrar producto:
- ✓ Código no vacío
- ✓ Código único (búsqueda O(1))
- ✓ Nombre no vacío
- ✓ Categoría no vacía
- ✓ Precio no negativo
- ✓ Stock no negativo

### Al registrar usuario:
- ✓ Identificación no vacía
- ✓ Identificación única
- ✓ Nombre no vacío
- ✓ Correo no vacío

### Al realizar venta:
- ✓ Usuario existe (búsqueda O(1))
- ✓ Producto existe (búsqueda O(1))
- ✓ Cantidad > 0
- ✓ Stock suficiente

## Ejecución de Pruebas

### Ejecutar todas las pruebas

```bash
python restaurante_app/test_semana_12.py
```

### Pruebas Incluidas

1. **Prueba 1:** Carga de datos y sincronización de índices
2. **Prueba 2:** Búsqueda de productos (O(1))
3. **Prueba 3:** Búsqueda de usuarios (O(1))
4. **Prueba 4:** Consulta de ventas por usuario (O(1))
5. **Prueba 5:** Registrar producto y verificar índice
6. **Prueba 6:** Registrar usuario y verificar índice
7. **Prueba 7:** Registrar venta y verificar índices
8. **Prueba 8:** Eliminar producto y verificar índice
9. **Prueba 9:** Recargar datos y reconstruir índices

Si todas las pruebas pasan, la salida final será:

```
============================================================
TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ✓
============================================================
```

## Troubleshooting

### Problema: "Archivo no encontrado"
**Solución:** Verificar que está ejecutando desde la carpeta correcta
```bash
cd Parcial\ 2/SEMANA\ 12/
python restaurante_app/main.py
```

### Problema: "Error en JSON"
**Solución:** Los archivos JSON pueden haberse corrompido. Copiar desde una copia de seguridad o reiniciar con archivos vacíos.

### Problema: Índices desincronizados
**Solución:** Ejecutar opción 11 para diagnóstico. Si muestra "✗ Desincroni
zados", reiniciar el programa.

## Características Únicas de Semana 12

### 1. Índices O(1)
- Búsqueda de producto por código: O(1)
- Búsqueda de usuario por ID: O(1)
- Consulta de ventas por usuario: O(1)

### 2. Sincronización Automática
- Los índices se actualizan con cada operación
- Se reconstruyen al cargar desde JSON

### 3. Diagnóstico
- Opción 11 para ver estado de índices
- Verifica sincronización automáticamente

### 4. Mismas Características de Semana 11
- ✓ Persistencia JSON
- ✓ Validaciones de negocio
- ✓ Control de stock
- ✓ Historial de ventas

## Próximos Pasos

Si desean agregar más funcionalidades:
- Índices por categoría (para búsquedas rápidas)
- Índices por rango de precio
- Estadísticas de ventas
- Reportes por período

Pero estas NO son necesarias para Semana 12.

## Soporte

Para entender mejor cómo funcionan los índices:
- Ver `GUIA_TECNICA.md` para análisis detallado
- Ver `restaurante_app/servicios/restaurante.py` para el código completo
- Ver `restaurante_app/test_semana_12.py` para ejemplos de uso

