# revista.py
# Miembros del grupo: [Nombre1, Nombre2, ...]

from src.Producto_prueba import Producto

class Revista(Producto):
    """
    Representa una revista en el inventario.
    """

    def __init__(self, codigo, nombre, precio, cantidad, edicion):
        super().__init__(codigo, nombre, precio, cantidad)
        self.edicion = edicion

    def aplicar_descuento(self):
        # 5% de descuento para revistas
        self.precio *= 0.95
