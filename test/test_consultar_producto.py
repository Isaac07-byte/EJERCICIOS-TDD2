"""Pruebas para la consulta de productos en el inventario."""

def test_consultar_producto_integridad_datos(mi_inventario):
    """
    Valida que al consultar un producto existente:
    1. El objeto retornado no sea None.
    2. Todos los campos (ID, nombre, cantidad, precio) coincidan exactamente.
    3. El objeto retornado sea una instancia correcta de la clase Producto.
    """
    # Arrange: Registro de un producto con datos específicos
    datos_esperados = {"nombre": "Audífonos Gamer", "cantidad": 15, "precio": 59.90}
    p_creado = mi_inventario.registrar_producto(**datos_esperados)

    # Act: Consulta por el ID asignado automáticamente
    p_consultado = mi_inventario.consultar_producto(p_creado.id)

    # Assert: Validación de integridad profunda
    assert p_consultado is not None
    assert p_consultado.id == p_creado.id
    assert p_consultado.nombre == datos_esperados["nombre"]
    assert p_consultado.cantidad == datos_esperados["cantidad"]
    assert p_consultado.precio == datos_esperados["precio"]

    # Verificamos que sea el mismo objeto en memoria (opcional pero recomendado)
    assert p_consultado is p_creado


def test_consultar_producto_comportamiento_no_existente(mi_inventario):
    """
    Valida que el sistema maneje correctamente IDs inexistentes:
    1. Retorne None si el ID no ha sido registrado.
    2. No afecte el funcionamiento de otras consultas tras una búsqueda fallida.
    """
    # Arrange: Aseguramos que hay algo en el inventario para que no esté vacío
    mi_inventario.registrar_producto("Producto Prueba", 1, 10.0)

    # Act: Buscamos IDs inválidos (negativos, cero o inexistentes)
    resultado_inexistente = mi_inventario.consultar_producto(999)
    resultado_negativo = mi_inventario.consultar_producto(-1)

    # Assert
    assert resultado_inexistente is None
    assert resultado_negativo is None
