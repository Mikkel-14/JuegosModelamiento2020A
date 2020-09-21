import pygame
import json
import settings as s
from cuadros import *
from solapamiento import *
import os.path as path
from herramientas import *
from posicion import Posicion
from fachadaJuegos import *

class App:
    def main(self, usuario):
        self.usuario = usuario
        CAMINO_PATH = obtenerPathAbsoluto('assets/matrizCamino.txt')
        ESTACION_PATH = obtenerPathAbsoluto('assets/matrizEstacion.txt')
        FONDO_PATH = obtenerPathAbsoluto('img/fondo.png')
        PISO_PATH = obtenerPathAbsoluto('img/piso.png')
        ALFOMBRA_PATH = obtenerPathAbsoluto('img/alfombra.png')
        PERSONAJE_PATH = obtenerPathAbsoluto('img/personaje.png')
        MENSAJE_PATH = obtenerPathAbsoluto('assets/direccionesMensajes.txt')
        MARCADOR_PATH = obtenerPathAbsoluto('img/marcador.png')
        INSTRUCCIONES = True
        PUNTOS_PATH = obtenerPathAbsoluto('assets/puntos.dat')
        JSON_PATH = obtenerPathAbsoluto('data.json')
        s.init()
        ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"w")
        ppNiña.write("0,204,0")
        ppNiña.close()
        puntos = open(PUNTOS_PATH, 'w')
        puntos.write('0')
        puntos.close()
        fachada = FachadaJuegos()
        mk = Marcador(MARCADOR_PATH, Posicion(565, 0), PUNTOS_PATH, fachada)
        flag = True
        while flag:
            pygame.init()
            reloj = pygame.time.Clock()

            ven_dim = (s.columnas * s.dim_Cuadro, s.filas * s.dim_Cuadro)

            ven = pygame.display.set_mode(ven_dim)
            pygame.display.set_caption('Proyecto 2020A')
            mk.actualizarMarcador()
            mapa = MapaMuseo()
            mapa.agregarCuadros(Fondo(FONDO_PATH,Posicion(0,0)))
            mapa.agregarCuadros(mk)

            with open(CAMINO_PATH) as f:
                for line in f:
                    coords = line.strip().split(',')
                    x = int(coords[0]) * s.dim_Cuadro
                    y = int(coords[1]) * s.dim_Cuadro
                    posicion = Posicion(x, y)
                    mapa.agregarCuadros(Camino(PISO_PATH, posicion))

            with open(ESTACION_PATH) as f:
                for line in f:
                    coords = line.strip().split(',')
                    x = int(coords[0]) * s.dim_Cuadro
                    y = int(coords[1]) * s.dim_Cuadro
                    posicion = Posicion(x, y)
                    mapa.agregarCuadros(Estacion(ALFOMBRA_PATH, posicion, coords[2]))

            ppNiña = open(obtenerPathAbsoluto("assets/ppNiña.txt"),"r")
            listNiña = ppNiña.readline().split(",")
            ppNiña.close()
            mapa.agregarCuadros(Personaje(PERSONAJE_PATH, Posicion(int(listNiña[0]),int(listNiña[1]))))

            with open(MENSAJE_PATH) as f:
                for line in f:
                    textos = line.strip().split(',')
                    mapa.agregarCuadros(Mensaje(obtenerPathAbsoluto(textos[0]),textos[1],fachada, self.usuario))
            solapamiento = Solapamiento(mapa)

            for cuadro in mapa.listaCuadros:
                cuadro.dibujar(ven)
            pygame.display.update()

            while True:
                reloj.tick(s.FPS)
                try:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            flag = False
                            pygame.quit()
                except Exception:
                    break

                for m in mapa.listaCuadros:
                    if isinstance(m, Mensaje):
                        if m.getNombre() == 'inicio' and INSTRUCCIONES:
                            m.permitirDibujo(True)
                            m.dibujar(ven)
                            INSTRUCCIONES = False
                        if m.getAparecer():
                            msj = m
                try:
                    msj.esperar()
                    mk.dibujar(ven)
                    pygame.display.update()
                except:
                    break

                if not msj.getAparecer():
                    for cuadro in mapa.listaCuadros:
                        if isinstance(cuadro, Personaje):
                            cuadro.mover(s.velocidad, solapamiento)
                        cuadro.dibujar(ven)
        if not mk.getPuntaje() == 0:
            with open(JSON_PATH) as r:
                diccionario = json.load(r)
            #Verifica si el JSON no se encuentra vacio
            if not len(diccionario['usuarios']) == 0:
                bandera = True
                #busca en los subdiccionario si existe el usuario
                for l in diccionario['usuarios']:
                    if usuario in l.values():
                        l['puntuaciones'].insert(0,mk.getPuntaje())
                        bandera=False
                        break
                if bandera:#esto es en el caso que no encuentre el usuario
                    nuevoUsuario = {'nombre': usuario, 'puntuaciones': []}
                    nuevoUsuario['puntuaciones'].insert(0,mk.getPuntaje())
                    diccionario['usuarios'].append(nuevoUsuario)
            else:
                nuevoUsuario = {'nombre': usuario, 'puntuaciones': []}
                nuevoUsuario['puntuaciones'].insert(0,mk.getPuntaje())
                diccionario['usuarios'].append(nuevoUsuario)

            f = open(JSON_PATH, 'w')
            nuevo = json.dumps(diccionario,indent=1)
            f.write(nuevo)
            f.close()
        exit()
