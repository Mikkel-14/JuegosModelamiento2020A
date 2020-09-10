#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                        Clase Botón
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.assets.herramientas import *
from ruta.assets.settingsMaya import *
from ruta.posicionMaya import *


class Boton:
    def __init__(self, tipo, posicion):
        self.tipo = tipo
        if self.tipo == "OK":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botonOk.png', __file__))
        elif self.tipo == "JUGAR":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botonJugar.png', __file__))
        elif self.tipo == "VOLVER_A_JUGAR":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botónJugarOtraVez.png', __file__))
        elif self.tipo == "VOLVER_AL_MUSEO":
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/botónVolverAlMuseoMorado.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoBoton"]) 
        self.posicion = posicion
        
    def render(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def onClic(self, event):
        # Inicialización de superficieBoton para obtener el área rectangular de la imagen del botón
        superficieBoton = pygame.Rect(self.posicion.obtenerCoordenadas(), (self.imagen.get_rect().width, self.imagen.get_rect().height))
        
        if event.type == pygame.MOUSEBUTTONDOWN: # evento del tipo puntero mouse sobre un botón
            if event.button == 1: # El numero 1 hace referencia a si se registró un clic izquierdo
                if superficieBoton.collidepoint(event.pos): # es verdadera la condicion si se dio clic en la superficie del botón
                    return (self.tipo, True) # Retorno verdadero puesto que se efectuó un clic
        return (self.tipo, False) # Retorna falso cuando no se ha dado clic en el botón

    def obtenerTipo(self):
        return self.tipo
