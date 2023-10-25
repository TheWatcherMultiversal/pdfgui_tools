#! /usr/bin/python3
#
# PDF GUI TOOLS - About
# 
# About - About section, displays information about PDF GUI Tools.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets
from pdfgui_tools_utils import Paths, version_app


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(534, 328)
        MainWindow.setMinimumSize(QtCore.QSize(491, 302))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Paths["icon_app"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(20, 20, 20, 20)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(15)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(Paths["icon_app"]))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 2, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.gridLayout.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setObjectName("button_ok")
        self.gridLayout.addWidget(self.button_ok, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 534, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # User input connection to functions:

        self.button_ok.clicked.connect(self.click_ok)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "About"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/TheWatcherMultiversal/pdfgui_tools\"><span style=\" text-decoration: underline; color:#3484e2;\">Web Page</span></a></p></body></html>"))
        self.label.setText(_translate("MainWindow", "PDF GUI Tools"))
        self.label_3.setText(_translate("MainWindow", f"Version {version_app}"))
        self.label_2.setText(_translate("MainWindow", "PDF GUI Tools is a graphical interface tool that integrates several utilities for managing PDF documents."))
        self.label_4.setText(_translate("MainWindow", "Developed by: Angel M."))
        self.label_5.setText(_translate("MainWindow", "GNU GENERAL PUBLIC LICENSE v3"))
        self.button_ok.setText(_translate("MainWindow", "Ok"))

# ======================================| Modify |=================================================================================+

    # Close window
    def click_ok(self):
        sys.exit()

# =================================================================================================================================+

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    with open(Paths["styles"], "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())