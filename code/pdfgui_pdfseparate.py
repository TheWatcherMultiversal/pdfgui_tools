#! /usr/bin/python3
#
# PDF GUI TOOLS - pdfseparate
# 
# pdfseparate - Split a PDF document into multiple pages.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfgui_tools_utils import Paths, spinBox_range
import subprocess
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 421)
        MainWindow.setMinimumSize(QtCore.QSize(753, 421))
        MainWindow.setMaximumSize(QtCore.QSize(753, 421))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(Paths["icon_app"]), QtGui.QIcon.Normal, QtGui.QIcon.Off)#-----> Icon App
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
        self.button_viewpdf = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_viewpdf.setObjectName("button_viewpdf")
        self.horizontalLayout.addWidget(self.button_viewpdf)
        self.button_separate = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.button_separate.setObjectName("button_separate")
        self.horizontalLayout.addWidget(self.button_separate)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 250, 58, 18))
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 240, 320, 51))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spin_start = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spin_start.setObjectName("spin_start")
        self.horizontalLayout_2.addWidget(self.spin_start)
        self.check_start = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.check_start.setObjectName("check_start")
        self.horizontalLayout_2.addWidget(self.check_start)
        self.spin_final = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spin_final.setObjectName("spin_final")
        self.horizontalLayout_2.addWidget(self.spin_final)
        self.check_final = QtWidgets.QCheckBox(self.horizontalLayoutWidget_2)
        self.check_final.setObjectName("check_final")
        self.horizontalLayout_2.addWidget(self.check_final)
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
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionabout = QtWidgets.QAction(MainWindow)
        self.actionabout.setObjectName("actionabout")
        self.actionAdd_File = QtWidgets.QAction(MainWindow)
        self.actionAdd_File.setObjectName("actionAdd_File")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionSeparate = QtWidgets.QAction(MainWindow)
        self.actionSeparate.setObjectName("actionSeparate")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionSeparate)
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
        self.actionSeparate.triggered.connect(self.separate_pdf)
        self.actionabout.triggered.connect(self._about)
        self.actionHelp.triggered.connect(self._help)
        self.actionExit.triggered.connect(self._exit)

        # spinBox
        # --> Max range:
        self.spin_start.setMinimum(spinBox_range[0])
        self.spin_final.setMinimum(spinBox_range[0])
        self.spin_start.setMaximum(spinBox_range[1])
        self.spin_final.setMaximum(spinBox_range[1])

        # Buttons
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_viewpdf.clicked.connect(self.viewpdf)
        self.button_separate.clicked.connect(self.separate_pdf)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Separate PDF"))
        self.groupBox.setTitle(_translate("MainWindow", "Separate PDF"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_viewpdf.setText(_translate("MainWindow", "View PDF"))
        self.button_separate.setText(_translate("MainWindow", "Separate"))
        self.check_start.setText(_translate("MainWindow", "Start"))
        self.check_final.setText(_translate("MainWindow", "Final"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionHelp.setText(_translate("MainWindow", "Help Separate PDF"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help Separate PDF"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionabout.setText(_translate("MainWindow", "about"))
        self.actionAdd_File.setText(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setStatusTip(_translate("MainWindow", "Add File"))
        self.actionAdd_File.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionDelete.setStatusTip(_translate("MainWindow", "Delete"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Backspace"))
        self.actionSeparate.setText(_translate("MainWindow", "Separate"))
        self.actionSeparate.setStatusTip(_translate("MainWindow", "Separate PDF"))
        self.actionSeparate.setShortcut(_translate("MainWindow", "Ctrl+S"))
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

    # Function view PDF document
    def viewpdf(self):

        if self.listWidget.count() < 1:
            print("you need to add file")
            self.inf_messages("Info", 'You need to add file')
        else:
            try:
                item = self.listWidget.item(0)
                subprocess.run([f'xdg-open "{item.text()}"'], check=True, shell=True)#------> Use xdg-open to open the default PDF viewer
            except subprocess.CalledProcessError:
                self.inf_messages("Error", 'The PDF file could not be viewed')

    # Separate PDF
    def separate_pdf(self):

        if self.listWidget.count() < 1:
            print("you need to add file")
            self.inf_messages("Info", 'You need to add file')

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # Command
            self.command = "pdfseparate"

            # Notice
            self.label_notice.setText("Separate pdf, please wait...")
            
            # Values of SpinBox and CheckBox start and finish
            spinstart = int(self.spin_start.value())
            spinfinish = int(self.spin_final.value())
            checkstart = int(self.check_start.checkState())
            checkfinish = int(self.check_final.checkState())

            # Compare the status of the checkboxes
            if checkstart != 0:
                self.command += ' ' + f'-f {spinstart}'
            if checkfinish != 0:
                self.command += ' ' + f'-l {spinfinish}'

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row)
                print(f'File {row}:', item.text())
                self.command += ' "' + item.text() + '"'

            options = QFileDialog.Options()
            options |= QFileDialog.ShowDirsOnly
            options |= QFileDialog.DontUseNativeDialog

            # Asks where to save and how to name the file, obtains the path
            directory, _ = QFileDialog.getSaveFileName(MainWindow, "Create Directory", "", "", options=options)
            directory_name = str(os.path.basename(directory))

            if directory:
                
                # An attempt is made to create the directory
                try:
                    subprocess.run([f'mkdir {directory}'], check=True, shell=True)#-----------> The 'mkdir' command is executed
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Error while creating the directory, please try with another name')

                self.command += " " + str(f'"{directory}/{directory_name}%d.pdf"')
                print(self.command)
                print("Save file:", directory)
                try:
                    subprocess.run([self.command], check=True, shell=True)#-------------------> The 'pdfseparate' command is executed
                    self.inf_messages("Info", "The process has completed")
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Verify the options and file integrity, use the F1 key for help')
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
- View PDF: Open the PDF document in your default PDF document viewer using xdg-open.
- Separate PDF: Ctrl+S (It is saved in a created directory)
                          
Options:
- Start: Specify the starting page for splitting.
- Final: Specify the ending page for splitting.
                          
* By default, the entire PDF is separated. 
Use the options to specify the PDF document 
separation more accurately. You can activate 
both options or just one, as long as they are 
consistent.
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
