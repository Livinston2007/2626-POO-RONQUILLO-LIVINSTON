# Archivo: main.py
# Programa 2: Programación Orientada a Objetos
# Demostración de uso de clases, objetos, atributos y métodos

from mascota import Mascota


def menu_principal():
    """Función que muestra el menú principal y gestiona las opciones"""
    mascotas = []
    
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE MASCOTAS - POO")
        print("="*50)
        print("1. Crear una nueva mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Hacer sonar una mascota")
        print("4. Envejecer una mascota")
        print("5. Cambiar nombre de mascota")
        print("6. Ver cantidad total de mascotas")
        print("7. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-7): ")
        
        if opcion == "1":
            crear_mascota(mascotas)
        elif opcion == "2":
            mostrar_todas_mascotas(mascotas)
        elif opcion == "3":
            hacer_sonido_mascota(mascotas)
        elif opcion == "4":
            envejecer_mascota(mascotas)
        elif opcion == "5":
            cambiar_nombre_mascota(mascotas)
        elif opcion == "6":
            print(f"\nTotal de mascotas creadas: {Mascota.obtener_cantidad_mascotas()}")
        elif opcion == "7":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 7.")


def crear_mascota(mascotas):
    """Función para crear una nueva mascota"""
    print("\n" + "="*50)
    print("CREAR NUEVA MASCOTA")
    print("="*50)
    
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (perro/gato/ave/conejo/etc.): ")
    
    try:
        edad = float(input("Ingrese la edad (en años): "))
        nueva_mascota = Mascota(nombre, especie, edad)
        mascotas.append(nueva_mascota)
        print(f"\n✓ Mascota '{nombre}' creada exitosamente!")
    except ValueError:
        print("\n✗ La edad debe ser un número válido.")


def mostrar_todas_mascotas(mascotas):
    """Función para mostrar todas las mascotas registradas"""
    if not mascotas:
        print("\n✗ No hay mascotas registradas.")
        return
    
    print("\n" + "="*50)
    print("LISTA DE MASCOTAS")
    print("="*50)
    for i, mascota in enumerate(mascotas, 1):
        print(f"\n{i}. {mascota}")
    
    print("\n" + "="*50)
    print("INFORMACIÓN DETALLADA")
    print("="*50)
    for mascota in mascotas:
        mascota.mostrar_informacion()


def hacer_sonido_mascota(mascotas):
    """Función para que una mascota emita su sonido"""
    if not mascotas:
        print("\n✗ No hay mascotas registradas.")
        return
    
    mostrar_lista_mascotas(mascotas)
    
    try:
        indice = int(input("\nSeleccione el número de la mascota: ")) - 1
        if 0 <= indice < len(mascotas):
            mascotas[indice].hacer_sonido()
        else:
            print("\n✗ Número de mascota inválido.")
    except ValueError:
        print("\n✗ Por favor, ingrese un número válido.")


def envejecer_mascota(mascotas):
    """Función para envejecer una mascota"""
    if not mascotas:
        print("\n✗ No hay mascotas registradas.")
        return
    
    mostrar_lista_mascotas(mascotas)
    
    try:
        indice = int(input("\nSeleccione el número de la mascota: ")) - 1
        if 0 <= indice < len(mascotas):
            mascotas[indice].envejecer()
        else:
            print("\n✗ Número de mascota inválido.")
    except ValueError:
        print("\n✗ Por favor, ingrese un número válido.")


def cambiar_nombre_mascota(mascotas):
    """Función para cambiar el nombre de una mascota"""
    if not mascotas:
        print("\n✗ No hay mascotas registradas.")
        return
    
    mostrar_lista_mascotas(mascotas)
    
    try:
        indice = int(input("\nSeleccione el número de la mascota: ")) - 1
        if 0 <= indice < len(mascotas):
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            mascotas[indice].cambiar_nombre(nuevo_nombre)
        else:
            print("\n✗ Número de mascota inválido.")
    except ValueError:
        print("\n✗ Por favor, ingrese un número válido.")


def mostrar_lista_mascotas(mascotas):
    """Función auxiliar para mostrar la lista de mascotas"""
    print("\nMascotas disponibles:")
    for i, mascota in enumerate(mascotas, 1):
        print(f"{i}. {mascota}")


def demostrar_poo():
    """
    Función de demostración que crea al menos 2 objetos de la clase Mascota
    y ejecuta sus métodos.
    """
    print("\n" + "="*70)
    print("DEMOSTRACIÓN: PROGRAMACIÓN ORIENTADA A OBJETOS")
    print("="*70)
    
    # Crear objetos (instancias) de la clase Mascota
    print("\n--- Creando objetos de la clase Mascota ---")
    mascota1 = Mascota("Rex", "perro", 5)
    print(f"✓ Objeto 1 creado: {mascota1}")
    
    mascota2 = Mascota("Misi", "gato", 3)
    print(f"✓ Objeto 2 creado: {mascota2}")
    
    mascota3 = Mascota("Tweety", "ave", 2)
    print(f"✓ Objeto 3 creado: {mascota3}")
    
    # Ejecutar método mostrar_informacion()
    print("\n--- Ejecutando método mostrar_informacion() ---")
    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()
    mascota3.mostrar_informacion()
    
    # Ejecutar método hacer_sonido()
    print("\n--- Ejecutando método hacer_sonido() ---")
    mascota1.hacer_sonido()
    mascota2.hacer_sonido()
    mascota3.hacer_sonido()
    
    # Ejecutar método envejecer()
    print("\n--- Ejecutando método envejecer() ---")
    mascota1.envejecer()
    mascota2.envejecer()
    
    # Ejecutar método cambiar_nombre()
    print("\n--- Ejecutando método cambiar_nombre() ---")
    mascota1.cambiar_nombre("Rocky")
    
    # Mostrar información actualizada
    print("\n--- Información actualizada de los objetos ---")
    mascota1.mostrar_informacion()
    mascota2.mostrar_informacion()
    
    # Mostrar cantidad total de mascotas (método estático)
    print(f"--- Total de mascotas creadas (método estático): {Mascota.obtener_cantidad_mascotas()} ---\n")


if __name__ == "__main__":
    # Ejecutar demostración
    demostrar_poo()
    
    # Iniciar menú interactivo
    menu_principal()
