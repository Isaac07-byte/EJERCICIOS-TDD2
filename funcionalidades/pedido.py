# ==========================
# Clase Pedido
# ==========================
# Esta clase representa un pedido de un cliente, donde se pueden agregar productos,
# calcular el total de la compra y aplicar descuentos.
class Pedido:
    # ==========================
    # Constructor de la clase
    # ==========================
    def __init__(self, cliente):
        # Almacena el nombre del cliente
        self.cliente = cliente
        # Lista que contendrá los productos del pedido
        self.productos = []

    # ==========================
    # Método para agregar un producto al pedido
    # ==========================
    def agregar_producto(self, nombre, precio, cantidad):
        # Validación: precio y cantidad deben ser mayores a 0
        if cantidad <= 0 or precio <= 0:
            return False  # Retorna False si los datos son inválidos
        
        # Agregamos el producto como un diccionario a la lista de productos
        self.productos.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })
        
        # Retorna True indicando que el producto se agregó correctamente
        return True

    # ==========================
    # Método para calcular el total del pedido
    # ==========================
    def calcular_total(self):
        # Verificamos que haya al menos un producto en el pedido
        if not self.productos:
            return None  # Retorna None si no hay productos
        
        # Inicializamos la variable total
        total = 0
        # Recorremos cada producto y sumamos precio * cantidad
        for p in self.productos:
            total += p["precio"] * p["cantidad"]
        
        # Retornamos el total calculado
        return total

    # ==========================
    # Método para aplicar un descuento sobre el total del pedido
    # ==========================
    def aplicar_descuento(self, porcentaje):
        # Calculamos el total actual del pedido
        total = self.calcular_total()

        # Si no hay productos, no se puede aplicar descuento
        if total is None:
            return None
        
        # Validamos que el porcentaje esté entre 0 y 100
        if porcentaje < 0 or porcentaje > 100:
            return None
        
        # Calculamos el descuento
        descuento = total * (porcentaje / 100)
        # Retornamos el total después de aplicar el descuento
        return total - descuento