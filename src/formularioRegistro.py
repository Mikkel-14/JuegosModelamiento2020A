from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.uic import loadUi
from herramientas import *
import sys

class FormularioRegistro(QMainWindow):
    def __init__(self,cf):
        super(FormularioRegistro, self).__init__()
        loadUi(obtenerPathAbsoluto("formularioRegistroUI.ui"), self) # transforma XML en término de clase en Py
        self.botonRegistrar.clicked.connect(self.onClickRegistrar) # asociamos la accion de click en un boton con una función
        self.botonVolver.clicked.connect(self.onClickRegresar)
        self.labelIncorrecto.hide()
        self.controlador = cf

    def mostrar(self):
        self.setWindowTitle("PoliJuego - Registro")
        self.setGeometry(40, 40, 698, 540) # dos primeros numeros son la posición y los otros son el tamaño de la ventana
        self.show()

    def onClickRegistrar(self):
        self.controlador.validar((self.textoUsuario.text(), self.textoPassword.text(), self.textoPasswordReiteracion.text()), self)

    def onClickRegresar(self):
        self.controlador.actualizarVista(self)

    def actualizar(self, mensaje):
        self.textoUsuario.setText('')
        self.textoPassword.setText('')
        self.textoPasswordReiteracion.setText('')
        self.labelIncorrecto.setText(mensaje)
        self.labelIncorrecto.show()
