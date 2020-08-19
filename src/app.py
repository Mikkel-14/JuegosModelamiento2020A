import pygame
from cuadros import *
from solapamiento import *

import os


# Este método permite obtener una dirección absoluta de un fichero o archivo
def obtenerPathAbsoluto(pathRelativo):
    pathAbsolutoScript = os.path.dirname(__file__)
    pathAbsoluto = os.path.join(pathAbsolutoScript, pathRelativo)
    return pathAbsoluto


pygame.init()
reloj = pygame.time.Clock()

CAMINO_PATH = obtenerPathAbsoluto('assets/matrizCamino.txt')
FONDO_PATH = obtenerPathAbsoluto('img/fondo.png')
PISO_PATH = obtenerPathAbsoluto('img/piso.png')
PERSONAJE_PATH = obtenerPathAbsoluto('img/personaje.png')

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
