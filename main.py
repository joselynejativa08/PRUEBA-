# main.py
from src.libro_prueba import Libro
from src.Revista_prueba import Revista
from src.material_escolar_prueba import MaterialEscolar

# Crear objetos
libro1 = Libro("L001", "Cien años de soledad", 20.0, 5, "Gabriel García Márquez", "Novela")
revista1 = Revista("R001", "National Geographic", 10.0, 3, "Mayo 2023")
material1 = MaterialEscolar("M001", "Lápiz", 1.0, 10, "Útiles")

# Aplicar descuentos
libro1.aplicar_descuento()
revista1.aplicar_descuento()
material1.aplicar_descuento()

# Mostrar totales
print(f"Total libro: ${libro1.calcular_total():.2f}")
print(f"Total revista: ${revista1.calcular_total():.2f}")
print(f"Total material escolar: ${material1.calcular_total():.2f}")
