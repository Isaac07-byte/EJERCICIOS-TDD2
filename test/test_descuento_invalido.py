from pedido import Pedido

# ==========================
# Test: Aplicar descuentos inválidos
# ==========================
def test_descuento_invalido():
    # Pedido con un producto
    p = Pedido("Carlos")
    p.agregar_producto("Gorra", 100000, 1)
    
    # Porcentaje mayor a 100 -> invalido
    assert p.aplicar_descuento(150) is None
    
    # Porcentaje negativo -> invalido
    assert p.aplicar_descuento(-10) is None