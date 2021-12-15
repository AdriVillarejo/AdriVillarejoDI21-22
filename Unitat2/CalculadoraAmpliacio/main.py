import sys
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QPushButton, QToolBar,

)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalculadoraDI")

        toolbar = QToolBar("ToolBar")
        toolbar.setIconSize(QSize(16, 16))

        calc_cient = QAction("&Cientifica", self)
        calc_cient.triggered.connect(self.cientifica)

        toolbar.addSeparator()

        calc_normal = QAction("&Normal", self)
        calc_normal.triggered.connect(self.normal)

        boton_salir = QAction("&Salir", self)
        boton_salir.triggered.connect(self.salir)
        boton_salir.setShortcut(QKeySequence("Ctrl+s"))

        operacions =  QAction("&Guardar", self)
        operacions.triggered.connect(self.guardados)
        operacions.setCheckable(True)

        menu = self.menuBar()
        file_menu = menu.addMenu("&File")


        file_submenu = file_menu.addMenu("Modos")
        file_submenu.addAction(calc_cient)
        file_submenu.addAction(calc_normal)

        file_menu.addAction(operacions)
        file_menu.addSeparator()
        file_menu.addAction(boton_salir)

        self.widget = QWidget()
        self.layout_general = QVBoxLayout(self.widget)
        self.setCentralWidget(self.widget)

        # Cremos la ventana con el QLineEdit y ponemos que solo pueda s er leida y no modificada
        self.ventana = QLineEdit()
        self.ventana.setReadOnly(True)
        self.layout_general.addWidget(self.ventana)

        # String para guardar los botones que hemos pulsado
        self.botones_guardados = ""

        # Array para guardar los botones
        self.letras = {}

        # Layout para los botones de la calculadora
        layout_letras = QGridLayout()

        letras_calculadora = {
            'C': (0, 0), '%': (0, 1), '<-': (0, 2), '/': (0, 3), '(': (0, 5),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), 'X': (1, 3), ')': (1, 5),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '00': (4, 0), '0': (4, 1), ',': (4, 2), '=': (4, 3),

        }

        # Creamos los botones
        for button, posicion in letras_calculadora.items():
            self.letras[button] = QPushButton(button)
            self.letras[button].setFixedSize(45, 25)
            self.letras[button].setShortcut(button)
            layout_letras.addWidget(self.letras[button],
                                    posicion[0], posicion[1])
            self.letras[button].clicked.connect(self.operacion)


        # Añadimos el layout
        self.layout_general.addLayout(layout_letras)
        self.letras['='].clicked.connect(self.resultado)



    # Falta la parte de los parentesis pero no sabía como hacerla
    # Definimos una funcion para que haga la operación correspondiente al botón
    def operacion(self):
        if self.sender().text() == "<-":
            self.display_text(self.botones_guardados[:-1])
            self.botones_guardados = self.botones_guardados[:-1]
        elif self.sender().text() == "C":
            self.clear_display()
        elif self.sender().text() == "X":
            self.botones_guardados += "*"
            self.display_text(self.botones_guardados)
        elif self.sender().text() == "=":
            pass
        else:
            self.botones_guardados += self.sender().text()
            self.display_text(self.botones_guardados)

    # Actualiza el string
    def display_text(self, text):
        self.ventana.setText(text)
        self.ventana.setFocus()

    # Borra el string
    def clear_display(self):
        self.display_text("")
        self.guardados = ""

    # Calcula la operación y devuelve el resultado
    def resultado(self):
        self.display_text(str(eval(self.botones_guardados)))

    def cientifica(self):
        print("Calculadora Cientifica")

    def normal(self):
        MainWindow()

    def guardados(self):
        print("Guardados ")

    def salir(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
