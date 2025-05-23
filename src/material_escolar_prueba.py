# material_escolar.py
# Miembros del grupo: [Nombre1, Nombre2, ...]

from src.Producto_prueba import Producto

class MaterialEscolar(Producto):
    """
    Representa un material escolar en el inventario.
    """

    def __init__(self, codigo, nombre, precio, cantidad, tipo):
        super().__init__(codigo, nombre, precio, cantidad)
        self.tipo = tipo

    def aplicar_descuento(self):
        # 15% de descuento para materiales escolares
        self.precio *= 0.85
