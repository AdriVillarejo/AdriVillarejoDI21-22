import sys
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QLineEdit, QMainWindow, QVBoxLayout, QWidget, QGridLayout, QPushButton, QStackedLayout,

)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CalculadoraDI")

        # Creamos los botones asignadoles el nombre que queramos
        calc_cient = QAction("&Cientifica", self)
        calc_cient.triggered.connect(self.cientifica)

        calc_normal = QAction("&Normal", self)
        calc_normal.triggered.connect(self.normal)

        boton_salir = QAction("&Salir", self)
        boton_salir.triggered.connect(self.salir)
        boton_salir.setShortcut(QKeySequence("Ctrl+s"))

        operacions = QAction("&Guardar", self)
        operacions.triggered.connect(self.guardados)
        operacions.setCheckable(True)

        menu = self.menuBar()
        file_menu = menu.addMenu("&Menu")

        file_submenu = file_menu.addMenu("Modos")
        file_submenu.addAction(calc_cient)
        file_submenu.addAction(calc_normal)

        file_menu.addAction(operacions)
        file_menu.addSeparator()
        file_menu.addAction(boton_salir)

        self.widget = QWidget()
        self.setCentralWidget(self.widget)

        # Creamos el stacked layout para cambiar entre la calculadora cientifica y la normal 
        self.stackedLayout = QStackedLayout(self.widget)

        # Añadimos el modo cientifico a un layout y un widget
        self.modo_cientifico = QWidget()
        self.layout_modocientifico = QVBoxLayout(self.modo_cientifico)
        self.modo_cientifico.setLayout(self.layout_modocientifico)
        
        # Añadimos el modo normal a un layout y un widget
        self.modo_normal = QWidget()
        self.layout_modonormal = QVBoxLayout(self.modo_normal)
        self.modo_normal.setLayout(self.layout_modonormal)

        # Añadimos los dos widgets al stacked layout
        self.stackedLayout.addWidget(self.modo_normal)
        self.stackedLayout.addWidget(self.modo_cientifico)

        # Cremos la ventana normal con el QLineEdit y ponemos que solo pueda ser leida y no modificada
        self.ventana_normal = QLineEdit()
        self.ventana_normal.setReadOnly(True)
        self.layout_modonormal.addWidget(self.ventana_normal)

        self.ventana_cientifica = QLineEdit()
        self.ventana_cientifica.setReadOnly(True)
        self.layout_modocientifico.addWidget(self.ventana_cientifica)

        # String para guardar los botones que hemos pulsado
        self.botones_guardados = ""

        # Array para guardar los botones
        self.letras = {}

        self.letras_cien = {}

        # Layout para los botones de la calculadora
        layout_letras = QGridLayout()
        layout_letrascien = QGridLayout()

        letras_calculadora = {
            'C': (0, 0), '%': (0, 1), '<-': (0, 2), '/': (0, 3), '(': (0, 5),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), 'X': (1, 3), ')': (1, 5),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3),
            '00': (4, 0), '0': (4, 1), ',': (4, 2), '=': (4, 3),
        }

        letras_calculadoracientifica = {
            'C': (0, 0), '%': (0, 1), '<-': (0, 2), '/': (0, 3), '(': (0, 5),
            '7': (1, 0), '8': (1, 1), '9': (1, 2), 'X': (1, 3), ')': (1, 5),
            '4': (2, 0), '5': (2, 1), '6': (2, 2), '-': (2, 3), 'mod': (2, 5),
            '1': (3, 0), '2': (3, 1), '3': (3, 2), '+': (3, 3), 'exp': (3, 5),
            '00': (4, 0), '0': (4, 1), ',': (4, 2), '=': (4, 3), 'n!': (4, 5),
            'log': (5, 0), 'ln': (5, 1), '+/-': (5, 2), '10x': (5, 3), '|x|': (5, 5),
        }

        # Creamos los botones de la calculadora normal
        for button, posicion in letras_calculadora.items():
            self.letras[button] = QPushButton(button)
            self.letras[button].setFixedSize(45, 25)
            self.letras[button].setShortcut(button)
            layout_letras.addWidget(self.letras[button],
                                    posicion[0], posicion[1])
            self.letras[button].clicked.connect(self.operacion)

        # Creamos los botones de la calculadora cientifica
        for button_cien, posicion_cien in letras_calculadoracientifica.items():
            self.letras_cien[button_cien] = QPushButton(button_cien)
            self.letras_cien[button_cien].setFixedSize(45, 25)
            self.letras_cien[button_cien].setShortcut(button_cien)
            layout_letrascien.addWidget(self.letras_cien[button_cien],
                    posicion_cien[0], posicion_cien[1])
            self.letras_cien[button_cien].clicked.connect(
                self.operacion)

        # Añadimos el layout de la normal
        self.layout_modonormal.addLayout(layout_letras)
        self.letras['='].clicked.connect(self.resultado)

        # Añadimos el layout de la cientifica 
        self.layout_modocientifico.addLayout(layout_letrascien)
        self.letras_cien['='].clicked.connect(self.resultado)

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
        self.ventana_normal.setText(text)
        self.ventana_normal.setFocus()
        self.ventana_cientifica.setText(text)
        self.ventana_normal.setFocus()

    # Borra el string
    def clear_display(self):
        self.display_text("")
        self.guardados = ""

    # Calcula la operación y devuelve el resultado
    def resultado(self):
        self.display_text(str(eval(self.botones_guardados)))

    def cientifica(self):
        self.stackedLayout.setCurrentWidget(self.modo_cientifico)

    def normal(self):
        self.stackedLayout.setCurrentWidget(self.modo_normal)

    def guardados(self):
        print("Guardando")

    def salir(self):
        sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())