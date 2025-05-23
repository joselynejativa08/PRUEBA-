# producto.py
# Miembros del grupo: [Nombre1, Nombre2, ...]

from abc import ABC, abstractmethod

class Producto(ABC):
    """
    Clase base abstracta que representa un producto genérico en la librería.
    """

    def __init__(self, codigo, nombre, precio, cantidad):
        self._codigo = codigo
        self._nombre = nombre
        self._precio = precio
        self._cantidad = cantidad

    # Getters y Setters con encapsulamiento
    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self._precio = nuevo_precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad

    @abstractmethod
    def aplicar_descuento(self):
        pass

    def calcular_total(self):
        return self._precio * self._cantidad
