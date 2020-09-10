from laberinto.cuadrosLaberinto import *

class SolapamientoLaberinto:

    def __init__(self, tablero):
        self.tablero = tablero
        self.listaObservadores = list()

    def verificar(self, personaje, posiblePos):
        permiso = False
        virus = False
        enemigo = False
        meta = False
        perdida = False
        corazon = -1
        listaCuadros = self.tablero.listaCuadros
        for cuadro in listaCuadros:
            (cuadroX, cuadroY) = (cuadro.posicion.x, cuadro.posicion.y)
            if (cuadroX, cuadroY) == posiblePos:
                if isinstance(cuadro, CaminoLaberinto):
                    permiso = True
                if isinstance(personaje, PersonajeLaberinto):
                    if isinstance(cuadro, VirusLaberinto):
                        corazon = personaje.numeroVidas
                        if corazon == 1:
                            perdida = True
                        virus = True
                    if isinstance(cuadro, EnemigoLaberinto):
                        corazon = personaje.numeroVidas
                        if corazon == 1:
                            perdida = True
                        enemigo = True
                        break
                    if isinstance(cuadro, MetaLaberinto):
                        meta = True
                        break
                elif isinstance(personaje, EnemigoLaberinto):
                    if isinstance(cuadro, PersonajeLaberinto):
                        corazon = cuadro.numeroVidas
                        if corazon == 1:
                            perdida = True
                        enemigo = True
                        permiso = False
                        break
        self.notificar(virus, enemigo, meta, perdida, corazon)
        return permiso

    def notificar(self, virus, enemigo, meta, perdida, corazon):
        for observador in self.listaObservadores:
            observador.actualizar(virus, enemigo, meta, perdida, corazon)

    def registrarObservador(self, observador):
        self.listaObservadores.append(observador)
