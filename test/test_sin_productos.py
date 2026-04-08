from pedido import Pedido

# ==========================
# Test: Calcular total sin productos
# ==========================
def test_sin_productos():
    # Pedido sin productos
    p = Pedido("Juan")
    
    # Como no hay productos, calcular total debería retornar None
    assert p.calcular_total() is None