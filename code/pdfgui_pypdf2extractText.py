#! /usr/bin/python3
#
# PDF GUI TOOLS - pypdf2extractText
# 
# pypdf2extractText - Convert PDF documents into text files.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfgui_tools_utils import Paths, extract_text
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 361)
        MainWindow.setMinimumSize(QtCore.QSize(753, 361))
        MainWindow.setMaximumSize(QtCore.QSize(753, 361))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Paths["icon_app"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 711, 261))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 60, 671, 111))
        self.listWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 190, 671, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_add = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.horizontalLayout.addWidget(self.button_add)
        self.button_delete = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_delete.setObjectName("button_delete")
        self.horizontalLayout.addWidget(self.button_delete)
        self.button_convert = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_convert.setObjectName("button_convert")
        self.horizontalLayout.addWidget(self.button_convert)
        self.label_notice = QtWidgets.QLabel(self.centralwidget)
        self.label_notice.setGeometry(QtCore.QRect(20, 290, 311, 18))
        self.label_notice.setText("")
        self.label_notice.setObjectName("label_notice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 24))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionAdd_File = QtWidgets.QAction(MainWindow)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionConvert = QtWidgets.QAction(MainWindow)
        self.actionConvert.setObjectName("actionConvert")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionConvert)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionConvert.triggered.connect(self.convert_text)
        self.actionabout.triggered.connect(self._about)
        self.actionHelp.triggered.connect(self._help)
        self.actionExit.triggered.connect(self._exit)

        # Buttons
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_convert.clicked.connect(self.convert_text)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF to text"))
        self.groupBox.setTitle(_translate("MainWindow", "Extract Text"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_convert.setText(_translate("MainWindow", "Convert"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help PDF to text"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help PDF to text"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setStatusTip(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionConvert.setText(_translate("MainWindow", "Convert"))
        self.actionConvert.setStatusTip(_translate("MainWindow", "Convert to text"))
        self.actionConvert.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))


# ======================================| Modify |=================================================================================+

    # Function to add a file to 'self.listWidget'
    def click_add(self):
        if self.listWidget.count() == 1:
            print("One file permited")
            self.inf_messages("Info", 'Only one file at a time.')
        else:
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(MainWindow, "Select File", "", "PDF Files (*.pdf)", options=options)
            if file_name:
                print("Add file:", file_name)
                new_element = file_name
                self.listWidget.addItem(new_element)
            else:
                print("Cancel...")

    # Function to delete the selected item from the 'self.listWidget' widget
    def click_delete(self):
            selected_item = self.listWidget.currentItem()
            if selected_item:
                row = self.listWidget.row(selected_item)
                self.listWidget.takeItem(row)
            else:
                print("No item selected for deletion.")

    # Convert PDF to Text
    def convert_text(self):
        if self.listWidget.count() < 1:
            print("you need to add file")
            self.inf_messages("Info", 'You need to add file')

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # Notice
            self.label_notice.setText("Convert pdf to text, please wait...")

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row)
                pdf = item.text()

            options = QFileDialog.Options()

            # Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", ".txt", "TXT Files (*.txt)", options=options)

            if file_name:
                status = extract_text(name_file=file_name, pdf=pdf)
                if status is not True: self.inf_messages(*status); self.label_notice.setText(""); return
                self.inf_messages("Info", "The process has completed")
            else:
                print("Cancel...")

            self.label_notice.setText("")

    def _about(self):
        os.system(Paths["about_window"])

    def _help(self):

# Help Message ------------------------------------------------------
        QMessageBox.about(MainWindow, "Help", """Controls:
- Add a file: Ctrl+A (Only one file at a time)
- Delete an item: Backspace
- Convert PDF to text file: Ctrl+S (It is saved in a created directory)
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