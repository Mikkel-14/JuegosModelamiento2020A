#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#          Clase abstracta Figura y Clases Personaje, Marcador, FiguraVida Fondo
#                                FiguraOpción, Camino y Mapa
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================

import pygame
from abc import ABC, abstractmethod
from ruta.assets.herramientas import *
from ruta.assets.settingsMaya import *
from ruta.audioPregunta import *
from ruta.solapamiento import *
from ruta.listener import *
from ruta.fabricas import *


class Figura(ABC):
    def __init__(self, posicion):
        self.posicion = posicion
        super().__init__()

    @abstractmethod
    def dibujar(self):
        pass

    @abstractmethod
    def mover(self):
        pass


class Personaje(Figura):
    def __init__(self, imagen, posicion, solapamientoConOpcion, solapamientoConObstaculo):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoPersonaje"])
        self.solapamientoConOpcion = solapamientoConOpcion
        self.solapamientoConObstaculo = solapamientoConObstaculo
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def mover(self):
        x, y = Listener.captarMouse()
        tamañoImagen = self.imagen.get_rect() # Obtiene la superficie de la imagen
        distanciaVereda = (settings["tamañoVentana"][0] - settings["tamañoCamino"][0])/2 # lo que mide en X una vereda lateral
        condicionLimiteX = x >= distanciaVereda*1.2 and x <= settings["tamañoVentana"][0] - distanciaVereda*1.2 # para que personaje no se mueva en las veredas laterales
        condicionLimiteY = y >= settings["tamañoVentana"][1] * 0.1 and y <= settings["tamañoVentana"][1]*0.9 # para que el movimiento del personaje no sobrepase las dimensiones en y
        
        if(condicionLimiteX and condicionLimiteY): # si está dentro de los limites el personaje se mueve
            self.posicion.actualizarX(Listener.captarMouse()[0]-tamañoImagen.width/2)
            self.posicion.actualizarY(Listener.captarMouse()[1]-tamañoImagen.height/2)
        
        # Solapamiento con las opciones
        for solapamiento in self.solapamientoConOpcion:
            solapamiento.verificarSolapamiento(self.posicion.obtenerCoordenadas())  
        
        # Solapamiento con un obstáculo
        self.solapamientoConObstaculo.verificarSolapamiento(self.posicion.obtenerCoordenadas())

class Marcador(Figura):
    def __init__(self, imagen, posicion, puntaje):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoMarcador"])
        self.posicion = posicion
        self.puntaje = puntaje

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas()) # dibuja el fondo del marcador
        fuente = pygame.font.SysFont('comicsansms', settings["tamañoLetraPuntaje"]) 
        textoPuntaje = fuente.render(f'Puntaje: {self.puntaje.getPuntos()}', True, (255, 255, 255)) # NOTE: Mantener True puesto que mejora la resolución de la letra
        ventana.blit(textoPuntaje, (self.posicion.obtenerCoordenadas()[0]*1.065, self.posicion.obtenerCoordenadas()[1]*1.3)) # Se dibuja el texto según la posición del marcador
        
    def subirPuntajeMarcador(self):
        return puntaje.aumentar()

    def mover(self):
        pass

class FiguraVida(Figura):
    def __init__(self, posicion):
        self.imagen = None
        self.numeroVidas = 4
        super().__init__(posicion)

    def dibujar(self, ventana):
        if(self.numeroVidas == 4):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida4.png', __file__))
        elif (self.numeroVidas == 3):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida3.png', __file__))
        elif (self.numeroVidas == 2):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida2.png', __file__))
        elif (self.numeroVidas == 1):
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida1.png', __file__))
        else:
            self.imagen = pygame.image.load(obtenerPathAbsoluto('img/vida0.png', __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoFigVida"])
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())
    
    def disminuirVidas(self):
        self.numeroVidas = self.numeroVidas - 1

    def obtenerNumeroVidas(self): 
        return self.numeroVidas

    def mover(self):
        pass

    def reiniciarNumeroDeVidas(self): # para cuando se reinicie el juego
        self.numeroVidas = 4

class Fondo(Figura):
    def __init__(self, imagen, posicion):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoVentana"])
        super().__init__(posicion)

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())

    def mover(self):
        pass

class FiguraOpcion(Figura):
    def __init__(self, imagen, posicion, letraAsociada):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoOpcion"])
        super().__init__(posicion)
        self.letraAsociada = letraAsociada
        self.solapamiento = None
        self.visibilidad = False

    def dibujar(self, ventana):
        if(self.visibilidad == True):
            ventana.blit(self.imagen, self.posicion.obtenerCoordenadas())
            self.notificar()
        elif(self.visibilidad == False):
            self.notificar()

    def mover(self):
        pass

    def añadirObservador(self, observador):
        self.solapamiento = observador

    def setVisibilidad(self, esVisible):
        self.visibilidad = esVisible

    # NOTE: notificar() del patrón observador entre FiguraOpción y SolapamientoConOpción
    def notificar(self): 
        self.solapamiento.actualizar()

    def obtenerDatos(self):
        return(self.visibilidad, self.posicion.obtenerCoordenadas(), self.letraAsociada)

    def obtenerVisibilidad(self):
        return self.visibilidad

class Camino(Figura):

    # Iteradores
    _iteradorObstaculo = 0
    _iteradorAudioPregunta = -1

    def __init__(self, imagen, posicion, playlist):
        self.imagen = pygame.image.load(obtenerPathAbsoluto(imagen, __file__))
        self.imagen = pygame.transform.scale(self.imagen, settings["tamañoCamino"])
        super().__init__(posicion)
        self.estadoMovimiento = True
        self.obstaculos = FabricaRandomica().crearObstaculo() # se utiliza la fábrica
        self.playlist = playlist

        
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.posicion.obtenerCoordenadas()[0], settings["tamañoCamino"][1]))
        
    def mover(self, ventana, opciones):

        if(self.estadoMovimiento and self._iteradorAudioPregunta < 3): # si el camino está en movimiento y aún no se han reproducido todas las canciones

            # Implementación para que se mueva el camino en el eje "y" usando la operación módulo %
            x, y = self.posicion.obtenerCoordenadas()
            alturaImagen = self.imagen.get_rect().height
            relativoY = y % alturaImagen
            self.distancia = abs(y)

            if(self.distancia <= alturaImagen*3): # si la distancia desplazada aún no es tres veces la altura de la imagen del camino
                ventana.blit(self.imagen, (x, relativoY - alturaImagen))
                if relativoY < settings['tamañoVentana'][1]:
                    ventana.blit(self.imagen, (x, relativoY))
                self.posicion.actualizarY(y-settings["factorDesplazamiento"])

                # Una vez en movimiento el camino se obtiene un obstáculo para que aparezca en el camino
                escogido = self.obstaculos[self._iteradorObstaculo]
                escogido.dibujar(ventana)
                escogido.mover()

                if escogido.posicion.obtenerCoordenadas()[1] < 0: # si la posición del obstaculo esta fuera del limite superior de la ventana
                    self._iteradorObstaculo+= 1
                    escogido = self.obstaculos[self._iteradorObstaculo] # se selecciona otro obstaculo
                    escogido.dibujar(ventana)
                    escogido.mover()

            else: # cuando la distancia desplazada es tres veces la altura de la imagen del camino
                self.estadoMovimiento = False # el camino deja de estar en movimiento
                self.posicion.actualizarY(0) # se reubica la imagen del camino
                self._iteradorAudioPregunta += 1
        
        else: # Cuando el camino está detenido se reproducto un audio pregunta del Playlist
            self.playlist.obtenerAudiosPreguntas()[self._iteradorAudioPregunta].reproducir(self.comunicarMovimiento(), opciones)
            ventana.blit(self.imagen, settings["coordenadaCamino"])

    def comunicarMovimiento(self):
        if(self.estadoMovimiento == False):
            return self.estadoMovimiento

    def obtenerObstaculos(self):
        return self.obstaculos
    
    def setEstadoMovimiento(self, valor):
        self.estadoMovimiento = valor

    def getEstado(self):
        return self.estadoMovimiento

    def reiniciarIteradores(self):
        self._iteradorObstaculo = 0
        self._iteradorAudioPregunta = -1
        self.posicion.actualizarY(0)
        self.obstaculos = FabricaRandomica().crearObstaculo()
        for audio in self.playlist.obtenerAudiosPreguntas():
            audio.setEstadoReproducido(True)


class Mapa(Figura):
    def __init__(self):
        self.listaFiguras = []

    def agregarFigura(self, figura):
        self.listaFiguras.append(figura)

    def quitarFigura(self):
        self.listaFiguras.remove(figura)

    def dibujar(self, ventana):
        for figura in self.listaFiguras:
            figura.dibujar(ventana)

    def mover(self, ventana):
        for figura in self.listaFiguras:
            if isinstance(figura, Camino):
                figura.mover(ventana, list(filter(lambda e: isinstance(e, FiguraOpcion), self.listaFiguras))) # con lambda se obtiene las figuras opciones para el reproducir() de audioPregunta que se emplea dentro del mover() de camino
            elif isinstance(figura, Personaje):
                figura.mover()
        pygame.mouse.set_visible(False)
        
    def obtenerOpciones(self):
        return filter(lambda e: isinstance(e, FiguraOpcion), self.listaFiguras)   

    def obtenerVidasActuales(self):
        return list(filter(lambda e: isinstance(e, FiguraVida), self.listaFiguras))[0].obtenerNumeroVidas()
    
    def obtenerFiguraVida(self):
        return list(filter(lambda e: isinstance(e, FiguraVida), self.listaFiguras))[0]
    
    def obtenerCamino(self):
        return list(filter(lambda e: isinstance(e, Camino), self.listaFiguras))[0]
    
    # Según el valor de comprobación (booleano) que envía la clase Verificación
    def actualizar(self, comprobacion):
        for figura in self.listaFiguras:
            if isinstance(figura, Camino):
                figura.setEstadoMovimiento(True) # se activa el movimiento del camino
            elif isinstance(figura, FiguraOpcion):
                figura.setVisibilidad(False) # se ocultan las opciones
            elif comprobacion == False and isinstance(figura, FiguraVida):
                figura.disminuirVidas() #  y en caso de un False se disminuye las vidas