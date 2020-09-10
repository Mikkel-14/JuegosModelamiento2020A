#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                     Clase AudioPregunta 
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.assets.herramientas import *
from ruta.figuras import *


class AudioPregunta:
    def __init__(self, audio, letraRespuesta):
        self.audio = pygame.mixer.Sound(obtenerPathAbsoluto(audio, __file__)) # carga el audio unicamente en formato wav
        self.letraRespuesta = letraRespuesta
        self.estadoReproducion = True

    def reproducir(self, movimientoCamino, opciones):
        keys = pygame.key.get_pressed() # captura si se aplastó una tecla
        
        if keys[pygame.K_s] and movimientoCamino == False: # si la tecla es la "S" y el camino está detenido
            self.estadoReproducion = False 
            pygame.mixer.stop() # se detiene el audio completamente
            for opcion in opciones:
                if opcion.obtenerVisibilidad() == False:
                    opcion.setVisibilidad(True) # se hacen visibles las Figuras Opción
        elif self.estadoReproducion and movimientoCamino == False:  
            self.audio.play() # se reproduce el audio si el caminon está detenido y si el estado de reproducción es True

    def setEstadoReproducido(self, value):
        self.estadoReproducion = value
    
    def obtenerLetraRespuesta(self):
        return self.letraRespuesta


class Playlist:

    listaAudiosPreguntas = []

    def añadirAudioPregunta(self, pregunta):
        if isinstance(pregunta, AudioPregunta):
            self.listaAudiosPreguntas.append(pregunta)

    def quitarAudioPregunta(self, pregunta):
        self.listaAudiosPreguntas.remove(pregunta)
    
    def obtenerAudiosPreguntas(self):
        return self.listaAudiosPreguntas
