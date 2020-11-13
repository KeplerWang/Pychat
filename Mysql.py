import pymysql
from Settings import *


class Sql:
    message = ''

    def __init__(self):
        try:
            self.insertUsers('0000', '1234', 'Python_QQ群聊', '保密', 'group@hust.edu.cn', 'images/hust.jpg', 'Y')
            self.insertUsers('1000', '1234', '陈建文的小迷妹', '女', 'robot@hust.edu.cn', 'images/avatar.jpg', 'Y')
        except IdExistException:
            pass

    def templateFunc(self, sql):
        database, cur = self._creatConnect()
        cur.execute(sql)
        database.commit()
        self.message = cur.fetchall()
        self._closeConnect(database, cur)

    @staticmethod
    def _creatConnect():
        try:
            database = pymysql.connect(host='localhost', user=settings.mysqlUsr, password=settings.mysqlPwd,
                                       port=settings.mysqlPort, db=settings.mysqlDB)
            cur = database.cursor()
        except pymysql.err.OperationalError:
            database = pymysql.connect(host='localhost', user=settings.mysqlUsr, password=settings.mysqlPwd,
                                       port=settings.mysqlPort)
            cur = database.cursor()
            cur.execute('create database ' + settings.mysqlDB + ' default character set utf8;')
            database.commit()
            cur.execute('use ' + settings.mysqlDB + ';')
            sql = """CREATE TABLE users (
                id CHAR(32) NOT NULL primary key,
                pwd CHAR(32) NOT NULL,
                nickname  CHAR(32) NOT NULL,
                sex CHAR(32) NOT NULL,
                email CHAR(32) NOT NULL,
                headAddr CHAR(64) NOT NULL,
                online CHAR(32) NOT NULL
                );"""
            cur.execute(sql)
            sql = """CREATE TABLE friends (
                id CHAR(32) NOT NULL primary key,
                friend1 CHAR(32),
                friend2 CHAR(32),
                friend3 CHAR(32),
                friend4 CHAR(32),
                friend5 CHAR(32),
                friend6 CHAR(32),
                friend7 CHAR(32)
                );"""
            cur.execute(sql)
        return database, cur

    @staticmethod
    def _closeConnect(database, cur):
        cur.close()
        database.close()

    def insertUsers(self, ID, pwd, nickname, sex, email, headAddr, online):
        sql = """INSERT INTO users(id, pwd, nickname, sex, email, headAddr, online)
                VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (ID, pwd, nickname, sex, email, headAddr, online)
        try:
            self.templateFunc(sql)
            sql = """INSERT INTO friends(id) VALUES('%s');""" % ID
            self.templateFunc(sql)
        except pymysql.err.IntegrityError:
            raise IdExistException from None

    def addFriend(self, ID, friendID):
        if ID == friendID:
            return 'False'  # 自己加自己
        else:
            res1 = self._ifFriends(ID, friendID)
            try:
                res2 = self._ifFriends(friendID, ID)
                if res1:  # 对方是你好友
                    if res2:  # 你是对方好友
                        return 'Already1'  # 都有
                    else:  # 你不是对方好友
                        self._tempFunc(friendID, ID)
                        return 'Already2'  # 你有 他没有
                else:  # 对方不是你好友
                    if res2:  # 你是对方好友
                        self._tempFunc(ID, friendID)
                        return 'Already3'  # 你没有 他有
                    else:  # 你不是对方好友
                        self._tempFunc(ID, friendID)
                        self._tempFunc(friendID, ID)
                        return 'True'  # 都没有
            except IndexError:
                return 'Error'

    def _tempFunc(self, ID, friendID):
        sql = """SELECT * FROM friends WHERE id = '%s';""" % ID
        self.templateFunc(sql)
        numOfNone = self.message[0][1:].count(None)
        numOfAll = len(self.message[0][1:])
        numOfFri = numOfAll - numOfNone
        if numOfNone == 0:
            sql = """ALTER TABLE friends ADD COLUMN friend%d VARCHAR(32);""" % (numOfAll + 1)
            self.templateFunc(sql)
            sql = """UPDATE friends SET friend%d = '%s' WHERE id = '%s';""" % (numOfAll + 1, friendID, ID)
            self.templateFunc(sql)
        else:
            sql = """UPDATE friends SET friend%d = '%s' WHERE id = '%s';""" % (numOfFri + 1, friendID, ID)
            self.templateFunc(sql)

    def getFriendsList(self, ID):
        sql = """SELECT * FROM friends WHERE id = '%s';""" \
              % ID
        self.templateFunc(sql)
        num = len(self.message[0][1:]) - self.message[0][1:].count(None)
        a = self.message[0][1:]
        li = list()
        for i in range(num):
            sql = """SELECT nickname, headAddr, sex, email FROM users WHERE id = '%s';""" % a[i]
            self.templateFunc(sql)
            li.append([self.message[0][0], a[i], self.message[0][1], self.message[0][2], self.message[0][3]])
        return {'num': str(num), 'friendsList': li}

    def getSelfInfo(self, ID):
        sql = """SELECT nickname, sex, email, headAddr FROM users WHERE id = '%s'""" % ID
        self.templateFunc(sql)
        nickname, sex, email, headAddr = self.message[0]
        return {'nickname': nickname, 'sex': sex, 'email': email, 'headAddr': headAddr, 'id': ID}

    def updateOnlineStatus(self, ID, online):
        sql = """UPDATE users SET online = '%s' WHERE id = '%s';""" % (online, ID)
        self.templateFunc(sql)

    def setOffline(self):
        sql = """UPDATE users SET online = 'N' WHERE id <> '1000' AND id <> '0000';"""
        self.templateFunc(sql)

    def loginCheck(self, ID, pwd):
        sql = """SELECT pwd FROM users WHERE id = '%s';""" % ID
        self.templateFunc(sql)
        if self.message:
            return self.message[0][0] == pwd
        else:
            return False

    def _ifFriends(self, friend1, friend2):
        sql = """SELECT * FROM friends WHERE id = '%s'""" % friend1
        self.templateFunc(sql)
        return self.message[0][1:].__contains__(friend2)

    def getOnlineUsers(self):
        sql = """SELECT id FROM users WHERE online != 'N';"""
        self.templateFunc(sql)
        return [msg[0] for msg in self.message]

    def deleteDataBase(self):
        sql = """DROP DATABASE IF EXISTS test;"""
        self.templateFunc(sql)


def init():
    s = Sql()
    s.deleteDataBase()
    s.insertUsers('0000', '1234', 'Python_QQ群聊', '保密', 'group@hust.edu.cn', 'images/hust.jpg', 'Y')
    s.insertUsers('1000', '1234', '陈建文的小迷妹', '女', 'robot@hust.edu.cn', 'images/avatar.jpg', 'Y')


def setOffline():
    s = Sql()
    s.setOffline()


if __name__ == '__main__':
    init()
    Sql().insertUsers('1210', '1234', '陈建文的小迷妹', '女', 'robot@hust.edu.cn', 'images/avatar.jpg', 'N')