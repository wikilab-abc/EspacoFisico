import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ui_mainwindow import Ui_MainWindow

def showWindowPessoa():
    print("olá")

def showWindowEspacoFisico():
    print("oi!")


app = QApplication(sys.argv)
window = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(window)

ui.btnPeople.clicked.connect(showWindowPessoa)
ui.btnPlaces.clicked.connect(showWindowEspacoFisico)

window.show()
sys.exit(app.exec_())
