from ui.MainWindow import *
from PyQt5.QtWidgets import QListWidgetItem
from AddFriend import *
from PyQt5 import QtCore, QtGui
from EventHandle import EventHandler
from games.game import run as gameRun
from Chat import run as chatRun
from Member import run as showMemberRun
from Load import run as UDloadRun


class MainForm(QMainWindow, Ui_MainForm):
    def __init__(self, infoPkt, meh):
        super().__init__()
        self.infoPkt = infoPkt
        self.windowPool = dict()
        self.meh = meh
        self.chatHandlePool = []
        self.fileHandlePool = []
        self.setupUi(self)
        qss_file = open('qss/MainWindowQss.qss').read()
        self.setWindowTitle('主界面')
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.setFixedSize(self.width(), self.height())
        self.listWidget.setIconSize(QtCore.QSize(40, 40))
        self.setStyleSheet(qss_file)
        self.showFriendList()
        self.pushButton.clicked.connect(self.addFriend)
        self.pushButton_2.clicked.connect(self.gameSelect)
        self.pushButton_3.clicked.connect(self.downloadAndUpload)
        self.pushButton_4.clicked.connect(self.showMembers)
        self.pushButton_5.clicked.connect(self.refresh)
        self.pushButton_6.clicked.connect(self.logout)
        self.listWidget.itemDoubleClicked.connect(self.openChatWindow)  # 双击好友打开聊天界面
        self.displayInformation()

    def showFriendList(self):  # 将好友列表显示在listWidget上
        for i in self.infoPkt['friendsList']:
            newItem = QListWidgetItem()
            newItem.setIcon(QtGui.QIcon('%s' % i[2]))
            newItem.setText("%s\n   <%s>" % (i[0], i[1]))
            self.listWidget.addItem(newItem)
            self.windowPool.update({i[1]: True if self.windowPool.get(i[1]) else False})

    def openChatWindow(self, index):
        toFriend = self.infoPkt['friendsList'][self.listWidget.row(index)]
        if not self.windowPool[toFriend[1]]:
            maps = {'nickname': toFriend[0], 'sex': toFriend[3], 'email': toFriend[4], 'id': toFriend[1],
                    'status': '在线', 'address': '华中科技大学', 'headAddr': toFriend[2],
                    'myHeadAddr': self.infoPkt['headAddr'], 'myName': self.infoPkt['nickname'],
                    'myid': self.infoPkt['id']}
            res = self.meh.userChatClick(maps['id'])
            if res:
                chatHandle = EventHandler()
                chatHandle.s.ID = self.meh.s.ID
                self.chatHandlePool.append(chatHandle)
                self.windowPool[toFriend[1]] = True
                chatHandle.connect(maps['id'])
                self.chat = chatRun(maps, chatHandle, self.windowPool)
                self.chat.show()
            else:
                QMessageBox.critical(self, '提示', '对方不在线！')
        else:
            QMessageBox.critical(self, '提示', '请不要重复打开聊天窗口！')

    def refresh(self):
        self.meh.refreshListClick()
        self.infoPkt = self.meh.getRefreshRes()
        self.listWidget.clear()
        self.showFriendList()

    def displayInformation(self):  # 显示自身头像、ID与昵称
        self.headPortait.setStyleSheet("border-radius:36px;border-image:url('%s');" % self.infoPkt['headAddr'])
        self.IDlabel.setText(self.infoPkt['id'])
        self.nicknamelable.setText(self.infoPkt['nickname'])
        self.nicknamelable.setStyleSheet("color:red")

    def addFriend(self):
        self.addFriendForm = AddFriendForm(self.meh)
        self.addFriendForm.refresh.connect(self.refresh)
        self.addFriendForm.show()

    def gameSelect(self):
        self.game = gameRun()
        self.game.show()

    def downloadAndUpload(self):
        self.UDload = UDloadRun(self.fileHandlePool)
        self.UDload.show()

    def showMembers(self):
        self.openMemberWindow = showMemberRun()
        self.openMemberWindow.show()

    def logout(self):
        self.meh.logoutClick()
        [i.s.closeConnection() for i in self.chatHandlePool]
        [i.s.closeConnection() for i in self.fileHandlePool]
        sys.exit()


def run(infoPkt, meh):
    return MainForm(infoPkt, meh)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainForm({'nickname': '陈建文的迷弟',
                           'sex': '男',
                           'email': '1692705146@qq.com',
                           'headAddr': 'images/headImages/head1.jpeg',
                           'num': '5',
                           'friendsList': [
                               ['陈建文的迷弟', '中文root中文', 'images/headImages/head15.jpeg', '男', '1692705146@qq.com'],
                               ['Kepler', '0', 'images/headImages/head1.jpeg', '男', '123456@qq.com'],
                               ['Kepler', '1', 'images/headImages/head1.jpeg', '男', '123456@qq.com'],
                               ['Kepler', '2', 'images/headImages/head1.jpeg', '男', '123456@qq.com'],
                               ['Kepler', '3', 'images/headImages/head1.jpeg', '男', '123456@qq.com']],
                           'id': 'root'}, None)
    mainWindow.show()
    sys.exit(app.exec())
