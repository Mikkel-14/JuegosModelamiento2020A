import pygame
import laberinto.settingsLaberinto as s
from .ventanaLaberinto import *
from .cuadrosLaberinto import *
from .herramientas import *
pygame.init()
s.init()
import os
import sys

bandera = True

class Laberinto():
    def __init__(self):
        self.ventana = None

    def iniciarJuego(self):
        self.ventana = VentanaLaberinto()
        self.ventana.cargarTablero()
        
        bandera = True

        while bandera:
            self.ventana.reloj.tick(s.FPS)
            manejo = self.ventana.manejarMensajes(self)

            try:
                if manejo and bandera:
                    for cuadro in self.ventana.tablero.listaCuadros:
                        if isinstance(cuadro, PersonajeLaberinto) or isinstance(cuadro, EnemigoLaberinto):
                            cuadro.mover(s.velocidad, self.ventana.solapamiento)
                        cuadro.dibujar(self.ventana.win)
                    pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        bandera = False
                        pygame.quit()
                        break
            except Exception:
                break

    def reiniciarJuego(self):
        bandera = False
        pygame.quit()
        pygame.init()
        self.iniciarJuego()

    def salirJuego(self):
        bandera = False
        pygame.quit()

    def getPuntos(self):
        puntos = self.ventana.puntuacion.obtenerPuntos()
        return puntos
