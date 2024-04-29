
import sys

sys.path.insert(1,'utils')
from ControladorBiblioteca import *

class Main:
    def __init__(self):
        self.controlador = ControladorBiblioteca()

    def ejecutar(self):
        self.controlador.agregar_libro("La Odisea", "Homero", "Épico", 5)
        self.controlador.agregar_libro("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 3)
        self.controlador.mostrar_libros()
        self.controlador.agregar_usuario("Alice", "alice@example.com")
        self.controlador.agregar_usuario("Bob", "bob@example.com")
        self.controlador.realizar_prestamo("La Odisea", "Alice")
        self.controlador.realizar_prestamo("Cien años de soledad", "Bob")

if __name__ == "__main__":
    main = Main()
    main.ejecutar()