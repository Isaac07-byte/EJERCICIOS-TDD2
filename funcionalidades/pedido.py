"""Utilidades para gestionar pedidos, productos y descuentos."""


class Pedido:
    """Representa un pedido asociado a un cliente."""

    def __init__(self, cliente):
        # Almacena el nombre del cliente.
        self.cliente = cliente
        # Lista que contiene los productos del pedido.
        self.productos = []

    def agregar_producto(self, nombre, precio, cantidad):
        """Agrega un producto valido al pedido."""
        if cantidad <= 0 or precio <= 0:
            return False

        self.productos.append(
            {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        )
        return True

    def calcular_total(self):
        """Calcula el total del pedido a partir de sus productos."""
        if not self.productos:
            return None

        total = 0
        for producto in self.productos:
            total += producto["precio"] * producto["cantidad"]

        return total

    def aplicar_descuento(self, porcentaje):
        """Aplica un descuento porcentual al total del pedido."""
        total = self.calcular_total()

        if total is None:
            return None

        if porcentaje < 0 or porcentaje > 100:
            return None

        descuento = total * (porcentaje / 100)
        return total - descuento
