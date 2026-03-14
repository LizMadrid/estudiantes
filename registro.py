from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow

class Registro(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("registro.ui", self)

        self.btn_volverR.clicked.connect(self.volverR_menu)

    def volverR_menu(self):
        self.ventana = Menu()
        self.ventana.show()
        self.close()