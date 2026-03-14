from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow
from registro import Registro

class Menu(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("menu.uic",self)

        self.btn_registrar.clicked.connect(self.abrir_registro)
        self.btn_ver.clicked.connect(self.abrir_lista)
        self.btn_reporte.clicked.connect(self.abrir_reporte)
        self.btn_salir.clicked.connect(self.close)

    def abrir_registro(self):
        self.ventana = Registro()
        self.ventana.show()
        self.close()