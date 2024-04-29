import psycopg2
try:
    connection = psycopg2.connect(
        host = 'localhost',
        user = 'postgres',
        password = '123456789',
        database = 'Biblioteca'
    )
finally:
    connection.close()


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

    def obtener_autores_por_nacionalidad(self, nacionalidad):
        autores_nacionalidad = []
        for autor in self.autores:
            if autor.nacionalidad == nacionalidad:
                autores_nacionalidad.append(autor)
        return autores_nacionalidad

    def eliminar_autor(self, nombre):
        for autor in self.autores:
            if autor.nombre == nombre:
                self.autores.remove(autor)
                return True
        return False

    def actualizar_informacion_autor(self, nombre, nueva_nacionalidad, nueva_fecha_nacimiento, nuevo_genero):
        autor = self.obtener_autor_por_nombre(nombre)
        if autor:
            autor.nacionalidad = nueva_nacionalidad
            autor.fecha_nacimiento = nueva_fecha_nacimiento
            autor.genero = nuevo_genero
            return True
        return False
