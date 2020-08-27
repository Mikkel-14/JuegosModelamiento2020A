import pygame
import laberinto.settingsLaberinto as s
from laberinto.cuadrosLaberinto import *
from laberinto.solapamientoLaberinto import *
from herramientas import *
from puntaje import *
pygame.init()

CAMINOLAB_PATH = obtenerPathAbsoluto('laberinto/assets/CaminoLaberinto1.txt')
POSICION_VIRUS_PATH = obtenerPathAbsoluto('laberinto/assets/VirusLaberinto1.txt')
FONDO_PATH = obtenerPathAbsoluto('laberinto/img/Fondo_Laberinto.png')
PISO_PATH = obtenerPathAbsoluto('laberinto/img/Piso_Laberinto.png')
VIRUS_PATH = obtenerPathAbsoluto('laberinto/img/Virus.png')
META_PATH = obtenerPathAbsoluto('laberinto/img/Meta.png')
PERSONAJE_PATH = obtenerPathAbsoluto('laberinto/img/niña.png')
MENSAJES_PATH = obtenerPathAbsoluto('laberinto/assets/direccionesMensajesLaberinto.txt')
CORAZON_PATH = obtenerPathAbsoluto('laberinto/img/vida1.png')
CORAZON_VACIO_PATH = obtenerPathAbsoluto('laberinto/img/vida0.png')
 

class VentanaLaberinto:
    def __init__(self):
        self.dimensiones = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)
        self.titulo = "Laberinto"
        self.reloj = pygame.time.Clock()
        self.tablero = None
        self.solapamiento = None
        self.win = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)