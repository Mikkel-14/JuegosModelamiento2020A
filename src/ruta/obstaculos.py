#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                Interfaz Obstáculo y clases Virus, ArañaGigante y MailInfectado 
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from ruta.assets.herramientas import *
from ruta.assets.settingsMaya import *
from ruta.posicionMaya import *
from random import randint
from abc import ABC, abstractmethod


class Obstaculo(ABC):
    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Virus(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/obs1.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        
        # Se emplea randint de la librería random para que la posición en x de cada obstáculo al aparecer sea randómica
        # NOTE: La posición original en y del obstáculo será siempre por debajo del margen de la ventana
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.obtenerCoordenadas()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): # En el caso de que el obstáculo este dentro del margen de la ventana
            self.posicion.actualizarY(self.posicion.obtenerCoordenadas()[1]-settings["tamañoVentana"][1]*0.03) # Entonces se mueve hacia arriba
        else:  # caso contrario se reubica al obstáculo
            self.posicion.actualizarY(settings["tamañoVentana"][1]) # a su posición en y original 
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"]))) # y con un valor aleatorio en x


class ArañaGigante(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/obs2.png', __file__)).convert_alpha()
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.obtenerCoordenadas()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): # En el caso de que el obstáculo este dentro del margen de la ventana
            self.posicion.actualizarY(self.posicion.obtenerCoordenadas()[1]-settings["tamañoVentana"][1]*0.03) # Entonces se mueve hacia arriba
        else:  # caso contrario se reubica al obstáculo
            self.posicion.actualizarY(settings["tamañoVentana"][1]) # a su posición en y original 
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"]))) # y con un valor aleatorio en x


class MailInfectado(Obstaculo):
    def __init__(self):
        self.imagen = pygame.image.load(obtenerPathAbsoluto('img/obs3.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoObstaculo"])
        self.posicion = Posicion((randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"])), settings["tamañoVentana"][1]))
 
    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def mover(self):
        alturaImagen = self.imagen.get_height()
        if (self.posicion.obtenerCoordenadas()[1] >= (-settings["tamañoVentana"][1]-alturaImagen)): # En el caso de que el obstáculo este dentro del margen de la ventana
            self.posicion.actualizarY(self.posicion.obtenerCoordenadas()[1]-settings["tamañoVentana"][1]*0.03) # Entonces se mueve hacia arriba
        else:  # caso contrario se reubica al obstáculo
            self.posicion.actualizarY(settings["tamañoVentana"][1]) # a su posición en y original 
            self.posicion.actualizarX(randint(int(settings["limiteMinObstaculoX"]), int(settings["limiteMaxObstaculoX"]))) # y con un valor aleatorio en x