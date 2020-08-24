import pygame
import laberinto.settingsLaberinto as s
from juego import *
from laberinto.cuadrosLaberinto import *
from laberinto.solapamientoLaberinto import *
from herramientas import *
pygame.init()
import os
import sys
sys.path.append('../juego.py')


CAMINOLAB_PATH = obtenerPathAbsoluto('laberinto/assets/CaminoLaberinto1.txt')
POSICION_VIRUS_PATH = obtenerPathAbsoluto('laberinto/assets/VirusLaberinto1.txt')
FONDO_PATH = obtenerPathAbsoluto('laberinto/img/Fondo_Laberinto.png')
PISO_PATH = obtenerPathAbsoluto('laberinto/img/Piso_Laberinto.png')
VIRUS_PATH = obtenerPathAbsoluto('laberinto/img/Virus.png')
META_PATH = obtenerPathAbsoluto('laberinto/img/Meta.png')
PERSONAJE_PATH = obtenerPathAbsoluto('laberinto/img/niña.png')
MENSAJES_PATH = obtenerPathAbsoluto('laberinto/assets/direccionesMensajesLaberinto.txt')


class Laberinto(Juego):
    def __init__(self):
        self.dimensiones = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)
        self.titulo = 'Laberinto'
        self.ventana = None
        self.imagen = pygame.image.load(FONDO_PATH)
        self.reloj = pygame.time.Clock()
        self.tablero = None
        self.solapamiento = None

    def iniciarJuego(self):
        self.ventana = pygame.display.set_mode(self.dimensiones)
        self.ventana.blit(pygame.transform.scale(self.imagen, (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)), (0, 0))
        pygame.display.set_caption(self.titulo)

        self.tablero = TableroLaberinto()
        self.tablero.agregarCuadros(FondoLaberinto(FONDO_PATH, PosicionLaberinto(0, 0)))

        with open(CAMINOLAB_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(CaminoLaberinto(PISO_PATH, posicion))

        with open(POSICION_VIRUS_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(VirusLaberinto(VIRUS_PATH, posicion))

        with open(MENSAJES_PATH) as f:
            for line in f:
                textos = line.strip().split(',')
                self.tablero.agregarCuadros(MensajeLaberinto(textos[0], textos[1]))

        self.tablero.agregarCuadros(PersonajeLaberinto(PERSONAJE_PATH, PosicionLaberinto(1 * s.dim_Cuadro, 0)))
        self.tablero.agregarCuadros(MetaLaberinto(META_PATH, PosicionLaberinto(20 * s.dim_Cuadro, 12 * s.dim_Cuadro)))
        self.solapamiento = SolapamientoLaberinto(self.tablero)
        self.tablero.dibujar(self.ventana)
        MOSTRAR_INSTRUCCIONES = True
        bandera = True

        while bandera:
            self.reloj.tick(s.FPS)

            lstMsj = self.tablero.accederLista()['mensaje']
            msj = lstMsj[0]
            for m in lstMsj:
                if MOSTRAR_INSTRUCCIONES and m.getNombre() == 'instrucciones':
                    m.permitirDibujo(True)
                    msj = m
                    MOSTRAR_INSTRUCCIONES = False
                    self.tablero.dibujar(self.ventana)
                    break
                if m.getAparecer():
                    msj = m
            msj.esperar()
            if not msj.getAparecer():
                self.tablero.mover(self.solapamiento)
                self.tablero.dibujar(self.ventana)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    bandera=False
                    pygame.quit()
                    break

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
