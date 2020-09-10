class Puntuacion:
    def __init__(self):
        self.puntos = 0

    def calcularPuntaje(self):
        self.puntos += 1

    def obtenerPuntos(self):
        return self.puntos
