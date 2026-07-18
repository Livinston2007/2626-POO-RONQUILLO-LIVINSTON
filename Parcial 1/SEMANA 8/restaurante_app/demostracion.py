from __future__ import annotations
import sys
from restaurante_app.demo_solid import main as demo_solid
from restaurante_app.demo_completo import ejemplo_completo


def menu_demo() -> None:
    print('\nElija una demostración:')
    print('1. Demo SOLID (explicaciones + prueba)')
    print('2. Demo completo (ejemplo con varios ítems)')
    opcion = input('Opción: ').strip()
    if opcion == '1':
        demo_solid()
    elif opcion == '2':
        ejemplo_completo()
    else:
        print('Opción no válida.')


if __name__ == '__main__':
    menu_demo()
