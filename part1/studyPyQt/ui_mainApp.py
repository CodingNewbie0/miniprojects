# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPyQt\mainApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(281, 162)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(281, 162))
        Form.setMaximumSize(QtCore.QSize(281, 162))
        self.btnOK = QtWidgets.QPushButton(Form)
        self.btnOK.setGeometry(QtCore.QRect(160, 120, 81, 31))
        self.btnOK.setObjectName("btnOK")
        self.lblMessage = QtWidgets.QLabel(Form)
        self.lblMessage.setGeometry(QtCore.QRect(10, 10, 261, 21))
        self.lblMessage.setObjectName("lblMessage")
        self.btnPOP = QtWidgets.QPushButton(Form)
        self.btnPOP.setGeometry(QtCore.QRect(70, 120, 81, 31))
        self.btnPOP.setObjectName("btnPOP")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "메인앱"))
        self.btnOK.setText(_translate("Form", "OK"))
        self.lblMessage.setText(_translate("Form", "메시지 : "))
        self.btnPOP.setText(_translate("Form", "Popup"))
