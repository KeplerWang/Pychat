from PyQt5.QtWidgets import QMainWindow
from ui.ChatForm import *
from Settings import getTime
import threading


class MyChat(QMainWindow, Ui_ChatForm):
    def __init__(self, infoPkt, meh, windowPool):
        super().__init__()
        self.setupUi(self)
        self.infoPkt = infoPkt
        self.windowPool = windowPool
        self.meh = meh
        self.showInit()
        self.textBrowser.clear()
        self.mes.setText('开始你的聊天吧！')
        self.sendButton.clicked.connect(self.send)
        self.pushButton.clicked.connect(self.closebtnClick)
        self.setWindowTitle('聊天界面')
        self.setWindowIcon(QtGui.QIcon('images/pythonIcon.jpg'))
        self.setFixedSize(self.width(), self.height())
        self.chat_th = threading.Thread(target=self.recv)  # 创建接收信息线程
        self.chat_th.setDaemon(True)
        self.chat_th.start()

    def send(self):
        text = self.textEdit.toPlainText()
        self.mes.clear()
        if text == '':
            self.mes.setText('请在聊天框输入文字')
        else:
            self.textBrowser.append("<font color= #00aa00>" + self.infoPkt['myName'] + ' ' + getTime()[:-4] + "\n")
            self.textBrowser.append("<font color= #000000>" + text + '\n')
            self.textBrowser.append(' ')
            self.textEdit.clear()
            data = {"fromID": self.infoPkt['myid'], "toID": self.infoPkt['id'], "time": getTime()[:-4], "msg": text,
                    'fromName': self.infoPkt['myName'], 'type': 'open'}
            self.meh.send(data)

    def recv(self):
        while True:
            messages = self.meh.recv()
            if messages['type'] == 'exit':
                break
            self.mes.clear()
            self.textBrowser.append("<font color= #58C9FF>" + messages['fromName'] + ' ' + messages['time'])
            self.textBrowser.append("<font color= #000000>" + messages['msg'])
            self.textBrowser.append(' ')
            self.textBrowser.ensureCursorVisible()  # 游标可用
            cursor = self.textBrowser.textCursor()  # 设置游标
            pos = len(self.textBrowser.toPlainText())  # 获取文本尾部的位置
            cursor.setPosition(pos)  # 游标位置设置为尾部
            self.textBrowser.setTextCursor(cursor)  # 滚动到游标位置

    def showInit(self):
        self.f_nickName.setText(self.infoPkt["nickname"])
        self.chatName.setText(self.infoPkt["nickname"])
        self.email.setText(self.infoPkt["email"])
        self.gender.setText(self.infoPkt["sex"])
        self.address.setText(self.infoPkt['address'])
        self.rootname.setText(self.infoPkt["id"])
        self.onlineStatus.setText(self.infoPkt["status"])
        self.my_avatar.setStyleSheet("background-color: gainsboro;border-image: url(" +
                                     self.infoPkt['myHeadAddr'] +
                                     ");border-radius:80px;")
        self.f_avatar.setStyleSheet("background-color: gainsboro;border-image: url(" +
                                    self.infoPkt['headAddr'] +
                                    ");border-radius:80px;")

    def closebtnClick(self):
        self.windowPool[self.infoPkt['id']] = False
        data = {"fromID": self.infoPkt['myid'], "toID": self.infoPkt['id'], "time": getTime()[:-4], "msg": 'exitexit',
                'fromName': self.infoPkt['myName'], 'type': 'exit'}
        self.meh.send(data)
        self.close()


def run(infoPkt, meh, windowPool):
    return MyChat(infoPkt, meh, windowPool)
