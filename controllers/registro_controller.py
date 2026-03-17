class RegistroController: 
    def __init__(self, window):
        self.window = window
        self.window.btn_volver.clicked.connect(self.volver)
    def volver(self):
        self.window.volver_menu.emit()    