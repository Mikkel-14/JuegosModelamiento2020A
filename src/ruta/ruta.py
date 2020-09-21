#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                         Clase Ruta
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================
import pygame
import os
import sys
from ruta.assets.settingsMaya import *
from ruta.audioPregunta import *
from ruta.solapamientoObstaculo import *
from ruta.solapamientoOpcion import *
from ruta.posicionMaya import *
from ruta.fabricas import *
from ruta.figuras import *
from ruta.mensaje import *
from ruta.puntaje import *
from ruta.boton import *

pygame.init()

class Ruta():
    def __init__(self):
        pygame.init()
        self.mapa = Mapa()
        self.puntaje = Puntaje(4, 0)    

    def iniciarJuego(self):

        pygame.init() # carga los modulos de la librería pygame
        self.ventanaRuta = pygame.display.set_mode(settings["tamañoVentana"])
        pygame.mouse.set_cursor(*pygame.cursors.tri_left) # cambia la apariencia del cursor por el diseño "tri_left"

        # creación de botones
        botonJugar = Boton('JUGAR', Posicion(settings["coordenadaBotonJugar"]))
        botonAtras = Boton('VOLVER_AL_MUSEO', Posicion(settings["coordenadaBotonAtras"]))
        botonOk = Boton('OK', Posicion(settings["coordenadaBotonOk"]))

        # creación de mensajes con sus botones respectivos
        mensajeBienvenida = Mensaje('img/fondoBienvenida.png', Posicion((0, 0)))
        mensajeBienvenida.agregarBoton(botonJugar)
        mensajeBienvenida.agregarBoton(botonAtras)

        mensajeInstrucciones = Mensaje('img/fondoInstrucciones.png', Posicion((0, 0)))
        mensajeInstrucciones.agregarBoton(botonOk)
        mensajeBienvenida.mostrar(self.ventanaRuta)

        if(mensajeBienvenida.visibilidad == False and mensajeBienvenida._flag):

            mensajeInstrucciones.mostrar(self.ventanaRuta)

        rutamayainiciado = True

        # Creación de mensajes y botones correspondientes para el GAME OVER y el Fin del juego
        btnVolverAtras = Boton('VOLVER_AL_MUSEO', Posicion(settings["coordenadaBotonAtras"]))
        btnVolverJugar = Boton('VOLVER_A_JUGAR', Posicion(settings["coordenadaBotonJugar"]))
        mensajeGameOver = Mensaje('img/fondoAvisoPerdiste.png', Posicion((0,0)))
        mensajeGameOver.agregarBoton(btnVolverAtras)
        mensajeGameOver.agregarBoton(btnVolverJugar)
        mensajeGanaste = Mensaje('img/fondoAvisoGanaste.png', Posicion((0,0)))
        mensajeGanaste = Mensaje('img/fondoAvisoGanaste.png', Posicion((0,0)))
        mensajeGanaste.agregarBoton(btnVolverAtras)
        mensajeGanaste.agregarBoton(btnVolverJugar)

        self.puntaje = Puntaje(4, 0)

        pregunta1 = AudioPregunta('sounds/pregunta1.wav', "C")
        pregunta2 = AudioPregunta('sounds/pregunta2.wav', "B")
        pregunta3 = AudioPregunta('sounds/pregunta3.wav', "C")
        pregunta4 = AudioPregunta('sounds/pregunta4.wav', "B")

        preguntas = Playlist()

        preguntas.añadirAudioPregunta(pregunta1)
        preguntas.añadirAudioPregunta(pregunta2)
        preguntas.añadirAudioPregunta(pregunta3)
        preguntas.añadirAudioPregunta(pregunta4)

        verificacion = Verificacion(preguntas, self.mapa, self.puntaje)
        camino = Camino('img/fondoCamino22.png', Posicion(settings["coordenadaCamino"]), preguntas)

        solapamientoOpcionA = SolapamientoConOpcion(verificacion)
        solapamientoOpcionB = SolapamientoConOpcion(verificacion)
        solapamientoOpcionC = SolapamientoConOpcion(verificacion)
        solapamientosConOpcion = [solapamientoOpcionA, solapamientoOpcionB, solapamientoOpcionC]


        opcionA = FiguraOpcion('img/botonA.png', Posicion(settings["coordenadaOpcion"][0]), "A")
        opcionA.añadirObservador(solapamientoOpcionA)

        opcionB = FiguraOpcion('img/botonB.png', Posicion(settings["coordenadaOpcion"][1]), "B")
        opcionB.añadirObservador(solapamientoOpcionB)

        opcionC = FiguraOpcion('img/botonC.png', Posicion(settings["coordenadaOpcion"][2]), "C")
        opcionC.añadirObservador(solapamientoOpcionC)

        solapamientoOpcionA.añadirOpcionObservada(opcionA)
        solapamientoOpcionB.añadirOpcionObservada(opcionB)
        solapamientoOpcionC.añadirOpcionObservada(opcionC)

        self.mapa.agregarFigura(Fondo('img/fondoJuego.png', Posicion(settings["coordenadaFondo"])))
        self.mapa.agregarFigura(camino)

        solapamientoConObstaculo = SolapamientoConObstaculo(self.mapa)
        figuraVida = FiguraVida(Posicion(settings["coordenadaFigVida"]))
        self.reiniciarJuego(figuraVida, camino, verificacion)
        mensajeGameOver._flag = True
        self.mapa.agregarFigura(figuraVida)
        self.mapa.agregarFigura(Marcador('img/marcador.png', Posicion(settings["coordenadaMarcador"]), self.puntaje))
        self.mapa.agregarFigura(opcionA)
        self.mapa.agregarFigura(opcionB)
        self.mapa.agregarFigura(opcionC)
        self.mapa.agregarFigura(Personaje('img/personaje.png', Posicion(settings["coordenadaPersonaje"]), solapamientosConOpcion, solapamientoConObstaculo))

        while rutamayainiciado:
            self.verificarCondiciones(mensajeGameOver, mensajeGanaste, verificacion)
            if(mensajeGameOver._flag):
                self.mapa.dibujar(self.ventanaRuta)

                for event in pygame.event.get():
                    pass

            if (mensajeGameOver._flag == True):
                pygame.display.update()
            else:
                break

    def verificarCondiciones(self, mensajeGameOver, mensajeGanaste, verificacion):
        if self.mapa.obtenerVidasActuales() >= 1:
            self.mapa.mover(self.ventanaRuta)
            if verificacion.obtenerNumeroPreguntasContestadas() == 4:
                pygame.mouse.set_visible(True)
                self.reiniciarJuego(self.mapa.obtenerFiguraVida(), self.mapa.obtenerCamino(), verificacion)
                mensajeGanaste.mostrar(self.ventanaRuta)
                mensajeGameOver._flag = True
        else:
            pygame.mouse.set_visible(True)
            self.reiniciarJuego(self.mapa.obtenerFiguraVida(), self.mapa.obtenerCamino(), verificacion)
            mensajeGameOver._flag = True
            mensajeGameOver.mostrar(self.ventanaRuta)

    def reiniciarJuego(self, figuraVida, camino, verificacion):
        figuraVida.reiniciarNumeroDeVidas()
        camino.reiniciarIteradores()
        verificacion.reiniciarNumeroPreguntasContestadas()
        verificacion._i = 0

    def getPuntos(self):
        return self.puntaje.getPuntos()
