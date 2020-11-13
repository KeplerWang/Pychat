import copy
import socket
import urllib.request
from threading import Thread
from Settings import getTime
import Settings
import Mysql
import demjson

clientPool = dict()  # {userID: clientSocket}
groupPool = dict()
chatPool = dict()


class Server:
    def __init__(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 负责监听的socket
        self.serverSocket.bind(Settings.settings.addr)
        self.serverSocket.listen(5)

    def serve_forever(self):
        print(getTime() + 'listening...')
        while True:
            clientSocket, addr = self.serverSocket.accept()
            threads = Thread(target=Handler(clientSocket, addr).handle)
            threads.setDaemon(True)
            threads.start()


class Handler:
    def __init__(self, clientSocket, addr):
        self.clientSocket = clientSocket
        self.clientAddr = addr
        self.mysql = Mysql.Sql()
        self.connectionEstablished = False

    def _sendData(self, data, marker, soc=None):
        size = len(bytes(str(data), encoding='utf-8'))
        if size <= 9:
            length = '00' + str(size)
        elif 9 < size <= 99:
            length = '0' + str(size)
        else:
            length = str(size)
        if soc:
            soc.sendall(bytes(marker + length + str(data), encoding='utf-8'))
        else:
            self.clientSocket.sendall(bytes(marker + length + str(data), encoding='utf-8'))

    def _getData(self):
        marker = self.clientSocket.recv(1).decode()
        if marker == '':
            return 'Null'
        else:
            if not '$#'.__contains__(marker):
                raise Settings.DataFetchException from None
            else:
                length = int(self.clientSocket.recv(3).decode())
                return self.clientSocket.recv(length).decode()

    def _connectionTest(self):
        if not self.connectionEstablished:
            raise Settings.ConnectionNotEstablishedException from None

    def _repostMsg(self):
        messagePool = []
        while True:
            try:
                msg = demjson.decode(self._getData(), encoding='utf8')
                index = ' '.join(sorted([msg['toID'], msg['fromID']]))
                if msg['toID'] != '1000':
                    if msg['type'] == 'exit':
                        m = copy.deepcopy(msg)
                        m['toID'], m['fromID'] = m['fromID'], m['toID']
                        self._sendData(m, '#')
                        chatPool.get(index)[msg['fromID']] = None
                        break
                    elif chatPool.get(index)[msg['toID']]:  # open
                        messagePool.append(msg)
                        for i in messagePool:
                            friendSoc = chatPool.get(index)[msg['toID']]
                            self._sendData(i, '#', friendSoc)
                        messagePool = []
                    else:
                        if msg['type'] != 'exit':
                            messagePool.append(msg)
                elif msg['toID'] == '1000':
                    if msg['type'] == 'exit':
                        self._sendData({'type': 'exit'}, '#')
                        break
                    req = {"perception": {"inputText": {"text": msg['msg']},
                                          "selfInfo": {"location": {"city": "武汉", "province": "湖北省", "street": "东湖"}}},
                           "userInfo": {"apiKey": "dbecb8157b834e21b26a87cb67792788", "userId": "OnlyUseAlphabet"}}
                    req = demjson.encode(req, encoding='utf8')
                    http_post = urllib.request.Request(Settings.settings.apiUrl, data=req, headers={
                        'content-type': 'application/json'})
                    response = urllib.request.urlopen(http_post)
                    response_str = response.read().decode('utf8')
                    response_dic = demjson.decode(response_str, encoding='utf8')
                    results_text = response_dic['results'][0]['values']['text']
                    maps = {"fromID": '1000', "toID": msg['fromID'], "time": getTime()[:-4], "msg": results_text,
                            'fromName': '陈建文的小迷妹', 'type': msg['type']}
                    self._sendData(maps, '#')
            except Exception as e:
                pass

    def _groupTalk(self):
        while bool(groupPool):
            try:
                msg = demjson.decode(self._getData(), encoding='utf8')
                fromID = msg['fromID']
                if msg['type'] != 'exit':
                    for k, v in groupPool.items():
                        if k != fromID:
                            self._sendData(msg, '#', v)
                else:
                    data = {'type': 'exit'}
                    self._sendData(data, '#')
                    groupPool.pop(msg['fromID'])
                    break
            except:
                raise

    def handle(self):
        while True:
            command = self._getData()
            if command == 'Open':
                print(getTime() + 'Get command:', command)
                self.connectionEstablished = True
                self._sendData(getTime() + 'Connection established ' + str(self.clientAddr), '#')
                print(getTime() + 'Connection established ' + str(self.clientAddr))

            elif command == 'Login':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                ID, pwd = self._getData().split(' ')
                if self.mysql.loginCheck(ID, pwd):
                    if self.mysql.getOnlineUsers().__contains__(ID):
                        print(getTime() + str(self.clientAddr), 'Login failed.', ID, 'is already online!')
                        self._sendData('False', '#')
                    else:
                        print(getTime() + str(self.clientAddr), 'login successful!')
                        clientPool.update({ID: self.clientSocket})
                        self.mysql.updateOnlineStatus(ID, 'Y')
                        self._sendData('True', '#')
                        maps = self.mysql.getSelfInfo(ID)
                        maps.update(self.mysql.getFriendsList(ID))
                        self._sendData(maps, '#')
                else:
                    print(getTime() + str(self.clientAddr), 'login failed!')
                    self._sendData('False', '#')

            elif command == 'Logout':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                ID = self._getData()
                self.mysql.updateOnlineStatus(ID, 'N')
                clientPool.pop(ID)

            elif command == 'Register':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                userID, nickname, sex, email, pwd, headAddr = self._getData().split(' ')
                try:
                    self.mysql.insertUsers(userID, pwd, nickname, sex, email, headAddr, 'N')
                    self.mysql.addFriend(userID, '1000')
                    self.mysql.addFriend(userID, '0000')
                    self._sendData('Y', '#')
                except Settings.IdExistException:
                    self._sendData('N', '#')

            elif command == 'Add':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                fromID, toID = self._getData().split(' ')
                self._sendData(self.mysql.addFriend(fromID, toID), '#')

            elif command == 'Refresh':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                ID = self._getData()
                maps = self.mysql.getSelfInfo(ID)
                maps.update(self.mysql.getFriendsList(ID))
                self._sendData(maps, '#')

            elif command == 'Connect':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                myID, toID = self._getData().split(' ')
                index = ' '.join(sorted([myID, toID]))
                x = chatPool.get(index)
                if not x:
                    chatPool.update({index: {myID: self.clientSocket, toID: None}})
                else:
                    chatPool[index][myID] = self.clientSocket
                self._repostMsg()

            elif command == 'Start':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                ifOnline = 'Online' if clientPool.get(self._getData()) else 'Offline'
                self._sendData(ifOnline, '#')

            elif command == 'GroupIn':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                talker = self._getData()
                groupPool[talker] = self.clientSocket
                self._groupTalk()

            elif command == 'Close':
                self._connectionTest()
                print(getTime() + 'Get command:', command)
                self.connectionEstablished = False
                self._sendData(getTime() + 'Connection closed ' + str(self.clientAddr), '#')
                print(getTime() + 'Connection closed ' + str(self.clientAddr))
                self.clientSocket.close()
                break


def run():
    Server().serve_forever()


if __name__ == '__main__':
    run()
