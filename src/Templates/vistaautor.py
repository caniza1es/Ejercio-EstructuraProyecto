class VistaAutorLibro:
    @staticmethod
    def mostrar_informacion_autor(self, autor):
        print(f"Nombre: {autor.nombre}")
        print(f"Nacionalidad: {autor.nacionalidad}")
        print(f"Fecha de Nacimiento: {autor.fecha_nacimiento}")
        print(f"Género: {autor.genero}")
        print("Libros escritos:")
        for libro in autor.obtener_libros():
            print(f"- {libro}")