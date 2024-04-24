class AutorLibro:
    def _init_(self, nombre, nacionalidad, fecha_nacimiento, genero):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento
        self.genero = genero
        self.libros_escritos = []
    
    def agregar_libro(self, libro):
        self.libros_escritos.append(libro)
    
    def obtener_libros(self):
        return self.libros_escritos
    
    def cantidad_libros(self):
        return len(self.libros_escritos)
    
    def escribir_libro(self, titulo):
        self.agregar_libro(titulo)
        return f"{self.nombre} ha escrito un nuevo libro: {titulo}"