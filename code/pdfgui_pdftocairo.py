#! /usr/bin/python3
#
# PDF GUI TOOLS - pdftocairo
# 
# pdftocairo - Converts the PDF file into multimedia files.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
import subprocess
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 421)
        MainWindow.setMinimumSize(QtCore.QSize(753, 421))
        MainWindow.setMaximumSize(QtCore.QSize(753, 421))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/share/pdfgui_tools/assets/pdfguitools.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 711, 331))
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
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 250, 58, 18))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(490, 240, 201, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.combo_filetype = QtWidgets.QComboBox(self.horizontalLayoutWidget_2)
        self.combo_filetype.setObjectName("combo_filetype")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_filetype)
        self.label_notice = QtWidgets.QLabel(self.centralwidget)
        self.label_notice.setGeometry(QtCore.QRect(20, 360, 311, 18))
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
        self.actionHelp_PDFtoMultimedia = QtWidgets.QAction(MainWindow)
        self.actionHelp_PDFtoMultimedia.setObjectName("actionHelp_PDFtoMultimedia")
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
        self.menuHelp.addAction(self.actionHelp_PDFtoMultimedia)
        self.menuHelp.addAction(self.actionabout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

# =============| Modify |=======================================+

        # User input connection to functions:

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionConvert.triggered.connect(self.convert)
        self.actionabout.triggered.connect(self._about)
        self.actionHelp_PDFtoMultimedia.triggered.connect(self._help)
        self.actionExit.triggered.connect(self._exit)

        # Buttons
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_convert.clicked.connect(self.convert)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF to multimedia file"))
        self.groupBox.setTitle(_translate("MainWindow", "PDF to multimedia file"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_convert.setText(_translate("MainWindow", "Convert"))
        self.label_2.setText(_translate("MainWindow", "File type    "))
        self.combo_filetype.setItemText(0, _translate("MainWindow", "PNG"))
        self.combo_filetype.setItemText(1, _translate("MainWindow", "JPEG"))
        self.combo_filetype.setItemText(2, _translate("MainWindow", "PS"))
        self.combo_filetype.setItemText(3, _translate("MainWindow", "EPS"))
        self.combo_filetype.setItemText(4, _translate("MainWindow", "SVG"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp_PDFtoMultimedia.setText(_translate("MainWindow", "Help PDF to multimedia file"))
        self.actionHelp_PDFtoMultimedia.setStatusTip(_translate("MainWindow", "Help PDF to multimedia file"))
        self.actionHelp_PDFtoMultimedia.setShortcut(_translate("MainWindow", "F1"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setStatusTip(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionConvert.setText(_translate("MainWindow", "Convert"))
        self.actionConvert.setStatusTip(_translate("MainWindow", "Convert"))
        self.actionConvert.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))

# ======================================| Modify |=================================================================================+

    # Function to add a file to 'self.listWidget'
    def click_add(self):
        if self.listWidget.count() == 1:
            print("One file permited")
            QMessageBox.critical(MainWindow, "Error", 'Only one file at a time.', QMessageBox.Ok)
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


    # Convert PDF
    def convert(self):

        if self.listWidget.count() < 1:
            print("you need to add file")
            QMessageBox.critical(MainWindow, "Error", 'You need to add file', QMessageBox.Ok)

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # Command
            self.command = "pdftocairo"

            # Get the value of the ComboBox
            filetype = str(self.combo_filetype.currentText())
            lower_filetype = filetype.lower()

            # Notice
            self.label_notice.setText(f"Convert pdf to {lower_filetype}, please wait...")

            # The parameter is added to the command.
            self.command += ' ' + f'-{lower_filetype}'

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row)
                print(f'File {row}:', item.text())
                self.command += ' "' + item.text() + '"'

            options = QFileDialog.Options()

            # Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", f".{lower_filetype}", f"{filetype} Files (*.{lower_filetype})", options=options)

            if file_name:
                self.command += " " + str(f'"{file_name}"')
                print(self.command)
                print("Save file:", file_name)

                try:
                    subprocess.run([self.command], check=True, shell=True)#-------------------> The 'pdftocairo' command is executed
                    sys.exit()#---------------------------------------------------------------> The application is closed
                except subprocess.CalledProcessError:
                    self.label_notice.setText("")
                    QMessageBox.critical(MainWindow, "Error", 'Error Executing the command, please verify the name and integrity of the document.', QMessageBox.Ok)
            else:
                print("Cancel...")

            self.label_notice.setText("")

    # Open the 'About' window
    def _about(self):
        os.system('python3 /usr/share/pdfgui_tools/about.py')

    # Function Help
    def _help(self):

# Help Message ------------------------------------------------------
        QMessageBox.about(MainWindow, "Help", """Controls:
- Add a file: Ctrl+A (Only one file at a time)
- Delete an item: Backspace
- Convert PDF to multimedia file: Ctrl+S
                          
Options:
- File type: Choose what to convert the PDF document into.
                          
* For PNG/JPEG files, the resulting file(s) will be one or 
multiple images from the selected PDF document. Please 
consider the number of pages in your PDF document.
                          
* For PS/EPS/SVG files, try to select single-page PDF 
documents. Remember, you can use the PDF separate tool
and then convert the document to the desired multimedia 
file if this situation arises.
""")
                          
# -------------------------------------------------------------------

    # Exit
    def _exit(self):
        print('Exit...')
        sys.exit()

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