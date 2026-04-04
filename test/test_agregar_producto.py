"""Pruebas para el registro de productos en el inventario."""


def test_registrar_producto_validacion_profunda(mi_inventario):
    """
    Test Robusto de Registro:
    - Atributos, IDs incrementales, Persistencia y Aislamiento de datos.
    """
    # --- REGISTRO DEL PRIMER PRODUCTO ---
    p1_nombre, p1_cant, p1_precio = "Monitor 4K", 5, 350.0
    p1 = mi_inventario.registrar_producto(p1_nombre, p1_cant, p1_precio)

    # Assert 1: Atributos y Tipos
    assert p1.id == 1, "Error: El primer ID debe ser 1"
    assert p1.nombre == p1_nombre
    assert isinstance(p1.precio, float)

    # Assert 2: Persistencia Real
    p1_recuperado = mi_inventario.consultar_producto(p1.id)
    assert p1_recuperado is not None, "Error: El producto no se guardó en memoria"
    assert p1_recuperado.nombre == p1_nombre

    # --- REGISTRO DEL SEGUNDO PRODUCTO (Robustez Incremental) ---
    p2_nombre = "Teclado"
    p2 = mi_inventario.registrar_producto(p2_nombre, 10, 50.0)

    # Assert 3: ID Incremental
    assert p2.id == 2, "Error: El ID no incrementó correctamente"

    # Assert 4: Aislamiento (Verificar que p2 no sobreescribió a p1)
    assert (
        mi_inventario.consultar_producto(1).nombre == p1_nombre
    ), "Error: El segundo registro alteró el primero"
    assert mi_inventario.consultar_producto(2).nombre == p2_nombre
