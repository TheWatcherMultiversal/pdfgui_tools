#! /usr/bin/python3
#
# PDF GUI TOOLS - pypdf2encrypt
# 
# pypdf2encrypt - Encrypt or Decrypt PDF Documents.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfgui_tools_utils import Paths, encrypt_pdf, decrypt_pdf
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 453)
        MainWindow.setMinimumSize(QtCore.QSize(1036, 453))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Paths["icon_app"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_3.setContentsMargins(20, 35, 20, 20)
        self.gridLayout_3.setHorizontalSpacing(2)
        self.gridLayout_3.setVerticalSpacing(20)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 222, 86))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_3.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 2000000000, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_password.setAcceptDrops(False)
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_4.addWidget(self.lineEdit_password)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 2)
        self.button_view = QtWidgets.QPushButton(self.groupBox_2)
        self.button_view.setObjectName("button_view")
        self.gridLayout_3.addWidget(self.button_view, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(20, 35, 20, 20)
        self.gridLayout_2.setSpacing(20)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setAcceptDrops(True)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_add = QtWidgets.QPushButton(self.groupBox)
        self.button_add.setObjectName("button_add")
        self.verticalLayout_2.addWidget(self.button_add)
        self.button_delete = QtWidgets.QPushButton(self.groupBox)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout_2.addWidget(self.button_delete)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.button_encrypt = QtWidgets.QPushButton(self.groupBox)
        self.button_encrypt.setObjectName("button_merge")
        self.verticalLayout.addWidget(self.button_encrypt)
        self.button_decrypt = QtWidgets.QPushButton(self.groupBox)
        self.button_decrypt.setObjectName("button_decrypt")
        self.verticalLayout.addWidget(self.button_decrypt)
        self.label_notice = QtWidgets.QLabel(self.groupBox)
        self.label_notice.setObjectName("label_notice")
        self.verticalLayout.addWidget(self.label_notice)
        self.gridLayout_2.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(0, 10)
        self.horizontalLayout.setStretch(1, 26)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAdd_File = QtWidgets.QAction(MainWindow)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEncrypt = QtWidgets.QAction(MainWindow)
        self.actionEncrypt.setWhatsThis("")
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtWidgets.QAction(MainWindow)
        self.actionDecrypt.setWhatsThis("")
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionEncrypt)
        self.menuFile.addAction(self.actionDecrypt)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # Dictionary of PDF Information
        self.dictPDFs = {}

        # Disable Elements
        self.button_view.setEnabled(False)

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionHelp.triggered.connect(self._help)
        self.actionAbout.triggered.connect(self._about)
        self.actionExit.triggered.connect(self._exit)
        self.actionEncrypt.triggered.connect(lambda: self.encrypt_decrypt(True))
        self.actionDecrypt.triggered.connect(lambda: self.encrypt_decrypt(False))

        # Buttons
        self.button_view.clicked.connect(self.click_view)
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_encrypt.clicked.connect(lambda: self.encrypt_decrypt(True))
        self.button_decrypt.clicked.connect(lambda: self.encrypt_decrypt(False))

        # listWidget:
        self.listWidget.selectionModel().selectionChanged.connect(self.click_listWidget)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merge PDFs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Advance Options"))
        self.label.setText(_translate("MainWindow", "Select a document"))
        self.label_2.setText(_translate("MainWindow", "Password"))
        self.button_view.setText(_translate("MainWindow", "View PDF"))
        self.groupBox.setTitle(_translate("MainWindow", "Encryption and Decryption PDFs"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.button_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.label_notice.setText(_translate("MainWindow", ""))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setStatusTip(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete Element"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Merge PDFs"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Help Merge PDF"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help Merge PDF"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.actionEncrypt.setStatusTip(_translate("MainWindow", "Encrypt File"))
        self.actionEncrypt.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.actionDecrypt.setStatusTip(_translate("MainWindow", "Decrypt File"))
        self.actionDecrypt.setShortcut(_translate("MainWindow", "Ctrl+D"))


# ======================================| Modify |=================================================================================+

    # Click listWidget
    def click_listWidget(self):
        if not self.dictPDFs:
            # Disabled buttons
            self.label.setText("Select a document")
            self.button_view.setDisabled(True)
            return

        # Current item
        selected_item = self.listWidget.currentItem().text()

        # Enabled buttons
        self.button_view.setEnabled(True)

        # Gets the state of the elements
        item = os.path.basename(selected_item)
        self.label.setText(item)
        
    def click_view(self):
        selected_item = self.listWidget.currentItem().text()
        try:
            subprocess.run(f"xdg-open '{selected_item}'", shell=True, check=True)
        except subprocess.CalledProcessError:
            self.inf_messages(*("Error", 'The selected document could not be viewed'))

    # Function to add a file to 'self.listWidget'
    def click_add(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(MainWindow, "Select PDF Files", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if files:
            for file_name in files:

                # Execute in case of a duplicate file
                if self.dictPDFs.get(file_name) is not None:
                    self.inf_messages("Info", f"This file {file_name} is already in the list")
                    continue

                print("Add file:", file_name)
                new_element = file_name
                self.listWidget.addItem(new_element)
                self.dictPDFs[new_element] = ""#----------> Leave for future functionalities
        else:
            print("Cancel...")

    # Function to delete the selected item from the 'self.listWidget' widget
    def click_delete(self):
            selected_item = self.listWidget.currentItem()
            if selected_item:
                item = selected_item.text()
                del self.dictPDFs[item]#-------------------> Remove the element from the PDF Dictionary
                row = self.listWidget.row(selected_item)
                self.listWidget.takeItem(row)
            else:
                print("No item selected for deletion.")

    # Merge PDFs
    def encrypt_decrypt(self, encrypt:bool):

        if self.listWidget.count() < 1:
            print("Add more files")
            self.inf_messages(*("Info", 'Add at least one file'))

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            if encrypt: notice = "Encrypting Files..."
            else:       notice = "Decrypting Files..."

            # Notice
            self.label_notice.setText(notice)
            pdfs = self.dictPDFs.keys()

            # Confirm the action of encrypting or decrypting
            confirm_dialog = QMessageBox.question(MainWindow, "Confirm the action", "Are you sure you want to perform the action?", QMessageBox.Yes | QMessageBox.No)
            if confirm_dialog == QMessageBox.No:
                print("Cancel..."); self.label_notice.setText(""); return

            if not self.lineEdit_password.text():
                self.inf_messages("Info", "Enter a password"); self.label_notice.setText(""); return

            for pdf in pdfs:
                if encrypt: status = encrypt_pdf(pdf, self.lineEdit_password.text())
                else:       status = decrypt_pdf(pdf, self.lineEdit_password.text())
                if status is not True: self.inf_messages(*status)

            self.inf_messages("Info", "The process has completed")
            self.label_notice.setText("")

    # Open the 'About' window
    def _about(self):
        os.system(Paths["about_window"])

    # Function Help
    def _help(self):

# Help Message ------------------------------------------------------
        QMessageBox.about(MainWindow, "Help", """Controls:
- Add files to the list: Ctrl+A (Two files needed to merge)
- Delete an item: Backspace
- Encrypt PDFs: Ctrl+E
- Decrypt PDFs: Ctrl+D
                          
Advance Options:
- Password: Field to set an encryption or decryption password for the documents in the list.
- View PDF: Open the PDF document in your default PDF document viewer using xdg-open.
""")
                          
# -------------------------------------------------------------------

    # Exit
    def _exit(self):
        print('Exit...')
        sys.exit()

    # Messages
    def inf_messages(self, title, message):
        if title == "Error":
            QMessageBox.critical(MainWindow, title, message, QMessageBox.Ok)
        elif title == "Info":
            QMessageBox.information(MainWindow, title, message, QMessageBox.Ok)

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
