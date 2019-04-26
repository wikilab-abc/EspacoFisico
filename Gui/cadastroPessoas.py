import sys
from PyQt5.QtWidgets import QDialog
from ui_cadastroPessoas import Ui_dlgPessoas  


class CadastroPessoas(QDialog):
    def __init__(self, parent):
        super(CadastroPessoas, self).__init__(parent)
        ui = Ui_dlgPessoas()
        ui.setupUi(self)
        self.show()

