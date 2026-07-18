from __future__ import annotations
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente


def prueba_rapida() -> None:
    print("\n--- Prueba rápida: registrar y listar objetos ---\n")
    serv = Restaurante()

    p1 = Producto('P001', 'Ensalada Cesar', 'Entrada', 5.50)
    b1 = Bebida('B001', 'Refresco Cola', 'Bebida', 1.75, '500ml', 'Lata')
    c1 = Cliente('C001', 'María Pérez', 'maria@example.com')

    serv.registrar_producto(p1)
    serv.registrar_producto(b1)
    serv.registrar_cliente(c1)

    print('\nListando productos:')
    for linea in serv.listar_productos():
        print(' ', linea)

    print('\nListando clientes:')
    for linea in serv.listar_clientes():
        print(' ', linea)

    print('\nIntentando registrar un producto con código duplicado (debe fallar):')
    try:
        serv.registrar_producto(Producto('P001', 'Sopa', 'Entrada', 3.00))
    except ValueError as e:
        print('  Error capturado:', e)


if __name__ == '__main__':
    prueba_rapida()
