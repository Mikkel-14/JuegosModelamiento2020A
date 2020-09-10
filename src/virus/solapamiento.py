from abc import ABC, abstractmethod
import pygame
from .cuadro import *


class Solapamiento(ABC):
    def __init__(self, Mapa, juego):
        self.mapa = Mapa
        self.juego = juego
        self.tipoCuadroSolapado = 'paginaNormal'
        self.pagina = None

    @abstractmethod
    def verificarSolapamiento(self, coordenadaActual, nuevasCoordenadas):
        pass

    def notify(self):
        self.juego.update(self.tipoCuadroSolapado)

class SolapamientoJugador(Solapamiento):

    def __init__(self, Mapa, juego):
        super().__init__(Mapa,juego)

    def verificarSolapamiento(self, coordenadaActual, nuevasCoordenadas):
        verificador = False
        for pagina in self.mapa.listaCuadros:
            if isinstance(pagina, CuadroPaginaWeb):
                self.pagina = pagina
                posicion, esMalo = self.pagina.getCoordenadasyEsMalo() #obtener informacion de posicion y estado de un cuadro pagina web
                if posicion == coordenadaActual and esMalo == False: #busca el cuadro sobre el que se encuentra el personaje y lo transforma a un virus
                    paginaActual = self.pagina
        for pagina in self.mapa.listaCuadros:
            #esta comprobacion es para luego poder ejecutar la transformacion de la pagina
            #sobre la cual el personaje se encuentra a una pagina virus (roja)
            if isinstance(pagina, CuadroPaginaWeb):
                self.pagina = pagina
                posicion, esMalo = self.pagina.getCoordenadasyEsMalo()
                if posicion == nuevasCoordenadas and esMalo == False: #verifica que la pagina web a la que se va a mover no es un virus
                    self.tipoCuadroSolapado = 'paginaNormal'
                    paginaActual.transformar()
                    self.notify()
                    verificador = True
                if posicion == nuevasCoordenadas and esMalo == True:#verifica si el personaje se esta moviendo a un virus
                #notificar perdida del juego
                    self.tipoCuadroSolapado = 'virus'
                    self.notify()
                    verificador = True
            if isinstance(pagina, CuadroObjetivo):
                if pagina.getCoordenadas() == nuevasCoordenadas:
                    paginaActual.transformar()
                    self.tipoCuadroSolapado = 'objetivo'
                    self.notify()
                    verificador = True

            if isinstance(pagina, CuadroPersonaje):
                posicion, tipo = pagina.getCoordenadasyTipo()
                if posicion == nuevasCoordenadas and tipo == 'malo': #verifica que la pagina web a la que se va a mover no es un virus
                    self.tipoCuadroSolapado = 'personaje'
                    self.notify()
                    verificador = True
        return verificador
