import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_home import Ui_TelaHome
from ui_pesquisa import Ui_TelaPesquisa
from ui_principal import Ui_MainWindow
from ui_relatorio import Ui_WindowRelatorio


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Tela Principal")

        self.telahome = TelaHome()
        self.telapesquisa = Pesquisa()
        self.telarelatorio = Relatorio()

        self.btn_apenados.clicked.connect(self.open_home)
        self.btn_pesquisa.clicked.connect(self.open_pesquisar)
        self.btn_relatorio.clicked.connect(self.open_relatorio)

    def open_home(self):
        self.telahome.show()
        self.hide()

    def open_pesquisar(self):
        self.telapesquisa.show()
        self.hide()

    def open_relatorio(self):
        self.telarelatorio.show()
        self.hide()


class TelaHome(QMainWindow, Ui_TelaHome):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Inserir Dados")

    def closeEvent(self, event) -> None:
        self.origem = MainWindow()
        self.origem.show()
        event.accept()


class Pesquisa(QMainWindow, Ui_TelaPesquisa):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Pesquisar")

        self.telahome = TelaHome()

        self.btn_homepesquisa.clicked.connect(self.open_home)

    def open_home(self):
        self.telahome.show()
        self.hide()

    def closeEvent(self, event) -> None:
        self.origem = MainWindow()
        self.origem.show()
        event.accept()


class Relatorio(QMainWindow, Ui_WindowRelatorio):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Relatório")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
