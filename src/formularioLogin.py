from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
from PyQt5.uic import loadUi

from herramientas import *
import sys


class FormularioLogIn(QMainWindow):
    def __init__(self,cf):
        super(FormularioLogIn, self).__init__()
        loadUi(obtenerPathAbsoluto("formularioLoginUI.ui"), self)
        self.labelUsuarioIncorrecto.hide()
        self.botonIngresar.clicked.connect(self.onClickIniciarSesion)
        self.botonAbrirFormRegistrar.clicked.connect(self.onClickNuevoUsuario)
        self.controlador = cf

    def mostrar(self):
        self.setWindowTitle("PoliJuego - LogIn")
        self.setGeometry(40, 40, 657, 446)
        self.show()

    def actualizar(self, mensaje):
        self.textoUsuario.setText('')
        self.textoPassword.setText('')
        self.labelUsuarioIncorrecto.setText(mensaje)
        self.labelUsuarioIncorrecto.show()

    def onClickIniciarSesion(self):
        self.controlador.validar((self.textoUsuario.text(), self.textoPassword.text()),self)

    def onClickNuevoUsuario(self):
        self.controlador.actualizarVista(self)
