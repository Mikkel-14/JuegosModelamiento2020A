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

class MensajeLaberinto(CuadroLaberinto):
    def __init__(self, imagen, nombre):
        self._CuadroLaberinto__posicion = PosicionLaberinto(0, 0)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def permitirDibujo(self, bool):
        self.aparecer = bool

    def getNombre(self):
        return self.nombre

    def getAparecer(self):
        return self.aparecer

    def esperar(self):
        if self.aparecer:
            keys = ListenerLaberinto.detectar()
            if keys[pygame.K_SPACE]:
                self.aparecer = False

    def dibujar(self, ventana):
        if self.aparecer:
            ventana.blit(pygame.transform.scale(self.imagen, (21 * 34, 14 * 34)), self.posicion.getPosicion())

    def mover(self):
        pass

class TableroLaberinto(CuadroLaberinto):
    def __init__(self):
        self._CuadroLaberinto__posicion = PosicionLaberinto(0,0)
        self.dictCuadros = dict()
        self.dictCuadros['camino'] = list()
        self.dictCuadros['virus'] = list()
        self.dictCuadros['personaje'] = None
        self.dictCuadros['fondo'] = None
        self.dictCuadros['meta'] = None
        self.dictCuadros['mensaje'] = list()

    def agregarCuadros(self, cuadro):
        if isinstance(cuadro, CaminoLaberinto):
             self.dictCuadros['camino'].append(cuadro)
        elif isinstance(cuadro, VirusLaberinto):
             self.dictCuadros['virus'].append(cuadro)
        elif isinstance(cuadro, PersonajeLaberinto):
             self.dictCuadros['personaje'] = cuadro
        elif isinstance(cuadro, MetaLaberinto):
             self.dictCuadros['meta'] = cuadro
        elif isinstance(cuadro, FondoLaberinto):
             self.dictCuadros['fondo'] = cuadro
        elif isinstance(cuadro, MensajeLaberinto):
            self.dictCuadros['mensaje'].append(cuadro)

    def accederLista(self):
        return self.dictCuadros

    def dibujar(self,ventana):
        self.dictCuadros['fondo'].dibujar(ventana)
        for camino in self.dictCuadros['camino']:
            camino.dibujar(ventana)
        for virus in self.dictCuadros['virus']:
            virus.dibujar(ventana)
        self.dictCuadros['meta'].dibujar(ventana)
        self.dictCuadros['personaje'].dibujar(ventana)
        for mensaje in self.dictCuadros['mensaje']:
            mensaje.dibujar(ventana)
        pygame.display.update()

    def mover(self, solapamiento):
        self.dictCuadros['fondo'].mover()
        for camino in self.dictCuadros['camino']:
            camino.mover()
        for virus in self.dictCuadros['virus']:
            virus.mover()
        self.dictCuadros['personaje'].mover(34, solapamiento)


class VidaLaberinto(CuadroLaberinto):
    def __init__(self, imagen1, imagen2, posicion):
        self._CuadroLaberinto__posicion = posicion
        self.imagenes = [pygame.image.load(imagen1), pygame.image.load(imagen2)]
        self.booleano = 1

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagenes[self.booleano], (s.dim_Cuadro, s.dim_Cuadro)), self.posicion.obtenerPosicion())

     def mover(self):
        pass
