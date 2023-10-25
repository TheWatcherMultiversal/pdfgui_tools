#! /usr/bin/python3
#
# PDF GUI TOOLS - pdfunite
# 
# pdfunite - Merge multiple PDFs into a single PDF.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfgui_tools_utils import Paths
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Paths["icon_app"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 511))
        self.groupBox.setObjectName("groupBox")
        self.listWidget = QtWidgets.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 571, 441))
        self.listWidget.setObjectName("listWidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(620, 50, 111, 191))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.button_add = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_add.setObjectName("button_add")
        self.verticalLayout.addWidget(self.button_add)
        self.button_delete = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_delete.setObjectName("button_delete")
        self.verticalLayout.addWidget(self.button_delete)
        self.button_up = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_up.setObjectName("button_up")
        self.verticalLayout.addWidget(self.button_up)
        self.button_down = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.button_down.setObjectName("button_down")
        self.verticalLayout.addWidget(self.button_down)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(620, 440, 111, 51))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.button_merge = QtWidgets.QPushButton(self.verticalLayoutWidget_2)
        self.button_merge.setObjectName("button_merge")
        self.verticalLayout_2.addWidget(self.button_merge)
        self.label_notice = QtWidgets.QLabel(self.centralwidget)
        self.label_notice.setGeometry(QtCore.QRect(10, 530, 431, 18))
        self.label_notice.setText("")
        self.label_notice.setObjectName("label_notice")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
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
        self.actionUp = QtWidgets.QAction(MainWindow)
        self.actionUp.setObjectName("actionUp")
        self.actionDown = QtWidgets.QAction(MainWindow)
        self.actionDown.setObjectName("actionDown")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionUp)
        self.menuFile.addAction(self.actionDown)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionUp.triggered.connect(self.move_up)
        self.actionDown.triggered.connect(self.move_down)
        self.actionSave.triggered.connect(self.merge_pdf)
        self.actionHelp.triggered.connect(self._help)
        self.actionAbout.triggered.connect(self._about)
        self.actionExit.triggered.connect(self._exit)

        # Buttons
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_up.clicked.connect(self.move_up)
        self.button_down.clicked.connect(self.move_down)
        self.button_merge.clicked.connect(self.merge_pdf)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merge PDFs"))
        self.groupBox.setTitle(_translate("MainWindow", "Merge PDFs"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_up.setText(_translate("MainWindow", "/\\"))
        self.button_down.setText(_translate("MainWindow", "\\/"))
        self.button_merge.setText(_translate("MainWindow", "Merge"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setStatusTip(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete Element"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionUp.setText(_translate("MainWindow", "Up"))
        self.actionUp.setStatusTip(_translate("MainWindow", "Up"))
        self.actionUp.setShortcut(_translate("MainWindow", "Up"))
        self.actionDown.setText(_translate("MainWindow", "Down"))
        self.actionDown.setStatusTip(_translate("MainWindow", "Down"))
        self.actionDown.setShortcut(_translate("MainWindow", "Down"))
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

# ======================================| Modify |=================================================================================+

    # Function to add a file to 'self.listWidget'
    def click_add(self):
        
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(MainWindow, "Select PDF Files", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if files:
            for file_name in files:
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

    # Move the position of an item in the list
    def move_up(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            row = self.listWidget.row(selected_item)
            if row > 0:
                self.listWidget.takeItem(row)
                self.listWidget.insertItem(row - 1, selected_item)
                self.listWidget.setCurrentItem(selected_item)
    
    def move_down(self):
        selected_item = self.listWidget.currentItem()
        if selected_item:
            row = self.listWidget.row(selected_item)
            if row < self.listWidget.count() - 1:
                self.listWidget.takeItem(row)
                self.listWidget.insertItem(row + 1, selected_item)
                self.listWidget.setCurrentItem(selected_item)

    # Merge PDFs
    def merge_pdf(self):

        if self.listWidget.count() < 2:
            print("Add more files")
            self.inf_messages("Info", 'Add at least two files')

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # Command
            self.command = "pdfunite"

            # Notice
            self.label_notice.setText("Merge PDFs, please wait...")

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row)
                print(f'File {row}:', item.text())
                self.command += ' "' + item.text() + '"'

            options = QFileDialog.Options()

            # Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", ".pdf", "PDF Files (*.pdf)", options=options)

            if file_name:
                self.command += " " + str(f'"{file_name}"')
                print(self.command)
                print("Save file:", file_name)
                try:
                    subprocess.run([self.command], check=True, shell=True)#-------------------> The 'pdfunite' command is executed
                    self.inf_messages("Info", "The process has completed")
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Error Executing the command, please check the name of the final file and the integrity of your other files.')
            else:
                print("Cancel...")

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
- Move an item to another position: Use the 'up' and 'down' keys
- Merge the PDFs: Use Ctrl+S
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
