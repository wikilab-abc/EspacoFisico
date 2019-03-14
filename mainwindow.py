import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow
from cadastroPessoas import mostrarJanela
from DlgEspacoFisico import showWindow 

def showWindowPessoa():
    print("olá")

def showWindowEspacoFisico():
    print("oi!")

app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.btnPeople.clicked.connect(mostrarJanela)
ui.btnPlaces.clicked.connect(showWindow)

window.show()
sys.exit(app.exec_())
