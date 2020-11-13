# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'serverDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_serverWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 464, 411))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(20, 0, 20, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.serverStart = QtWidgets.QPushButton(self.layoutWidget)
        self.serverStart.setMinimumSize(QtCore.QSize(100, 30))
        self.serverStart.setMaximumSize(QtCore.QSize(100, 30))
        self.serverStart.setObjectName("serverStart")
        self.horizontalLayout.addWidget(self.serverStart)
        self.serverClose = QtWidgets.QPushButton(self.layoutWidget)
        self.serverClose.setMinimumSize(QtCore.QSize(100, 30))
        self.serverClose.setMaximumSize(QtCore.QSize(100, 30))
        self.serverClose.setObjectName("serverClose")
        self.horizontalLayout.addWidget(self.serverClose)
        self.offLine = QtWidgets.QPushButton(self.layoutWidget)
        self.offLine.setObjectName("offLine")
        self.horizontalLayout.addWidget(self.offLine)
        self.mysqlInit = QtWidgets.QPushButton(self.layoutWidget)
        self.mysqlInit.setMinimumSize(QtCore.QSize(100, 30))
        self.mysqlInit.setMaximumSize(QtCore.QSize(100, 30))
        self.mysqlInit.setObjectName("mysqlInit")
        self.horizontalLayout.addWidget(self.mysqlInit)
        self.gridLayout.addLayout(self.horizontalLayout, 6, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.port = QtWidgets.QLabel(self.layoutWidget)
        self.port.setObjectName("port")
        self.horizontalLayout_4.addWidget(self.port)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.portLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.portLineEdit.setMinimumSize(QtCore.QSize(320, 30))
        self.portLineEdit.setMaximumSize(QtCore.QSize(320, 30))
        self.portLineEdit.setObjectName("portLineEdit")
        self.horizontalLayout_4.addWidget(self.portLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.mysqlpwd = QtWidgets.QLabel(self.layoutWidget)
        self.mysqlpwd.setObjectName("mysqlpwd")
        self.horizontalLayout_3.addWidget(self.mysqlpwd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.mysqlpwdLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.mysqlpwdLineEdit.setMinimumSize(QtCore.QSize(320, 30))
        self.mysqlpwdLineEdit.setMaximumSize(QtCore.QSize(320, 30))
        self.mysqlpwdLineEdit.setObjectName("mysqlpwdLineEdit")
        self.horizontalLayout_3.addWidget(self.mysqlpwdLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.host = QtWidgets.QLabel(self.layoutWidget)
        self.host.setObjectName("host")
        self.horizontalLayout_5.addWidget(self.host)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.hostLineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.hostLineEdit.sizePolicy().hasHeightForWidth())
        self.hostLineEdit.setSizePolicy(sizePolicy)
        self.hostLineEdit.setMinimumSize(QtCore.QSize(320, 30))
        self.hostLineEdit.setMaximumSize(QtCore.QSize(320, 30))
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.horizontalLayout_5.addWidget(self.hostLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 5, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.hostLineEdit, self.portLineEdit)
        MainWindow.setTabOrder(self.portLineEdit, self.mysqlpwdLineEdit)
        MainWindow.setTabOrder(self.mysqlpwdLineEdit, self.serverStart)
        MainWindow.setTabOrder(self.serverStart, self.mysqlInit)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.serverStart.setText(_translate("MainWindow", "启动服务器"))
        self.serverClose.setText(_translate("MainWindow", "退出"))
        self.offLine.setText(_translate("MainWindow", "一键离线"))
        self.mysqlInit.setText(_translate("MainWindow", "数据库初始化"))
        self.port.setText(_translate("MainWindow", "port:"))
        self.mysqlpwd.setText(_translate("MainWindow", "mysqlpwd:"))
        self.host.setText(_translate("MainWindow", "host:"))
