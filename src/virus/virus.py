import pygame
import os
import sys
from .cuadro import *
from .solapamiento import *
from .posicion import *
from .listener import *
from .puntuacion import *
from .herramientas import *

# NOTE: dado que las dimensiones de este juego son 600 x 550, se consideraran 24 columnas y 22 filas
# NOTE: las dimensiones de cada imagen que interactuara con el juego son de 25px por 25px

class EvitandoVirus():

    def __init__(self):
        pygame.init()
        self.dimensiones = (600,550)
        self.titulo = 'Esquivando Virus'
        self.ventana = None
        self.clock = pygame.time.Clock()
        self.mapa = None
        self.bandera = True

    def iniciarJuego(self):
        pygame.init()
        self.bandera = True
        INSTRUCCIONES = True
        FONTO_PATH = obtenerPathAbsoluto('img/Fondo.png')
        OBJETIVO_PATH = obtenerPathAbsoluto('img/cuadroObjetivo.png')
        WEB_PATH = obtenerPathAbsoluto('img/cuadroPagWeb.png')
        INST_PATH = obtenerPathAbsoluto('img/inicioVirus.png')
        PARED_PATH = obtenerPathAbsoluto('img/Pared.png')
        CAMINO_PATH = obtenerPathAbsoluto('assets/matrizCamino.dat')
        PAREDES = obtenerPathAbsoluto('assets/matrizPared.dat')
        PERSONAJE_PATH = obtenerPathAbsoluto('img/personaje.png')
        HACKER_PATH = obtenerPathAbsoluto('img/hacker.png')
        VIRUS_PATH = obtenerPathAbsoluto('img/cuadroVirus.png')
        MENSAJES_PATH = obtenerPathAbsoluto('assets/mensajes.dat')
        MK_PATH= obtenerPathAbsoluto('assets/s.ttf')
        self.ventana = pygame.display.set_mode(self.dimensiones)
        self.mapa = Mapa(FONTO_PATH)
        pygame.display.set_caption(self.titulo)
        puntos = Puntuacion()
        self.puntaje = puntos
        with open(PAREDES) as p:
            for line in p:
                info = line.strip().split(',')
                x = int(info[0])*25
                y = int(info[1])*25
                pared = CuadroPared(PARED_PATH, Posicion(x, y))
                self.mapa.agregarCuadros(pared)
        with open(CAMINO_PATH) as c:
            for line in c:
                info = line.strip().split(',')
                x = int(info[0])*25
                y = int(info[1])*25
                paginaWeb = CuadroPaginaWeb(WEB_PATH, VIRUS_PATH, Posicion(x,y))
                self.mapa.agregarCuadros(paginaWeb)
        objetivo = CuadroObjetivo(OBJETIVO_PATH, Posicion(18*25,15*25))
        self.mapa.agregarCuadros(objetivo)
        solapamiento = SolapamientoJugador(self.mapa, self)
        solHacker = SolapamientoHacker(self.mapa, self)
        keyMapBueno = (pygame.K_UP,pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        keyMapMalo = (pygame.K_w,pygame.K_s, pygame.K_a, pygame.K_d)
        escuchador = Listener(keyMapBueno)
        escuchadorHacker = Listener(keyMapMalo)
        personaje = CuadroPersonaje(PERSONAJE_PATH, Posicion(18*25,5*25), solapamiento, escuchador, 'bueno')
        hacker = CuadroPersonaje(HACKER_PATH, Posicion(19*25,15*25),solHacker,escuchadorHacker, 'malo')
        mk = CuadroMarcador(Posicion(5,5),puntos,MK_PATH)
        self.mapa.agregarCuadros(mk)
        self.mapa.agregarCuadros(personaje)
        self.mapa.agregarCuadros(hacker)
        with open(MENSAJES_PATH) as m:
            for line in m:
                datos = line.strip().split(',')
                path = obtenerPathAbsoluto(datos[0])
                mensaje = Mensaje(path, datos[1], Posicion(0,0))
                self.mapa.agregarCuadros(mensaje)

        self.mapa.dibujar(self.ventana)
        for cuadros in self.mapa.listaCuadros:
            cuadros.dibujar(self.ventana)

        while self.bandera:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bandera=False
                    pygame.quit()
                    break

            for m in self.mapa.listaCuadros:
                if isinstance(m, Mensaje):
                    if m.getNombre() == 'instrucciones' and INSTRUCCIONES:
                        m.autorizarDibujo(True)
                        INSTRUCCIONES = False
                    if m.getAparecer():
                        msj = m

            try:
                msj.esperar(self)
            except Exception:
                break

            if not msj.getAparecer():
                try:
                    personaje.mover(25)
                    hacker.mover(25)
                except Exception:
                    break
            self.mapa.dibujar(self.ventana)
            for cuadros in self.mapa.listaCuadros:
                cuadros.dibujar(self.ventana)
            pygame.display.update()

    def reiniciarJuego(self):
        self.iniciarJuego()

    def salirJuego(self):
        self.bandera = False
        pygame.quit()

    def getPuntos(self):
        return self.puntaje.obtenerPuntos()

    def verificarCondiciones(self, tipoCuadroSolapado):
        """
        En base al tipo de cuadro solapado, determina si se gano o se perdio el juego
        """
        if tipoCuadroSolapado == 'objetivo':
            for mensaje in self.mapa.listaCuadros:
                if isinstance(mensaje, Mensaje):
                    if mensaje.getNombre() == 'victoria':
                        mensaje.autorizarDibujo(True)
                        self.puntaje.calcularPuntaje()
        elif tipoCuadroSolapado == 'virus':
            for mensaje in self.mapa.listaCuadros:
                if isinstance(mensaje, Mensaje):
                    if mensaje.getNombre() == 'fallo':
                        mensaje.autorizarDibujo(True)
        elif tipoCuadroSolapado == 'personaje':
            for mensaje in self.mapa.listaCuadros:
                if isinstance(mensaje, Mensaje):
                    if mensaje.getNombre() == 'atrapado':
                        mensaje.autorizarDibujo(True)
        else:
            self.puntaje.calcularPuntaje()


    def update(self, tipoCuadroSolapado):
        self.verificarCondiciones(tipoCuadroSolapado)

