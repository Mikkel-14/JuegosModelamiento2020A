from .Ventana import *
import pygame
from .Control_Movimiento import *
from .Mensaje import *
from .Marcador import *

class Snake(object):

    def __init__(self):
        self.ventana=None
        self.velocidad=5
        self.marcador= Marcador()

    def iniciarJuego(self):
        pygame.init()
        mensaje = Mensaje()
        self.ventana = Ventana()
        mapa = self.ventana.obtenerMapa()
        malware = mapa.obtenerMalware()
        pantalla = self.ventana.cargarPantalla()#pygame

        def redibujarComponentes():
            malware.dibujar(pantalla)
            mapa.dibujarMapa(pantalla)
            self.marcador.dibujar(pantalla)

        limiteVentanaX = self.ventana.obtenerLimites()[0]
        limiteVentanaY = self.ventana.obtenerLimites()[1]
        clock= pygame.time.Clock()
        bandera = True

        mensaje.estadoMensaje((True,False,False,False,False))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        Control_Movimiento.esperarTeclaEnter()

        mensaje.estadoMensaje((False,False,False,False,True))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        Control_Movimiento.esperarTeclaSpace()

        mensaje.estadoMensaje((False,False,False,True,False))
        mensaje.dibujar(pantalla)
        pygame.display.update()
        Control_Movimiento.esperarTeclaEnter()

        while bandera and self.marcador.obtenerVidas()>=0:
            clock.tick(self.velocidad)
            run = [False,False,False,False]
            while not run[1] and not run[3]:
                clock.tick(self.velocidad)
                for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pathAbsolutoScript = os.path.dirname(file)
                            pathAbsoluto = os.path.join(pathAbsolutoScript,"../assets/puntos.dat" )
                            with open (pathAbsoluto) as f: 
                                for lines in f:
                                    dato = int(lines.strip())
                            dato += self.marcador.puntuacion
                            print (dato)
                            arch = open(pathAbsoluto,'w')
                            arch.write(str(dato))
                            arch.close()
                            exit()
                mapa.cabeza.mover(limiteVentanaX,limiteVentanaY)
                mapa.cabeza2.mover(limiteVentanaX,limiteVentanaY)

                run = mapa.verificarElementosMapa(self.ventana.obtenerLimites(),malware.obtenerPosicion())

                if run[0] or run[2]:
                    self.marcador.calcularPuntuacion(malware.obtenerValor())
                    malware = mapa.obtenerMalware()
                    self.ventana.dibujarFondo(pantalla)
                    redibujarComponentes()
                    if run[0]:
                        mapa.cola.agregarSegmento(mapa.cabeza.obtenerPosicion())
                        mapa.cola2.mover(mapa.cabeza2.obtenerPosicion())
                    elif run[2]:
                        mapa.cola2.agregarSegmento(mapa.cabeza2.obtenerPosicion())
                        mapa.cola.mover(mapa.cabeza.obtenerPosicion())
                elif not (run[1] or run [3]):
                    self.ventana.dibujarFondo(pantalla)
                    redibujarComponentes()
                    mapa.cola.mover(mapa.cabeza.obtenerPosicion())
                    mapa.cola2.mover(mapa.cabeza2.obtenerPosicion())
                pygame.display.update()
            self.marcador.quitarVida()
            if run[1]:
                mapa.cabeza.retornarPosicion(limiteVentanaX,limiteVentanaY)
            elif run[3]:
                mapa.cabeza2.retornarPosicion(limiteVentanaX,limiteVentanaY)

            #mostrar el mensaje
            if self.marcador.obtenerVidas()>=0:
                mensaje.estadoMensaje((False,True,False,False,False))
            else:
                mensaje.estadoMensaje((False,False,True,False,False))
            self.ventana.dibujarFondo(pantalla)
            redibujarComponentes()
            mensaje.dibujar(pantalla)
            pygame.display.update()
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pathAbsolutoScript = os.path.dirname(file)
                        pathAbsoluto = os.path.join(pathAbsolutoScript,"../assets/puntos.dat" )
                        with open (pathAbsoluto) as f: 
                            for lines in f:
                                dato = int(lines.strip())
                        dato += self.marcador.puntuacion
                        print (dato)
                        arch = open(pathAbsoluto,'w')
                        arch.write(str(dato))
                        arch.close()
                        exit()
                keys = Control_Movimiento.detectarMovimiento()
                if keys[pygame.K_ESCAPE]:
                    bandera=False
                    break
                elif keys[pygame.K_SPACE] and self.marcador.obtenerVidas()>=0:
                    break
                elif keys[pygame.K_RETURN] and self.marcador.obtenerVidas()<0:
                    self.reiniciar(mapa.cola,mapa.cola2,self.marcador)
                    break

            mapa.cabeza.cambiarPosicion(0,-64)
            mapa.cabeza2.cambiarPosicion(704,512)
            for segmento in mapa.cola.obtenerCola():
                segmento.cambiarPosicion((-128,-128))
            for segmento in mapa.cola2.obtenerCola():
                segmento.cambiarPosicion((-128,-128))
            self.ventana.dibujarFondo(pantalla)
            redibujarComponentes()
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

