# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventana_principal.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 822)
        MainWindow.setStyleSheet("alternate-background-color: rgb(85, 255, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: italic 14pt \"Brush Script MT\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 100, 431, 51))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.entrada_euros = QtWidgets.QLineEdit(self.centralwidget)
        self.entrada_euros.setGeometry(QtCore.QRect(480, 90, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.entrada_euros.setFont(font)
        self.entrada_euros.setObjectName("entrada_euros")
        self.boton_rublo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_rublo.setGeometry(QtCore.QRect(60, 390, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.boton_rublo.setFont(font)
        self.boton_rublo.setObjectName("boton_rublo")
        self.boton_yuan = QtWidgets.QPushButton(self.centralwidget)
        self.boton_yuan.setGeometry(QtCore.QRect(240, 390, 131, 81))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.boton_yuan.setFont(font)
        self.boton_yuan.setObjectName("boton_yuan")
        self.boton_cordoba = QtWidgets.QPushButton(self.centralwidget)
        self.boton_cordoba.setGeometry(QtCore.QRect(640, 390, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.boton_cordoba.setFont(font)
        self.boton_cordoba.setObjectName("boton_cordoba")
        self.boton_dolar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dolar.setGeometry(QtCore.QRect(440, 390, 141, 81))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.boton_dolar.setFont(font)
        self.boton_dolar.setObjectName("boton_dolar")
        self.label_resultado = QtWidgets.QLabel(self.centralwidget)
        self.label_resultado.setGeometry(QtCore.QRect(430, 570, 211, 61))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_resultado.setFont(font)
        self.label_resultado.setText("")
        self.label_resultado.setObjectName("label_resultado")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(250, 540, 171, 101))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.boton_libra = QtWidgets.QPushButton(self.centralwidget)
        self.boton_libra.setGeometry(QtCore.QRect(840, 390, 151, 81))
        font = QtGui.QFont()
        font.setFamily("Brush Script MT")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.boton_libra.setFont(font)
        self.boton_libra.setObjectName("boton_libra")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 34))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "INTRODUCE UNA CANTIDAD DE EUROS:"))
        self.boton_rublo.setText(_translate("MainWindow", "RUBLO: "))
        self.boton_yuan.setText(_translate("MainWindow", "YUAN:"))
        self.boton_cordoba.setText(_translate("MainWindow", "CORDOBA:"))
        self.boton_dolar.setText(_translate("MainWindow", "DOLAR:"))
        self.label_7.setText(_translate("MainWindow", "CONVIERTE...."))
        self.boton_libra.setText(_translate("MainWindow", "LIBRA:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
