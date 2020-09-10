import pygame
from abc import *
import random
import ctypes
import pygame

NIVEL = 0
N = NIVEL + 2
DIM = int(420 / N)
DIMENSION = 500, 500  # Se define las dimensiones de la ventana del juego

class Listener:
    @staticmethod
    def detectar() -> tuple:
        return pygame.key.get_pressed() 

class Posicion:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def obtenerCoordenadas(self):
        return self.x, self.y

    def actualizarCoordenadas(self, x, y):
        self.x = x
        self.y = y
        
class Mensaje(object):

    def __init__(self):
        self.mensajeInstruccion = [mensajeInstrucciones,False]
        self.mensajeGanar = [mensajeGanar,False]
        self.mensajePerder=[mensajePerder,False]


    def dibujar(self,ventana):
        if self.mensajeInstruccion[1]:
            ventana.blit(self.mensajeInstruccion[0], (0,0))
        elif self.mensajeGanar[1]:
            ventana.blit(self.mensajeGanar[0], (0,0))
        elif self.mensajePerder[1]:
            ventana.blit(self.mensajePerder[0], (0,0))

    def cambiarEstado(self,estado):
        self.mensajeInstruccion[1]=estado[0]
        self.mensajeGanar[1]=estado[1]
        self.mensajePerder[1]=estado[2]


class Cuadro(ABC):
    def __init__(self, posicionRef, posicionAct):
        self.posicionReferencial = posicionRef
        self.posicionActual=posicionAct
        super().__init__()

    @property
    def posicionReferencial(self):
        return self.__posicionReferencial

    @property
    def posicionActual(self):
        return self.__posicionActual

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class CuadroVacio(Cuadro):

    def __init__(self, posicionR, imagen):
        self._Cuadro__posicionReferencial = posicionR
        self._Cuadro__posicionActual = None
        self.imagen = pygame.image.load(imagen)

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicionActual.getX(), self.posicionActual.getY()))

    def iniciarMovimiento(self, colision):
        keys = Listener.detectar()
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()

        if keys[pygame.K_LEFT]:
            colision.verificarColision((x + DIM, y))
        if keys[pygame.K_RIGHT]:
            colision.verificarColision((x - DIM, y))
        if keys[pygame.K_UP]:
            colision.verificarColision((x, y + DIM))
        if keys[pygame.K_DOWN]:
            colision.verificarColision((x, y - DIM))

    def mover(self, pos):
        self.posicionActual.setX(pos[0])
        self.posicionActual.setY(pos[1])

    def getPosicionActual(self):
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()
        return x, y

    def getPosicionRef(self):
        x = self.posicionReferencial.getX()
        y = self.posicionReferencial.getY()
        return x, y

    def setPosicionActual(self, posicion):
        self._Cuadro__posicionActual = Posicion(posicion[0], posicion[1])


class FragmentoImagen(Cuadro):

    def __init__(self, posicionR, imagen):
        self._Cuadro__posicionReferencial = posicionR
        self._Cuadro__posicionActual = None
        self.imagen = imagen
        self.estaOculto = False

    def dibujar(self, fondo):
        dimension = (DIM, DIM)
        fondo.blit(pygame.transform.scale(self.imagen, dimension),
                   (self.posicionActual.getX(), self.posicionActual.getY()))

    def mover(self, pos):
        self.posicionActual.setX(pos[0])
        self.posicionActual.setY(pos[1])

    def getPosicionActual(self):
        x = self.posicionActual.getX()
        y = self.posicionActual.getY()
        return x, y

    def getPosicionRef(self):
        x = self.posicionReferencial.getX()
        y = self.posicionReferencial.getY()
        return x, y

    def setPosicionActual(self, posicion):
        self._Cuadro__posicionActual = Posicion(posicion[0], posicion[1])

    def ocultar(self):
        self.estaOculto = True
        self.imagen = pygame.image.load(os.path.join(os.path.dirname(__file__), "CuadroVacio.png"))

    def verificarOcultamiento(self):
        return self.estaOculto


class Imagen(Cuadro):
    def __init__(self,contador,verificacion):
        self._Cuadro__posicion = None
        self.imagen = None
        self.dimension = DIM
        self.lista_cuadros = list()
        self.verificacion=verificacion
        self.contador=contador

    def mover(self, colision):
        self.lista_cuadros[-1].iniciarMovimiento(colision)

    def dibujar(self, posicion, imagen, pantalla):
        self.imagen = pygame.image.load(imagen)
        self._Cuadro__posicion = posicion

    def descomponer(self):
        listarand = list()
        for item in self.lista_cuadros:
            listarand.append(item.getPosicionRef())
        random.shuffle(listarand)
        i = int(0)
        for item in self.lista_cuadros:
            item.setPosicionActual(listarand[i])
            i += 1

    def actualizarImagen(self, ventana):
        for i in range(len(self.lista_cuadros)):
            self.lista_cuadros[i].dibujar(ventana)
        ventana.blit(self.imagen, (500, 40))

    def agregarCuadro(self, fragmentoimagen):
        self.lista_cuadros.append(fragmentoimagen)

    def intercambiar(self, posicion):
        listapos = list()
        for elemento in self.lista_cuadros:
            listapos.append((elemento.getPosicionActual(),elemento.getPosicionRef()))
            if (elemento.getPosicionActual() == posicion):
                elemento.mover(self.lista_cuadros[-1].getPosicionActual())
                fragmento = elemento
                self.contador.aumentar()
                self.contador.verificar(fragmento)
        self.lista_cuadros[-1].mover(posicion)
        self.verificacion.verificarCondiciones(self.lista_cuadros)


class Contador:
    def __init__(self, verificacion):
        self.numeroMovimientos = int(0)
        self.verificacion = verificacion

    def aumentar(self):
        self.numeroMovimientos += 1
        self.verificacion.verificarCondiciones(self.numeroMovimientos)


class Colision:
    def __init__(self, contador, imagen):
        self.imagen = imagen
        self.contador = contador

    def verificarColision(self, posicion):

        for pos in self.imagen.getLista():
            if pos.getPosicionActual() == posicion:
                self.imagen.intercambiar(posicion)
                self.contador.aumentar()


class Verificacion:
    def __init__(self, imagen, puntaje):
        self.imagen = imagen
        self.puntaje = puntaje

    def verificarCondiciones(self, numeroMovimientos):
        cont = 0

        for elemento in self.imagen.getLista():
            if ((elemento.posicionReferencial.getX(), elemento.posicionReferencial.getY())
                    == (elemento.posicionActual.getX(),elemento.posicionActual.getY())):
                cont += 1
        if cont == len(self.imagen.getLista()):
            self.puntaje.calcularPuntaje(numeroMovimientos)


class Puntaje:

    def __init__(self,puzzle, contador):
        self.contador = contador
        self.puzzle=puzzle
        self.puntajeFinal = 0

    def calcularPuntaje(self,estado):
        if estado:
            self.puntajeFinal = int(1000 / self.contador.numeroMovimientos)

        else:
            self.puntajeFinal = -1

#ponle tipo juego en el constructor
class Puzzle():

    def iniciarJuego(self):
        pygame.init()
        clock = pygame.time.Clock()
        imagen=Imagen()
        imagen.dibujar(Posicion(0, 0), "puzzle\ImagenMonitor.png",)
        imagen.descomponer()
        puzzle = Puzzle()
        puntaje = Puntaje(puzzle)
        verificacion = Verificacion(imagen, puntaje)
        contador = Contador(verificacion)
        colision = Colision(contador, imagen)

        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        titulo_juego = pygame.display.set_caption('I <3 PUZZLE')  # Se inserta un titulo a la ventana creada

        iniciado = True
        while iniciado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    iniciado=False
                pantalla_juego.blit(pygame.transform.scale(pygame.image.load("puzzle\img\inicioPuzzle.png"),(500,300)),(0,0))
                pygame.display.update()
        iniciado = True
        while iniciado:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    iniciado = False
                if puntaje.puntajeFinal != 0:
                    ctypes.windll.user32.MessageBoxW(0, "TU PUNTAJE OBTENIDO FUE:" + str(puntaje.puntajeFinal)
                                                     , "FELICIDADES GANASTE!!", 1)
                    pygame.quit()
                    puzzle.finalizarJuego()
                    iniciado = False
                pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                imagen.mover(colision)
                imagen.actualizarImagen(pantalla_juego)
                pygame.display.update()

    def finalizarJuego(self):
        pass
    def reiniciarJuego(self):
        pass
