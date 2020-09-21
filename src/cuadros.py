import pygame
import os
import settings as s
from abc import ABC, abstractmethod
from posicion import Posicion
from listener import *
from fachadaJuegos import *
from ventanaPuntuacion import *
pygame.init()


class Cuadro(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Fondo(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ancho = s.columnas * s.dim_Cuadro
        alto = s.filas * s.dim_Cuadro
        ventana.blit(pygame.transform.scale(self.imagen, (ancho, alto)), self.posicion.getPosicion())

    def mover(self):
        pass


class Personaje(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), self.posicion.getPosicion())

    def mover(self, dr, sl):
        keys = Listener.detectar()
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


class MapaMuseo(Cuadro):
    def __init__(self):
        super().__init__(Posicion(0,0))
        self.listaCuadros = []

    def agregarCuadros(self, cuadro):
        self.listaCuadros.append(cuadro)

    def dibujar(self):
        pass

    def mover(self):
        pass


class Estacion(Cuadro):
    def __init__(self, imagen, posicion, nombreEstacion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombreEstacion

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()


class Camino(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(pygame.transform.scale(self.imagen, (s.dim_Cuadro, s.dim_Cuadro)), self.posicion.getPosicion())

    def mover(self):
        pass

    def obtenerPosicion(self):
        return self.posicion.getPosicion()

class Mensaje(Cuadro):
    def __init__(self, imagen, nombre, facade, usuario):
        super().__init__(Posicion(175,120))
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False
        self.fachadaJuegos = facade
        self.winPuntuaciones = VentanaPuntuaciones(usuario)

    def dibujar(self, ventana):
        if self.aparecer:
            ventana.blit(self.imagen, self.posicion.getPosicion())

    def permitirDibujo(self, booleano):
        self.aparecer = booleano

    def getAparecer(self):
        return self.aparecer

    def getNombre(self):
        return self.nombre

    def mover(self):
        pass

    def esperar(self):
        if self.aparecer:
            keys = Listener.detectar()
            juego = None
            if keys[pygame.K_RETURN] and self.nombre != 'inicio' and self.nombre != 'tableroPuntaje':
                self.aparecer = False
                pygame.quit()
                self.fachadaJuegos.arrancarJuego(self.nombre)
            elif keys[pygame.K_RETURN] and self.nombre == 'tableroPuntaje':
                self.aparecer = False
                pygame.quit()
                self.winPuntuaciones.mostrarPuntuaciones()
            elif keys[pygame.K_ESCAPE]:
                self.aparecer = False

class Marcador(Cuadro):

    def __init__(self, imagen, posicion, puntos, facade):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.imagen = pygame.transform.scale(self.imagen, (190,39) )
        self.fachada = facade
        self.puntaje = self.fachada.getPuntaje()

    def actualizarMarcador(self):
        self.puntaje = self.fachada.getPuntaje()
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getPosicion())
        fuente = pygame.font.SysFont('Arial', 16)
        texto_puntaje = fuente.render(f'Puntos: {self.puntaje}', 0, (255, 255, 255))
        ventana.blit(texto_puntaje, (self.posicion.getPosicion()[0]+42, self.posicion.getPosicion()[1] + 10))

    def mover(self):
        pass

    def getPuntaje(self):
        return self.puntaje
