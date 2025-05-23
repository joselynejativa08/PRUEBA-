# libro.py
# Miembros del grupo: [Nombre1, Nombre2, ...]

from src.Producto_prueba import Producto

class Libro(Producto):
    """
    Representa un libro en el inventario.
    """

    def __init__(self, codigo, nombre, precio, cantidad, autor, genero):
        super().__init__(codigo, nombre, precio, cantidad)
        self.autor = autor
        self.genero = genero

    def aplicar_descuento(self):
        # 10% de descuento para libros
        self.precio *= 0.90
