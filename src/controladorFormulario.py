import re
from formularioLogin import *
from formularioRegistro import *
from PyQt5.QtWidgets import QMessageBox

class ControladorFormulario:
    def __init__(self, modeloLogin):
        self.patronValidacionAlfanumerico = re.compile("[A-Za-z]+[0-9]*")
        self.formularioLogIn = FormularioLogIn(self)
        self.formularioReg = FormularioRegistro(self)
        self.formularioLogIn.mostrar()
        self.modelo = modeloLogin

    def validar(self, datos, form):
        valor = self.patronValidacionAlfanumerico.match(datos[0])
        if not valor == None:
            if isinstance(form, FormularioLogIn):
                if self.modelo.autenticarUsuario(datos[0], datos[1]):
                    self.formularioLogIn.close()
                    self.modelo.lanzarAplicacion(datos[0])
                else:
                    self.formularioLogIn.actualizar("Usuario o contraseña inválidos")
            elif isinstance(form, FormularioRegistro):
                if datos[1] == datos[2]:
                    if self.modelo.registrarUsuario(datos[0], datos[1]):
                        self.formularioReg.hide()
                        self.formularioLogIn.mostrar()
                        msg = QMessageBox()
                        msg.setWindowTitle('Registro')
                        msg.setText('Registro Exitoso')
                        msg.setIcon(QMessageBox.Information)
                        msg.exec_()
                    else:
                        self.formularioReg.actualizar("El usuario ya se encuentra registrado")
                else:
                    self.formularioReg.actualizar("Las contraseñas no coinciden")
        else:
            if isinstance(form, FormularioLogIn):
                self.formularioLogIn.actualizar("Usuario o contraseña inválidos")
            else:
                self.formularioReg.actualizar("Usuario o contraseña inválidos")

    def actualizarVista(self, form):
        if isinstance(form, FormularioLogIn):
            self.formularioLogIn.hide()
            self.formularioReg.mostrar()
        elif isinstance(form, FormularioRegistro):
            self.formularioReg.hide()
            self.formularioLogIn.show()