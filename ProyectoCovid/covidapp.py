''' Todos los import que he usado para la APP covid'''
import csv
import sys
import matplotlib
import pandas as pd
import matplotlib.pyplot
import os
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QMainWindow, QComboBox, QVBoxLayout, QWidget, QMessageBox,
     QLabel, QToolBar, QPushButton, QGridLayout, QLineEdit,
)


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


# Clase para hacer la ventana de login
class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        ''' En esta clase he creado dos labels, uno para el
            usuario y otro para la contraseña. Los he 
            posicionado uno debajo de otro y los he añadido a 
            un layout que he definido'''

        self.setWindowTitle("Login Window")
        self.resize(500, 120)

        self.mainwindow = MainWindow()
        layout = QGridLayout()

        label_usuario = QLabel('<font size="4"> Usuario: </font>')
        self.usuario = QLineEdit()
        self.usuario.setPlaceholderText("Usuario: admin")
        layout.addWidget(label_usuario, 0, 0)
        layout.addWidget(self.usuario, 0, 1)

        label_contraseña = QLabel('<font size="4"> Password </font>')
        self.contraseña = QLineEdit()
        self.contraseña.setPlaceholderText("Contraseña: 1234")
        layout.addWidget(label_contraseña, 1, 0)
        layout.addWidget(self.contraseña, 1, 1)

        ''' Creamos un boton, lo conectamos a la función comprobar
            y lo añadimos al layout'''
        boton_login = QPushButton("Iniciar sesión")
        boton_login.clicked.connect(self.comprobar)
        layout.addWidget(boton_login, 2, 0, 1, 2)
        layout.setRowMinimumHeight(2, 75)

        self.setLayout(layout)

        ''' Función que sirve para que cuando el usuario introduzca
            mal los valores le salga un aviso y si los introduce bien
            se le abra el mainwindow'''

    def comprobar(self):

        mensaje = QMessageBox()
        
        if self.usuario.text() == "admin" and self.contraseña.text() == "1234":
            self.hide()
            self.mainwindow.show()
        else: 
            mensaje.setText("Contraseña incorrecta")
            mensaje.setIcon(QMessageBox.Warning)
            mensaje.exec_()

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Definimos el nombre y las dimensiones 
        self.setWindowTitle("CovidAPP")
        self.setFixedWidth(1000)
        self.setFixedHeight(600)

        carpeta_iconos = os.path.dirname(__file__)
        self.icono_salir = os.path.join(carpeta_iconos, "iconos/salir.png")
        

        # Boton salir que conecta con la función definida abajo
        boton_exit = QAction(QIcon(self.icono_salir), "&SALIR", self)
        boton_exit.triggered.connect(self.funcion_salir) 
        boton_exit.setShortcut(QKeySequence("Ctrl+s"))

        ''' Ahora hemos creado tres botones para los graficos.
            Uno de barras, uno de circulos y uno de linea.
            También he hecho un botón para que limpie el gráfico
            y el label de la información'''

        self.boton_graficobarra = QAction("ESTADISTICAS BARRA", self)
        self.boton_graficobarra.triggered.connect(self.estadisticas_barra)
    
        self.boton_graficocirculo = QAction("ESTADISTICAS CIRCULO", self)
        self.boton_graficocirculo.triggered.connect(self.estadisticas_circulo) 

        self.boton_graficolinea = QAction("ESTADISTICAS LINEA", self)
        self.boton_graficolinea.triggered.connect(self.estadisticas_linea) 

        self.boton_limpiar = QAction("LIMPIAR", self)
        self.boton_limpiar.triggered.connect(self.limpiar_grafico)

        #Creamos el ToolBar y añadimos todos los botones a el
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        toolbar.addAction(boton_exit)
        toolbar.addAction(self.boton_graficobarra)
        toolbar.addAction(self.boton_graficocirculo)
        toolbar.addAction(self.boton_graficolinea)
        toolbar.addAction(self.boton_limpiar)

        # Creamos un layout horizontal, uno vertical y un QWidget
        self.layout_general = QVBoxLayout() 
        self.layout_comboBox = QHBoxLayout()
        self.widget = QWidget()

        #Este para el país
        self.comboBox1 = QComboBox()
        self.comboBox1.setFixedWidth(200)
        self.comboBox1.addItem("ESPAÑA")
        self.layout_comboBox.addWidget(self.comboBox1)

        #Este es para la comunidad autónoma
        self.comboBox3 = QComboBox()
        self.comboBox3.setFixedWidth(200)
        self.comboBox3.addItem("COMUNIDAD VALENCIANA")
        self.layout_comboBox.addWidget(self.comboBox3)

        ''' Este combobox es para todas las ciudades. 
            Vamos a hacerlo editable para poder buscar
            las ciudades sin tener que buscarlas con 
            el scroll
            '''
        self.comboBox2 = QComboBox()
        self.comboBox2.setFixedWidth(200)
        self.comboBox2.setEditable(True)
        self.layout_comboBox.addWidget(self.comboBox2)

        ''' Creamos otro layout horizontal que será
            para añadir el QChartView y un label
            '''
        self.layout_general2 = QHBoxLayout()

        # Añadimos el layout horizontal al vertical
        self.layout_general.addLayout(self.layout_comboBox)
    
        ''' Creamosel label, 
            le ponemos tamaño por defecto y 
            los añadimos al último layout. '''
            
        self.informacion = QLabel() 
        self.informacion.setFixedWidth(200)
        self.informacion.setFixedHeight(500)
        self.layout_general2.addWidget(self.informacion)

        # Añadimos el nuevo layout al layout vertical
        self.layout_general.addLayout(self.layout_general2)

        self.widget.setLayout(self.layout_general)
        self.setCentralWidget(self.widget)

        ''' Definimos otro label para que cuando la pantalla esté
            vacia nos de algo de información'''
        self.labelinicial = QLabel()
        self.labelinicial.setText("ESTADISTICAS BASADAS DESDE EL 01/02/2022 AL 14/02/2022" "\n"
                                  "BIENVENIDO A MI PROYECO COVID")

        self.layout_general2.addWidget(self.labelinicial)

        ''' Vamos a usar un CSV para rellenar 
            el combobox de las ciudades/pueblos 
            de la comunidad valenciana '''

        with open ('ciudades.csv') as csvfile:
            
            self.readerciudades = csv.reader(csvfile)

            for i in self.readerciudades:
                self.comboBox2.addItems(i)
                

    ''' Función para limpiar el gráfico de la pantalla 
        y el label '''
    def limpiar_grafico(self):
        self.sc.close()
        self.informacion.clear()

    # Función para hacer los gráficos de barras.
    def estadisticas_barra(self):

        # Leemos el csv y le añadimos los delimitadores
        covid = pd.read_csv('detodo.csv', sep=';', decimal=',')
        
        ''' Le decimos que columnas queremos que use,
            usamos la función definida arriba y lo añadimos al layout '''
        columnas = ['Casos PCR+', 'Casos PCR+ 14 dies', 'Defuncions', 'Taxa de defuncio']
        self.layout_general2.removeWidget(self.labelinicial)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        covid.loc[covid.Municipi == self.comboBox2.currentText(), columnas].plot.bar(ax=self.sc.axes)
        self.layout_general2.addWidget(self.sc)

        pcr=0
        fallecidos = 0
        casos = 0
        
        ''' Volvemos a leer los csv para que nos devuelva
            las columnas que le he pedido y poder añadirlas
            al label definido abajo'''
        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    fallecidos = i[6]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    casos = i[4]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    pcr = i[2]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    tasa_defun = i[7]

        self.informacion.setText("PCR: " + pcr + "\n"
                                 "CASOS" + casos + "\n"
                                 "FALLECIDOS" +fallecidos+ "\n"
                                 "TAXA DEFUNCIÓ: " +tasa_defun)



    # Función para hacer los gráficos de circulos.
    def estadisticas_circulo(self):
        # Leemos el csv y le añadimos los delimitadores
        covid = pd.read_csv('detodo.csv', sep=';', decimal=',')

        
        ''' Le decimos que columnas queremos que use,
            usamos la función definida arriba y lo añadimos al layout '''
        columnas = ['Casos PCR+', 'Casos PCR+ 14 dies', 'Defuncions', 'Taxa de defuncio']
        self.layout_general2.removeWidget(self.labelinicial)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        covid.loc[covid.Municipi == self.comboBox2.currentText(), columnas, ].T.plot.pie(ax=self.sc.axes, subplots = True)
        self.layout_general2.addWidget(self.sc)

        pcr=0
        fallecidos = 0
        casos = 0
        tasa_defun = 0
        
        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    fallecidos = i[6]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    casos = i[4]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    pcr = i[2]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    tasa_defun = i[7]

        self.informacion.setText("PCR: " + pcr + "\n"
                                 "CASOS" + casos + "\n"
                                 "FALLECIDOS" +fallecidos+ "\n"
                                 "TAXA DEFUNCIÓ: " +tasa_defun)


    # Función para hacer los gráficos de barras.
    def estadisticas_linea(self):
        covid = pd.read_csv('detodo.csv', sep=';', decimal=',')

        ''' Le decimos que columnas queremos que use,
            usamos la función definida arriba y lo añadimos al layout '''
        columnas = ['Casos PCR+', 'Casos PCR+ 14 dies', 'Defuncions', 'Taxa de defuncio']
        self.layout_general2.removeWidget(self.labelinicial)
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        covid.loc[covid.Municipi == self.comboBox2.currentText(), columnas].T.plot.line(ax=self.sc.axes, subplots = True)
        self.layout_general2.addWidget(self.sc)

        pcr=0
        fallecidos = 0
        casos = 0
        tasa_defun = 0
        
        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    fallecidos = i[6]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    casos = i[4]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    pcr = i[2]

        with open('detodo.csv') as csvfile:
            reader = csv.reader(csvfile, delimiter=";")

            for i in reader:
                if i[1] == self.comboBox2.currentText():
                    tasa_defun = i[7]

        self.informacion.setText("PCR: " + pcr + "\n"
                                 "CASOS" + casos + "\n"
                                 "FALLECIDOS" +fallecidos+ "\n"
                                 "TAXA DEFUNCIÓ: " +tasa_defun)


    ''' Función que al pulsar el botón
        de exit te pregunta si quieres salir'''
    def funcion_salir(self):

        salir_boton = QMessageBox(self)
        salir_boton.setWindowTitle("Salir")
        salir_boton.setText("Estás seguro de que quieres salir? ")
        salir_boton.setIcon(QMessageBox.Question)
        salir_boton.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        boton_salir = salir_boton.exec()

        if boton_salir == QMessageBox.Ok:
            sys.exit()
        elif boton_salir == QMessageBox.Cancel:
            QMainWindow()
       
if __name__ == "__main__":
    app = QApplication([])
    logWin = LoginWindow()
    logWin.show()
    app.exec()