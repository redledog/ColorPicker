import os

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QAction, qApp, QLabel, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from src.Screens.screen import Screen
from src.Informations import Information as Info


class MainScreen(Screen):

    def init(self):
        self.setWindowTitle('Color Picker!')

        self.makeMenubar()
        #self.makeLayout()

        self.setWindowIcon(
            QIcon(os.path.join(Info.IMG_PATH, 'screen-icon.png'))
        )

    def makeMenubar(self):
        exitAction = QAction('Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        menubar.addMenu('&Info')

    def makeLayout(self):
        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(label1)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

