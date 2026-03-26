from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Producto:
    """Representa un producto dentro del sistema de inventario."""
    id: int
    nombre: str
    cantidad: int
    precio: float

class Inventario:
    def __init__(self):
        """
        Inicializa el inventario con una estructura de datos en memoria.
        Se utiliza un diccionario para permitir búsquedas rápidas por ID.
        """
        self._productos = {}
        self._id_actual = 1

    def registrar_producto(self, nombre: str, cantidad: int, precio: float) -> Producto:
        """
        Crea un nuevo producto, lo almacena y le asigna un ID único auto-incremental.
        """
        nuevo_p = Producto(self._id_actual, nombre, cantidad, precio)
        self._productos[nuevo_p.id] = nuevo_p
        self._id_actual += 1
        return nuevo_p

    def consultar_producto(self, producto_id: int) -> Optional[Producto]:
        """
        Busca un producto por su identificador único. 
        Retorna el objeto Producto si existe, de lo contrario retorna None.
        """
        return self._productos.get(producto_id)

    def actualizar_cantidad(self, producto_id: int, nueva_cantidad: int) -> Producto:
        """
        Modifica la cantidad disponible de un producto existente.
        Lanza ValueError si el ID proporcionado no existe en el sistema.
        """
        if producto_id not in self._productos:
            raise ValueError("Error: Producto no encontrado en el inventario.")
        
        producto = self._productos[producto_id]
        producto.cantidad = nueva_cantidad
        return producto

    def listar_productos(self) -> List[Producto]:
        """
        Retorna una lista con todos los productos registrados actualmente.
        """
        return list(self._productos.values())