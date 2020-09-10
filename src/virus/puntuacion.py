class Puntuacion:
    def __init__(self):
        self.puntos = 0

    def calcularPuntaje(self):
        self.puntos += 5

    def obtenerPuntos(self):
        return self.puntos
