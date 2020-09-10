#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                         Interfaz Fábrica y Clase FábricaRandómica 
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
import random
from ruta.obstaculos import *
from abc import ABC, abstractmethod


class FabricaObstaculos:
    @abstractmethod
    def crearObstaculo(self):
        pass


class FabricaRandomica(FabricaObstaculos):
    def crearObstaculo(self):
        obstaculosAleatorios = []
        numeroObstaculos = 32
        for i in range (numeroObstaculos):
            aleatorio = random.randrange(1,4) # En randrange el 4 es excluido por lo que el número aleatorio estaría entre 1 a 3
            if aleatorio == 1:
                obstaculo = ObstaculoA()
                obstaculosAleatorios.append(obstaculo)
            elif aleatorio == 2:
                obstaculo = ObstaculoB()
                obstaculosAleatorios.append(obstaculo)
            elif aleatorio == 3:
                obstaculo = ObstaculoC()
                obstaculosAleatorios.append(obstaculo)
        return obstaculosAleatorios # retorna la lista de obstáculos randómicos a utilizar en el camino