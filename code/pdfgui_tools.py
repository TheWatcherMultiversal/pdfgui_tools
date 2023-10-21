#! /usr/bin/python3
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
        MainWindow.resize(830, 502)
        MainWindow.setMinimumSize(QtCore.QSize(381, 339))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pdfgui_tools/assets/pdfguitools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 818, 404))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/home/patatasfritas/Escritorio/Code/pdfgui_tools/icons/pdfguitools.svg"))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_7.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_7.addWidget(self.label_3)
        self.verticalLayout_3.addLayout(self.verticalLayout_7)
        self.poppler_button = QtWidgets.QPushButton(self.groupBox)
        self.poppler_button.setObjectName("poppler_button")
        self.verticalLayout_3.addWidget(self.poppler_button)
        self.pypdf2_button = QtWidgets.QPushButton(self.groupBox)
        self.pypdf2_button.setObjectName("pypdf2_button")
        self.verticalLayout_3.addWidget(self.pypdf2_button)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setContentsMargins(20, 15, 20, -1)
        self.verticalLayout_5.setSpacing(4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.util_label = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.util_label.setFont(font)
        self.util_label.setAlignment(QtCore.Qt.AlignCenter)
        self.util_label.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.util_label)
        self.utils_stacked = QtWidgets.QStackedWidget(self.groupBox_2)
        self.utils_stacked.setObjectName("utils_stacked")
        self.Poppler_page = QtWidgets.QWidget()
        self.Poppler_page.setObjectName("Poppler_page")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.Poppler_page)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pdfunite_button = QtWidgets.QPushButton(self.Poppler_page)
        self.pdfunite_button.setObjectName("pdfunite_button")
        self.verticalLayout.addWidget(self.pdfunite_button)
        self.pdfseparate_button = QtWidgets.QPushButton(self.Poppler_page)
        self.pdfseparate_button.setObjectName("pdfseparate_button")
        self.verticalLayout.addWidget(self.pdfseparate_button)
        self.pdftocairo_button = QtWidgets.QPushButton(self.Poppler_page)
        self.pdftocairo_button.setObjectName("pdftocairo_button")
        self.verticalLayout.addWidget(self.pdftocairo_button)
        self.pdftohtml_button = QtWidgets.QPushButton(self.Poppler_page)
        self.pdftohtml_button.setObjectName("pdftohtml_button")
        self.verticalLayout.addWidget(self.pdftohtml_button)
        self.pdftotext_button = QtWidgets.QPushButton(self.Poppler_page)
        self.pdftotext_button.setObjectName("pdftotext_button")
        self.verticalLayout.addWidget(self.pdftotext_button)
        self.verticalLayout_8.addLayout(self.verticalLayout)
        self.utils_stacked.addWidget(self.Poppler_page)
        self.PyPDF2_page = QtWidgets.QWidget()
        self.PyPDF2_page.setObjectName("PyPDF2_page")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.PyPDF2_page)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setContentsMargins(50, 20, 50, 20)
        self.verticalLayout_9.setSpacing(15)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pypdf2merge_button = QtWidgets.QPushButton(self.PyPDF2_page)
        self.pypdf2merge_button.setObjectName("pypdf2merge_button")
        self.verticalLayout_9.addWidget(self.pypdf2merge_button)
        self.pypdf2separate_button = QtWidgets.QPushButton(self.PyPDF2_page)
        self.pypdf2separate_button.setObjectName("pypdf2separate_button")
        self.verticalLayout_9.addWidget(self.pypdf2separate_button)
        self.pypdf2extract_image_button = QtWidgets.QPushButton(self.PyPDF2_page)
        self.pypdf2extract_image_button.setObjectName("pypdf2extract_image_button")
        self.verticalLayout_9.addWidget(self.pypdf2extract_image_button)
        self.pypdf2extract_text_button = QtWidgets.QPushButton(self.PyPDF2_page)
        self.pypdf2extract_text_button.setObjectName("pypdf2extract_text_button")
        self.verticalLayout_9.addWidget(self.pypdf2extract_text_button)
        self.pypdf2encryption_button = QtWidgets.QPushButton(self.PyPDF2_page)
        self.pypdf2encryption_button.setObjectName("pypdf2encryption_button")
        self.verticalLayout_9.addWidget(self.pypdf2encryption_button)
        self.verticalLayout_10.addLayout(self.verticalLayout_9)
        self.utils_stacked.addWidget(self.PyPDF2_page)
        self.verticalLayout_5.addWidget(self.utils_stacked)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 830, 24))
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

        # Path utilities:
        self.path_utilities    = ("/usr/share/pdfgui_tools")
        self.path_popplerutils = (f"{self.path_utilities}/poppler_utils")
        self.path_pypdf2utils  = (f"{self.path_utilities}/pypdf2_utils")

        # Actions:
        self.actionAbout.triggered.connect(self._about)

        # Buttons - Tool utilities:
        self.poppler_button.clicked.connect(self.poppler_buttons)
        self.pypdf2_button.clicked.connect(self.pypdf2_buttons)

        # Buttons - Poppler-utils:
        self.pdfunite_button.clicked.connect(self.pdfunite)
        self.pdfseparate_button.clicked.connect(self.pdfseparate)
        self.pdftocairo_button.clicked.connect(self.pdftocairo)
        self.pdftohtml_button.clicked.connect(self.pdftohtml)
        self.pdftotext_button.clicked.connect(self.pdftotext)

        # Buttons - PyPDF2:
        self.pypdf2merge_button.clicked.connect(self.pypdf2_merge)
        self.pypdf2separate_button.clicked.connect(self.pypdf2_separate)
        self.pypdf2extract_image_button.clicked.connect(self.pypdf2_extractimage)
        self.pypdf2extract_text_button.clicked.connect(self.pypdf2_extrattext)
        self.pypdf2encryption_button.clicked.connect(self.pypdf2_encryption)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF GUI Tools"))
        self.label.setText(_translate("MainWindow", "PDF GUI Tools"))
        self.groupBox.setTitle(_translate("MainWindow", "Tool utilities"))
        self.label_3.setText(_translate("MainWindow", "PDF GUI TOOLS V1.1.0"))
        self.poppler_button.setText(_translate("MainWindow", "Poppler"))
        self.pypdf2_button.setText(_translate("MainWindow", "PyPDF2"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Utilities"))
        self.util_label.setText(_translate("MainWindow", "Poppler"))
        self.pdfunite_button.setText(_translate("MainWindow", "Merge PDFs"))
        self.pdfseparate_button.setText(_translate("MainWindow", "Separate PDF"))
        self.pdftocairo_button.setText(_translate("MainWindow", "PDF to multimedia file"))
        self.pdftohtml_button.setText(_translate("MainWindow", "PDF to html"))
        self.pdftotext_button.setText(_translate("MainWindow", "PDF to text"))
        self.pypdf2merge_button.setText(_translate("MainWindow", "Merge PDFs"))
        self.pypdf2separate_button.setText(_translate("MainWindow", "Separate PDF"))
        self.pypdf2extract_image_button.setText(_translate("MainWindow", "Extract Images"))
        self.pypdf2extract_text_button.setText(_translate("MainWindow", "Extract Text"))
        self.pypdf2encryption_button.setText(_translate("MainWindow", "Encryption and Decryption PDFs"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


# ======================================| Modify |=================================================================================+

    # >> StackedWidget - Poppler & PyPDF2:
    def poppler_buttons(self): self.utils_stacked.setCurrentIndex(0); self.util_label.setText("Poppler")
    def pypdf2_buttons(self):  self.utils_stacked.setCurrentIndex(1); self.util_label.setText("PyPDF2")
    
    # >> Poppler-utils:

    # Open the 'Merge PDFs' window
    def pdfunite(self):    os.system(f'{self.path_popplerutils}/pdfgui_pdfunite.py')
    # Open the 'Separate PDF' window
    def pdfseparate(self): os.system(f'{self.path_popplerutils}/pdfgui_pdfseparate.py')
    # Open the 'PDF to multimedia file' window
    def pdftocairo(self):  os.system(f'{self.path_popplerutils}/pdfgui_pdftocairo.py')
    # Open the 'PDF to html' window
    def pdftohtml(self):   os.system(f'{self.path_popplerutils}/pdfgui_pdftohtml.py')
    # Open the 'PDF to text' window
    def pdftotext(self):   os.system(f'{self.path_popplerutils}/pdfgui_pdftotext.py')

    # >> PyPDF2:
    
    # Open the 'Merge PDFs' window
    def pypdf2_merge(self):        os.system(f'{self.path_pypdf2utils}/pdfgui_pypdf2_merge.py')
    # Open the 'Separate PDF' window
    def pypdf2_separate(self):     os.system(f'{self.path_pypdf2utils}/pdfgui_pypdf2_separate.py')
    # Open the 'Extract Images' window
    def pypdf2_extractimage(self): os.system(f'{self.path_pypdf2utils}/pdfgui_pypdf2_extractimage.py')
    # Open the 'Extract Text' window
    def pypdf2_extrattext(self):   os.system(f'{self.path_pypdf2utils}/pdfgui_pypdf2_extracttext.py')
    # Open the 'Encryption and Decryption PDFs' window
    def pypdf2_encryption(self):   os.system(f'{self.path_pypdf2utils}/pdfgui_pypdf2_encryption.py')

    # >> About:
    def _about(self): os.system(f'{self.path_utilities}/about.py')

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
