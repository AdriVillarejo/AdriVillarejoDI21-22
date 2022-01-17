
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QPushButton, QWidget, QVBoxLayout)

import PySide6.QtWidgets as qtw

import sys


class LoginAdmin(QWidget):
    def __init__(self, usuario):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("Has iniciado sesion con " + usuario)
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.boton = QPushButton("Cerrar Sesion")
        self.boton.setEnabled(True)
        layout.addWidget(self.boton)
        self.boton.clicked.connect(self.cerrarSesion)

        
    def cerrarSesion(self):
        self.close()
        

        
''' 

class LoginUser(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        self.label = QLabel("Has iniciado sesion con Usuario")
        layout.addWidget(self.label)
        self.setLayout(layout)

        self.boton = QPushButton("Cerrar Sesion")
        self.boton.setEnabled(True)
        layout.addWidget(self.boton)
        self.boton.clicked.connect(self.cerrarSesion)

        
    def cerrarSesion(self):
        self.hide()
        self.c = MainWindow()
        self.c.show()

'''

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # creamos un layout en formulario
        formulario = qtw.QFormLayout()
        self.f_usuario = qtw.QLineEdit(self)
        self.f_contraseña = qtw.QLineEdit(self)

        # Creamos los botones para el login
        self.button = qtw.QPushButton("Login")

        # Añadimos los valores a cada fila
        formulario.addRow("Usuario", self.f_usuario)
        formulario.addRow("Contraseña", self.f_contraseña)
        formulario.addRow(self.button)

        widget = QWidget()
        widget.setLayout(formulario)
        self.setCentralWidget(widget)

        self.button.clicked.connect(
            lambda checked: self.comprobar(self.f_usuario.text(),
            self.f_contraseña.text()
            )
        )

    def cerrar(self):
        app.closeAllWindows()


#Creamos una funcion para comprobar al usuario y a la contraseña
    def comprobar(self, usuario, contraseña):
        if (usuario == "admin" or usuario == "user" and contraseña == "1234" ):
            self.ventanaAdmin(usuario)
            self.hide()
            

    def ventanaAdmin(self, usuario ):
        self.v = LoginAdmin(usuario)
        self.v.show()

'''
    def ventanaUser(self, usuario):
        self.u = LoginUser(usuario)
        self.u.show()
'''

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    exit(app.exec_())