# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPyQt\naverApiSearch.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FrmMain(object):
    def setupUi(self, FrmMain):
        FrmMain.setObjectName("FrmMain")
        FrmMain.setEnabled(True)
        FrmMain.resize(640, 400)
        FrmMain.setMinimumSize(QtCore.QSize(640, 400))
        FrmMain.setMaximumSize(QtCore.QSize(640, 400))
        font = QtGui.QFont()
        font.setFamily("맑은 고딕")
        FrmMain.setFont(font)
        self.verticalLayoutWidget = QtWidgets.QWidget(FrmMain)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 620, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.searchLatout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.searchLatout.setContentsMargins(0, 0, 0, 0)
        self.searchLatout.setObjectName("searchLatout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(30, 24, 551, 31))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.txtsearch = QtWidgets.QLineEdit(self.widget)
        self.txtsearch.setObjectName("txtsearch")
        self.horizontalLayout.addWidget(self.txtsearch)
        self.btnsearch = QtWidgets.QPushButton(self.widget)
        self.btnsearch.setObjectName("btnsearch")
        self.horizontalLayout.addWidget(self.btnsearch)
        self.searchLatout.addWidget(self.groupBox)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(FrmMain)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 90, 621, 301))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lsvResult = QtWidgets.QListView(self.verticalLayoutWidget_2)
        self.lsvResult.setObjectName("lsvResult")
        self.verticalLayout.addWidget(self.lsvResult)

        self.retranslateUi(FrmMain)
        QtCore.QMetaObject.connectSlotsByName(FrmMain)

    def retranslateUi(self, FrmMain):
        _translate = QtCore.QCoreApplication.translate
        FrmMain.setWindowTitle(_translate("FrmMain", "네이버API 뉴스검색"))
        self.groupBox.setTitle(_translate("FrmMain", "뉴스검색"))
        self.label.setText(_translate("FrmMain", "검색어 : "))
        self.btnsearch.setText(_translate("FrmMain", "검색"))