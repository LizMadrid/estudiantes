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

class Lista(QtWidgets.QMainWindow):
    volver_menu = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("lista.ui",self)
        self.controller = ListaController(self)

class Registro(QtWidgets.QMainWindow):
    volver_menu = pyqtSignal()
    def __init__(self):
        super().__init__()
        uic.loadUi("registro.ui",self)
        self.controller = RegistroController(self)
                    

class Reporte(QtWidgets.QMainWindow):
    volver_menu = pyqtSignal()

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

        self.login.open_lista.connect(self.show_lista)
        self.login.open_registro.connect(self.show_registro)
        self.login.open_reporte.connect(self.show_reporte)

        self.lista.volver_menu.connect(self.show_menu)
        self.registro.volver_menu.connect(self.show_menu)
        self.reporte.volver_menu.connect(self.show_menu)

        self.login.show()

    def show_lista(self):
        self.lista.show()
        self.login.close() 

    def show_registro(self):
        self.registro.show()
        self.login.close()   

    def show_reporte(self):
        self.reporte.show()
        self.login.close()  

    def show_menu(self):
        self.login.show()
        self.lista.close() 
        self.registro.close() 
        self.reporte.close() 


app = QtWidgets.QApplication(sys.argv)
manager = AppManager()
sys.exit(app.exec())
