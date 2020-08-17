import pygame
from abc import ABC, abstractmethod

pygame.init()

class Cuadro(ABC):
	def __init__(self, posicion):
	    self.posicion = posicion
	    super().__init__()

	@property
    def posicion(self):
        return self.__posicion

	@abstractmethod
	def dibujar(self):
		pass
