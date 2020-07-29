from PyQt5.QtGui import QIcon


class ScreenManager:

    def create_screen(self, screen, size, move, icon=None):
        screen.resize(size[0], size[1])
        screen.move(move[0], move[1])
        if icon is not None:
            screen.setWindowIcon(QIcon(icon))
