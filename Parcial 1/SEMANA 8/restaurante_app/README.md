Nombre del estudiante: [Tu Nombre Aquí]

Descripción
-----------
Proyecto de ejemplo para la Semana 8 — sistema de restaurante simple que demuestra SRP, OCP y LSP.

Estructura
---------
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py

Ejecución
--------
Desde la raíz del proyecto (o desde la carpeta que contiene restaurante_app), ejecutar:

python -m restaurante_app.main

Principios aplicados
-------------------
- SRP: cada clase tiene una responsabilidad única.
- OCP: Bebida extiende Producto sin modificar la lógica del servicio.
- LSP: Bebida puede usarse donde se espere un Producto.

Breve reflexión
---------------
Diseñar con responsabilidades claras facilita mantener y ampliar el sistema sin tocar la lógica existente.
