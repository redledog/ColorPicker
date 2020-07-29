from PyQt5.QtWidgets import QWidget


class MainScreen(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Color Picker!')

