from PyQt5.QtCore import QSettings, QTimer
from PyQt5.QtGui import QIcon
from ui.LoginWindow import Ui_loginWindow
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QApplication
import sys
from EventHandle import EventHandler
from Main import run as mainFormRun
from Register import run as regWindowRun


class LoginWindow(QMainWindow, Ui_loginWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.meh = EventHandler()
        qssFile = open('qss/LoginStyle.qss').read()
        self.setStyleSheet(qssFile)
        self.setWindowTitle('登录')
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.initLoginInfo()
        self.loginButton.clicked.connect(
            lambda: self._tempFunc(self.userLineEdit.text(), self.pwdLineEdit.text()))
        self.registerButton.clicked.connect(self.register)

    def _tempFunc(self, userID, pwd):
        self.meh.loginClick(userID, pwd)
        res, addr = self.meh.getLoginRes()
        if res:
            self.saveLoginInfo(addr)
            self.close()
            self.mainWindow = mainFormRun(self.meh.getInfoPkt(), self.meh)
            self.mainWindow.show()
        else:
            QMessageBox.critical(QMessageBox(), "提示", "登录失败，请重试！")
            self.pwdLineEdit.clear()

    # 初始化登录信息
    def initLoginInfo(self):
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        userid = settings.value('userid')
        password = settings.value('password')
        rememberPassword = settings.value('rememberpassword')
        autologin = settings.value('autologin')
        headAddr = settings.value('headAddr')
        settings.setValue("headAddr", 'images/pythonIcon.jpg')
        self.headimage.setStyleSheet("border-radius:50px;border-image:url('%s');" % headAddr)
        self.userLineEdit.setText(userid)
        if rememberPassword == 'true':
            self.pwdLineEdit.setText(password)
            self.remPwdCheck.setChecked(True)
        if autologin == 'true':
            self.autoCheck.setChecked(True)
            self.timer = QTimer()
            self.timer.setInterval(1500)
            self.timer.start()
            self.timer.timeout.connect(self.gotoAutologin)

    # 保存登录信息
    def saveLoginInfo(self, addr):
        settings = QSettings("config/config.ini", QSettings.IniFormat)
        settings.setValue("userid", self.userLineEdit.text())
        settings.setValue("password", self.pwdLineEdit.text())
        # 此处应该将数据库中匹配的值放入
        settings.setValue("headAddr", addr)
        self.headimage.setStyleSheet("border-radius:36px;border-image:url('%s');" % addr)
        if self.autoCheck.isChecked():
            settings.setValue("rememberpassword", True)
        else:
            settings.setValue("rememberpassword", self.remPwdCheck.isChecked())
        settings.setValue("autologin", self.autoCheck.isChecked())

    def gotoAutologin(self):
        if self.autoCheck.isChecked():
            self.timer.stop()
            self._tempFunc(self.userLineEdit.text(), self.pwdLineEdit.text())

    def register(self):
        self.reg = regWindowRun()
        self.reg.show()


def run():
    app = QApplication(sys.argv)
    chat = LoginWindow()
    chat.show()
    sys.exit(app.exec_())
