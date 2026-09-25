# Restaurante App - Semana 15

Aplicación modular de gestión de restaurante desarrollada con Tkinter, evolucionando la versión anterior para incorporar ventas y el flujo de eventos del usuario hacia la lógica de negocio.

## Objetivo de la semana

- Mantener el inicio de sesión y la navegación previa.
- Conservar la gestión de productos y usuarios ya funcionando.
- Añadir la sección de ventas como evolución del proyecto.
- Evidenciar el flujo: usuario → botón → command= → callback → servicio → persistencia → respuesta visual.
- Separar responsabilidades entre interfaz, servicios, modelos y archivos JSON.

## Estructura del proyecto

```text
restaurante_app/
├── assets/
│   ├── icon_ventas.png
│   └── logo_restaurante.png
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
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── __init__.py
├── main.py
├── README.md
└── __pycache__/
```

## Funcionalidades agregadas

- Sección de ventas dentro del menú principal.
- Selección de usuario y producto mediante `ttk.Combobox`.
- Botón `Registrar venta` asociado a `command=self.registrar_venta`.
- Callback de venta que obtiene los datos de la interfaz y delega la operación a `RestauranteServicio`.
- Validación de usuario, producto y stock dentro del servicio.
- Persistencia de ventas mediante `datos/ventas.json`.
- Actualización automática de la tabla de ventas tras registrar una operación.
- Integración visual de activos en `assets/` para logo e ícono de ventas.

## Flujo funcional

Usuario
↓
Botón / componente
↓
command=
↓
Callback de venta
↓
RestauranteServicio
↓
Validación y persistencia
↓
Actualizar Treeview y mensaje visual

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `1234`

También existen usuarios de prueba como `ana` y `carlos`.

## Reglas de diseño

- La interfaz captura la interacción del usuario y presenta resultados.
- Las validaciones, negocio y persistencia de ventas quedan en `RestauranteServicio`.
- `ArchivoServicio` administra la lectura y escritura de archivos JSON.
- Los modelos representan entidades del restaurante: usuarios, productos y ventas.
- La aplicación conserva una sola ventana y alterna entre login y panel principal.
