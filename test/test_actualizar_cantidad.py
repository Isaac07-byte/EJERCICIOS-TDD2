"""Pruebas para la actualizacion de cantidades en el inventario."""

import pytest

def test_actualizar_cantidad_exitoso_y_consistente(mi_inventario):
    """
    Valida la actualización de stock asegurando:
    1. Que la cantidad se modifique al valor exacto solicitado.
    2. Que el nombre y el precio NO cambien (invariabilidad de otros campos).
    3. Que los cambios se reflejen al consultar el inventario nuevamente.
    """
    # Arrange: Registramos un producto con datos fijos
    nombre_original = "Monitor 24 pulg"
    precio_original = 150.0
    p = mi_inventario.registrar_producto(
        nombre_original, cantidad=2, precio=precio_original
    )

    # Act: Actualizamos la cantidad de 2 a 10
    nueva_cantidad = 10
    producto_retornado = mi_inventario.actualizar_cantidad(p.id, nueva_cantidad)

    # Assert: Validación de la actualización
    assert producto_retornado.cantidad == nueva_cantidad

    # Verificación de Invariabilidad: El nombre y precio deben seguir igual
    assert producto_retornado.nombre == nombre_original
    assert producto_retornado.precio == precio_original

    # Verificación de Persistencia: Consultamos de nuevo para asegurar que se guardó
    p_en_memoria = mi_inventario.consultar_producto(p.id)
    assert p_en_memoria.cantidad == nueva_cantidad

def test_actualizar_cantidad_error_negativo(mi_inventario):
    """Valida que no se permitan cantidades negativas al actualizar."""
    p = mi_inventario.registrar_producto("Laptop", 5, 800.0)

    with pytest.raises(ValueError, match="La cantidad no puede ser negativa"):
        mi_inventario.actualizar_cantidad(p.id, -10)

def test_actualizar_cantidad_error_producto_inexistente(mi_inventario):
    """
    Valida el comportamiento defensivo del sistema:
    1. Debe lanzar ValueError si el ID no existe.
    2. El mensaje de error debe ser el definido por los requisitos.
    """
    # Arrange: Inventario vacío o con IDs diferentes
    id_falso = 999

    # Act & Assert: Verificamos que falle con la excepción y mensaje correctos
    mensaje_esperado = "Error: Producto no encontrado en el inventario."
    with pytest.raises(ValueError, match=mensaje_esperado):
        mi_inventario.actualizar_cantidad(id_falso, 50)
