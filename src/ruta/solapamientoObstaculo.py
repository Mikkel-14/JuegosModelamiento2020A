#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                Clase SolapamientoConObstaculo
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

from ruta.figuras import *
from ruta.verificacion import *
import math


class SolapamientoConObstaculo():
    def __init__(self,  mapa):
        self.umbral = int(settings["tamañoVentana"][1]*0.09) # Para controlar la distancia minima entre los objetos al solapar
        self.s_posicionObstaculo = None # Variable para asociar la posición de un obstáculo
        self.mapa = mapa
    def verificarSolapamiento(self, posicionPersonaje):
        (x1, y1) = posicionPersonaje # se almacena en una tupla

        for obstaculo in self.mapa.obtenerCamino().obtenerObstaculos():
            (x2, y2) = obstaculo.posicion.obtenerCoordenadas()
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)) # Aplicación de la fórmula de distancia entre dos puntos

            if distancia <= self.umbral: # verifica la distancia mínima para el solapamiento con un obstáculo
                if self.mapa.obtenerCamino().estadoMovimiento: # solo si el camino sigue en movimiento
                    self.mapa.actualizar(False) 
                obstaculo.posicion.actualizarY(settings["tamañoVentana"][1])
            else:
                pass
