RESUMEN COMPLETO
=================

Este documento resume brevemente el proyecto restaurante_app y cómo se aplican
los principios SOLID en el diseño.

Estructura del proyecto
- modelos/: Contiene Producto, Bebida y Cliente.
- servicios/: Contiene Restaurante que administra colecciones.
- main.py: Interacción por consola y menú principal.
- demo_*.py: Scripts de demostración y pruebas.

Aplicación de SOLID
- SRP: Cada clase tiene una única responsabilidad.
- OCP: Nuevas subclases (p. ej. Bebida) amplían el sistema sin cambiar Restaurante.
- LSP: Las subclases de Producto (Bebida) pueden sustituir a la clase base sin errores.

Archivos añadidos
- explicaciones.py: Explicaciones didácticas.
- prueba_solid2.py: Prueba rápida que registra objetos y muestra listas.
- demo_solid.py, demo_completo.py, demostracion.py: Scripts para ejecutar demostraciones.

Instrucciones
Ejecutar demos desde la carpeta del proyecto con:

python -m restaurante_app.demo_solid
python -m restaurante_app.demo_completo
python -m restaurante_app.demostracion

Reflexión
Diseñar con responsabilidades claras facilita el mantenimiento y la extensibilidad.
