from __future__ import annotations
from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente
from restaurante_app.explicaciones import mostrar_explicaciones


def ejemplo_completo() -> None:
    mostrar_explicaciones()
    serv = Restaurante()

    items = [
        Producto('P100','Hamburguesa','Principal',8.50),
        Producto('P101','Papas Fritas','Acompañamiento',2.50),
        Bebida('B100','Agua Mineral','Bebida',1.00,'600ml','Botella'),
        Bebida('B101','Jugo Natural','Bebida',2.25,'350ml','Vaso'),
    ]
    clientes = [
        Cliente('CL01','Ana López','ana.lopez@example.com'),
        Cliente('CL02','Juan Gómez','juan.gomez@example.com'),
    ]

    for it in items:
        serv.registrar_producto(it)
    for cl in clientes:
        serv.registrar_cliente(cl)

    print('\n=== Productos registrados ===')
    for p in serv.listar_productos():
        print(' ', p)

    print('\n=== Clientes registrados ===')
    for c in serv.listar_clientes():
        print(' ', c)


if __name__ == '__main__':
    ejemplo_completo()
