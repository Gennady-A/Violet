# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Db_El2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TextElementWidget(object):
    def setupUi(self, TextElementWidget):
        TextElementWidget.setObjectName("TextElementWidget")
        TextElementWidget.resize(600, 122)
        TextElementWidget.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(76, 72, 102);")
        self.gridLayout = QtWidgets.QGridLayout(TextElementWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Db_Element_gBox = QtWidgets.QGroupBox(TextElementWidget)
        self.Db_Element_gBox.setMaximumSize(QtCore.QSize(16777215, 100))
        self.Db_Element_gBox.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"border: 0px;\n"
"border-bottom: 3px solid rgb(178, 0, 242);\n"
"\n"
"border-top: 3px solid rgb(178, 0, 242);")
        self.Db_Element_gBox.setObjectName("Db_Element_gBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.Db_Element_gBox)
        self.gridLayout_2.setContentsMargins(5, 10, 5, 10)
        self.gridLayout_2.setHorizontalSpacing(5)
        self.gridLayout_2.setVerticalSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.El_Text_tEdit = QtWidgets.QTextEdit(self.Db_Element_gBox)
        self.El_Text_tEdit.setMinimumSize(QtCore.QSize(300, 0))
        self.El_Text_tEdit.setMaximumSize(QtCore.QSize(3000, 60))
        self.El_Text_tEdit.setStyleSheet("border: 3px solid rgb(178, 0, 242);")
        self.El_Text_tEdit.setReadOnly(True)
        self.El_Text_tEdit.setObjectName("El_Text_tEdit")
        self.gridLayout_2.addWidget(self.El_Text_tEdit, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.El_Key_lab = QtWidgets.QLabel(self.Db_Element_gBox)
        self.El_Key_lab.setMaximumSize(QtCore.QSize(200, 100))
        self.El_Key_lab.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(157, 123, 71);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-bottom: 0px;")
        self.El_Key_lab.setObjectName("El_Key_lab")
        self.verticalLayout.addWidget(self.El_Key_lab)
        self.El_Key_lEdit = QtWidgets.QLineEdit(self.Db_Element_gBox)
        self.El_Key_lEdit.setMaximumSize(QtCore.QSize(200, 100))
        self.El_Key_lEdit.setStyleSheet("border: 3px solid rgb(178, 0, 242);")
        self.El_Key_lEdit.setReadOnly(True)
        self.El_Key_lEdit.setObjectName("El_Key_lEdit")
        self.verticalLayout.addWidget(self.El_Key_lEdit)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.El_Date_lab = QtWidgets.QLabel(self.Db_Element_gBox)
        self.El_Date_lab.setMaximumSize(QtCore.QSize(200, 100))
        self.El_Date_lab.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(157, 123, 71);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-bottom: 0px;")
        self.El_Date_lab.setObjectName("El_Date_lab")
        self.verticalLayout_2.addWidget(self.El_Date_lab)
        self.El_Date_lEdit = QtWidgets.QLineEdit(self.Db_Element_gBox)
        self.El_Date_lEdit.setMaximumSize(QtCore.QSize(200, 100))
        self.El_Date_lEdit.setStyleSheet("border: 3px solid rgb(178, 0, 242);")
        self.El_Date_lEdit.setReadOnly(True)
        self.El_Date_lEdit.setObjectName("El_Date_lEdit")
        self.verticalLayout_2.addWidget(self.El_Date_lEdit)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.Db_Element_gBox)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(60, 60))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 3px solid rgb(178, 0, 242);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 3, 1, 1)
        self.gridLayout.addWidget(self.Db_Element_gBox, 0, 0, 1, 1)

        self.retranslateUi(TextElementWidget)
        QtCore.QMetaObject.connectSlotsByName(TextElementWidget)

    def retranslateUi(self, TextElementWidget):
        _translate = QtCore.QCoreApplication.translate
        TextElementWidget.setWindowTitle(_translate("TextElementWidget", "Form"))
        self.Db_Element_gBox.setTitle(_translate("TextElementWidget", "Element"))
        self.El_Key_lab.setText(_translate("TextElementWidget", "Ключ:"))
        self.El_Date_lab.setText(_translate("TextElementWidget", "Время"))
        self.pushButton.setText(_translate("TextElementWidget", "Удалить"))
