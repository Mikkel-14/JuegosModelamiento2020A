import pygame
import laberinto.settingsLaberinto as s
from juego import *
from laberinto.cuadrosLaberinto import *
from laberinto.solapamientoLaberinto import *
from herramientas import *
pygame.init()
import os
import sys
sys.path.append('../juego.py')


CAMINOLAB_PATH = obtenerPathAbsoluto('laberinto/assets/CaminoLaberinto1.txt')
POSICION_VIRUS_PATH = obtenerPathAbsoluto('laberinto/assets/VirusLaberinto1.txt')
FONDO_PATH = obtenerPathAbsoluto('laberinto/img/Fondo_Laberinto.png')
PISO_PATH = obtenerPathAbsoluto('laberinto/img/Piso_Laberinto.png')
VIRUS_PATH = obtenerPathAbsoluto('laberinto/img/Virus.png')
META_PATH = obtenerPathAbsoluto('laberinto/img/Meta.png')
PERSONAJE_PATH = obtenerPathAbsoluto('laberinto/img/niña.png')
MENSAJES_PATH = obtenerPathAbsoluto('laberinto/assets/direccionesMensajesLaberinto.txt')


class Laberinto(Juego):
    def __init__(self):
        self.dimensiones = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)
        self.titulo = 'Laberinto'
        self.ventana = None
        self.imagen = pygame.image.load(FONDO_PATH)
        self.reloj = pygame.time.Clock()
        self.tablero = None
        self.solapamiento = None
    
    def iniciarJuego(self):
        self.ventana = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)
        bandera=True
        while bandera:
            self.clock.tick(30)
            self.ventana.blit(self.imagen, (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
                    pygame.quit()

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass