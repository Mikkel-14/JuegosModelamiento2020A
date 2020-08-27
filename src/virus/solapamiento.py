import sys
sys.path.append('../juego.py')
from herramientas import *
from virus.cuadro import *
from virus.solapamiento import *
class Solapamiento:

    def __init__(self, Mapa, juego):
        self.mapa = Mapa
        self.juego = juego
        self.tipoCuadroSolapado = 'paginaNormal'
        self.pagina = None

    
