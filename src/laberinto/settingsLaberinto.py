def init():
    global dim_Cuadro
    global columnas
    global filas
    global FPS
    global velocidad
    global maximo_de_vidas
    global posInicial_Personaje
    global posInicial_Enemigo
    global posMeta
    global puntosTOTALES
    puntosTOTALES = 100
    dim_Cuadro = 34
    columnas = 21
    filas = 14
    FPS = 60
    velocidad = 34
    maximo_de_vidas = 4
    posInicial_Personaje = (0, 0)
    posInicial_Enemigo = (20 * dim_Cuadro, 1 * dim_Cuadro)
    posMeta = (20 * dim_Cuadro, 12 * dim_Cuadro)
