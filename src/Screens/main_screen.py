import os

from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QAction, qApp, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QColorDialog, QFrame
from src.Screens.screen import Screen
from src.Informations import Information as Info


class MainScreen(Screen):

    def init(self):
        self.setWindowTitle('Color Picker!')

        self.makeMenubar()
        self.central_widget = self.makeCentralContent()
        self.setCentralWidget(self.central_widget)

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

    def makeCentralContent(self):
        wg = QWidget()
        col = QColor(0, 0, 0)

        colordialog = QColorDialog()
        colorBox = QFrame()

        colordialog.setOption(QColorDialog.NoButtons)
        colordialog.setOption(QColorDialog.ShowAlphaChannel)
        #colordialog.setOption(QColorDialog.DontUseNativeDialog, False)

        colorBox.setStyleSheet('QWidget { background-color: %s }' % col.name())
        colorBox.setGeometry(0, 0, 100, 100)

        hbox = QHBoxLayout()
        hbox.addWidget(colordialog)

        vbox_colorbox = QVBoxLayout()
        #vbox_colorbox.addStretch(1)
        vbox_colorbox.addWidget(colorBox, 1)
        vbox_colorbox.addStretch(3)

        hbox.addLayout(vbox_colorbox)

        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        Info.MAIN_SCREEN_WIDTH += colordialog.width()
        Info.MAIN_SCREEN_WIDTH += colorBox.width()

        wg.setLayout(vbox)
        return wg

