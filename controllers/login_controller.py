class LoginController:
    def __init__(self, window):
        self.window = window

        self.window.btn_registrar.clicked.connect(self.abrir_registro)
        self.window.btn_lista.clicked.connect(self.abrir_lista)
        self.window.btn_reporte.clicked.connect(self.abrir_reporte)
        self.window.btn_salir.clicked.connect(self.salir)

    def abrir_registro(self):
        self.window.open_registro.emit()

    def abrir_lista(self):
        self.window.open_lista.emit()

    def abrir_reporte(self):
        self.window.open_reporte.emit()

    def salir(self):
        self.window.close()