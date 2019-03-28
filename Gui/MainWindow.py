import sys
from PyQt5.QtWidgets import QMainWindow
from ui_MainWindow import Ui_MainWindow
from cadastroPessoas import mostrarJanela
from DlgEspacoFisico import showWindow 

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        ui = Ui_MainWindow()
        ui.setupUi(self)
        self.show()
        ui.btnPeople.clicked.connect(mostrarJanela)
        ui.btnPlaces.clicked.connect(showWindow)

