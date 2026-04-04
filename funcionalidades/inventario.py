"""Funciones y clases para gestionar productos en un inventario en memoria."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Producto:
    """Representa un producto dentro del sistema de inventario."""
    id: int
    nombre: str
    cantidad: int
    precio: float


class Inventario:
    """Administra el registro, consulta y actualización de productos."""

    def __init__(self) -> None:
        """Inicializa el inventario con una estructura en memoria."""
        self._productos: Dict[int, Producto] = {}
        self._id_actual = 1

    def registrar_producto(self, nombre: str, cantidad: int, precio: float) -> Producto:
        """Registra un producto nuevo validando los datos de entrada."""
        if not nombre or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa")
        if precio <= 0:
            raise ValueError("El precio debe ser mayor a cero")

        nuevo_producto = Producto(self._id_actual, nombre, cantidad, precio)
        self._productos[nuevo_producto.id] = nuevo_producto
        self._id_actual += 1
        return nuevo_producto

    def consultar_producto(self, producto_id: int) -> Optional[Producto]:
        """Refactor: Consulta con validación de tipo de entrada."""
        if not isinstance(producto_id, int):
            raise TypeError("El ID del producto debe ser un número entero.")

        if producto_id <= 0:
            return None

        return self._productos.get(producto_id)

    def actualizar_cantidad(self, producto_id: int, nueva_cantidad: int) -> Producto:
        """Refactor: Actualiza cantidad con validaciones de integridad."""
        if producto_id not in self._productos:
            raise ValueError("Error: Producto no encontrado en el inventario.")

        if nueva_cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")

        producto = self._productos[producto_id]
        producto.cantidad = nueva_cantidad
        return producto

    def listar_productos(self) -> List[Producto]:
        """
        Refactor: Retorna una lista protegida y ordenada de los productos.
        Ordena los resultados por ID para mantener la consistencia en la vista.
        """
        # Obtenemos los valores y los ordenamos por el atributo ID
        return sorted(self._productos.values(), key=lambda p: p.id)
