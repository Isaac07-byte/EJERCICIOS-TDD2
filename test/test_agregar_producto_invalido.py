from pedido import Pedido

# ==========================
# Test: Agregar productos inválidos
# ==========================
def test_agregar_producto_invalido():
    # Pedido para "Juan"
    p = Pedido("Juan")
    
    # Precio negativo -> no se agrega
    assert p.agregar_producto("X", -100, 1) == False
    
    # Cantidad cero -> no se agrega
    assert p.agregar_producto("X", 100, 0) == False