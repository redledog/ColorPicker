import os

from PyQt5 import QtCore
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QAction, qApp, QLabel, QHBoxLayout, QVBoxLayout, QWidget, QColorDialog, QFrame, QLineEdit
from src.Screens.screen import Screen
from src.Informations import Information as Info
import clipboard

class MainScreen(Screen):
    colordialog = None
    colorBox = None
    html_lbl = None

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
        col = QColor(255, 255, 255)

        self.colordialog = QColorDialog()
        self.colorBox = QFrame()

        self.html_lbl = Label('HTML : ')

        linedit = QLineEdit()
        linedit.setReadOnly(True)
        linedit.setText(col.name())
        linedit.mousePressEvent = lambda ev: clipboard.copy(linedit.text())

        # self.colordialog.currentColorChanged.connect(self.on_changed_color)
        self.colordialog.currentColorChanged.connect(lambda: self.on_changed_color(self.colordialog, self.colorBox, linedit))


        self.colordialog.setOption(QColorDialog.NoButtons)
        self.colordialog.setOption(QColorDialog.ShowAlphaChannel)
        #colordialog.setOption(QColorDialog.DontUseNativeDialog, False)

        self.colorBox.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.colorBox.setGeometry(0, 0, 100, 100)

        hbox = QHBoxLayout()
        hbox.addWidget(self.colordialog)

        hbox_html = QHBoxLayout()
        hbox_html.addWidget(self.html_lbl)

        hbox_html.addWidget(linedit, 1)


        vbox_colorbox = QVBoxLayout()
        #vbox_colorbox.addStretch(1)
        vbox_colorbox.addWidget(self.colorBox, 1)
        # vbox_colorbox.addStretch(1)
        vbox_colorbox.addLayout(hbox_html, 1)
        vbox_colorbox.addStretch(2)

        hbox.addLayout(vbox_colorbox)

        vbox = QVBoxLayout()
        #vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        Info.MAIN_SCREEN_WIDTH += self.colordialog.width()
        Info.MAIN_SCREEN_WIDTH += self.colorBox.width()

        wg.setLayout(vbox)
        return wg

    def on_changed_color(self, dialog, frame, line_edit):
        color = dialog.currentColor()
        frame.setStyleSheet('QWidget { background-color: %s }' % color.name())
        # print(color.name())
        line_edit.setText(color.name())


class Label(QLabel):
    header_str = None
    body_str = None

    def __init__(self, header):
        super().__init__(header)
        # self.focusInEvent(self.on_click_label)
        self.header_str = header
        self.text = self.header_str

    def set_body(self, body):
        self.body_str = body
        self.text = self.header_str + self.body_str

    def on_click_label(self):
        print(self.body_str)


class LineEdit(QLineEdit):
    pass