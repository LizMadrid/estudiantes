from PyQt6 import QtWidgets, uic
import sys
from controllers.login_controller import LoginController
from controllers.registro_controller import RegistroController
from controllers.lista_controller import ListaController
from controllers.reporte_controller import ReporteController
from PyQt6.QtCore import pyqtSignal

class Login(QtWidgets.QMainWindow):
    open_registro = pyqtSignal()
    open_lista = pyqtSignal()
    open_reporte = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi("login.ui", self)
        self.controller = LoginController(self)

class Reporte(QtWidgets.QMainWindow):
    volver_menu = pyqt6Signal()

    def __init__(self):
        super().__init__()
        uic.loadUi("reporte.ui", self)
        self.controller = ReporteController(self)

class AppManager:
    def __init__(self):
        self.login = Login()
        self.lista = Lista()
        self.registro = Registro()
        self.reporte = Reporte()

        self.menu.open_lista.connect(self.show_lista)
        self.menu.open_registro.connect(self.show_registro)
        self.menu.open_reporte.connect(self.show_reporte)

        self.lista.volver_menu.connect(self.show_menu)
        self.registro.volver_menu.connect(self.show_menu)
        self.reporte.volver_menu.connect(self.show_menu)

        self.menu.show()

    def show_reporte(self):
        self.reporte.show()
        self.menu.close()

app = QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())