# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HelpWindow(object):
    def setupUi(self, HelpWindow):
        HelpWindow.setObjectName("HelpWindow")
        HelpWindow.resize(1000, 700)
        HelpWindow.setMinimumSize(QtCore.QSize(900, 600))
        HelpWindow.setStyleSheet("background-color: rgb(106, 104, 98);\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(76, 72, 102);")
        self.centralwidget = QtWidgets.QWidget(HelpWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Header_Lay = QtWidgets.QHBoxLayout()
        self.Header_Lay.setContentsMargins(-1, -1, 0, -1)
        self.Header_Lay.setObjectName("Header_Lay")
        self.Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Header_lab.setMinimumSize(QtCore.QSize(0, 60))
        self.Header_lab.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.Header_lab.setFont(font)
        self.Header_lab.setStyleSheet("background-color: rgb(52, 52, 52);\n"
"color: rgb(255, 255, 255);\n"
"border-bottom: 3px solid rgb(178, 0, 242);")
        self.Header_lab.setWordWrap(True)
        self.Header_lab.setObjectName("Header_lab")
        self.Header_lab.setMargin(5)
        self.Header_Lay.addWidget(self.Header_lab)
        self.gridLayout.addLayout(self.Header_Lay, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Enc_Layout_2 = QtWidgets.QVBoxLayout()
        self.Enc_Layout_2.setSpacing(0)
        self.Enc_Layout_2.setObjectName("Enc_Layout_2")
        self.Hist_Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Hist_Header_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.Hist_Header_lab.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Hist_Header_lab.setFont(font)
        self.Hist_Header_lab.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);")
        self.Hist_Header_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Hist_Header_lab.setObjectName("Hist_Header_lab")
        self.Enc_Layout_2.addWidget(self.Hist_Header_lab)
        self.Hist_Text_lab = QtWidgets.QLabel(self.centralwidget)
        self.Hist_Text_lab.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-top: 0px;\n"
"\n"
"background-color: rgb(102, 102, 131);")
        self.Hist_Text_lab.setTextFormat(QtCore.Qt.RichText)
        self.Hist_Text_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Hist_Text_lab.setWordWrap(True)
        self.Hist_Text_lab.setObjectName("Hist_Text_lab")
        self.Enc_Layout_2.addWidget(self.Hist_Text_lab)
        self.horizontalLayout_2.addLayout(self.Enc_Layout_2)
        self.Dec_Layout_2 = QtWidgets.QVBoxLayout()
        self.Dec_Layout_2.setSpacing(0)
        self.Dec_Layout_2.setObjectName("Dec_Layout_2")
        self.Db_Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Db_Header_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.Db_Header_lab.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Db_Header_lab.setFont(font)
        self.Db_Header_lab.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);")
        self.Db_Header_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Db_Header_lab.setObjectName("Db_Header_lab")
        self.Dec_Layout_2.addWidget(self.Db_Header_lab)
        self.Db_Text_lab = QtWidgets.QLabel(self.centralwidget)
        self.Db_Text_lab.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-top: 0px;\n"
"\n"
"background-color: rgb(102, 102, 131);")
        self.Db_Text_lab.setTextFormat(QtCore.Qt.RichText)
        self.Db_Text_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Db_Text_lab.setWordWrap(True)
        self.Db_Text_lab.setObjectName("Db_Text_lab")
        self.Dec_Layout_2.addWidget(self.Db_Text_lab)
        self.horizontalLayout_2.addLayout(self.Dec_Layout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 0, 10, -1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Enc_Layout = QtWidgets.QVBoxLayout()
        self.Enc_Layout.setSpacing(0)
        self.Enc_Layout.setObjectName("Enc_Layout")
        self.Enc_Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Enc_Header_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.Enc_Header_lab.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Enc_Header_lab.setFont(font)
        self.Enc_Header_lab.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);")
        self.Enc_Header_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Enc_Header_lab.setObjectName("Enc_Header_lab")
        self.Enc_Layout.addWidget(self.Enc_Header_lab)
        self.Enc_Text_lab = QtWidgets.QLabel(self.centralwidget)
        self.Enc_Text_lab.setMinimumSize(QtCore.QSize(300, 0))
        self.Enc_Text_lab.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-top: 0px;\n"
"\n"
"background-color: rgb(142, 141, 158);\n"
"background-color: rgb(102, 102, 131);")
        self.Enc_Text_lab.setTextFormat(QtCore.Qt.RichText)
        self.Enc_Text_lab.setScaledContents(False)
        self.Enc_Text_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Enc_Text_lab.setWordWrap(True)
        self.Enc_Text_lab.setObjectName("Enc_Text_lab")
        self.Enc_Layout.addWidget(self.Enc_Text_lab)
        self.horizontalLayout.addLayout(self.Enc_Layout)
        self.Dec_Layout = QtWidgets.QVBoxLayout()
        self.Dec_Layout.setSpacing(0)
        self.Dec_Layout.setObjectName("Dec_Layout")
        self.Dec_Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Dec_Header_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.Dec_Header_lab.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Dec_Header_lab.setFont(font)
        self.Dec_Header_lab.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);")
        self.Dec_Header_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Dec_Header_lab.setObjectName("Dec_Header_lab")
        self.Dec_Layout.addWidget(self.Dec_Header_lab)
        self.Dec_Text_lab = QtWidgets.QLabel(self.centralwidget)
        self.Dec_Text_lab.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-top: 0px;\n"
"\n"
"background-color: rgb(102, 102, 131);")
        self.Dec_Text_lab.setTextFormat(QtCore.Qt.RichText)
        self.Dec_Text_lab.setScaledContents(False)
        self.Dec_Text_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Dec_Text_lab.setWordWrap(True)
        self.Dec_Text_lab.setObjectName("Dec_Text_lab")
        self.Dec_Layout.addWidget(self.Dec_Text_lab)
        self.horizontalLayout.addLayout(self.Dec_Layout)
        self.Break_Layout = QtWidgets.QVBoxLayout()
        self.Break_Layout.setSpacing(0)
        self.Break_Layout.setObjectName("Break_Layout")
        self.Break_Header_lab = QtWidgets.QLabel(self.centralwidget)
        self.Break_Header_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.Break_Header_lab.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Break_Header_lab.setFont(font)
        self.Break_Header_lab.setStyleSheet("background-color: rgb(76, 76, 76);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);")
        self.Break_Header_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.Break_Header_lab.setObjectName("Break_Header_lab")
        self.Break_Layout.addWidget(self.Break_Header_lab)
        self.Break_Text_lab = QtWidgets.QLabel(self.centralwidget)
        self.Break_Text_lab.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(178, 0, 242);\n"
"border-top: 0px;\n"
"\n"
"background-color: rgb(102, 102, 131);")
        self.Break_Text_lab.setTextFormat(QtCore.Qt.RichText)
        self.Break_Text_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.Break_Text_lab.setWordWrap(True)
        self.Break_Text_lab.setObjectName("Break_Text_lab")
        self.Break_Layout.addWidget(self.Break_Text_lab)
        self.horizontalLayout.addLayout(self.Break_Layout)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        HelpWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HelpWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 26))
        self.menubar.setObjectName("menubar")
        HelpWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HelpWindow)
        self.statusbar.setObjectName("statusbar")
        HelpWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HelpWindow)
        QtCore.QMetaObject.connectSlotsByName(HelpWindow)

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "HelpWindow"))
        self.Header_lab.setText(_translate("HelpWindow", "Violet - шифровальщик текста с функцией дешифровки, взлома шифра посредством \"протягивания слова\" по тексту и сохранения записей в базу данных приложения. Подробнее функционал приложения описан ниже. "))
        self.Hist_Header_lab.setText(_translate("HelpWindow", "Гистограмма"))
        self.Hist_Text_lab.setText(_translate("HelpWindow", "Гистограмма - удобная возможность представить распределение букв в тексте. По нажатию клавиши программа проанализирует введённый текст и выведет в новое окно гистограмму распределения букв в тексте в порядке убывания частотности."))
        self.Db_Header_lab.setText(_translate("HelpWindow", "База данных"))
        self.Db_Text_lab.setText(_translate("HelpWindow", "База данных - удобный способ не потерять свои шифры и ключи от них. В данной программе сохранить введённый текст можно клавишей \"Сохранить\". В случае, если текст был зашифрован - вместе с ним сохранится и ключ от него."))
        self.Enc_Header_lab.setText(_translate("HelpWindow", "Шифровка"))
        self.Enc_Text_lab.setText(_translate("HelpWindow", "Шифровка осуществляется посредством нажатия на клавишу \"шифровка\". Предустановка осуществляется в боковом меню справа - для шифра сначала необходимо установить ключ(кроме шифра инверсией) в раздел \"ключ\". В зависимости от типа шифра к ключу могут предъявляться разные требования по содержанию."))
        self.Dec_Header_lab.setText(_translate("HelpWindow", "Расшифровка"))
        self.Dec_Text_lab.setText(_translate("HelpWindow", "Расшифровка проходит образом, схожим с процессом шифровки: необходимо сначала установить ключ(шифровка инверсией - исключение), а затем нажать на клавишу \"Расшифровка\"."))
        self.Break_Header_lab.setText(_translate("HelpWindow", "Взлом"))
        self.Break_Text_lab.setText(_translate("HelpWindow", "Взлом - сильно сказано. В приложении используется простой метод протяжки предполагаемого слова по тексту. При этом методе вам необходимо ввести слово, которое, как вы предполагаете, может содержаться в шифре. После этого вам нужно ввести предпологаемую силу ключа(длинну) и запустить процесс подбора клавишей \"Запуск\". Приложение начнёт перебирать ключи, расшифровывать по ним текст и проверят, на наличие искомого слова. Набор возможных ключей возвращается в список ключей."))
