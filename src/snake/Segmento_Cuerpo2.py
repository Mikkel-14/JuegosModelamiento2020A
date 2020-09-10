import pygame
import os
import sys
from ISegmento import ISegmento

segmento = pygame.image.load(os.path.join(os.path.dirname(__file__), "img/segmentoCola2.png"))

class Segmento_Cuerpo2(ISegmento):

    def __init__(self,x,y):
        self.posX = x
        self.posY = y
        self.imagen = segmento

    def dibujar(self,ventana):
        ventana.blit(self.imagen, (self.posX,self.posY))

    def ocultar(self):
        pass

    def obtenerPosicion(self):
        return self.posX,self.posY

    def cambiarPosicion(self,pos):
        self.posX=pos[0]
        self.posY=pos[1]