import pygame
from time import time
from ruta.assets.herramientas import *
from ruta.figuras import *


class AudioPregunta:
    def __init__(self, audio, letraRespuesta, opciones):
        pygame.mixer.init()
        self.audio = pygame.mixer.Sound(obtenerPathAbsoluto(audio, __file__))
        self.letraRespuesta = letraRespuesta
        self.opciones = opciones
        self.estadoReproducido = True

    def reproducir(self, camino):
        keys = pygame.key.get_pressed()
        if(keys[pygame.K_s] and camino.notificar() == False):
            self.estadoReproducido = False
        
        if(self.estadoReproducido and camino.notificar() == False):
            self.audio.play()

        if(self.estadoReproducido == False and camino.notificar() == False ):
            pygame.mixer.stop()
            for opcion in self.opciones:
                if opcion.obtenerVisibilidad() == False:
                    opcion.setVisibilidad(True)

    def setEstadoReproducido(self, value):
        self.estadoReproducido = value
    
    def obtenerLetraRespuesta(self):
        return self.letraRespuesta