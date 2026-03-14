import sys
from PyQt6.QtWidgets import QApplication
from menu import Menu

app = QApplication(sys.argv)

ventana = Menu()
ventana.show()

sys.exit(app.exec())