import pygame
import os
import sys
from ruta.figuras import *
from ruta.posicionMaya import *
from ruta.mensaje import *
from ruta.solapamiento import *
from ruta.assets.settings import *
from ruta.boton import *
from ruta.audioPregunta import *
sys.path.append('../juego.py')
from juego import *


class Ruta(Juego):
    def __init__(self):
        self.dimensiones = settings["tamañoVentana"]
        self.titulo = settings["nombre"]
        self.ventana = None
        self.clock = pygame.time.Clock()

    def iniciarJuego(self):
        self.ventana = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)

        rutamayainiciado = True

        # Mensajes iniciales GUI
        mensajeBienvenida = MensajeRuta('img/fondoBienvenida.png', PosicionRuta((0, 0)))
        mensajeInstrucciones = MensajeRuta('img/fondoInstrucciones.png', PosicionRuta((0, 0)))
        btnJugar = BotonRuta('JUGAR', PosicionRuta(settings["coordenadaBotonJugar"]))
        btnAtras = BotonRuta('ATRAS', PosicionRuta(settings["coordenadaBotonAtras"]))
        btnOk = BotonRuta('OK', PosicionRuta(settings["coordenadaBotonOk"]))
        mensajeBienvenida.agregarBoton(btnJugar)
        mensajeBienvenida.agregarBoton(btnAtras)
        mensajeInstrucciones.agregarBoton(btnOk)
        mensajeBienvenida.mostrar(self.ventana)
        mensajeInstrucciones.mostrar(self.ventana)

        mapa = Mapa()

        audioPruebaSonido = AudioPregunta('sounds/p1.wav', "A", mapa.obtenerOpciones())

        verificacion = VerificacionRuta(audioPruebaSonido, mapa)

        solapamientoOpcionA = SolapamientoRuta(30, verificacion)
        solapamientoOpcionB = SolapamientoRuta(30, verificacion)
        solapamientoOpcionC = SolapamientoRuta(30, verificacion)

        solapamientos = [solapamientoOpcionA,solapamientoOpcionB,solapamientoOpcionC]

        mapa.agregarFigura(Fondo('img/fondoJuego.png', PosicionRuta(settings["coordenadaFondo"])))
        camino = Camino('img/fondoCamino.png',PosicionRuta(settings["coordenadaCamino"]))
        mapa.agregarFigura(camino)
        mapa.agregarFigura(FiguraVida(PosicionRuta(settings["coordenadaFigVida"])))
        mapa.agregarFigura(Marcador('img/marcador.png', PosicionRuta(settings["coordenadaMarcador"]), 0))
        mapa.agregarFigura(Personaje('img/personaje.png', PosicionRuta(settings["coordenadaPersonaje"]), solapamientos))

        opcionA = FiguraOpcion('img/botonA.png', PosicionRuta(settings["coordenadaOpcion"][0]), "A", solapamientoOpcionA)
        opcionB = FiguraOpcion('img/botonB.png', PosicionRuta(settings["coordenadaOpcion"][1]), "B", solapamientoOpcionB)
        opcionC = FiguraOpcion('img/botonC.png', PosicionRuta(settings["coordenadaOpcion"][2]), "C", solapamientoOpcionC)

        mapa.agregarFigura(opcionA)
        mapa.agregarFigura(opcionB)
        mapa.agregarFigura(opcionC)

        while rutamayainiciado:
            mapa.mover(self.ventana)
            mapa.dibujar(self.ventana)
            audioPruebaSonido.reproducir(camino)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rutamayainiciado = False
                    pygame.quit()
            pygame.display.update()
                    

    def reiniciarJuego(self):
        pass

    def salirJuego(self):
        pass
