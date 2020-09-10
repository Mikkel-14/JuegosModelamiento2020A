import tkinter as tk

root = tk.Tk()

# Para obtener el tamaño real del screen de su PC
anchoScreenPC, altoScreenPC  = root.winfo_screenwidth(), root.winfo_screenheight()

tamañoVentana = ancho, alto = int(anchoScreenPC*0.65), int(altoScreenPC*0.7) 

# tamaño de los elementos visuales del juego
tamañoCamino = int(ancho*0.5), alto
tamañoPersonaje = int(ancho*0.11), int(alto*0.18)
tamañoBoton = int(ancho*0.13), int(alto*0.1)
tamañoFigPregunta = int(ancho*0.5), int(alto*0.45)
tamañoFigVida = int(ancho*0.18), int(alto*0.07)
tamañoOpcion = int(ancho*0.1), int(alto*0.15)
tamañoMarcador = int(ancho*0.18), int(alto*0.07)
tamañoObstaculo = int(ancho*0.1), int(alto*0.14)
tamañoLetraPuntaje = int(alto*0.025)

#Coordenadas de Posicion de Botones GUI
coordenadaBotonJugar = (ancho*0.7, alto*0.75)
coordenadaBotonAtras = (ancho*0.17), (alto*0.75)
coordenadaBotonOk = (ancho*0.45, alto*0.85)

#Coordenadas de Posicion de los otros elementos
coordenadaCamino = (ancho*0.25,0)
coordenadaFondo = (0,0)
coordenadaPersonaje = (129*4, 100)
coordenadaFigVida = ( ancho*0.035, alto*0.08)
coordenadaFigPregunta = (ancho*0.55, alto*0.08)
coordenadaMarcador = ( ancho*0.79, alto*0.08)
coordenadaOpcion = [( ancho*0.3, alto*0.82), (ancho*0.45, alto*0.82), (ancho*0.6, alto*0.82)]
coordenadaObstaculo = (ancho*0.35, alto*0.5)

#limite obstaculos en el camino
limiteMinObstaculoX = ancho*0.32
limiteMaxObstaculoX = ancho*0.62

#para definir cuanto se desplazará el camino de manera de escala (en figuras.py, clase Mapa)
factorDesplazamiento = int(11*(ancho/1164))

settings = {
    "tamañoVentana": tamañoVentana,
    "tamañoCamino": tamañoCamino,
    "tamañoBoton": tamañoBoton,
    "tamañoPersonaje": tamañoPersonaje,
    "tamañoFigPregunta": tamañoFigPregunta,
    "tamañoFigVida": tamañoFigVida,
    "tamañoOpcion": tamañoOpcion,
    "tamañoMarcador": tamañoMarcador,
    "tamañoObstaculo": tamañoObstaculo,
    "tamañoLetraPuntaje": tamañoLetraPuntaje,
    "coordenadaFondo": coordenadaFondo,
    "coordenadaCamino": coordenadaCamino,
    "coordenadaPersonaje": coordenadaPersonaje,
    "coordenadaFigPregunta": coordenadaFigPregunta,
    "coordenadaOpcion": coordenadaOpcion,
    "coordenadaFigVida": coordenadaFigVida,
    "coordenadaMarcador": coordenadaMarcador,
    "coordenadaBotonJugar": coordenadaBotonJugar,
    "coordenadaBotonAtras": coordenadaBotonAtras,
    "coordenadaBotonOk": coordenadaBotonOk,
    "coordenadaObstaculo": coordenadaObstaculo,
    "factorDesplazamiento": factorDesplazamiento,
    "limiteMinObstaculoX": limiteMinObstaculoX,
    "limiteMaxObstaculoX": limiteMaxObstaculoX,
    "nombre": "Juego Ruta Maya",
    "icon": ""
}
