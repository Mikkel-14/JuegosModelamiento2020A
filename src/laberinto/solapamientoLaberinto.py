class SolapamientoLaberinto:

    def __init__(self, tablero):
        self.tablero = tablero

    def verificar(self, posiblePos):
        camino = self.verificarCamino(posiblePos)
        virus = self.verificarVirus(posiblePos)
        meta = self.verificarMeta(posiblePos)
        return camino or virus or meta

    def verificarCamino(self, posiblePos):
        dict = self.tablero.accederLista()
        for piso in dict['camino']:
            if piso.obtenerPosicion() == posiblePos:
                return True
        return False

    def verificarVirus(self, posiblePos):
        dict = self.tablero.accederLista()
        for virus in dict['virus']:
            if virus.obtenerPosicion() == posiblePos:
                for mensaje in dict['mensaje']:
                    if mensaje.getNombre() == 'perdida':
                        mensaje.permitirDibujo(True)
                return True
        return False

    def verificarMeta(self, posiblePos):
        dict = self.tablero.accederLista()
        if dict['meta'].obtenerPosicion() == posiblePos:
            for mensaje in dict['mensaje']:
                if mensaje.getNombre() == 'victoria':
                    mensaje.permitirDibujo(True)
            return True
        return False