import pygame

pygame.init()

class Listener():
    def __init__(self, keyMap):
        #el keymap es una tupla que contiene las teclas que debe escuchar el listener
        #ej: el keymap puede ser (pygame.K_UP,pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT)
        self.keyMap = keyMap

    def detectar(self) -> tuple:
        mapa = pygame.key.get_pressed()
        listaDeteccion = list()
        for x in self.keyMap:
            listaDeteccion.append(mapa[x])
        tuplaDetectados = tuple(listaDeteccion)
        return tuplaDetectados
