import pygame
from herramientas import *
import json

class VentanaPuntuaciones():
    def __init__(self, usuario):
        pygame.init()
        self.fondo = pygame.image.load(obtenerPathAbsoluto('img/ventanaPuntuacion.png'))
        self.nombreUsuario = usuario
        self.dimensiones = (381,443)

    def mostrarPuntuaciones(self):
        pygame.init()
        fuente = pygame.font.Font(None, 25)
        with open(obtenerPathAbsoluto('data.json')) as archivo:
            diccionario = json.load(archivo)
        ventana = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption("Tabla de puntuaciones")
        ultimos10 = list()
        for diccionarios in diccionario['usuarios']:
            if self.nombreUsuario in diccionarios.values():
                historia = diccionarios['puntuaciones']
                if len(historia) > 10:
                    ultimos10 = historia[0:10]
                else:
                    ultimos10 = historia
                break
        ventana.blit(self.fondo, (0,0))
        usuarioGrafico = fuente.render('Usuario: {:}'.format(self.nombreUsuario), True, (255,255,255))
        ventana.blit(usuarioGrafico, (50,62))
        (x, y) = (75, 87)
        for valores in ultimos10:
            texto = fuente.render(str(valores), True, (255,255,255))
            ventana.blit(texto, (x, y))
            y += 32
        flag = True
        while flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    flag = False
                    pygame.quit()
            pygame.display.update()
