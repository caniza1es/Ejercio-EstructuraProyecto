from autor import *

class ControladorAutorLibro:
    def _init_(self):
        self.autores = []

    def agregar_autor(self, autor):
        self.autores.append(autor)

    def obtener_autor_por_nombre(self, nombre):
        for autor in self.autores:
            if autor.nombre == nombre:
                return autor
        return None

