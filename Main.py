import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from src import Controller
from src import Manager
from src.Screens import main_screen

MAIN_SCREEN_SIZE = [512, 512]
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
IMG_PATH = os.path.join(ROOT_DIR, 'img')


def img_path(filename):
    return os.path.join(IMG_PATH, filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    mainScreen = main_screen.MainScreen()
    Manager.ScreenManager().create_screen(mainScreen, MAIN_SCREEN_SIZE, [300, 300],
                                          img_path('screen-icon.png'))
    Manager.ScreenManager().create_status_bar(mainScreen, 'Ready')

    Controller.ScreenController().show(mainScreen)

    sys.exit(app.exec_())

