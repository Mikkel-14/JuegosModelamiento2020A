import pygame
import laberinto.settingsLaberinto as s
from .cuadrosLaberinto import *
from .posicionLaberinto import *
from .solapamientoLaberinto import *
from .puntuacionLaberinto import *
from .herramientas import *
pygame.init()
s.init()

CAMINOLAB_PATH = obtenerPathAbsoluto('assets/CaminoLaberinto1.txt')
POSICION_VIRUS_PATH = obtenerPathAbsoluto('assets/VirusLaberinto1.txt')
FONDO_PATH = obtenerPathAbsoluto('img/Fondo_Laberinto.png')
PISO_PATH = obtenerPathAbsoluto('img/Piso_Laberinto.png')
VIRUS_PATH = obtenerPathAbsoluto('img/Virus.png')
META_PATH = obtenerPathAbsoluto('img/Meta.png')
PERSONAJE_PATH = obtenerPathAbsoluto('img/niña.png')
ENEMIGO_PATH = obtenerPathAbsoluto('img/enemigo.png')
MENSAJES_PATH = obtenerPathAbsoluto('assets/direccionesMensajesLaberinto.txt')
CORAZON_PATH = obtenerPathAbsoluto('img/vida1.png')
CORAZON_VACIO_PATH = obtenerPathAbsoluto('img/vida0.png')


class VentanaLaberinto:
    def __init__(self):
        self.dimensiones = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)
        self.titulo = "Laberinto"
        self.reloj = pygame.time.Clock()
        self.tablero = None
        self.solapamiento = None
        self.puntuacion = PuntuacionLaberinto()
        self.win = pygame.display.set_mode(self.dimensiones)
        pygame.display.set_caption(self.titulo)

    def cargarTablero(self):
        self.tablero = TableroLaberinto()
        self.solapamiento = SolapamientoLaberinto(self.tablero)
        
        self.tablero.agregarCuadros(FondoLaberinto(FONDO_PATH, PosicionLaberinto(0, 0)))

        with open(CAMINOLAB_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(CaminoLaberinto(PISO_PATH, posicion))

        with open(POSICION_VIRUS_PATH) as f:
            for line in f:
                coords = line.strip().split(',')
                x = int(coords[0]) * s.dim_Cuadro
                y = int(coords[1]) * s.dim_Cuadro
                posicion = PosicionLaberinto(x, y)
                self.tablero.agregarCuadros(VirusLaberinto(VIRUS_PATH, posicion))

        self.tablero.agregarCuadros(MetaLaberinto(META_PATH, PosicionLaberinto(s.posMeta[0], s.posMeta[1])))

        personaje = PersonajeLaberinto(PERSONAJE_PATH, PosicionLaberinto(s.posInicial_Personaje[0], s.posInicial_Personaje[1]))
        self.tablero.agregarCuadros(personaje)
        self.solapamiento.registrarObservador(personaje)

        enemigo = EnemigoLaberinto(ENEMIGO_PATH, PosicionLaberinto(s.posInicial_Enemigo[0], s.posInicial_Enemigo[1]))
        self.tablero.agregarCuadros(enemigo)
        self.solapamiento.registrarObservador(enemigo)

        for vida, numCorazon in zip(range(s.columnas - s.maximo_de_vidas, s.columnas), range(1, s.maximo_de_vidas + 1)):
            corazon = VidaLaberinto(CORAZON_VACIO_PATH, CORAZON_PATH, PosicionLaberinto(vida * s.dim_Cuadro, 0), numCorazon)
            self.tablero.agregarCuadros(corazon)
            self.solapamiento.registrarObservador(corazon)

        self.solapamiento.registrarObservador(self.puntuacion)

        with open(MENSAJES_PATH) as f:
            for line in f:
                textos = line.strip().split(',')
                mensaje = MensajeLaberinto(obtenerPathAbsoluto(textos[0]), textos[1])
                self.tablero.agregarCuadros(mensaje)
                self.solapamiento.registrarObservador(mensaje)

        for cuadro in self.tablero.listaCuadros:
            if isinstance(cuadro, MensajeLaberinto):
                if cuadro.getNombre() == 'instrucciones':
                    cuadro.permitirDibujo(True)
            cuadro.dibujar(self.win)
        pygame.display.update()

    def manejarMensajes(self, juego):
        lstMsj = self.tablero.listaCuadros
        for m in lstMsj:
            if isinstance(m, MensajeLaberinto):
                if m.getAparecer():
                    keys = ListenerLaberinto.detectar()
                    if m.getNombre().startswith('virus') and keys[pygame.K_SPACE]:
                        m.permitirDibujo(False)
                        return True
                    elif m.getNombre() == 'enemigo' and keys[pygame.K_SPACE]:
                        m.permitirDibujo(False)
                        return True
                    elif m.getNombre() == 'instrucciones' and keys[pygame.K_SPACE]:
                        m.permitirDibujo(False)
                        return True
                    elif m.getNombre() == 'victoria':
                        self.puntuacion.calcularPuntos()
                        pygame.font.init()
                        fuente = pygame.font.SysFont('Arial', 15)
                        texto_puntaje = fuente.render('Puntuación: {:}'.format(self.puntuacion.puntos), True, (0,0,0))
                        self.win.blit(texto_puntaje, (318, 160))
                        pygame.display.update()
                        if keys[pygame.K_ESCAPE]:
                            juego.salirJuego()
                            return True
                    elif m.getNombre() == 'perdida':
                        if keys[pygame.K_SPACE]:
                            juego.reiniciarJuego()
                            return True
                        elif keys[pygame.K_ESCAPE]:
                            juego.salirJuego()
                            return True
                    return False
        return True
