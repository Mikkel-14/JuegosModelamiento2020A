from controladorFormulario import *
from modeloLogIn import *
# Ejecutar desde aquí la aplicación
def main():
    app = QApplication(sys.argv) # necesario para cargar todos los componentes necesarios para ejecutar una ventana en pyqt5
    modelo = ModeloLogIn()
    controlador = ControladorFormulario(modelo)

    app.exec_()

if __name__ == "__main__":
    main()
