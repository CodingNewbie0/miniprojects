# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPython\comInfo.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(370, 240)
        Form.setMinimumSize(QtCore.QSize(370, 240))
        Form.setMaximumSize(QtCore.QSize(370, 240))
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 120, 351, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lblExtraNet = QtWidgets.QLabel(self.groupBox_3)
        self.lblExtraNet.setGeometry(QtCore.QRect(120, 40, 221, 16))
        self.lblExtraNet.setObjectName("lblExtraNet")
        self.lblInnerNet = QtWidgets.QLabel(self.groupBox_3)
        self.lblInnerNet.setGeometry(QtCore.QRect(120, 20, 221, 16))
        self.lblInnerNet.setObjectName("lblInnerNet")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label.setStyleSheet("font-weight: bold;")
        self.label.setObjectName("label")
        self.lblNetStat = QtWidgets.QLabel(self.groupBox_3)
        self.lblNetStat.setGeometry(QtCore.QRect(120, 60, 221, 16))
        self.lblNetStat.setObjectName("lblNetStat")
        self.label_25 = QtWidgets.QLabel(self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_25.setStyleSheet("font-weight: bold;")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_26.setStyleSheet("font-weight: bold;")
        self.label_26.setObjectName("label_26")
        self.btnRefresh = QtWidgets.QPushButton(Form)
        self.btnRefresh.setGeometry(QtCore.QRect(290, 200, 75, 31))
        self.btnRefresh.setObjectName("btnRefresh")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 351, 101))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lblDisk = QtWidgets.QLabel(self.groupBox_2)
        self.lblDisk.setGeometry(QtCore.QRect(120, 80, 221, 16))
        self.lblDisk.setObjectName("lblDisk")
        self.lblCore = QtWidgets.QLabel(self.groupBox_2)
        self.lblCore.setGeometry(QtCore.QRect(120, 40, 221, 16))
        self.lblCore.setObjectName("lblCore")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 101, 16))
        self.label_3.setStyleSheet("font-weight: bold;")
        self.label_3.setObjectName("label_3")
        self.lblCPU = QtWidgets.QLabel(self.groupBox_2)
        self.lblCPU.setGeometry(QtCore.QRect(120, 20, 221, 16))
        self.lblCPU.setObjectName("lblCPU")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 101, 16))
        self.label_2.setStyleSheet("font-weight: bold;")
        self.label_2.setObjectName("label_2")
        self.lblMemory = QtWidgets.QLabel(self.groupBox_2)
        self.lblMemory.setGeometry(QtCore.QRect(120, 60, 221, 16))
        self.lblMemory.setObjectName("lblMemory")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 40, 101, 16))
        self.label_17.setStyleSheet("font-weight: bold;")
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_18.setStyleSheet("font-weight: bold;")
        self.label_18.setObjectName("label_18")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "내 컴퓨터 정보"))
        self.groupBox_3.setTitle(_translate("Form", "네트워크 정보"))
        self.lblExtraNet.setText(_translate("Form", "외부아이피"))
        self.lblInnerNet.setText(_translate("Form", "내부아이피"))
        self.label.setText(_translate("Form", "내부아이피"))
        self.lblNetStat.setText(_translate("Form", "전송상태"))
        self.label_25.setText(_translate("Form", "외부아이피"))
        self.label_26.setText(_translate("Form", "전송상태"))
        self.btnRefresh.setText(_translate("Form", "새로고침"))
        self.groupBox_2.setTitle(_translate("Form", "컴퓨터 정보"))
        self.lblDisk.setText(_translate("Form", "디스크"))
        self.lblCore.setText(_translate("Form", "코어"))
        self.label_3.setText(_translate("Form", "디스크"))
        self.lblCPU.setText(_translate("Form", "CPU(속도)"))
        self.label_2.setText(_translate("Form", "CPU(속도)"))
        self.lblMemory.setText(_translate("Form", "메모리"))
        self.label_17.setText(_translate("Form", "코어"))
        self.label_18.setText(_translate("Form", "메모리"))
