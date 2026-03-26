

def test_registrar_producto_validacion_profunda(mi_inventario):
    """
    Test de alta fidelidad para el registro de productos:
    1. Verifica la asignación correcta de todos los atributos.
    2. Valida que el ID sea auto-incremental y único.
    3. Confirma que el producto se ha persistido en el estado interno del inventario.
    4. Asegura que los tipos de datos (str, int, float) sean los correctos.
    """
    # Arrange: Definimos los datos de entrada
    nombre_test = "Teclado Mecánico RGB"
    cantidad_test = 10
    precio_test = 45.99

    # Act: Realizamos el registro
    producto = mi_inventario.registrar_producto(nombre_test, cantidad_test, precio_test)

    # Assert 1: Validación de atributos del objeto retornado
    assert producto.id == 1, "El ID inicial debería ser 1"
    assert producto.nombre == nombre_test
    assert producto.cantidad == cantidad_test
    assert producto.precio == precio_test

    # Assert 2: Validación de Tipos (Seguridad de Tipado)
    assert isinstance(producto.id, int)
    assert isinstance(producto.nombre, str)
    assert isinstance(producto.cantidad, int)
    assert isinstance(producto.precio, float)

    # Assert 3: Validación de Persistencia (¿Realmente se guardó?)
    # Consultamos el inventario para ver si el producto existe dentro
    producto_en_memoria = mi_inventario.consultar_producto(producto.id)
    assert producto_en_memoria is not None, "El producto debería estar guardado en el inventario"
    assert producto_en_memoria.nombre == nombre_test

    # Assert 4: Validación de ID Incremental (Caso de segundo producto)
    segundo_producto = mi_inventario.registrar_producto("Mouse", 5, 15.0)
    assert segundo_producto.id == 2, "El sistema de IDs debe ser auto-incremental"