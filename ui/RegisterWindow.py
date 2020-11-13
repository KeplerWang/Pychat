# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QLineEdit


class Ui_registerWindow(object):
    def setupUi(self, registerWindow, QtLineEdit=None):
        registerWindow.setObjectName("registerWindow")
        registerWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        registerWindow.resize(438, 565)
        registerWindow.setAutoFillBackground(False)
        registerWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(registerWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(20, -1, 30, -1)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(7)
        self.gridLayout.setVerticalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.headChangePushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.headChangePushButton.sizePolicy().hasHeightForWidth())
        self.headChangePushButton.setSizePolicy(sizePolicy)
        self.headChangePushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.headChangePushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.headChangePushButton.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.headChangePushButton.setObjectName("headChangePushButton")
        self.gridLayout.addWidget(self.headChangePushButton, 0, 0, 1, 7, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 13, 0, 1, 1)
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.idLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.idLabel.setObjectName("idLabel")
        self.gridLayout.addWidget(self.idLabel, 1, 0, 1, 3)
        self.pwdLabel = QtWidgets.QLabel(self.centralwidget)
        self.pwdLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.pwdLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pwdLabel.setObjectName("pwdLabel")
        self.gridLayout.addWidget(self.pwdLabel, 9, 0, 1, 3)
        self.genderLabel = QtWidgets.QLabel(self.centralwidget)
        self.genderLabel.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.genderLabel.sizePolicy().hasHeightForWidth())
        self.genderLabel.setSizePolicy(sizePolicy)
        self.genderLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.genderLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.genderLabel.setObjectName("genderLabel")
        self.gridLayout.addWidget(self.genderLabel, 5, 0, 1, 3)
        self.nickNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.nickNameLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.nickNameLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.nickNameLabel.setObjectName("nickNameLabel")
        self.gridLayout.addWidget(self.nickNameLabel, 3, 0, 1, 3)
        self.emailLabel = QtWidgets.QLabel(self.centralwidget)
        self.emailLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.emailLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.emailLabel.setObjectName("emailLabel")
        self.gridLayout.addWidget(self.emailLabel, 7, 0, 1, 3)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 12, 1, 1, 1)
        self.idLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.idLineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.idLineEdit.sizePolicy().hasHeightForWidth())
        self.idLineEdit.setSizePolicy(sizePolicy)
        self.idLineEdit.setTabletTracking(True)
        self.idLineEdit.setObjectName("idLineEdit")
        self.gridLayout.addWidget(self.idLineEdit, 1, 3, 1, 4)
        self.vcLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.vcLineEdit.sizePolicy().hasHeightForWidth())
        self.vcLineEdit.setSizePolicy(sizePolicy)
        self.vcLineEdit.setTabletTracking(True)
        self.vcLineEdit.setObjectName("vcLineEdit")
        self.gridLayout.addWidget(self.vcLineEdit, 13, 3, 1, 3)
        self.cvPushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cvPushButton.sizePolicy().hasHeightForWidth())
        self.cvPushButton.setSizePolicy(sizePolicy)
        self.cvPushButton.setMouseTracking(True)
        self.cvPushButton.setTabletTracking(True)
        self.cvPushButton.setObjectName("cvPushButton")
        self.gridLayout.addWidget(self.cvPushButton, 13, 6, 1, 1)
        self.nickNameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nickNameLineEdit.sizePolicy().hasHeightForWidth())
        self.nickNameLineEdit.setSizePolicy(sizePolicy)
        self.nickNameLineEdit.setTabletTracking(True)
        self.nickNameLineEdit.setObjectName("nickNameLineEdit")
        self.gridLayout.addWidget(self.nickNameLineEdit, 3, 3, 1, 4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 5, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem4, 8, 1, 1, 1)
        self.emailLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.emailLineEdit.sizePolicy().hasHeightForWidth())
        self.emailLineEdit.setSizePolicy(sizePolicy)
        self.emailLineEdit.setTabletTracking(True)
        self.emailLineEdit.setObjectName("emailLineEdit")
        self.gridLayout.addWidget(self.emailLineEdit, 7, 3, 1, 4)
        self.resureLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.resureLineEdit.sizePolicy().hasHeightForWidth())
        self.resureLineEdit.setSizePolicy(sizePolicy)
        self.resureLineEdit.setTabletTracking(True)
        self.resureLineEdit.setObjectName("resureLineEdit")
        self.gridLayout.addWidget(self.resureLineEdit, 11, 3, 1, 4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem5, 2, 1, 1, 1)
        self.vcLabel = QtWidgets.QLabel(self.centralwidget)
        self.vcLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.vcLabel.setTabletTracking(True)
        self.vcLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.vcLabel.setObjectName("vcLabel")
        self.gridLayout.addWidget(self.vcLabel, 13, 1, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem6, 10, 1, 1, 1)
        self.pwdLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pwdLineEdit.sizePolicy().hasHeightForWidth())
        self.pwdLineEdit.setSizePolicy(sizePolicy)
        self.pwdLineEdit.setTabletTracking(True)
        self.pwdLineEdit.setObjectName("pwdLineEdit")
        self.gridLayout.addWidget(self.pwdLineEdit, 9, 3, 1, 4)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMaximumSize(QtCore.QSize(60, 35))
        self.comboBox.setMouseTracking(True)
        self.comboBox.setTabletTracking(True)
        self.comboBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.comboBox.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.comboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox.setEditable(False)
        self.comboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.comboBox.setIconSize(QtCore.QSize(10, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 5, 3, 1, 2)
        self.resureLabel = QtWidgets.QLabel(self.centralwidget)
        self.resureLabel.setMaximumSize(QtCore.QSize(35, 35))
        self.resureLabel.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.resureLabel.setObjectName("resureLabel")
        self.gridLayout.addWidget(self.resureLabel, 11, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.surePushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.surePushButton.sizePolicy().hasHeightForWidth())
        self.surePushButton.setSizePolicy(sizePolicy)
        self.surePushButton.setMouseTracking(True)
        self.surePushButton.setTabletTracking(True)
        self.surePushButton.setObjectName("surePushButton")
        self.horizontalLayout.addWidget(self.surePushButton)
        self.canclePushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.canclePushButton.sizePolicy().hasHeightForWidth())
        self.canclePushButton.setSizePolicy(sizePolicy)
        self.canclePushButton.setMouseTracking(True)
        self.canclePushButton.setTabletTracking(True)
        self.canclePushButton.setObjectName("canclePushButton")
        self.horizontalLayout.addWidget(self.canclePushButton)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem8)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)
        registerWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(registerWindow)
        self.statusbar.setObjectName("statusbar")
        registerWindow.setStatusBar(self.statusbar)
        self.idLineEdit.setPlaceholderText("请输入账号")
        self.nickNameLineEdit.setPlaceholderText("请输入昵称")
        self.emailLineEdit.setPlaceholderText("请输入邮箱")
        self.pwdLineEdit.setPlaceholderText("请输入密码")
        self.resureLineEdit.setPlaceholderText("确认密码")
        self.vcLineEdit.setPlaceholderText("请输入验证码")

        self.pwdLineEdit.setEchoMode(QLineEdit.Password)
        self.resureLineEdit.setEchoMode(QLineEdit.Password)


        self.retranslateUi(registerWindow)

        QtCore.QMetaObject.connectSlotsByName(registerWindow)
        registerWindow.setTabOrder(self.idLineEdit, self.nickNameLineEdit)
        registerWindow.setTabOrder(self.nickNameLineEdit, self.comboBox)
        registerWindow.setTabOrder(self.comboBox, self.emailLineEdit)
        registerWindow.setTabOrder(self.emailLineEdit, self.pwdLineEdit)
        registerWindow.setTabOrder(self.pwdLineEdit, self.resureLineEdit)
        registerWindow.setTabOrder(self.resureLineEdit, self.vcLineEdit)
        registerWindow.setTabOrder(self.vcLineEdit, self.cvPushButton)
        registerWindow.setTabOrder(self.cvPushButton, self.surePushButton)
        registerWindow.setTabOrder(self.surePushButton, self.canclePushButton)

    def retranslateUi(self, registerWindow):
        _translate = QtCore.QCoreApplication.translate
        registerWindow.setWindowTitle(_translate("registerWindow", "MainWindow"))
        self.headChangePushButton.setText(_translate("registerWindow", "更改头像"))
        self.idLabel.setText(_translate("registerWindow", ""))
        self.pwdLabel.setText(_translate("registerWindow", ""))
        self.genderLabel.setText(_translate("registerWindow", ""))
        self.nickNameLabel.setText(_translate("registerWindow", ""))
        self.emailLabel.setText(_translate("registerWindow", ""))
        self.cvPushButton.setText(_translate("registerWindow", "获取验证码"))
        self.vcLabel.setText(_translate("registerWindow", ""))
        self.comboBox.setItemText(0, _translate("registerWindow", "男"))
        self.comboBox.setItemText(1, _translate("registerWindow", "女"))
        self.resureLabel.setText(_translate("registerWindow", ""))
        self.surePushButton.setText(_translate("registerWindow", "确定"))
        self.canclePushButton.setText(_translate("registerWindow", "取消"))
