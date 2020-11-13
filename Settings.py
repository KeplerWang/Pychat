from datetime import datetime


class Settings:
    host = 'localhost'
    ftp_host = 'localhost'
    port = 8025
    addr = (host, port)
    mysqlUsr = 'root'
    mysqlPwd = '12345678'
    mysqlDB = 'test'
    mysqlPort = 3306
    msgFrom = 'none'
    password = "none"
    apiUrl = "http://openapi.tuling123.com/openapi/api/v2"


class ConnectionNotEstablishedException(Exception):
    pass


class DataFetchException(Exception):
    pass


class IdExistException(Exception):
    pass


class EmailSendException(Exception):
    pass


def getTime():
    return datetime.now().strftime('[%H:%M:%S] -- ')


settings = Settings()
