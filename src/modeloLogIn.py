from herramientas import * 
import csv
from app import *

class ModeloLogIn():

    _archivoUsuarios = obtenerPathAbsoluto('dataUsuarios.csv')

    def __init__(self):
        self.app = App()       


    def registrarUsuario(self, nombreUsuario, password):
        found = False
        with open(self._archivoUsuarios, 'r') as f:
            filas = csv.reader(f)
            for usuario in filas:
                try:
                    if nombreUsuario == usuario[0]:
                        found = True
                        break
                except Exceptiorn:
                    continue
        if not found:
            with open(self._archivoUsuarios, 'a', newline='') as f:
                writer = csv.writer(f, delimiter = ',', dialect = 'excel')
                writer.writerow([nombreUsuario, password])
            return True
        else:
            return False

    def autenticarUsuario(self, nombreUsuario, password):
        found = False 
        with open(self._archivoUsuarios, 'r') as f:
            filas = csv.reader(f)
            for usuario in filas:
                try:
                    if nombreUsuario == usuario[0] and password == usuario[1]:
                        found = True
                        return found
                        break
                except Exception:
                    continue
        return found
    
    def lanzarAplicacion(self, nombreUsuario):
        self.app.main(nombreUsuario)

"""
cesar,444
jose,111
alex,222
alejandro,444
"""