from ruta.figuras import *
from ruta.audioPregunta import *

class VerificacionRuta:
    def __init__(self, audioPregunta, mapa):
        self.mapa = mapa
        self.respuestaPregunta = audioPregunta.obtenerLetraRespuesta()

    