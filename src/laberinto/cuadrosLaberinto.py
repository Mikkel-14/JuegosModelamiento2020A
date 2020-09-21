import pygame
import laberinto.settingsLaberinto as s
from pygame.locals import *
from abc import ABC, abstractmethod
from .posicionLaberinto import *
from .listenerLaberinto import *
from .observadorLaberinto import *
from .herramientas import *

class CuadroLaberinto(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class FondoLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = s.columnas * s.dim_Cuadro
        alto = s.filas * s.dim_Cuadro
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), (x, y))

    def mover(self):
        pass


class PersonajeLaberinto(CuadroLaberinto, ObservadorLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.numeroVidas = s.maximo_de_vidas

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self, dr, sl):
        keys = ListenerLaberinto.detectar()
        (x, y) = (self.posicion.x, self.posicion.y)
        if keys[pygame.K_UP] and sl.verificar(self, (x, y - dr)):
            self.posicion.actualizarY(y - dr)
            pygame.time.delay(150)
        if keys[pygame.K_DOWN] and sl.verificar(self, (x, y + dr)):
            self.posicion.actualizarY(y + dr)
            pygame.time.delay(150)
        if keys[pygame.K_LEFT] and sl.verificar(self, (x - dr, y)):
            self.posicion.actualizarX(x - dr)
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and sl.verificar(self, (x + dr, y)):
            self.posicion.actualizarX(x + dr)
            pygame.time.delay(150)

    def actualizar(self, virus, enemigo, meta, perdida, corazon):
        if virus or enemigo:
            self.numeroVidas -= 1


class EnemigoLaberinto(CuadroLaberinto, ObservadorLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self, dr, sl):
        keys = ListenerLaberinto.detectar()
        (x, y) = (self.posicion.x, self.posicion.y)
        if keys[pygame.K_w] and sl.verificar(self, (x, y - dr)):
            self.posicion.actualizarY(y - dr)
            pygame.time.delay(150)
        if keys[pygame.K_s] and sl.verificar(self, (x, y + dr)):
            self.posicion.actualizarY(y + dr)
            pygame.time.delay(150)
        if keys[pygame.K_a] and sl.verificar(self, (x - dr, y)):
            self.posicion.actualizarX(x - dr)
            pygame.time.delay(150)
        if keys[pygame.K_d] and sl.verificar(self, (x + dr, y)):
            self.posicion.actualizarX(x + dr)
            pygame.time.delay(150)

    def actualizar(self, virus, enemigo, meta, perdida, corazon):
        if enemigo:
            self.posicion.actualizarX(s.posInicial_Enemigo[0])
            self.posicion.actualizarY(s.posInicial_Enemigo[1])


class CaminoLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass


class VirusLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass


class MetaLaberinto(CuadroLaberinto):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass

class MensajeLaberinto(CuadroLaberinto, ObservadorLaberinto):
    def __init__(self, imagen, nombre):
        super().__init__(PosicionLaberinto(0, 0))
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def permitirDibujo(self, bool):
        self.aparecer = bool

    def getNombre(self):
        return self.nombre

    def getAparecer(self):
        return self.aparecer

    def dibujar(self, ventana):
        if self.aparecer:
            (x, y) = (self.posicion.x, self.posicion.y)
            ventana.blit(pygame.transform.scale(self.imagen, (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)), (x, y))

    def mover(self):
        pass

    def actualizar(self, virus, enemigo, meta, perdida, corazon):
        if perdida and self.nombre == 'perdida':
            self.aparecer = True
        elif virus and not perdida:
            if self.nombre == 'virus' + str(corazon - 1):
                self.aparecer = True
        elif enemigo and self.nombre == 'enemigo' and not perdida:
            self.aparecer = True
        elif meta and self.nombre == 'victoria':
            self.aparecer = True

class TableroLaberinto(CuadroLaberinto):
    def __init__(self):
        super().__init__(PosicionLaberinto(0, 0))
        self.listaCuadros = list()

    def agregarCuadros(self, cuadro):
        self.listaCuadros.append(cuadro)

    def dibujar(self):
        pass

    def mover(self):
        pass


class VidaLaberinto(CuadroLaberinto, ObservadorLaberinto):
    def __init__(self, imagen1, imagen2, posicion, numCorazon):
        super().__init__(posicion)
        self.imagenes = [pygame.image.load(imagen1), pygame.image.load(imagen2)]
        self.numCorazon = numCorazon
        self.lleno = 1

    def dibujar(self, ventana):
        (x, y) = (self.posicion.x, self.posicion.y)
        ventana.blit(pygame.transform.scale(self.imagenes[self.lleno], (s.dim_Cuadro, s.dim_Cuadro)), (x, y))

    def mover(self):
        pass

    def actualizar(self, virus, enemigo, meta, perdida, corazon):
        if virus or enemigo:
            if self.numCorazon == corazon and self.lleno:
                self.lleno = 0
