import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import argparse

class MainWindow(QMainWindow):
    def __init__(self, title="Title", button_text="Text", fixed=False):
        super().__init__()
        self.setWindowTitle(title)

        self.button = QPushButton(button_text)

        self.setCentralWidget(self.button)

        #self.setFixedSize(400,600)
        self.button.setMaximumSize(100,25)
        self.setMaximumSize(400,400)
        self.setMinimumSize(200,200)

        self.button.show()
        self.show()

app = QApplication(sys.argv)

window = MainWindow()

app.exec()

def main():
    parser = argparse.ArgumentParser(description = " ")
    parser.add_argument("-t", "--title", help="Title of application")
    parser.add_argument("-b", "--button-text", )
    parser.add_argument("-f", "--fixed-size",
                        help="Window fixed size")
    parser.add_argument("-s", "--size",
                        help="Window's size")

if __name__ == '__main__':
    main()
