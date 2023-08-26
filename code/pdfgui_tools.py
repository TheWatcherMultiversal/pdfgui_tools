#
# PDF GUI TOOLS
# 
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 283)
        MainWindow.setMinimumSize(QtCore.QSize(381, 283))
        MainWindow.setMaximumSize(QtCore.QSize(381, 283))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pdfgui_tools/assets/pdfguitools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 10, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(100, 70, 181, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pdfunite_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pdfunite_button.setObjectName("pdfunite_button")
        self.verticalLayout.addWidget(self.pdfunite_button)
        self.pdftohtml_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pdftohtml_button.setObjectName("pdftohtml_button")
        self.verticalLayout.addWidget(self.pdftohtml_button)
        self.pdftotext_button = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pdftotext_button.setObjectName("pdftotext_button")
        self.verticalLayout.addWidget(self.pdftotext_button)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 24))
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # User input connection to functions:

        # Actions
        self.actionAbout.triggered.connect(self._about)

        # Buttons
        self.pdfunite_button.clicked.connect(self.pdfunite)
        self.pdftohtml_button.clicked.connect(self.pdftohtml)
        self.pdftotext_button.clicked.connect(self.pdftohtml)
        

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF GUI Tools"))
        self.label.setText(_translate("MainWindow", "PDF gui Tools"))
        self.pdfunite_button.setText(_translate("MainWindow", "Merge PDFs"))
        self.pdftohtml_button.setText(_translate("MainWindow", "PDF to html"))
        self.pdftotext_button.setText(_translate("MainWindow", "PDF to text"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

# ======================================| Modify |=================================================================================+

    # Open the 'Merge PDFs' window
    def pdfunite(self):
        os.system('python3 /usr/share/pdfgui_tools/pdfgui_pdfunite.py')

    # Open the 'PDF to html' window
    def pdftohtml(self):
        os.system('python3 /usr/share/pdfgui_tools/pdfgui_pdftohtml.py')

    # Open the 'PDF to text' window
    def pdftotext(self):
        os.system('python3 /usr/share/pdfgui_tools/pdfgui_pdftotext.py')

    # Open the 'About' window
    def _about(self):
        os.system('python3 /usr/share/pdfgui_tools/about.py')

# =================================================================================================================================+

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    with open("/usr/share/pdfgui_tools/styles/styles.qss", "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())