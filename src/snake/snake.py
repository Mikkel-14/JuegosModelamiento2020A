from .Ventana import *
import pygame
from .Control_Movimiento import *
from .Mensaje import *
from .Marcador import *


class Snake(object):

    def __init__(self):
        self.ventana=None
        self.velocidad=5

    def iniciarJuego(self):
        pygame.init()
        mensaje = Mensaje()
        self.ventana = Ventana()
        mapa = self.ventana.obtenerMapa()
        cabeza = mapa.obtenerComponentes()[0]
        cola = mapa.obtenerComponentes()[1]
        cabeza2 = mapa.obtenerComponentes()[2]
        cola2 = mapa.obtenerComponentes()[3]
        malware = mapa.obtenerMalware()
        pantalla = self.ventana.cargarPantalla()#pygame

        limiteVentanaX = self.ventana.obtenerLimites()[0]
        limiteVentanaY = self.ventana.obtenerLimites()[1]
        clock= pygame.time.Clock()
        bandera = True

        mensaje.estadoMensaje((True,False,False,False,False))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if keys[pygame.K_RETURN]:
                break

        mensaje.estadoMensaje((False,False,False,False,True))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if keys[pygame.K_SPACE]:
                break

        mensaje.estadoMensaje((False,False,False,True,False))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        while True:
            keys = Control_Movimiento.detectarMovimiento()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            if keys[pygame.K_RETURN]:
                break

        marcador= Marcador()
        while bandera and marcador.obtenerVidas()>=0:
            clock.tick(self.velocidad)
            run = [False,False,False,False]
            while not run[1] and not run[3]:
                clock.tick(self.velocidad)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                cabeza.mover(limiteVentanaX,limiteVentanaY)
                cabeza2.mover(limiteVentanaX,limiteVentanaY)

                run = mapa.verificarElementosMapa(self.ventana.obtenerLimites(),malware.obtenerPosicion())

                if run[0] or run[2]:
                    marcador.calcularPuntuacion(malware.obtenerValor())
                    malware = mapa.obtenerMalware()
                    #self.modificarPuntuacion(malware.obtenerValor())
                    #añada un segmentpo de cola
                    self.ventana.dibujarFondo(pantalla)
                    malware.dibujar(pantalla)
                    mapa.dibujarMapa(pantalla)
                    marcador.dibujar(pantalla)
                    if run[0]:
                        cola.agregarSegmento(cabeza.obtenerPosicion())
                        cola2.mover(cabeza2.obtenerPosicion())
                    elif run[2]:
                        cola2.agregarSegmento(cabeza2.obtenerPosicion())
                        cola.mover(cabeza.obtenerPosicion())
                elif not (run[1] or run [3]):
                    self.ventana.dibujarFondo(pantalla)
                    malware.dibujar(pantalla)
                    mapa.dibujarMapa(pantalla)
                    marcador.dibujar(pantalla)
                    cola.mover(cabeza.obtenerPosicion())
                    cola2.mover(cabeza2.obtenerPosicion())
                pygame.display.update()
            marcador.quitarVida()
            if run[1]:
                cabeza.retornarPosicion(limiteVentanaX,limiteVentanaY)
            elif run[3]:
                cabeza2.retornarPosicion(limiteVentanaX,limiteVentanaY)

            #mostrar el mensaje
            if marcador.obtenerVidas()>=0:
                mensaje.estadoMensaje((False,True,False,False,False))
            else:
                mensaje.estadoMensaje((False,False,True,False,False))
            self.ventana.dibujarFondo(pantalla)
            mapa.dibujarMapa(pantalla)
            mensaje.dibujar(pantalla)
            marcador.dibujar(pantalla)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        exit()
                keys = Control_Movimiento.detectarMovimiento()
                if keys[pygame.K_ESCAPE]:
                    bandera=False
                    break
                elif keys[pygame.K_SPACE] and marcador.obtenerVidas()>=0:
                    break
                elif keys[pygame.K_RETURN] and marcador.obtenerVidas()<0:
                    self.reiniciar(cola,cola2,marcador)
                    break

            cabeza.cambiarPosicion(0,-64)
            cabeza2.cambiarPosicion(704,512)

            """

            Preguntar acerca del método de arriba.
            """
            for segmento in cola.obtenerCola():
                segmento.cambiarPosicion((-128,-128))
            for segmento in cola2.obtenerCola():
                segmento.cambiarPosicion((-128,-128))
            self.ventana.dibujarFondo(pantalla)
            malware.dibujar(pantalla)
            mapa.dibujarMapa(pantalla)
            marcador.dibujar(pantalla)
            pygame.display.update()
        pygame.quit()

    def reiniciar(self,cola,cola2,marcador):
        marcador.reiniciar()
        tam= len(cola.obtenerCola())
        for i in range(tam):
            cola.quitarUltimo()
        tam= len(cola2.obtenerCola())
        for i in range(tam):
            cola2.quitarUltimo()


