import pygame
import os
import sys
sys.path.append('../juego.py')
from juego import *


class Laberinto(Juego):
    def __init__(self):
        self.dimensiones = (958,534)
        self.titulo = 'Laberinto'
        self.ventana = None
        self.imagen = pygame.image.load(os.path.join(os.path.dirname(__file__),'img/inicioLaberinto.png'))
        self.clock = pygame.time.Clock()