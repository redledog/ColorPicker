import os
import sys

from PyQt5.QtWidgets import QApplication
from src.Screens import main_screen
from src.Informations import Information as Info


def img_path(filename):
    return os.path.join(Info.IMG_PATH, filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainScreen = main_screen.MainScreen()
    mainScreen.setFixedSize(Info.MAIN_SCREEN_WIDTH, Info.MAIN_SCREEN_HEIGHT)
    mainScreen.moveToCenter()
    mainScreen.setStatusBar('Ready')
    mainScreen.show()

    sys.exit(app.exec_())

