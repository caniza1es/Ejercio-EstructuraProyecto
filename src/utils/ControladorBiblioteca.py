from Biblioteca import *
from VistaBiblioteca import *
from Prestamo import *
from Usuario import *
from Libro import *

class ControladorBiblioteca:
    def __init__(self):
        self.modelo = Biblioteca()
        self.usuarios = []
        self.prestamos = []
        self.vista = VistaBiblioteca()

    def agregar_libro(self, titulo, autor, genero, copias=1):
        libro = Libro(titulo, autor, genero, copias)
        self.modelo.agregar_libro(libro)

    def mostrar_libros(self):
        libros = self.modelo.obtener_libros()
        self.vista.mostrar_libros(libros)

    def agregar_usuario(self, nombre, email):
        usuario = Usuario(nombre, email)
        self.usuarios.append(usuario)

    def realizar_prestamo(self, libro_titulo, usuario_nombre):
        libro = next((libro for libro in self.modelo.libros if libro.titulo == libro_titulo and libro.copias > 0), None)
        usuario = next((usuario for usuario in self.usuarios if usuario.nombre == usuario_nombre), None)
        if libro and usuario:
            prestamo = Prestamo(libro, usuario)
            libro.copias -= 1
            usuario.prestamos_activos.append(prestamo)
            self.prestamos.append(prestamo)
            print(f"Prestamo realizado: {libro_titulo} a {usuario_nombre}")
        else:
            print("Prestamo no realizado. Verifique el título del libro y el nombre del usuario.")