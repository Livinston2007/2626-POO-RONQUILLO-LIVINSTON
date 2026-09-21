# Restaurante App - Semana 14

Aplicación modular de gestión de restaurante desarrollada con Tkinter, siguiendo la arquitectura de datos, modelos, servicios e interfaz de usuario.

## Estructura del proyecto

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
├── __init__.py
├── main.py
├── README.md
└── __pycache__/
```

## Objetivo de la semana

- Mantener el flujo de inicio de sesión.
- Mejorar la interfaz principal con contenedores y organización visual.
- Utilizar componentes de Tkinter para formularios, navegación y visualización.
- Mantener la lógica de negocio en `RestauranteServicio`.
- Realizar operaciones de productos con registro, consulta, actualización y eliminación.
- Persistir los cambios en `datos/productos.json` mediante el servicio correspondiente.

## Funcionalidades

- Inicio de sesión con credenciales válidas.
- Consulta de usuarios registrados.
- Gestión de productos con formulario y botones de acción.
- Búsqueda, actualización y eliminación de productos por código.
- Revisión inmediata de la información mostrada después de cada operación.

## Ejecución

Desde la carpeta del proyecto:

```bash
python main.py
```

## Credenciales de prueba

- Usuario: `admin`
- Contraseña: `admin123`

También hay usuarios de prueba como `ana` y `carlos`.

## Reglas de diseño

- La interfaz se encarga de capturar información y mostrar resultados.
- Las validaciones y cambios de estado del negocio quedan en `RestauranteServicio`.
- El acceso a archivos JSON se realiza a través de `ArchivoServicio`.
- La aplicación mantiene una sola ventana y alterna entre login y panel principal.
