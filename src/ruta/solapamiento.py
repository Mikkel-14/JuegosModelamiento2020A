#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#       Interfaz Solapamiento y clases SolapamientoConOpción y SolapamientoConObstáculo
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

from ruta.figuras import *
from ruta.verificacion import *
import math


class Solapamiento():
    @abstractmethod
    def verificarSolapamiento(self):
        pass


class SolapamientoConObstaculo(Solapamiento):
    def __init__(self, verificacion, camino):
        self.verificacion = verificacion
        self.camino = camino
        self.umbral = int(settings["tamañoVentana"][1]*0.09) # Para controlar la distancia minima entre los objetos al solapar
        self.s_posicionObstaculo = None # Variable para asociar la posición de un obstáculo
    
    def verificarSolapamiento(self, posicionPersonaje):
        (x1, y1) = posicionPersonaje # se almacena en una tupla

        for obstaculo in self.camino.obtenerObstaculos():
            (x2, y2) = obstaculo.posicion.obtenerCoordenadas()
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)) # Aplicación de la fórmula de distancia entre dos puntos

            if distancia <= self.umbral: # verifica la distancia mínima para el solapamiento con un obstáculo
                self.verificacion.comunicarSolapamientoObstaculo(True) # Luego verificación comunicará a Mapa dicho solapamiento
                obstaculo.posicion.actualizarY(settings["tamañoVentana"][1])
            else:
                self.verificacion.comunicarSolapamientoObstaculo(False) # Luego verificación comunicará a Mapa que no ocurrió solapamiento


class SolapamientoConOpcion(Solapamiento):
    def __init__(self, verificacion):
        self.verificacion = verificacion
        self.umbral = int(settings["tamañoVentana"][1]*0.08)
        self.posicionOpcion = None # Variable para asociar la posición de una opción
        self.visibilidadOpcion = None # Variable para asociar el estado de visibilidad de una opción
        self.opcionObservada = None
        self.letraSeleccionada = None
        
    def añadirOpcionObservada(self, figuraOpcion):
        self.opcionObservada = figuraOpcion

    def verificarSolapamiento(self, posicionJugador):
        if self.posicionOpcion != None and self.visibilidadOpcion == True:
            (x1, y1) = posicionJugador # coordenadas 
            (x2, y2) = self.posicionOpcion # coordenadas
            distancia = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)) 

            if distancia <= self.umbral:  # verifica la distancia mínima para el solapamiento con una opción
                self.verificacion.verificarSeleccion(self.letraSeleccionada) # Luego verificación comparará la letra seleccionada con la letra respuesta del audio
    
    def actualizar(self): # Método actualizar() del patrón observador entre SolapamientoConOpcion y FiguraOpción
        if self.opcionObservada.visibilidad == True:
            self.visibilidadOpcion, self.posicionOpcion, self.letraSeleccionada = self.opcionObservada.obtenerDatos()
        else:
            self.visibilidadOpcion, self.posicionOpcion, self.letraSeleccionada = None, None, None