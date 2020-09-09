from herramientas import *
from cuadros import *
class Solapamiento:

    def __init__(self, mapaMuseo):
        self.mapa = mapaMuseo

    def verificar(self, posiblePos):
        verificador = False
        for cuadro in self.mapa.listaCuadros:
            if isinstance(cuadro, Camino):
                tupla = cuadro.obtenerPosicion()
                if tupla == posiblePos:
                    verificador = True
            if isinstance(cuadro, Estacion):
                tupla = cuadro.obtenerPosicion()
                if tupla == posiblePos:
                    verificador = True
                    for mensaje in self.mapa.listaCuadros:
                        if isinstance(mensaje, Mensaje):
                            if mensaje.getNombre() == cuadro.getNombre():
                                mensaje.permitirDibujo(True)
                                try:
                                    ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"r")
                                    puntuacion = ppNiña.readline().split(",")[2]
                                    ppNiña.close()
                                    ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"w")
                                    ppNiña.write(str(posiblePos[0]) + "," + str(posiblePos[1]) + "," + str(puntuacion))
                                    ppNiña.close()
                                except IOError:
                                    print("Error al manejar el archivo")
        return verificador
