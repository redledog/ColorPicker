import sys
from PyQt5.QtWidgets import QApplication, QWidget


class ScreenController:

    def __init__(self):
        app = QApplication(sys.argv)
        sys.exit(app.exec_())

    def show(self, screen):
        screen.show()
