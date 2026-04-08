from pedido import Pedido

# ==========================
# Test: Aplicar descuentos válidos
# ==========================
def test_descuento_valido():
    # Creamos un pedido para "Luis"
    p = Pedido("Luis")
    p.agregar_producto("Zapatos", 100000, 1)
    
    # Aplicamos un descuento del 10%
    assert p.aplicar_descuento(10) == 90000  # 100000 - 10% = 90000
    
    # Aplicamos un descuento del 0%
    assert p.aplicar_descuento(0) == 100000  # No hay descuento, total igual
    
    # Aplicamos un descuento del 100%
    assert p.aplicar_descuento(100) == 0      # Total gratis