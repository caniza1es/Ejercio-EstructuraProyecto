class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.prestamos_activos = []