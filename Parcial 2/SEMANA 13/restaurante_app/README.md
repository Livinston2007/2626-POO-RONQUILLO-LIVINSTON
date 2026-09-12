# Restaurante App

Esta aplicación es una base gráfica para un sistema de restaurante, organizada siguiendo una estructura modular que separa modelos, servicios, datos y vistas.

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
├── README.md
└── __init__.py
```

## Objetivo

- Centralizar la carga de información desde archivos JSON.
- Mantener la lógica de negocio en `RestauranteServicio`.
- Separar la interfaz en una vista de acceso y una vista principal.
- Usar una sola ventana de Tkinter y cambiar entre pantallas sin abrir ventanas nuevas.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

## Credenciales de ejemplo

- Usuario: `admin`
- Contraseña: `admin123`

También se incluyen otros usuarios de prueba como `ana` y `carlos`.

## Funcionalidad actual

- Login con validación de credenciales.
- Visualización de productos desde `productos.json`.
- Visualización de usuarios desde `usuarios.json`.
- Panel principal con opciones de Productos, Usuarios y funcionalidad pendiente de ventas.
- Cierre de sesión que devuelve al login dentro de la misma ventana.
