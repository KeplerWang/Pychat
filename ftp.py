import ftplib
import Settings


class FTP:
    def __init__(self):
        self.f = ftplib.FTP(Settings.settings.ftp_host)
        self.f.encoding = 'utf8'
        self.f.connect()
        self.f.login('Kepler', '063710')
        self.f.set_pasv(True)

    def getFileList(self):
        return [[i, self.f.size(i)] for i in self.f.nlst()]

    def upload(self, filePath):
        try:
            file = open(filePath, 'rb')
            filename = filePath.split('/')[-1]

            self.f.storbinary('STOR ' + filename, file)
            file.close()
            return True
        except Exception as e:
            return False

    def download(self, filename, fileWriter):
        try:
            self.f.retrbinary('RETR ' + filename, fileWriter)
            return True
        except:
            return False

    def close(self):
        self.f.quit()

