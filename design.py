from PyQt5.QtCore import QRect, Qt
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QPaintEvent, QPaintDevice
from PyQt5.QtWidgets import QWidget, qApp
from PyQt5 import QtGui


class MySplash(QWidget):
    def __init__(self):
        super(MySplash, self).__init__()
        self.setWindowOpacity(1)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 设置无边框
        self.setGeometry(700, 190, 570, 420)

    def paintEvent(self, event):
        painter = QPainter()
        font = QtGui.QFont()
        font.setBold(True)
        font.setFamily("Arial")
        font.setPointSize(12)
        painter.begin(self)
        painter.setFont(font)
        painter.setPen(QPen())
        painter.setBrush(QBrush())
        painter.drawPixmap(QRect(0, 0, 570, 370), QPixmap("images/5.jpg"))
        painter.drawText(QRect(30, 385, 570, 100), Qt.AlignLeft, self.text)  # showMessage
        painter.end()

    def setText(self, text):
        self.text = text
        self.paintEvent(None)
        self.update()
        qApp.processEvents()

