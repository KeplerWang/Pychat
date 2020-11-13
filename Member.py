from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QMainWindow, QApplication, QToolTip
import sys
from ui.MemberWindow import *


class MemberWindow(QMainWindow, Ui_MemberWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('小组成员')
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.setFixedSize(self.width(), self.height())
        qss_file = open('qss/MemberQss.qss').read()
        self.setStyleSheet(qss_file)
        self.hlabel1.setToolTip("这里还啥都没有写。。。")
        self.hlabel2.setToolTip("这里还啥都没有写。。。")
        self.hlabel3.setToolTip("这里还啥都没有写。。。")
        self.hlabel4.setToolTip("这里还啥都没有写。。。")
        self.hlabel5.setToolTip("我永远喜欢陈建文！")
        self.hlabel6.setToolTip("这里还啥都没有写。。。")
        self.hlabel7.setToolTip("这里还啥都没有写。。。")
        QToolTip.setFont(QFont("宋体", 24))

        self.nlabel1.setStyleSheet("color:#6666ff")
        self.nlabel2.setStyleSheet("color:#6666ff")
        self.nlabel3.setStyleSheet("color:#6666ff")
        self.nlabel4.setStyleSheet("color:#6666ff")
        self.nlabel5.setStyleSheet("color:#6666ff")
        self.nlabel6.setStyleSheet("color:#6666ff")
        self.nlabel7.setStyleSheet("color:#6666ff")

        self.nlabel1_2.setStyleSheet("color:#6666ff")
        self.nlabel2_2.setStyleSheet("color:#6666ff")
        self.nlabel3_2.setStyleSheet("color:#6666ff")
        self.nlabel4_2.setStyleSheet("color:#6666ff")
        self.nlabel5_2.setStyleSheet("color:#6666ff")
        self.nlabel6_2.setStyleSheet("color:#6666ff")
        self.nlabel7_2.setStyleSheet("color:#6666ff")


def run():
    return MemberWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat = MemberWindow()
    chat.show()
    sys.exit(app.exec_())
