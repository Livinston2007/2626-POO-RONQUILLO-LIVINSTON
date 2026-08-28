# Restaurante App - Semana 11

Aplicacion de consola para administrar productos, usuarios y ventas de un restaurante. Esta version evoluciona el trabajo de la Semana 10 incorporando stock, relacion entre usuario y producto vendido, consulta de ventas por usuario y persistencia JSON para las tres colecciones principales.

## Estructura

```text
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
├── main.py
└── README.md
```

## Modelos

- `Producto`: conserva codigo, nombre, categoria, precio y stock. Valida que el stock no sea negativo y descuenta unidades mediante `vender()`.
- `Usuario`: conserva identificacion, nombre y correo.
- `Venta`: registra `usuario_id`, `producto_codigo` y `cantidad`, creando la relacion entre usuario y producto.

Cada modelo tiene metodos para convertirse a diccionario y reconstruirse desde JSON.

## Servicios

- `Restaurante`: administra las colecciones de objetos y contiene la logica de negocio. Permite registrar, buscar, actualizar, eliminar, vender y consultar ventas por usuario.
- `ArchivoServicio`: carga y guarda `productos.json`, `usuarios.json` y `ventas.json` usando `json.load()`, `json.dump()`, `with open()` y codificacion UTF-8.

## Operacion de venta

La venta se realiza con `vender_producto(codigo_producto, identificacion_usuario, cantidad)`.

Antes de registrar una venta se valida:

- Que el usuario exista.
- Que el producto exista.
- Que la cantidad sea mayor que cero.
- Que exista stock suficiente.

Si la venta es valida, se crea un objeto `Venta`, se agrega a la coleccion interna y se descuenta el stock del producto. Luego se guardan `ventas.json` y `productos.json`.

## Persistencia

Los archivos JSON se almacenan en `restaurante_app/datos/`.

- `productos.json`: productos y stock actualizado.
- `usuarios.json`: usuarios registrados.
- `ventas.json`: ventas realizadas.

Si un archivo no existe, el sistema inicia esa coleccion vacia. Si un archivo tiene JSON invalido, se informa el problema y se inicia esa coleccion vacia. Los registros incompletos se omiten mostrando el error correspondiente.

## Ejecucion

Desde la carpeta `SEMANA 11`:

```bash
python .\restaurante_app\main.py
```

Tambien puede ejecutarse como modulo:

```bash
python -m restaurante_app.main
```

## Prueba manual sugerida

1. Ejecutar `main.py`.
2. Registrar un usuario.
3. Registrar un producto con stock disponible.
4. Vender una cantidad valida del producto al usuario.
5. Listar productos y confirmar que el stock disminuyo.
6. Revisar `datos/ventas.json` y confirmar que se registro la venta.
7. Consultar ventas por usuario.
8. Cerrar el programa.
9. Ejecutarlo nuevamente y confirmar que productos, usuarios y ventas se cargan desde JSON.
10. Intentar vender mas unidades que el stock disponible y confirmar que la venta se rechaza.
