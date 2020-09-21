#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                       Clase Mensaje
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.assets.herramientas import *
from ruta.posicionMaya import *
from ruta.boton import *


class Mensaje:

    _flag = True

    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoVentana"])
        self.posicion = posicion
        self.visibilidad = False
        self.listaBotones = []

    def agregarBoton(self, boton):
        self.listaBotones.append(boton)

    def quitarBoton(self, boton):
        self.listaBotones.remove(boton)

    def mostrar(self, ventana):
        self.visibilidad = True
        
        while self.visibilidad:
            ventana.blit(self.imagen, self.posicion.obtenerCoordenadas()) # Se dibuja el fondo del mensaje respectivo

            for boton in self.listaBotones: # para dibujar cada uno de los botones en el mensaje
                boton.render(ventana)
            
            for event in pygame.event.get(): 
                for boton in self.listaBotones:
                    # Los botones "OK", "JUGAR" y "VOLVER_A_JUGAR" si son seleccionados unicamente cerrarán el mensaje respectivo 
                    if (boton.obtenerTipo() == "OK" or boton.obtenerTipo() == "JUGAR" or boton.obtenerTipo() == "VOLVER_A_JUGAR") and boton.onClic(event)[1]:
                        self.visibilidad = False
                    elif boton.obtenerTipo() == "VOLVER_AL_MUSEO" and boton.onClic(event)[1]:
                        pygame.quit()
                        self._flag = False
                        self.visibilidad = False
                        break
                if event.type == pygame.QUIT:
                    self.visibilidad = False
                    break
                    pygame.quit()
            if (self.visibilidad or self._flag):
                pygame.display.update()