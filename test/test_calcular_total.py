from pedido import Pedido

# ==========================
# Test: Calcular total con productos
# ==========================
def test_calcular_total():
    # Creamos un pedido para "Ana"
    p = Pedido("Ana")
    
    # Agregamos dos productos con precio y cantidad
    p.agregar_producto("Producto1", 30000, 2)  # 30000*2 = 60000
    p.agregar_producto("Producto2", 20000, 1)  # 20000*1 = 20000
    
    # Calculamos el total y verificamos que sea 80000
    assert p.calcular_total() == 80000