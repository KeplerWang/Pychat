import ftp
import demjson
from Settings import getTime
from socket import *
import Settings
import Login


class Socket:
    def __init__(self):
        self.clientSocket = socket(AF_INET, SOCK_STREAM)
        self.clientSocket.connect(Settings.settings.addr)
        self.ID = None

    def sendData(self, message, marker):
        size = len(bytes(str(message), encoding='utf-8'))
        if size <= 9:
            length = '00' + str(size)
        elif 9 < size <= 99:
            length = '0' + str(size)
        else:
            length = str(size)
        self.clientSocket.sendall(bytes(marker + length + str(message), encoding='utf-8'))

    def getData(self):
        marker = self.clientSocket.recv(1).decode()
        if not '$#'.__contains__(marker):
            raise Settings.DataFetchException
        else:
            length = int(self.clientSocket.recv(3).decode())
            return self.clientSocket.recv(length).decode()

    # 打开C/S通信 命令: Open
    def openConnection(self):
        self.sendData('Open', '$')
        print(self.getData())

    # 关闭C/S通信 命令: Close
    def closeConnection(self):
        self.sendData('Close', '$')
        print(self.getData())
        self.clientSocket.close()

    # 登录检验 命令: Login
    def login(self, data):
        self.sendData('Login', '$')
        self.sendData(data, '#')
        res = self.getData()
        if res == 'True':
            self.ID = data.split(' ')[0]
            print(getTime() + 'Login Successful!')
            return True, demjson.decode(self.getData(), encoding='utf8')
        else:
            print(getTime() + 'Login Failed!')
            return False, None

    # 退出登录 命令: Logout
    def logout(self):
        self.sendData('Logout', '$')
        self.sendData(self.ID, '#')

    # 注册 命令: Register
    def register(self, data):
        self.sendData('Register', '$')
        self.sendData(data, '#')
        return self.getData() == 'Y'

    # 添加好友 命令: Add
    def addFriend(self, toID):
        self.sendData('Add', '$')
        self.sendData(self.ID + ' ' + toID, '#')
        return self.getData()

    # 刷新好友列表 命令: Refresh
    def refresh(self):
        self.sendData('Refresh', '$')
        self.sendData(self.ID, '#')
        info = demjson.decode(self.getData(), encoding='utf8')
        return info

    # 尝试打开toID的聊天框 命令: Start
    def chatStart(self, toID):
        if toID == '0000' or toID == '1000':
            return True
        else:
            self.sendData('Start', '$')
            self.sendData(toID, '#')
            return self.getData() == 'Online'

    # 将self.ID 和 toID绑定
    def connect(self, toID):
        if toID == '0000':
            self.sendData('GroupIn', '$')
            self.sendData(self.ID, '#')
        else:
            self.sendData('Connect', '$')
            self.sendData(self.ID + ' ' + toID, '#')

    # 上传文件 命令: Upload
    def upload(self, filePath):
        try:
            f = ftp.FTP()
            f.upload(filePath)
            f.close()
            return True
        except:
            return False

    # 下载文件 命令: Download
    def download(self, filename, fileWriter):
        try:
            f = ftp.FTP()
            f.download(filename, fileWriter)
            f.close()
            return True
        except:
            return False

    # 可下载文件列表刷新
    def dirRefresh(self):
        try:
            f = ftp.FTP()
            li = f.getFileList()
            f.close()
            return li
        except:
            return []


if __name__ == '__main__':
    Login.run()
