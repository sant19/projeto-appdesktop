# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_principal.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("backgroud-color: rgb(8, 8, 8);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 214, 580))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_apenados = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_apenados.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_apenados.setFont(font)
        self.btn_apenados.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_apenados.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.btn_apenados.setObjectName("btn_apenados")
        self.gridLayout_2.addWidget(self.btn_apenados, 0, 0, 1, 1)
        self.btn_pesquisa = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_pesquisa.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_pesquisa.setFont(font)
        self.btn_pesquisa.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_pesquisa.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.btn_pesquisa.setObjectName("btn_pesquisa")
        self.gridLayout_2.addWidget(self.btn_pesquisa, 2, 0, 1, 1)
        self.btn_usuario = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_usuario.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_usuario.setFont(font)
        self.btn_usuario.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_usuario.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.btn_usuario.setObjectName("btn_usuario")
        self.gridLayout_2.addWidget(self.btn_usuario, 3, 0, 1, 1)
        self.btn_relatorio = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.btn_relatorio.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_relatorio.setFont(font)
        self.btn_relatorio.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_relatorio.setStyleSheet("QPushButton{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(255, 255, 255);\n"
"}")
        self.btn_relatorio.setObjectName("btn_relatorio")
        self.gridLayout_2.addWidget(self.btn_relatorio, 1, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 4, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setMinimumSize(QtCore.QSize(560, 0))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 558, 580))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem1, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem2, 8, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem3, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMinimumSize(QtCore.QSize(0, 0))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("pppb.jpeg"))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 5, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_apenados.setText(_translate("MainWindow", "APENADOS"))
        self.btn_pesquisa.setText(_translate("MainWindow", "PESQUISA"))
        self.btn_usuario.setText(_translate("MainWindow", "USUÁRIO"))
        self.btn_relatorio.setText(_translate("MainWindow", "RELATÓRIO"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Governo do Estado da Paraíba</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Controle de Internos</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Penitenciária Pradrão Procurador Romero Nóbrega</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Secretaria de Estado da Administração Penitenciária</span></p></body></html>"))
