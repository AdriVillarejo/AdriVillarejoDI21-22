from PySide6 import QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QSize



class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        self.setFixedSize(QSize(300, 300))
        self.setWindowTitle("Exemple signals-slots 1")

        self.pybutton = QPushButton('Maximiza', self)
        self.pybutton2 = QPushButton("Minimiza" , self)
        self.pybutton3 = QPushButton("Normaliza" , self)

        # Connectem la senyal clicked a la ranura button_pressed
        self.pybutton.clicked.connect(self.max)
        self.pybutton2.clicked.connect(self.min)
        self.pybutton3.clicked.connect(self.normal)

        self.pybutton.resize(100, 50)
        self.pybutton2.resize(100, 50)
        self.pybutton3.resize(100, 50)

        self.pybutton.move(0, 115)
        self.pybutton2.move(100, 115)
        self.pybutton3.move(200, 115)

        self.pybutton.setEnabled(True)
        self.pybutton2.setEnabled(True)
        self.pybutton3.setEnabled(True)

    def max(self):
        self.setFixedSize(600,600)

        self.pybutton.resize(100, 100)
        self.pybutton2.resize(100, 100)
        self.pybutton3.resize(100, 100)

        self.pybutton.move(60, 210)
        self.pybutton2.move(250, 210)
        self.pybutton3.move(430, 210)

        self.pybutton.setEnabled(False)
        self.pybutton2.setEnabled(True)
        self.pybutton3.setEnabled(True)

    def min(self):
        self.setFixedSize(300,120)

        self.pybutton.resize(100, 120)
        self.pybutton2.resize(100, 120)
        self.pybutton3.resize(100, 120)

        self.pybutton.move(0, 0)
        self.pybutton2.move(100, 0)
        self.pybutton3.move(200, 0)

        self.pybutton.setEnabled(True)
        self.pybutton2.setEnabled(False)
        self.pybutton3.setEnabled(True)

    def normal(self):
        self.setFixedSize(300, 300)

        self.pybutton.resize(100, 50)
        self.pybutton2.resize(100, 50)
        self.pybutton3.resize(100, 50)

        self.pybutton.move(0, 115)
        self.pybutton2.move(100, 115)
        self.pybutton3.move(200, 115)

        self.pybutton.setEnabled(True)
        self.pybutton2.setEnabled(True)
        self.pybutton3.setEnabled(False)


if __name__ == "__main__":
    app = QApplication([])
    mainWin = MainWindow()
    mainWin.show()
    app.exec()
