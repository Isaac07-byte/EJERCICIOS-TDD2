from pedido import Pedido

# ==========================
# Test: Calcular total con múltiples productos
# ==========================
def test_multiples_productos():
    # Creamos un pedido para "Maria"
    p = Pedido("Maria")
    
    # Agregamos varios productos
    p.agregar_producto("A", 10000, 3)  # 10000*3 = 30000
    p.agregar_producto("B", 5000, 4)   # 5000*4 = 20000
    
    # Total esperado = 50000
    assert p.calcular_total() == 50000