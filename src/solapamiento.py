class Solapamiento:

    def __init__(self, mapaMuseo):
        self.mapa = mapaMuseo

    def verificar(self, posiblePos):
        dict = self.mapa.accederLista()
        for piso in dict['camino']:
            if piso.posicion.getPosicion() == posiblePos:
                return True
        return False
