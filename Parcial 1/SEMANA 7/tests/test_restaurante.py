def test_registrar_y_buscar():
    """Prueba simple: registrar productos y clientes y buscarlos."""
    from restaurante_app.servicios.restaurante import Restaurante
    from restaurante_app.modelos.producto import Producto
    from restaurante_app.modelos.cliente import Cliente

    r = Restaurante()
    r.precargar_ejemplos()
    # Se esperan 3 productos y 2 clientes precargados
    assert len(r.listar_productos()) >= 3
    assert len(r.listar_clientes()) >= 2

    # Registrar nuevo producto y cliente
    nuevo = Producto("Tallarín Saltado", "Plato Principal", 28.0)
    r.registrar_producto(nuevo)
    encontrado = r.buscar_producto("Tallarín Saltado")
    assert encontrado is not None and encontrado.nombre == "Tallarín Saltado"

    nuevo_cli = Cliente("99", "Prueba Test", "t@test.com")
    r.registrar_cliente(nuevo_cli)
    encontrado_cli = r.buscar_cliente("99")
    assert encontrado_cli is not None and encontrado_cli.id_cliente == "99"

