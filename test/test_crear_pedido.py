# Importamos la clase Pedido desde el archivo pedido.py
from pedido import Pedido

# ==========================
# Test: Crear pedido
# ==========================
def test_crear_pedido():
    # Creamos un pedido para el cliente "Juan"
    p = Pedido("Juan")
    
    # Verificamos que el atributo cliente se haya guardado correctamente
    assert p.cliente == "Juan"
    
    # Verificamos que la lista de productos esté vacía al inicio
    assert p.productos == []