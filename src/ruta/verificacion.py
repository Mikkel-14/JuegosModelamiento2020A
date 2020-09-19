#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                     Clase Verificación 
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

from ruta.assets.herramientas import *
from ruta.audioPregunta import *
from ruta.figuras import *
from time import sleep


class Verificacion:

    _numeroPreguntasContestadas = 0
    _i = 0

    def __init__(self, audiosPreguntas, mapa, puntaje):
        self.mapa = mapa
        self.audios = audiosPreguntas
        self.puntaje = puntaje
        
    def verificarSeleccion(self, letraSeleccionada):
        self._numeroPreguntasContestadas += 1 # Luego de haber seleccionado una opción se incrementa la variable
        if(self.audios.listaAudiosPreguntas[self._i].obtenerLetraRespuesta() == letraSeleccionada):
            pygame.mixer.music.load(obtenerPathAbsoluto('sounds/sonidoRespuestaCorrecta.mp3', __file__))
            pygame.mixer.music.play(0) # Se reproduce reiteradamente
            sleep(3) # para controlar la fluidez del juego con el audio se emplea sleep
            self.mapa.actualizar(True) # True para actualizar la visibilidad de las opcines
            self.puntaje.incrementar()
        else:
            pygame.mixer.music.load(obtenerPathAbsoluto('sounds/sonidoRespuestaIncorrecta.mp3', __file__))
            pygame.mixer.music.play(0)
            sleep(3)
            self.mapa.actualizar(False) # False para actualizar la FiguraVida y restar una vida
        self._i+=1

    def reiniciarNumeroPreguntasContestadas(self):
        self._numeroPreguntasContestadas = 0

    def obtenerNumeroPreguntasContestadas(self):
        return self._numeroPreguntasContestadas