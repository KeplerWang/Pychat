import sys
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QAction, qApp, QApplication)
from PyQt5.QtGui import QIcon
import os
from games.MainWindow import *


class mainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        qss_file = open('qss/GameQss.qss').read()
        self.setStyleSheet(qss_file)
        self.setEnabled(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/pythonIcon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        exitAction = QAction(QIcon('Exit.jpg'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        # 创建一个菜单栏
        menubar = self.menuBar()
        # 添加菜单
        optionMenu = menubar.addMenu('&Option')
        # 添加事件
        optionMenu.addAction(exitAction)

        self.pushButton.clicked.connect(self.GreedySnakeClicked)
        self.pushButton.setToolTip("start up GreedySnake")
        self.pushButton.setStyleSheet("border-radius: 120%")
        self.pushButton_2.clicked.connect(self.AircraftWarClicked)
        self.pushButton_2.setToolTip("start up AircraftWar")
        self.pushButton_2.setStyleSheet("border-radius: 100%")
        self.pushButton_3.clicked.connect(self.PacManClicked)
        self.pushButton_3.setToolTip("start up PacMan")
        self.pushButton_3.setStyleSheet("border-radius: 75%")
        self.pushButton_4.clicked.connect(self.ExitClicked)
        self.pushButton_4.setToolTip("Exit")

        self.statusBar()

        self.setGeometry(500, 50, 290, 150)
        self.setWindowTitle('games')

    def GreedySnakeClicked(self):
        os.system("python ./games/GreedySnake.py")

    def AircraftWarClicked(self):
        os.system("python ./games/feiji/start.py")

    def PacManClicked(self):
        os.system("python ./games/Pacman.py")

    def ExitClicked(self):
        self.close()


def run():
    return mainWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    qssStyle = '''
        
    '''
    mainWindow().show()
    sys.exit(app.exec_())


