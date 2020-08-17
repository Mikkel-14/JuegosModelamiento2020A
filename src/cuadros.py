import pygame
from abc import ABC, abstractmethod

pygame.init()

class Cuadro(ABC):
	def __init__(self, posicion):
	    self.posicion = posicion
	    super().__init__()

	@abstractmethod
	def mover(self):
		pass

	@property
    def posicion(self):
        return self.__posicion

	@abstractmethod
	def dibujar(self):
		pass

class Fondo(Cuadro):
	    def __init__(self, imagen, posicion):
	        self._Cuadro__posicion = posicion
	        self.imagen = pygame.image.load(imagen)
			