from PyQt5.QtGui import QIcon
from ui.LoadWindow import Ui_loadWindow
from Download import run as downloadRun
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QFileDialog
import EventHandle


class Load(QMainWindow, Ui_loadWindow):
    def __init__(self, pool):
        super().__init__()
        self.setupUi(self)
        qssFile = open('qss/LoadQss.qss').read()
        self.setStyleSheet(qssFile)
        self.setWindowTitle('上传下载')
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.meh = EventHandle.EventHandler()
        self.pool = pool
        self.pool.append(self.meh)
        self.uploadPushButton.clicked.connect(self.upload)
        self.downloadPushButton.clicked.connect(self.download)

    def upload(self):
        self.uploadFile, _ = QFileDialog.getOpenFileName(self, '上传文件', 'images/headImages/', 'All files(*.*)')
        if self.uploadFile == "":
            QMessageBox.critical(self, '提示', '您还未选择上传文件')
        else:
            self.meh.uploadClick(self.uploadFile)
            res = self.meh.getULRes()
            if res:
                QMessageBox.information(self, '提示', '上传成功！')
            else:
                QMessageBox.critical(self, '提示', '上传失败！')

    def download(self):
        self._tempWinndow = downloadRun(self.pool)
        self._tempWinndow.show()


def run(pool):
    return Load(pool)
