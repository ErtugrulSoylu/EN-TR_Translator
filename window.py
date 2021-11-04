from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(270, 103)
        MainWindow.setDockOptions(QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.LeftText = QPlainTextEdit(self.centralwidget)
        self.LeftText.setObjectName(u"LeftText")
        self.LeftText.setGeometry(QRect(10, 20, 91, 31))
        self.LeftText.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.LeftText.setReadOnly(False)
        self.Button = QPushButton(self.centralwidget)
        self.Button.setObjectName(u"Button")
        self.Button.setGeometry(QRect(120, 29, 31, 21))
        self.Button.setStyleSheet(u"font: 20pt \"MS Shell Dlg 2\";\n")
        self.LeftLabel = QLabel(self.centralwidget)
        self.LeftLabel.setObjectName(u"LeftLabel")
        self.LeftLabel.setGeometry(QRect(30, 0, 47, 13))
        self.RightLabel = QLabel(self.centralwidget)
        self.RightLabel.setObjectName(u"RightLabel")
        self.RightLabel.setGeometry(QRect(190, 0, 47, 13))
        self.RightText = QPlainTextEdit(self.centralwidget)
        self.RightText.setObjectName(u"RightText")
        self.RightText.setGeometry(QRect(170, 20, 91, 31))
        self.RightText.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.RightText.setReadOnly(True)
        self.details = QTextEdit(self.centralwidget)
        self.details.setObjectName(u"details")
        self.details.setGeometry(QRect(10, 90, 251, 181))
        self.details.setReadOnly(True)
        self.ExpNrw = QPushButton(self.centralwidget)
        self.ExpNrw.setObjectName(u"ExpNrw")
        self.ExpNrw.setGeometry(QRect(10, 60, 111, 23))
        self.ExitButton = QPushButton(self.centralwidget)
        self.ExitButton.setObjectName(u"ExitButton")
        self.ExitButton.setGeometry(QRect(150, 60, 111, 23))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setSizeGripEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"by Ertugrul", None))
        self.Button.setText(QCoreApplication.translate("MainWindow", u"\u21c4", None))
        self.LeftLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">English</span></p></body></html>", None))
        self.RightLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-weight:600;\">Turkish</span></p></body></html>", None))
        self.ExpNrw.setText(QCoreApplication.translate("MainWindow", u"Expand", None))
        self.ExitButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi