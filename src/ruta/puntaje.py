class Puntaje:

    _constanteMaximo = 1000

    def __init__(self,numeroFallos,puntos):
        self.numeroFallos = numeroFallos
        self.puntos = puntos

    def incrementar(self):
        self.puntos = self.puntos + int( self._constanteMaximo / self.numeroFallos )
    
    def getPuntos(self):
        return self.puntos