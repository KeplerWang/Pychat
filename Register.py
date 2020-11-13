import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui.RegisterWindow import Ui_registerWindow
from EventHandle import EventHandler


class myJoinIn(QMainWindow, Ui_registerWindow):
    def __init__(self, parent=None):
        super(myJoinIn, self).__init__(parent)
        self.setupUi(self)
        self.qssFile = open('qss/RegisterStyle.qss').read()
        self.setStyleSheet(self.qssFile)
        self.setWindowTitle('注册')
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.gender = '男'
        self.meh = EventHandler()
        self.initHead = 'images/pythonIcon.jpg'
        self.headChangePushButton.clicked.connect(self.openImage)
        self.comboBox.activated.connect(self.genderSelected)
        self.cvPushButton.clicked.connect(
            lambda: self._tempFunc(self.emailLineEdit.text()))
        self.surePushButton.clicked.connect(self.display)  # connect to registerInfoClick in the project
        self.canclePushButton.clicked.connect(self.closeWindow)

    def openImage(self):
        # self.initHead存图片地址
        self.initHead, _ = QFileDialog.getOpenFileName(self, '选择图片', 'images/headImages/', 'All files(*.*)')
        if self.initHead == '':
            self.initHead = 'images/pythonIcon.jpg'
        else:
            pos = self.initHead.find('images')
            self.setStyleSheet(self.qssFile.replace('images/pythonIcon.jpg', self.initHead))
            self.initHead = self.initHead[pos:]
            self.headChangePushButton.setText('')

    def genderSelected(self):
        self.gender = self.comboBox.currentText()

    def display(self):
        # 获取文本框内容，并弹框显示内容
        self.userID = self.idLineEdit.text()
        self.verifyCode = self.vcLineEdit.text()
        self.email = self.emailLineEdit.text()
        self.pwd = self.pwdLineEdit.text()
        self.ackPwd = self.resureLineEdit.text()
        self.nickname = self.nickNameLineEdit.text()
        if self.userID.strip() == '' or self.verifyCode.strip() == '' or self.email.strip() == '' \
                or self.pwd.strip() == '' or self.ackPwd.strip() == '' or self.nickname.strip() == '':
            QMessageBox.critical(self, '提示', '请不要将信息框空填！')
        else:
            self.meh.registerInfoClick(self.userID, self.nickname, self.gender, self.email, self.pwd, self.ackPwd,
                                       self.verifyCode, self.initHead)
            if self.meh.getEmailRes():
                if self.meh.getEmailChangeRes():
                    QMessageBox.critical(self, '提示', '您已更改邮箱，请重新发送验证码！')
                else:
                    if not self.meh.getVCRes():
                        QMessageBox.critical(self, '提示', '验证码错误！')
                    else:
                        if not self.meh.getPwdMatchRes():
                            QMessageBox.critical(self, '提示', '密码不匹配！')
                        else:
                            if not self.meh.getRegRes():
                                QMessageBox.critical(self, '提示', '账号已存在！')
                            else:
                                QMessageBox.information(self, '提示', '注册成功！')
                                self.idLineEdit.clear()
                                self.nickNameLineEdit.clear()
                                self.emailLineEdit.clear()
                                self.pwdLineEdit.clear()
                                self.resureLineEdit.clear()
                                self.vcLineEdit.clear()
            else:
                QMessageBox.critical(self, '提示', '注册失败！')

    def _tempFunc(self, email):
        self.meh.getVerifyCodeClick(email)
        if not self.meh.getEmailRes():
            QMessageBox.warning(self, '提示', '验证码发送失败，请检查邮箱格式后重试！')

    def closeWindow(self):
        self.close()
        self.meh.s.closeConnection()


def run():
    return myJoinIn()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = myJoinIn()
    myWin.show()
    sys.exit(app.exec_())
