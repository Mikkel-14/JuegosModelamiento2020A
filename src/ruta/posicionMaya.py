#=============================================================================================
#                               JUEGO RUTA MAYA - Version 0.9
#                                       Clase Posición
# Implementado por: Alejandro Llanganate, Anderson Cárdenas, Henrry Cordovillo y David Moreno
#=============================================================================================


class Posicion:
    def __init__(self, tupla): # la tupla es una coordenada (x, y)
        self.x, self.y = tupla[0], tupla[1]

    def actualizarX(self, nuevoX):
        self.x = nuevoX

    def actualizarY(self, nuevoY):
        self.y = nuevoY

    def obtenerCoordenadas(self):
        return self.x, self.y # devuelve una tupla (x, y)