import demjson
import Client as _Socket
from VerifyEmail import sendVerifyEmail
from Settings import EmailSendException


class EventHandler:
    _loginRes = False
    _emailSendRes = False
    _emailChange = False
    _verifyCodeCheckRes = False
    _pwdMatchRes = False
    _regRes = False
    verifyCode = ''
    _email = ''
    _info = {}
    _addRes = ''
    _refreshRes = {}
    _downloadRes = False
    _uploadRes = False
    _fileList = []
    _chatTag = True

    def __init__(self):
        self.s = _Socket.Socket()
        self.s.openConnection()

    @staticmethod
    def _delWhiteSpace(string):
        return ''.join(string.strip().split(' '))

    # 点击登录
    def loginClick(self, userID, pwd):
        userID = self._delWhiteSpace(userID)
        pwd = self._delWhiteSpace(pwd)
        res, info = self.s.login(userID + ' ' + pwd)
        self._loginRes, self._info = (True, info) if res else (False, None)

    # 点击生成验证码 (之后若邮件发送失败, 要弹窗)
    def getVerifyCodeClick(self, email):
        try:
            self.verifyCode = sendVerifyEmail(self._delWhiteSpace(email))
            self._emailSendRes = True
            self._email = email
            self._emailChange = False
        except EmailSendException:
            self._emailSendRes = False

    # 点击注册 (若验证码不对, 要弹窗; 若账号已存在, 要弹窗; 若前后密码不一致, 要弹窗; 注册成功, 要弹窗)
    def registerInfoClick(self, userID, nickname, sex, email, pwd, ackPwd, verifyCodeIn, headAddr):
        userID = self._delWhiteSpace(userID)
        nickname = self._delWhiteSpace(nickname)
        sex = self._delWhiteSpace(sex)
        email = self._delWhiteSpace(email)
        pwd = self._delWhiteSpace(pwd)
        ackPwd = self._delWhiteSpace(ackPwd)
        verifyCodeIn = self._delWhiteSpace(verifyCodeIn)
        headAddr = self._delWhiteSpace(headAddr)
        if self._email != email:
            self._emailChange = True
        else:
            if verifyCodeIn.upper() == self.verifyCode:
                self._verifyCodeCheckRes = True
                if pwd == ackPwd:
                    self._pwdMatchRes = True
                    self._regRes = self.s.register(userID + ' ' + nickname + ' ' + sex + ' ' + email + ' ' + pwd + ' '
                                                   + headAddr)
                else:
                    self._pwdMatchRes = False
            else:
                self._verifyCodeCheckRes = False

    # 邮件是否发送成功
    def getEmailRes(self):
        return self._emailSendRes

    # 检查是否成功获取验证码后，又更改邮箱
    def getEmailChangeRes(self):
        return self._emailChange

    # 验证码是否匹配
    def getVCRes(self):
        return self._verifyCodeCheckRes

    # 两次密码是否一致
    def getPwdMatchRes(self):
        return self._pwdMatchRes

    # 注册是否成功
    def getRegRes(self):
        return self._regRes

    # 登录是否成功
    def getLoginRes(self):
        return self._loginRes, self._info['headAddr'] if self._info else None

    # 获取登录后用户信息
    def getInfoPkt(self):
        return self._info

    # 添加好友
    def addFriendClick(self, fromID):
        self._addRes = self.s.addFriend(fromID)

    # 获取加好友的结果
    def getAddRes(self):
        return self._addRes

    # 刷新好友列表
    def refreshListClick(self):
        self._refreshRes = self.s.refresh()

    # 返回刷新结果
    def getRefreshRes(self):
        return self._refreshRes

    # 点击主窗口的用户尝试聊天
    def userChatClick(self, toID):
        return self.s.chatStart(toID)

    def connect(self, toID):
        self.s.connect(toID)

    # 发送消息
    def send(self, msg):
        self.s.sendData(str(msg), '#')

    # 接收消息
    def recv(self):
        try:
            return demjson.decode(self.s.getData(), encoding='utf8')
        except Exception:
            print('error in handle_recv')

    # 退出登录
    def logoutClick(self):
        self.s.logout()
        self.s.closeConnection()

    # 上传文件
    def uploadClick(self, filePath):
        self._uploadRes = self.s.upload(filePath)

    # 下载文件
    def downloadClick(self, filename, fileWriter):
        self._downloadRes = self.s.download(filename, fileWriter)

    # 可下载文件列表刷新
    def dirRefreshClick(self):
        self._fileList = self.s.dirRefresh()

    # 下载是否成功 不成功弹窗
    def getDLRes(self):
        return self._downloadRes

    # 上传是否成功 不成功弹窗
    def getULRes(self):
        return self._uploadRes

    # 获取文件列表
    def getDirRes(self):
        return self._fileList
