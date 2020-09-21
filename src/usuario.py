class Usuario:
    def __init__(self, nombreUsuario, password):
        self.nombreUsuario: nombreUsuario
        self.password: password

    def registrar(self):
        pass

    def ingresar(self):
        pass

    def getNombreUsuario(self):
        return self.nombreUsuario

    def getContraseña(self):
        return self.password