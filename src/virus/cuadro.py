from abc import ABC, abstractmethod
import pygame
from .listener import *
from .posicion import *
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

class CuadroPared(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

class CuadroPaginaWeb(Cuadro):
    def __init__(self, imagen, imagenMala, posicion):
        super().__init__(posicion)
        self.imagenBuena = pygame.image.load(imagen)
        self.imagenMala = pygame.image.load(imagenMala)
        self.esMalo = False

    def dibujar(self, ventana):
        if not self.esMalo:
            ventana.blit(self.imagenBuena, self.posicion.getCoordenadas())
        else:
            ventana.blit(self.imagenMala, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def transformar(self):
        self.esMalo = not self.esMalo

    def getCoordenadasyEsMalo(self):
        return (self.posicion.getCoordenadas(), self.esMalo)



class CuadroObjetivo(Cuadro):
    def __init__(self, imagen, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def getCoordenadas(self):
        return self.posicion.getCoordenadas()

class CuadroPersonaje(Cuadro):
    def __init__(self, imagen, posicion, solapamiento, escuchador, tipo):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.solapamiento = solapamiento
        self.listener = escuchador
        self.tipo = tipo
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self, dr):
        #NOTE: el keymap debe ser ARRIBA, ABAJO, IZQ, DER
        tupla = self.listener.detectar()
        x, y = self.posicion.getCoordenadas()
        if tupla[0] and self.solapamiento.verificarSolapamiento((x,y),(x, y - dr)):
            self.posicion.y -= dr
            pygame.time.delay(150)
        if tupla[1] and self.solapamiento.verificarSolapamiento((x,y),(x, y + dr)):
            self.posicion.y += dr
            pygame.time.delay(150)
        if tupla[2] and self.solapamiento.verificarSolapamiento((x,y),(x - dr, y)):
            self.posicion.x -= dr
            pygame.time.delay(150)
        if tupla[3] and self.solapamiento.verificarSolapamiento((x,y),(x + dr, y)):
            self.posicion.x += dr
            pygame.time.delay(150)

    def getCoordenadasyTipo(self):
        return (self.posicion.getCoordenadas(),self.tipo)

class Mensaje(Cuadro):
    def __init__(self, imagen, nombre, posicion):
        super().__init__(posicion)
        self.imagen = pygame.image.load(imagen)
        self.nombre = nombre
        self.aparecer = False

    def dibujar(self, ventana):
        if self.aparecer:
            ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def esperar(self, juego):
        listener = Listener((pygame.K_SPACE, pygame.K_RETURN, pygame.K_ESCAPE))
        if self.aparecer:
            keys = listener.detectar()
            if keys[0] and self.nombre == 'instrucciones':
                self.aparecer = False
            elif keys[1] and self.nombre == 'fallo':
                self.aparecer = False
                juego.reiniciarJuego()
            elif keys[1] and self.nombre == 'atrapado':
                self.aparecer = False
                juego.reiniciarJuego()
            elif keys[1] and self.nombre == 'victoria':
                self.aparecer = False
                juego.reiniciarJuego()
            elif keys[2] and self.nombre == 'victoria':
                self.aparecer = False
                juego.salirJuego()

    def autorizarDibujo(self, booleano):
        self.aparecer = booleano

    def getAparecer(self):
        return self.aparecer

    def getNombre(self):
        return self.nombre

class Mapa(Cuadro):

    def __init__(self, imagen):
        super().__init__(Posicion(0,0))
        self.imagen = pygame.image.load(imagen)
        self.listaCuadros = list()

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.getCoordenadas())

    def mover(self):
        pass

    def agregarCuadros(self, cuadro):
        self.listaCuadros.append(cuadro)

class CuadroMarcador(Cuadro):
    def __init__(self, posicion, puntaje, fuente):
        pygame.init()
        super().__init__(posicion)
        self.puntaje = puntaje
        self.fuente = pygame.font.Font(fuente, 25)

    def dibujar(self, win):
        srf = self.fuente.render('Puntuacion: {:}'.format(self.puntaje.obtenerPuntos()), True, (0,0,0))
        win.blit(srf, self.posicion.getCoordenadas())

    def mover(self):
        pass
