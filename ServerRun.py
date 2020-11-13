import sys
import threading
from ui.serverWindow import Ui_serverWindow
from PyQt5.QtWidgets import *
import Server
import Settings
import Mysql


class ServerRun(QMainWindow, Ui_serverWindow):
    def __init__(self, parent=None):
        super(ServerRun, self).__init__(parent)
        self.setupUi(self)
        self.serverStart.clicked.connect(self.startServer)
        self.mysqlInit.clicked.connect(self.initMysql)
        self.offLine.clicked.connect(self.setOffline)
        self.serverClose.clicked.connect(sys.exit)
        self.hostLineEdit.setText(Settings.settings.host)
        self.portLineEdit.setText(str(Settings.settings.port))
        self.mysqlpwdLineEdit.setText(Settings.settings.mysqlPwd)

    def startServer(self):
        Settings.settings.host = self.hostLineEdit.text()
        Settings.settings.port = int(self.portLineEdit.text())
        Settings.settings.addr = (self.hostLineEdit.text(), int(self.portLineEdit.text()))
        Settings.settings.mysqlPwd = self.mysqlpwdLineEdit.text()
        t = threading.Thread(target=Server.run)
        t.setDaemon(True)
        t.start()

    def initMysql(self):
        Settings.settings.mysqlPwd = self.mysqlpwdLineEdit.text()
        Mysql.init()

    def setOffline(self):
        Settings.settings.mysqlPwd = self.mysqlpwdLineEdit.text()
        Mysql.setOffline()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = ServerRun()
    myWin.show()
    sys.exit(app.exec_())
