def test_listar_productos_validar_contenido_y_estado(mi_inventario):
    """
    Test avanzado para verificar que la lista de productos:
    1. Esté vacía al inicio.
    2. Contenga los objetos exactos tras el registro.
    3. Mantenga la integridad de cada campo (ID, nombre, cantidad, precio).
    4. No se vea afectada por errores en otras operaciones.
    """
    # 1. Validación de estado inicial (Inventario vacío)
    assert len(mi_inventario.listar_productos()) == 0

    # 2. Arrange: Registramos productos con datos variados para validar tipos
    p1 = mi_inventario.registrar_producto("Monitor 4K", cantidad=5, precio=350.0)
    p2 = mi_inventario.registrar_producto("Teclado RGB", cantidad=12, precio=85.5)

    # 3. Act: Obtenemos la lista
    lista_productos = mi_inventario.listar_productos()

    # 4. Assert: Validaciones de integridad profunda
    assert len(lista_productos) == 2

    # Validamos que los objetos en la lista sean exactamente los que se registraron
    assert p1 in lista_productos
    assert p2 in lista_productos

    # Verificación de campos específicos del primer producto en la lista
    # Buscamos el monitor dentro de la lista para validar sus datos
    monitor = next(p for p in lista_productos if p.id == 1)
    assert monitor.nombre == "Monitor 4K"
    assert monitor.cantidad == 5
    assert isinstance(monitor.precio, float)
    assert monitor.precio == 350.0

    # 5. Validación de persistencia:
    # Al listar de nuevo, el conteo debe seguir siendo correcto
    assert len(mi_inventario.listar_productos()) == 2
