from Segmento_Cuerpo2 import Segmento_Cuerpo2
from ICola import ICola


class Cola2(ICola):
    def __init__(self):
        self.cola = []

    def agregarSegmento(self,pos):
        segmento = Segmento_Cuerpo2(pos[0],pos[1])
        self.cola.insert(0,segmento)

    def dibujar(self,ventana):
        for segmento in self.cola:
            segmento.dibujar(ventana)

    def mover(self,pos):
        self.agregarSegmento(pos)
        self.quitarUltimo()

 #Se le pasa la posición de la cabeza para que así el priemr segmento tome este.
    def quitarUltimo(self):
        self.cola.pop()

    def obtenerCola(self):
        return self.cola