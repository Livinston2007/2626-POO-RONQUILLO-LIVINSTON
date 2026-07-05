# Sistema Restaurante - App

**Estudiante:** Ronquillo Livinston

## Descripción
Este proyecto es una aplicación de consola en Python que administra los productos de un restaurante. Se ha desarrollado como parte de la evaluación de Programación Orientada a Objetos (POO), implementando conceptos clave como herencia, encapsulación y polimorfismo. El sistema permite gestionar los productos diferenciando entre platillos y bebidas, además de administrar sus precios y visualización.

## Estructura del Proyecto
El proyecto está dividido de forma modular para garantizar un código limpio y mantenible:
- `restaurante_app/`
  - `modelos/`: Contiene las clases base y derivadas.
    - `producto.py`: Clase padre `Producto`.
    - `platillo.py`: Clase hija `Platillo`.
    - `bebida.py`: Clase hija `Bebida`.
  - `servicios/`: Contiene la lógica de administración.
    - `restaurante.py`: Clase `Restaurante` que gestiona el menú.
  - `main.py`: Archivo principal que ejecuta la aplicación y contiene las demostraciones.

## Conceptos de POO Aplicados
1. **Herencia:** Se aplicó una relación lógica donde `Platillo` y `Bebida` heredan atributos y comportamientos comunes (como `nombre`, `precio` y `disponibilidad`) de la clase padre `Producto`. Se utilizó `super().__init__()` en las clases hijas para inicializar estos atributos heredados y añadir los propios (`calorias` y `tiempo_preparacion` en Platillo; `volumen_ml` y `tipo_bebida` en Bebida).
2. **Encapsulación:** Se protegió el atributo `__precio` en la clase `Producto` haciéndolo privado. De esta manera, se evita su modificación directa o la asignación de valores inválidos desde fuera de la clase. Para interactuar con él, se crearon los métodos de acceso `obtener_precio()` y de modificación `cambiar_precio()`, el cual incluye una validación lógica que impide establecer un precio negativo o cero.
3. **Polimorfismo:** El método `mostrar_informacion()` fue definido en la clase padre (`Producto`) y luego **sobrescrito** en las clases `Platillo` y `Bebida`. Al recorrer la lista de productos en el servicio de restaurante, se invoca a este método y cada objeto responde con su propia implementación, mostrando su información específica según sea platillo o bebida.

## Reflexión
Aplicar los principios de POO en proyectos modulares de Python permite crear código más organizado, altamente mantenible y fácil de escalar. La herencia evita la repetición de código al reutilizar lógica común, la encapsulación protege la integridad de los datos evitando que el sistema entre en estados inconsistentes, y el polimorfismo hace que el sistema sea más flexible al interactuar con diferentes tipos de objetos a través de una interfaz común. Finalmente, la separación del proyecto en módulos facilita el trabajo, la lectura del código y el mantenimiento a largo plazo.
