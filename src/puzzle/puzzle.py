import pygame
from abc import *
import random
import ctypes
import pygame

import os
import sys

import os.path
from .herramientas import *

mensajeInstrucciones= pygame.image.load(os.path.join(os.path.dirname(__file__), "Inicio_Puzzle.png"))
mensajeInstrucciones = pygame.transform.scale(mensajeInstrucciones, (1000, 500))
mensajeGanar= pygame.image.load(os.path.join(os.path.dirname(__file__), "Ganar.png"))
mensajeGanar = pygame.transform.scale(mensajeGanar, (1000, 500))
mensajePerder= pygame.image.load(os.path.join(os.path.dirname(__file__), "Perder.png"))
mensajePerder = pygame.transform.scale(mensajePerder, (1000, 500))



NIVEL = 1
N = NIVEL + 2
DIM = int(420 / N)
DIMENSION = 1000, 500  # Se define las dimensiones de la ventana del juego


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
        self.posicionActual = posicionAct
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
        self.imagen = pygame.image.load(os.path.join(os.path.dirname(__file__), "CuadroVacio2.png"))

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
    def __init__(self):
        self.numeroMovimientos = int(0)

    def aumentar(self):
        self.numeroMovimientos += 1
        

    def verificar(self, fragmento):
        if (self.numeroMovimientos % 10 == 0) & (self.numeroMovimientos >= 1) & isinstance(fragmento,FragmentoImagen):
            fragmento.ocultar()


class Colision:
    def __init__(self, imagen):
        self.imagen = imagen

    def verificarColision(self, posicion):
        for pos in self.imagen.lista_cuadros:
            if pos.getPosicionActual() == posicion:
                self.imagen.intercambiar(posicion)
                break


class Verificacion:
    def __init__(self, puntaje):
        self.puntaje = puntaje

    def verificarCondiciones(self, listafragmentos):
        contG = 0
        contP=0
        for elemento in listafragmentos:
            if isinstance(elemento,FragmentoImagen):
                if elemento.verificarOcultamiento():
                    contP += 1
        if contP == len(listafragmentos)-1:
            self.puntaje.calcularPuntaje(False)


        for elemento in listafragmentos:
            if (elemento.getPosicionActual()==elemento.getPosicionRef()):
                contG += 1

        if contG == len(listafragmentos):
            self.puntaje.calcularPuntaje(True)


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




class Puzzle:

    def __init__(self):
        pygame.init()
        self.dimensiones = (500,500)
        self.titulo = 'I <3 PUZZLE'
        self.clock = pygame.time.Clock()
        self.fondo = None
        # Instancia de Contador


    def iniciarJuego(self):
        CUADROVACIO_PATH = 'puzzle/CuadroVacio.png'
        TROYANO_PATH = 'puzzle/Troyano.png'

        titulo_juego = pygame.display.set_caption(self.titulo)
        self.contador = Contador()
        # Instancia de Puntaje
        self.puntaje = Puntaje(self, self.contador)

        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
        
        mensaje=Mensaje()
        mensaje.cambiarEstado((True,False,False))
        mensaje.dibujar(pantalla_juego)
        pygame.display.update()



        # instancia de la imagen
        imagen = Imagen(self.contador, Verificacion(self.puntaje))
        # Instancia de Verificacion
        # Instancia de Colision
        colision = Colision(imagen)
        imagen.dibujar(Posicion(0, 0), TROYANO_PATH, pantalla_juego)
        # Instancias de los fragmentos
        listapos = list()
        listaimg = list()
        listaFragmentos = list()
        for i in range(N):
            for j in range(N):
                posx = int(40 + j * DIM)
                posy = int(40 + i * DIM)
                listapos.append((posx, posy))  # Se guardan las posiciones correctas de los fragmento
                imaux = pygame.Surface((DIM, DIM))  # Se crea una superficie
                imaux.blit(pygame.image.load(TROYANO_PATH), (0, 0), (posx - 40, posy - 40, DIM, DIM))
                listaimg.append(imaux)

        #Se agrega las listas de imagenes y las posiciones de referencia a la lista de Fragmentos
        for i in range(len(listapos)):
             listaFragmentos.append(FragmentoImagen(
                    Posicion(listapos[i][0], listapos[i][1]),
                    listaimg[i]))

        # Instancia del cuadro Vacio
        cuadro_vacio = CuadroVacio(Posicion(listapos[-1][0], listapos[-1][1]), CUADROVACIO_PATH)

        for i in range(len(listaFragmentos) - 1):
            imagen.agregarCuadro(listaFragmentos[i])

        imagen.agregarCuadro(cuadro_vacio)
        imagen.descomponer()
        clock = pygame.time.Clock()

        pantalla_juego = pygame.display.set_mode(DIMENSION)  # Se crea la ventana con las dimensiones especificas
 
        self.fondo = pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
        pygame.display.set_caption(self.titulo)

        iniciado = True
        bandera=False
        while iniciado:
            
            try:
                self.clock.tick(30)
                for event in pygame.event.get():
                    if bandera:
                        pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                        imagen.mover(colision)
                        imagen.actualizarImagen(pantalla_juego)
                        pygame.display.update()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                            pantalla_juego.fill((255, 255, 255))  # Dar un color blanco a la pantalla
                            imagen.mover(colision)
                            imagen.actualizarImagen(pantalla_juego)
                            pygame.display.update()
                            bandera=True
                        if event.key == pygame.K_r:
                            self.reiniciarJuego()
                        if event.key == pygame.K_e:
                            self.salirJuego(self.puntaje.puntajeFinal)
                            break
                    if event.type == pygame.QUIT:
                        self.salirJuego(self.puntaje.puntajeFinal)
                        break




                    if self.puntaje.puntajeFinal > 0:
                        mensaje.cambiarEstado((False,True,False))
                        mensaje.dibujar(pantalla_juego)
                        pygame.display.update()
                        bandera=False
                    

                    elif self.puntaje.puntajeFinal == -1:
                        mensaje.cambiarEstado((False,False,True))
                        mensaje.dibujar(pantalla_juego)
                        pygame.display.update()
                        bandera=False

                        
                      

            except Exception:
                break

    def getPuntos(self):
        if self.puntaje.puntajeFinal==-1:
            puntos=0
        else:
            puntos = self.puntaje.puntajeFinal
            self.puntaje.puntajeFinal=0
        return puntos



    def reiniciarJuego(self):
        pygame.quit()
        self.iniciarJuego()


    def salirJuego(self,puntaje):
        pygame.quit()