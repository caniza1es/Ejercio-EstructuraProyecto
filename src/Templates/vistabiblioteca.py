class VistaBiblioteca:
    @staticmethod
    def mostrar_libro(libro):
        print(f"Libro: {libro.titulo}, Autor: {libro.autor}, Género: {libro.genero}, Copias: {libro.copias}")

    @staticmethod
    def mostrar_libros(libros):
        for libro in libros:
            VistaBiblioteca.mostrar_libro(libro)

    @staticmethod
    def mostrar_usuario(usuario):
        print(f"Usuario: {usuario.nombre}, Email: {usuario.email}")

    @staticmethod
    def mostrar_prestamo(prestamo):
        print(f"Prestamo: {prestamo.libro.titulo} a {prestamo.usuario.nombre}, Activo: {prestamo.activo}")