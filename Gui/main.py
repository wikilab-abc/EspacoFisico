import sys
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow

#Cria aplicação e exibe a janela principal para o usuário.
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())
