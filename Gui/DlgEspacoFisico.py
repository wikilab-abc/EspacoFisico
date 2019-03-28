import sys
from PyQt5.QtWidgets import QDialog
from ui_DlgEspacoFisico import Ui_DlgEspacoFisico

def showWindow():
    window = QDialog()
    ui = Ui_DlgEspacoFisico()
    ui.setupUi(window)
    print("hi")
    window.show()
