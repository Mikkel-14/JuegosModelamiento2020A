from Segmento_Cuerpo import Segmento_Cuerpo
from Segmento_Cuerpo2 import Segmento_Cuerpo2
class Colision(object):
    def colisionarCabezaMalware(self,posCabeza,posMalware):
        if posCabeza==posMalware:
            return True
        else:
            return False

    def colisionarCabezaVentana(self,posCabeza,limiteVentanaX,limiteVentanaY):
        if posCabeza[0] < 0 or posCabeza[0]>limiteVentanaX-64 or posCabeza[1] < 0 or posCabeza[1]>limiteVentanaY-64:
            return True
        else:
            return False

    def colisionarCabezaSegmento(self,posCabeza,cola,cola2):
        run = False
        segmento : Segmento_Cuerpo
        for i in range (len(cola)):
            if cola[i].obtenerPosicion()==posCabeza:
                run=True
                break
        for i in range (len(cola2)):
            if cola2[i].obtenerPosicion()==posCabeza:
                run=True
                break
        return run

    def colisionarCabezaSegmento2(self,posCabeza,cola2,cola):
        run = False
        segmento : Segmento_Cuerpo2
        for i in range (len(cola2)):
            if cola2[i].obtenerPosicion()==posCabeza:
                run=True
                break
        for i in range (len(cola)):
            if cola[i].obtenerPosicion()==posCabeza:
                run=True
                break
        return run

    def colisionCabezaCabeza(self,posCabeza,posCabeza2):
        if posCabeza==posCabeza2:
            return True
        else:
            return False

    def verificarColision(self,cabeza,cabeza2,cola,cola2,limVentana,posMalware):
        run = [False,False,False,False]

        posCabeza = cabeza.obtenerPosicion()
        posCabeza2 = cabeza2.obtenerPosicion()

        cola = cola.obtenerCola()
        cola2 = cola2.obtenerCola()

        run[0] = self.colisionarCabezaMalware(posCabeza,posMalware)
        run[1] = self.colisionarCabezaVentana(posCabeza,limVentana[0],limVentana[1]) or self.colisionarCabezaSegmento(posCabeza,cola,cola2) or self.colisionCabezaCabeza(posCabeza,posCabeza2)

        run[2] = self.colisionarCabezaMalware(posCabeza2,posMalware)
        run[3] = self.colisionarCabezaVentana(posCabeza2,limVentana[0],limVentana[1]) or self.colisionarCabezaSegmento2(posCabeza2,cola2,cola) or self.colisionCabezaCabeza(posCabeza2,posCabeza)
        return run
