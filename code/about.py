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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(491, 302)
        MainWindow.setMinimumSize(QtCore.QSize(491, 302))
        MainWindow.setMaximumSize(QtCore.QSize(491, 302))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pdfgui_tools/assets/pdfguitools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 70, 271, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 30, 121, 141))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("/usr/share/pdfgui_tools/assets/pdfguitools.svg"))
        self.label_6.setObjectName("label_6")
        self.button_ok = QtWidgets.QPushButton(self.centralwidget)
        self.button_ok.setGeometry(QtCore.QRect(240, 220, 91, 24))
        self.button_ok.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 180, 61, 18))
        self.label_7.setOpenExternalLinks(True)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 491, 24))
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
        self.label.setText(_translate("MainWindow", "PDF GUI Tools"))
        self.label_3.setText(_translate("MainWindow", "Version 1.0.0"))
        self.label_2.setText(_translate("MainWindow", "PDF GUI Tools is a graphical user interface tool that integrates the features of poppler-utils."))
        self.label_4.setText(_translate("MainWindow", "© Angel M 2021 - 2023"))
        self.label_5.setText(_translate("MainWindow", "GNU GENERAL PUBLIC LICENSE v3"))
        self.button_ok.setText(_translate("MainWindow", "Ok"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><a href=\"https://github.com/TheWatcherMultiversal/pdfgui_tools\"><span style=\" text-decoration: underline; color:#3484e2;\">Web Page</span></a></p></body></html>"))

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
    with open("/usr/share/pdfgui_tools/styles/about.qss", "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())