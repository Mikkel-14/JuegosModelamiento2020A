#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                       Clase Listener
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.listener import *

class Listener:
    @staticmethod
    def captarMouse():
        return pygame.mouse.get_pos() # devuelve la posición del cursor del mouse en una tupla (x, y)
