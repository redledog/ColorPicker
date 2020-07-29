from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MainScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Color Picker!')
        self.setWindowIcon(QIcon('../img/screen-icon.png'))
        # self.move(300, 300)
        # self.resize(512, 512)
        # self.show()
