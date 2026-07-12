# Estructura final del proyecto

restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py         (Constructor, @property, @setter)
│   └── cliente.py          (@dataclass)
├── servicios/
│   ├── __init__.py
│   ├── restaurante.py      (Clase servicio principal)
│   ├── GUIA_DIDACTICA.md
│   ├── RESUMEN_EJECUTIVO.txt
│   ├── EJEMPLO_INTERACTIVO.md
│   ├── ESTRUCTURA_FINAL.md
│   ├── ARCHIVOS_CREADOS.txt
│   └── INICIO_RAPIDO.txt
└── main.py                 (Menú interactivo)

## Descripciones por archivo:

- **producto.py**: Modelo con constructor tradicional y propiedades
- **cliente.py**: Modelo con @dataclass
- **restaurante.py**: Servicio que administra productos y clientes
- **main.py**: Menú interactivo de consola

