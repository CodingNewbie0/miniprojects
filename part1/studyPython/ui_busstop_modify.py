# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPython\busstop_modify.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(380, 350)
        font = QtGui.QFont()
        font.setFamily("나눔고딕")
        Form.setFont(font)
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(180, 50, 181, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.bus3Cnt = QtWidgets.QLabel(self.groupBox_2)
        self.bus3Cnt.setGeometry(QtCore.QRect(100, 140, 51, 21))
        self.bus3Cnt.setText("")
        self.bus3Cnt.setObjectName("bus3Cnt")
        self.bus2Cnt = QtWidgets.QLabel(self.groupBox_2)
        self.bus2Cnt.setGeometry(QtCore.QRect(100, 90, 50, 20))
        self.bus2Cnt.setText("")
        self.bus2Cnt.setObjectName("bus2Cnt")
        self.bus1Cnt = QtWidgets.QLabel(self.groupBox_2)
        self.bus1Cnt.setGeometry(QtCore.QRect(100, 40, 50, 20))
        self.bus1Cnt.setText("")
        self.bus1Cnt.setObjectName("bus1Cnt")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(20, 40, 50, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 50, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 50, 20))
        self.label_3.setObjectName("label_3")
        self.busPlus = QtWidgets.QPushButton(Form)
        self.busPlus.setGeometry(QtCore.QRect(50, 260, 91, 41))
        self.busPlus.setObjectName("busPlus")
        self.busMinus = QtWidgets.QPushButton(Form)
        self.busMinus.setGeometry(QtCore.QRect(210, 260, 81, 41))
        self.busMinus.setObjectName("busMinus")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 50, 121, 181))
        self.groupBox.setObjectName("groupBox")
        self.btnBus1 = QtWidgets.QPushButton(self.groupBox)
        self.btnBus1.setGeometry(QtCore.QRect(0, 20, 121, 51))
        self.btnBus1.setStyleSheet("background-color:rgb(255,255,255);")
        self.btnBus1.setObjectName("btnBus1")
        self.btnBus2 = QtWidgets.QPushButton(self.groupBox)
        self.btnBus2.setGeometry(QtCore.QRect(0, 70, 121, 51))
        self.btnBus2.setStyleSheet("background-color:rgb(255,255,255);")
        self.btnBus2.setObjectName("btnBus2")
        self.btnBus3 = QtWidgets.QPushButton(self.groupBox)
        self.btnBus3.setGeometry(QtCore.QRect(0, 120, 121, 51))
        self.btnBus3.setStyleSheet("background-color:rgb(255,255,255);")
        self.btnBus3.setObjectName("btnBus3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 10, 131, 31))
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox_2.setTitle(_translate("Form", "Info."))
        self.label.setText(_translate("Form", "탑승인원 : "))
        self.label_2.setText(_translate("Form", "탑승인원 : "))
        self.label_3.setText(_translate("Form", "탑승인원 : "))
        self.busPlus.setText(_translate("Form", "탑승대기"))
        self.busMinus.setText(_translate("Form", "탑승취소"))
        self.groupBox.setTitle(_translate("Form", "BusList"))
        self.btnBus1.setText(_translate("Form", "10번"))
        self.btnBus2.setText(_translate("Form", "100-1번"))
        self.btnBus3.setText(_translate("Form", "155번"))
        self.label_4.setText(_translate("Form", "※용당 Bus STOP※"))
