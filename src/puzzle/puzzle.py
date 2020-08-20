import pygame
import os
import sys
sys.path.append('../juego.py')
from juego import *


class Puzzle(Juego):
    def __init__(self):
        self.dimensiones = (960,540)
        self.titulo = 'Puzzle'
        self.ventana = None
        self.imagen = pygame.image.load(os.path.join(os.path.dirname(__file__),'img/inicioPuzzle.png'))
        self.clock = pygame.time.Clock()

    def iniciarJuego(self):
        self.ventana = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)
        bandera=True
        while bandera:
            self.clock.tick(30)
            self.ventana.blit(pygame.transform.scale(self.imagen,(960,540)), (0,0))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
                    pygame.quit()
    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
