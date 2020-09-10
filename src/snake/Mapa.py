import pygame
from .Colision import Colision
from .Fabrica_Troyano import Fabrica_Troyano
from .Fabrica_Spyware import Fabrica_Spyware
from .Fabrica_Bomba import Fabrica_Bomba
from random import randint
from .Cabeza import Cabeza
from .Cabeza2 import Cabeza2
from .Cola import Cola
from .Cola2 import Cola2

class Mapa(object):

    def __init__(self):
        self.cabeza = Cabeza(0,0,64,64)
        self.cabeza2 = Cabeza2(704,448,64,64)
        self.cola = Cola()
        self.cola2 = Cola2()
        self.ancho = 768
        self.alto = 512

    def obtenerMalware(self):
        pos = (randint(0,11)*64, randint(0,7)*64)
        bandera = True
        while bandera:
            bandera=False
            for segmento in self.cola.obtenerCola():
                if segmento.obtenerPosicion() == pos or self.cabeza.obtenerPosicion() == pos:
                    pos = (randint(0,11)*64, randint(0,7)*64)
                    #bandera=True POSIBLE CAMBIO
            for segmento in self.cola2.obtenerCola():
                if segmento.obtenerPosicion() == pos or self.cabeza2.obtenerPosicion() == pos:
                    pos = (randint(0,11)*64, randint(0,7)*64)
                    bandera=True
        aleatorio=randint(0,100)
        if aleatorio >=0 and aleatorio <=33:
            return Fabrica_Troyano().crearImagen(pos)

        elif aleatorio >33 and aleatorio <=66:
            return Fabrica_Spyware().crearImagen(pos)

        else:
            return Fabrica_Bomba().crearImagen(pos)

    def dibujarMapa(self, ventana):
        self.cola.dibujar(ventana)
        self.cabeza.dibujar(ventana)
        self.cola2.dibujar(ventana)
        self.cabeza2.dibujar(ventana)

    def obtenerComponentes(self):
        return (self.cabeza,self.cola,self.cabeza2,self.cola2)

    def verificarElementosMapa(self,limVentana,posMalware):
        return Colision().verificarColision(self.cabeza,self.cabeza2,self.cola,self.cola2,limVentana,posMalware)
