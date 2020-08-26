class SolapamientoLaberinto:

    def __init__(self, tablero):
        self.tablero = tablero

    def verificar(self, posiblePos):
        caminoB = False
        virusB = False
        metaB = False
        dict = self.tablero.dictCuadros
        for piso in dict['camino']:
            (x, y) = (piso.posicion.x, piso.posicion.y)
            if (x, y) == posiblePos:
                caminoB = True
        for virus in dict['virus']:
            (x, y) = (virus.posicion.x, virus.posicion.y)
            if (x, y) == posiblePos:
                dict['personaje'].numeroVidas -= 1
                corazon = dict['personaje'].numeroVidas
                dict['vidas'][corazon].booleano = 0
                if dict['personaje'].numeroVidas == 0:
                    for mensaje in dict['mensaje']:
                        if mensaje.getNombre() == 'perdida':
                            mensaje.permitirDibujo(True)
                virusB = True
        (a, b) = (dict['meta'].posicion.x, dict['meta'].posicion.y)
        if (a, b) == posiblePos:
            for mensaje in dict['mensaje']:
                if mensaje.getNombre() == 'victoria':
                    mensaje.permitirDibujo(True)
            metaB = True
        return caminoB or virusB or metaB
