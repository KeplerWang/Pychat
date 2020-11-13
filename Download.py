from progressbar import ProgressBar, Percentage, Bar, ETA, FileTransferSpeed
from PyQt5.QtGui import QIcon
import design
from ui.DownloadWindow import Ui_downloadWindow
from PyQt5.QtWidgets import QMessageBox, QMainWindow, QListWidgetItem
import EventHandle


class MyPB(ProgressBar):
    def __init__(self, maxval=None, widgets=None, term_width=None, poll=1,
                 left_justify=True, fd=None):
        super(MyPB, self).__init__(maxval, widgets, term_width, poll, left_justify, fd)

    def getText(self):
        return self._format_line()


class Download(QMainWindow, Ui_downloadWindow):
    def __init__(self, pool):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('下载')
        qssFile = open('qss/DownloadQss.qss').read()
        self.setStyleSheet(qssFile)
        self.setWindowIcon(QIcon('images/pythonIcon.jpg'))
        self.filePlaceEdit.setText('G:/test_1/stage/')
        self.meh = EventHandle.EventHandler()
        pool.append(self.meh)
        self.splash = design.MySplash()
        self.comfirmButton.clicked.connect(lambda: self._temp(self.fileNameEdit.text(), self.filePlaceEdit.text()))
        self.flashButton.clicked.connect(lambda: self.List())
        self.List()
        self.listWidget.itemDoubleClicked.connect(self.display)  # 双击文件名称显示在输入框内

    def fileWriter(self, data):
        self.file.write(data)
        self.length += len(data)
        self.pb.update(self.length)
        self.splash.setText(self.pb.getText())

    def _temp(self, filename, filepath):
        if filepath == "":
            QMessageBox.critical(self, '提示', '请输入你将要保存的路径')
        else:
            self.file = open(filepath, 'wb')
            size = [i[1] for i in self.dirList if i[0] == filename][0]
            widgets = ['Downloading: ', Percentage(), ' ',
                       Bar(marker='#', left='[', right=']'), ' ', ETA(), ' ', FileTransferSpeed()]
            self.pb = MyPB(widgets=widgets, maxval=size)
            self.length = 0
            self.pb.start()
            self.splash.show()
            self.meh.downloadClick(filename, self.fileWriter)
            self.splash.close()

    def List(self):
        self.listWidget.clear()
        self.meh.dirRefreshClick()
        self.dirList = self.meh.getDirRes()
        for count in self.dirList:
            newItem = QListWidgetItem()
            self.listWidget.addItem(newItem)
            newItem.setText(count[0])

    def display(self, index):
        self.fileNameEdit.setText(self.listWidget.item(self.listWidget.row(index)).text())
        self.filePlaceEdit.setText('../' + self.fileNameEdit.text())


def run(pool):
    return Download(pool)
