import pygame
import laberinto.settingsLaberinto as s
from laberinto.ventanaLaberinto import *
from laberinto.cuadrosLaberinto import *
pygame.init()
s.init()
import os
import sys

bandera = True
PUNTOS_PATH = obtenerPathAbsoluto('assets/puntos.dat')

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
        with open(PUNTOS_PATH) as f:
            for lines in f:
                dato = int(lines.strip())
        dato += self.ventana.puntuacion.puntos
        arch = open(PUNTOS_PATH,'w')
        arch.write(str(dato))
        arch.close()
