from .observadorLaberinto import *
import laberinto.settingsLaberinto as s

class PuntuacionLaberinto(ObservadorLaberinto):
    def __init__(self):
        self.numeroErrores = 0
        self.puntos = 0

    def actualizar(self, virus, enemigo, meta, perdida, corazon):
        if virus or enemigo:
            self.numeroErrores += 1

    def calcularPuntos(self):
        self.puntos = int(s.puntosTOTALES - (self.numeroErrores * s.puntosTOTALES / s.maximo_de_vidas))

    def obtenerPuntos(self):
        return self.puntos
