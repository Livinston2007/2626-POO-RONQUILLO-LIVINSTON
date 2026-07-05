import sys
import os

# Asegurar que las importaciones funcionen correctamente añadiendo el directorio actual
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

def main():
    print("Iniciando el sistema del restaurante...\n")

    # 1. Instanciar la clase de servicio Restaurante
    mi_restaurante = Restaurante("El Sabor Oriental")

    # 2. Crear objetos de tipo Platillo
    platillo1 = Platillo("Ramen Tradicional", 8.50, True, 600, 20)
    platillo2 = Platillo("Sushi Roll (8 piezas)", 12.00, True, 450, 15)

    # 3. Crear objetos de tipo Bebida
    bebida1 = Bebida("Té Verde Helado", 2.50, True, 400, "Fría")
    bebida2 = Bebida("Sake Caliente", 6.00, True, 150, "Caliente")

    # 4. Agregar los objetos a la lista administrada por Restaurante
    print("Registrando productos...")
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(bebida2)

    # 5. Mostrar la información registrada de forma organizada (Demostración de Polimorfismo)
    mi_restaurante.mostrar_menu()

    # 6. Demostrar la encapsulación y sus métodos de acceso/modificación
    print("Demostración de Encapsulación:")
    # Obtener precio
    print(f"Precio actual del Sushi Roll: ${platillo2.obtener_precio():.2f}")
    
    # Modificar precio con valor válido
    platillo2.cambiar_precio(13.50)
    
    # Intentar modificar precio con valor inválido (Validación)
    bebida1.cambiar_precio(-1.00)

    # 7. Mostrar el menú actualizado
    mi_restaurante.mostrar_menu()

if __name__ == "__main__":
    main()
