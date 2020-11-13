import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui.AddFriendWindow import *
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal, QThread


class AddFriendForm(QMainWindow, Ui_AddFriendForm, QThread):
    refresh = pyqtSignal()

    def __init__(self, meh):
        super().__init__()
        self.meh = meh
        self.setupUi(self)
        qss_file = open('qss/AddFriendQss.qss').read()
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.setStyleSheet(qss_file)
        self.IDEdit.setStyleSheet("color:black")
        self.pushButton.clicked.connect(lambda: self.clickedHandle(self.IDEdit.text()))
        self.label.setStyleSheet("color:#66a3ff")

    def clickedHandle(self, toID):
        self.meh.addFriendClick(toID)
        res = self.meh.getAddRes()
        if res == 'True':
            QMessageBox.information(self, '提示', '添加成功！')
            self.refresh.emit()
        elif res == 'Already1':
            QMessageBox.critical(self, '提示', '你们已是好友，请勿重复添加！')
        elif res == 'Already2':
            QMessageBox.critical(self, '提示', '你已有对方好友，但对方无，已将你添加为对方好友！')
        elif res == 'Already3':
            QMessageBox.critical(self, '提示', '对方好友列表已有你，但你无，已添加对方为你的好友！')
            self.refresh.emit()
        elif res == 'False':
            QMessageBox.critical(self, '提示', '请不要添加自己为好友！')
        elif res == 'Error':
            QMessageBox.critical(self, '提示', '对方账号不存在，请重新输入！')
