# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Source\miniprojects\part1\studyPython\qrcodeApp.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 390)
        Form.setMinimumSize(QtCore.QSize(320, 390))
        Form.setMaximumSize(QtCore.QSize(320, 390))
        self.lblQrCode = QtWidgets.QLabel(Form)
        self.lblQrCode.setGeometry(QtCore.QRect(10, 10, 300, 300))
        self.lblQrCode.setStyleSheet("background-color : rgb(0, 0, 0);")
        self.lblQrCode.setObjectName("lblQrCode")
        self.btnQrGen = QtWidgets.QPushButton(Form)
        self.btnQrGen.setGeometry(QtCore.QRect(240, 360, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnQrGen.sizePolicy().hasHeightForWidth())
        self.btnQrGen.setSizePolicy(sizePolicy)
        self.btnQrGen.setObjectName("btnQrGen")
        self.txtQrData = QtWidgets.QLineEdit(Form)
        self.txtQrData.setGeometry(QtCore.QRect(10, 330, 301, 20))
        self.txtQrData.setObjectName("txtQrData")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QRCODE App"))
        self.lblQrCode.setText(_translate("Form", "TextLabel"))
        self.btnQrGen.setText(_translate("Form", "Generate"))
