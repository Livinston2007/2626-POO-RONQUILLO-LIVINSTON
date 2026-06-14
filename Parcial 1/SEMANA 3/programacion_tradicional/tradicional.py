# Programa 1: Programación Tradicional
# Solución para registrar y mostrar información de mascotas
# Utilizando funciones y variables, sin clases ni objetos

# Lista global para almacenar mascotas
mascotas = []


def registrar_mascota():
    """Solicita los datos de una mascota por teclado y los registra"""
    print("\n" + "="*50)
    print("REGISTRO DE MASCOTA")
    print("="*50)
    
    # Solicitar datos
    nombre = input("Ingrese el nombre de la mascota: ")
    especie = input("Ingrese la especie (perro/gato/ave/otro): ")
    raza = input("Ingrese la raza: ")
    edad = input("Ingrese la edad (en años): ")
    color = input("Ingrese el color: ")
    peso = input("Ingrese el peso (en kg): ")
    dueno = input("Ingrese el nombre del dueño: ")
    
    # Crear diccionario con la información
    mascota = {
        "nombre": nombre,
        "especie": especie,
        "raza": raza,
        "edad": edad,
        "color": color,
        "peso": peso,
        "dueno": dueno
    }
    
    # Agregar a la lista
    mascotas.append(mascota)
    print("\n✓ Mascota registrada exitosamente!")


def mostrar_mascotas():
    """Muestra todas las mascotas registradas de forma organizada"""
    if not mascotas:
        print("\n" + "="*50)
        print("No hay mascotas registradas.")
        print("="*50)
        return
    
    print("\n" + "="*50)
    print("INFORMACIÓN DE MASCOTAS REGISTRADAS")
    print("="*50)
    
    for indice, mascota in enumerate(mascotas, 1):
        print(f"\n--- Mascota #{indice} ---")
        print(f"Nombre:    {mascota['nombre']}")
        print(f"Especie:   {mascota['especie']}")
        print(f"Raza:      {mascota['raza']}")
        print(f"Edad:      {mascota['edad']} años")
        print(f"Color:     {mascota['color']}")
        print(f"Peso:      {mascota['peso']} kg")
        print(f"Dueño:     {mascota['dueno']}")


def buscar_mascota_por_nombre():
    """Busca una mascota por nombre"""
    if not mascotas:
        print("\nNo hay mascotas registradas para buscar.")
        return
    
    nombre_buscar = input("\nIngrese el nombre de la mascota a buscar: ")
    encontrada = False
    
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscar.lower():
            print("\n" + "="*50)
            print("MASCOTA ENCONTRADA")
            print("="*50)
            print(f"Nombre:    {mascota['nombre']}")
            print(f"Especie:   {mascota['especie']}")
            print(f"Raza:      {mascota['raza']}")
            print(f"Edad:      {mascota['edad']} años")
            print(f"Color:     {mascota['color']}")
            print(f"Peso:      {mascota['peso']} kg")
            print(f"Dueño:     {mascota['dueno']}")
            encontrada = True
            break
    
    if not encontrada:
        print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscar}'")


def editar_mascota():
    """Permite editar la información de una mascota"""
    if not mascotas:
        print("\nNo hay mascotas registradas para editar.")
        return
    
    nombre_buscar = input("\nIngrese el nombre de la mascota a editar: ")
    
    for mascota in mascotas:
        if mascota['nombre'].lower() == nombre_buscar.lower():
            print("\n" + "="*50)
            print("EDITAR MASCOTA")
            print("="*50)
            print("Ingrese los nuevos datos (presione Enter para mantener el valor actual):")
            
            nuevo_nombre = input(f"Nombre [{mascota['nombre']}]: ") or mascota['nombre']
            nueva_especie = input(f"Especie [{mascota['especie']}]: ") or mascota['especie']
            nueva_raza = input(f"Raza [{mascota['raza']}]: ") or mascota['raza']
            nueva_edad = input(f"Edad [{mascota['edad']}]: ") or mascota['edad']
            nuevo_color = input(f"Color [{mascota['color']}]: ") or mascota['color']
            nuevo_peso = input(f"Peso [{mascota['peso']}]: ") or mascota['peso']
            nuevo_dueno = input(f"Dueño [{mascota['dueno']}]: ") or mascota['dueno']
            
            # Actualizar
            mascota['nombre'] = nuevo_nombre
            mascota['especie'] = nueva_especie
            mascota['raza'] = nueva_raza
            mascota['edad'] = nueva_edad
            mascota['color'] = nuevo_color
            mascota['peso'] = nuevo_peso
            mascota['dueno'] = nuevo_dueno
            
            print("\n✓ Mascota actualizada exitosamente!")
            return
    
    print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscar}'")


def eliminar_mascota():
    """Elimina una mascota del registro"""
    if not mascotas:
        print("\nNo hay mascotas registradas para eliminar.")
        return
    
    nombre_buscar = input("\nIngrese el nombre de la mascota a eliminar: ")
    
    for i, mascota in enumerate(mascotas):
        if mascota['nombre'].lower() == nombre_buscar.lower():
            confirmacion = input(f"¿Desea eliminar a {mascota['nombre']}? (s/n): ")
            if confirmacion.lower() == 's':
                mascotas.pop(i)
                print("✓ Mascota eliminada exitosamente!")
            else:
                print("✗ Operación cancelada.")
            return
    
    print(f"\n✗ No se encontró una mascota con el nombre '{nombre_buscar}'")


def menu_principal():
    """Muestra el menú principal y gestiona las opciones"""
    while True:
        print("\n" + "="*50)
        print("SISTEMA DE REGISTRO DE MASCOTAS")
        print("="*50)
        print("1. Registrar una mascota")
        print("2. Mostrar todas las mascotas")
        print("3. Buscar mascota por nombre")
        print("4. Editar mascota")
        print("5. Eliminar mascota")
        print("6. Salir")
        print("="*50)
        
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            registrar_mascota()
        elif opcion == "2":
            mostrar_mascotas()
        elif opcion == "3":
            buscar_mascota_por_nombre()
        elif opcion == "4":
            editar_mascota()
        elif opcion == "5":
            eliminar_mascota()
        elif opcion == "6":
            print("\n¡Hasta luego!")
            break
        else:
            print("\n✗ Opción inválida. Por favor, seleccione una opción del 1 al 6.")


if __name__ == "__main__":
    menu_principal()