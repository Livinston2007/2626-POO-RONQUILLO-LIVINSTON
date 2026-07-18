from __future__ import annotations

"""Módulo con explicaciones didácticas sobre SOLID aplicado al proyecto.
Se usa desde los scripts de demostración."""


def mostrar_explicaciones() -> None:
    print("\n*** Explicación didáctica de SOLID aplicada al restaurante_app ***\n")
    print("SRP (Responsabilidad única): Cada clase cumple una sola responsabilidad:")
    print(" - Producto/Bebida: contienen datos y mostrar_informacion().")
    print(" - Cliente: representa datos de cliente.")
    print(" - Restaurante: gestiona colecciones y operaciones de registro/listado.")

    print("\nOCP (Abierto/Cerrado): Podemos añadir nuevas subclases de Producto (p. ej. Bebida)")
    print(" sin cambiar la lógica de Restaurante; el servicio sigue funcionando igual.")

    print("\nLSP (Sustitución de Liskov): Una Bebida puede usarse donde se espere un Producto.")
    print(" Restaurante llama a mostrar_informacion() en cada elemento sin preguntar el tipo.")

    print("\nPolimorfismo: Al listar productos, tanto Producto como Bebida responden a")
    print(" mostrar_informacion() con su propia representación.")

    print("\nFin de la explicación.\n")
