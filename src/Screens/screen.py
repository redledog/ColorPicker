from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget


class Screen(QMainWindow):

    def __init__(self):
        super().__init__()
        self.init()

    def init(self):
        pass

    def setStatusBar(self, text=None):
        if text is not None:
            self.statusBar().showMessage(text)
        else:
            self.statusBar()

    def setTransform(self, size, move=None):
        if move is not None and len(move) >= 2:
            self.setGeometry(move[0], move[1], size[0], size[1])
        else:
            self.setGeometry(0, 0, size[0], size[1])
            self.moveToCenter()

    def moveToCenter(self):
        centerPos = QDesktopWidget().availableGeometry().center()
        screenTrans = self.frameGeometry()
        screenTrans.moveCenter(centerPos)
        self.move(screenTrans.topLeft())
