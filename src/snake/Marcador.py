import pygame
import os.path
tablero= pygame.image.load(os.path.join(os.path.dirname(__file__), "img/Tablero.png"))
class Marcador(object):
    def __init__(self):
        self.imagenTablero=tablero
        self.puntuacion= 0
        self.vidas= 2
    #Definir la imagen y la posición.

    def dibujar(self,pantalla):
        pantalla.blit(self.imagenTablero, (0,512))
        punt =  pygame.font.Font(None, 75).render('{:}'.format(str(self.puntuacion)), True, (255,255,255))
        pantalla.blit(punt, [256,520])
        vid =  pygame.font.Font(None, 75).render('{:}'.format(str(self.vidas+1)), True, (255,255,255))
        pantalla.blit(vid, [705,520])
    def calcularPuntuacion(self,valorMalware):
        self.puntuacion+=valorMalware

    def quitarVida(self):
        self.vidas-=1

    def reiniciar(self):
        self.puntuacion= 0
        self.vidas= 2

    def obtenerVidas(self):
        return self.vidas

    def obtenerPuntuacion(self):
        return self.puntuacion
