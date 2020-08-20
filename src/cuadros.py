import pygame
import os
import settings as s
from abc import ABC, abstractmethod
from posicion import *
from listener import *
from virus.virus import *
from laberinto.laberinto import *
from ruta.ruta import *
from snake.snake import *
from puzzle.puzzle import *

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

    @abstractmethod
    def mover(self):
        pass


class Fondo(Cuadro):
    def _init_(self, imagen, posicion):
        self.Cuadro_posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = s.columnas * s.dim_Cuadro
        alto = s.filas * s.dim_Cuadro
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), self.posicion.getPosicion())

    def mover(self):
        pass


class Personaje(Cuadro):
    def __init__(self, imagen, posicion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self, dr, sl):
        keys = Listener.detectar()
        x, y = self.posicion.getPosicion()
        if keys[pygame.K_UP] and sl.verificar((x, y-dr)):
            self.posicion.y -= dr
        if keys[pygame.K_DOWN] and sl.verificar((x, y+dr)):
            self.posicion.y += dr
        if keys[pygame.K_LEFT] and sl.verificar((x-dr, y)):
            self.posicion.x -= dr
        if keys[pygame.K_RIGHT] and sl.verificar((x+dr, y)):
            self.posicion.x += dr


class MapaMuseo(Cuadro):
    def __init__(self):
        self._Cuadro__posicion = Posicion(0, 0)
        self.dictCuadros = dict()
        self.dictCuadros['camino'] = list()
        #self.dictCuadros['estaciones'] = list()
        self.dictCuadros['personaje'] = None
        self.dictCuadros['fondo'] = None

    def agregarCuadros(self, cuadro):
        if isinstance(cuadro, Camino):
            self.dictCuadros['camino'].append(cuadro)
        # elif isinstance(cuadro, Estacion):
        #     self.dictCuadros['estaciones'].append(cuadro)
        elif isinstance(cuadro, Personaje):
            self.dictCuadros['personaje'] = cuadro
        elif isinstance(cuadro, Fondo):
            self.dictCuadros['fondo'] = cuadro

    def accederLista(self):
        return self.dictCuadros

    def dibujar(self, ventana):
        self.dictCuadros['fondo'].dibujar(ventana)
        for camino in self.dictCuadros['camino']:
            camino.dibujar(ventana)
        # for estacion in self.dictCuadros['estaciones']:
        #    estacion.dibujar(ventana)
        self.dictCuadros['personaje'].dibujar(ventana)
        pygame.display.update()

    def mover(self, solapamiento):
        self.dictCuadros['fondo'].mover()
        for camino in self.dictCuadros['camino']:
            camino.mover()
        # for estacion in self.dictCuadros['estaciones']:
        #    estacion.mover()
        self.dictCuadros['personaje'].mover(34, solapamiento)


class Camino(Cuadro):
    def __init__(self, imagen, posicion):
        self._Cuadro__posicion = posicion
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def mover(self):
        pass
