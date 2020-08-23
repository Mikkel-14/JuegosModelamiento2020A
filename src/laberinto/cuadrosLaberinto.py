import pygame
from pygame.locals import *
from abc import ABC, abstractmethod
from laberinto.posicionLaberinto import *
from laberinto.listenerLaberinto import *

class CuadroLaberinto(ABC):
    def _init_(self, posicion):
        self.posicion = posicion
        super()._init_()

    @property
    def posicion(self):
        return self.__posicion

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class FondoLaberinto(CuadroLaberinto):
    def _init_(self, imagen, posicion):
        self.CuadroLaberinto_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = 21 * 34
        alto = 14 * 34
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), self.posicion.getPosicion())

    def mover(self):
        pass


class PersonajeLaberinto(CuadroLaberinto):
    def _init_(self, imagen, posicion):
        self.CuadroLaberinto_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (34, 34)), self.posicion.getPosicion())

    def mover(self, dr, sl):
        keys = ListenerLaberinto.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_UP] and sl.verificar((x, y - dr)):
            self.posicion.y -= dr
            pygame.time.delay(150)
        if keys[pygame.K_DOWN] and sl.verificar((x, y + dr)):
            self.posicion.y += dr
            pygame.time.delay(150)
        if keys[pygame.K_LEFT] and sl.verificar((x - dr, y)):
            self.posicion.x -= dr
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and sl.verificar((x + dr, y)):
            self.posicion.x += dr
            pygame.time.delay(150)


class CaminoLaberinto(CuadroLaberinto):
    def _init_(self, imagen, posicion):
        self.CuadroLaberinto_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (34, 34)), self.posicion.getPosicion())

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()


class VirusLaberinto(CuadroLaberinto):
    def _init_(self, imagen, posicion):
        self.CuadroLaberinto_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (34, 34)), self.posicion.getPosicion())

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()


class MetaLaberinto(CuadroLaberinto):
    def _init_(self, imagen, posicion):
        self.CuadroLaberinto_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (34, 34)), self.posicion.getPosicion())

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()