import pygame
import settings as s
from cuadros import *
from solapamiento import *
from puntaje import *
import os.path as path
from herramientas import *

CAMINO_PATH = obtenerPathAbsoluto('assets/matrizCamino.txt')
ESTACION_PATH = obtenerPathAbsoluto('assets/matrizEstacion.txt')
FONDO_PATH = obtenerPathAbsoluto('img/fondo.png')
PISO_PATH = obtenerPathAbsoluto('img/piso.png')
ALFOMBRA_PATH = obtenerPathAbsoluto('img/alfombra.png')
PERSONAJE_PATH = obtenerPathAbsoluto('img/personaje.png')
MENSAJE_PATH = obtenerPathAbsoluto('assets/direccionesMensajes.txt')
MARCADOR_PATH = obtenerPathAbsoluto('img/marcador.png')
INSTRUCCIONES = True
s.init()

ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"w")
ppNiña.write("0,204,0")
ppNiña.close()

# Reemplazo -------
ven_dim = (714, 476)
ven = pygame.display.set_mode(ven_dim)
pygame.display.set_caption('Proyecto 2020A')

mapa = MapaMuseo()
mapa.agregarCuadros(Fondo(FONDO_PATH, Posicion(0, 0)))
with open(CAMINO_PATH) as f:
    for line in f:
        coords = line.strip().split(',')
        x = int(coords[0])*34
        y = int(coords[1])*34
        posicion = Posicion(x, y)
        mapa.agregarCuadros(Camino(PISO_PATH, posicion))
# Reemplazo -------

mapa.agregarCuadros(Personaje(PERSONAJE_PATH, Posicion(0, 6*34)))
solapamiento = Solapamiento(mapa)
mapa.dibujar(ven)

while True:
    reloj.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    mapa.mover(solapamiento)
    mapa.dibujar(ven)
