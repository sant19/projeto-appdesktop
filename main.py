import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_home import Ui_TelaHome
from ui_principal import Ui_MainWindow


class TelaHome(QMainWindow, Ui_TelaHome):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Inserir Dados")

    def closeEvent(self, event) -> None:
        self.origem = MainWindow()
        self.origem.show()
        event.accept()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setWindowTitle("Tela Principal")

        self.telahome = TelaHome()

        self.btn_apenados.clicked.connect(self.open_home)

    def open_home(self):
        self.telahome.show()
        self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
