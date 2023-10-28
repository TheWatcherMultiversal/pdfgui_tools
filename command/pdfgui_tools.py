#! /usr/bin/python3
#
# PDF GUI TOOLS - pdfgui_tools
# 
# PDF GUI Tools app - Main file of pdfgui_tools 
# Utilities are found in another file: pdfguiUtils
#
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfguiUtils import version_app, title_app, Paths, repeat_symbol, spinBox_range, PyPDF2utils
import subprocess, sys, os, argparse


# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Argument:

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--man',     action='store_true', help='man page')
parser.add_argument('-v', '--version', action='store_true', help='print version')
args = parser.parse_args()

if   args.man     is True : os.system('man pdfgui_tools')          ; sys.exit()
elif args.version is True : print(f'PDF GUI Tools v{version_app}') ; sys.exit()



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 650)
        MainWindow.setMinimumSize(QtCore.QSize(1060, 650))
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
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(20, 2000000000, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.checkBox_range = QtWidgets.QCheckBox(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.checkBox_range.setFont(font)
        self.checkBox_range.setObjectName("checkBox_range")
        self.verticalLayout_4.addWidget(self.checkBox_range)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.spinBox_range_final = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_range_final.setMaximum(1000)
        self.spinBox_range_final.setObjectName("spinBox_range_final")
        self.gridLayout.addWidget(self.spinBox_range_final, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.spinBox_range_initial = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_range_initial.setMaximum(1000)
        self.spinBox_range_initial.setObjectName("spinBox_range_initial")
        self.gridLayout.addWidget(self.spinBox_range_initial, 0, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(-1, -1, 0, 20)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_password = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_password.setAcceptDrops(False)
        self.lineEdit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhNoAutoUppercase|QtCore.Qt.ImhNoPredictiveText|QtCore.Qt.ImhSensitiveData)
        self.lineEdit_password.setText("")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setPlaceholderText("")
        self.lineEdit_password.setObjectName("lineEdit_password")
        self.verticalLayout_5.addWidget(self.lineEdit_password)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.button_view = QtWidgets.QPushButton(self.groupBox_2)
        self.button_view.setObjectName("button_view")
        self.verticalLayout_4.addWidget(self.button_view)
        self.button_separate = QtWidgets.QPushButton(self.groupBox_2)
        self.button_separate.setObjectName("button_separate")
        self.verticalLayout_4.addWidget(self.button_separate)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_convert = QtWidgets.QPushButton(self.groupBox_2)
        self.button_convert.setObjectName("button_convert")
        self.horizontalLayout_2.addWidget(self.button_convert)
        self.combo_filetype = QtWidgets.QComboBox(self.groupBox_2)
        self.combo_filetype.setObjectName("combo_filetype")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.combo_filetype.addItem("")
        self.horizontalLayout_2.addWidget(self.combo_filetype)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 2)
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
        self.button_up = QtWidgets.QPushButton(self.groupBox)
        self.button_up.setObjectName("button_up")
        self.verticalLayout_2.addWidget(self.button_up)
        self.button_down = QtWidgets.QPushButton(self.groupBox)
        self.button_down.setObjectName("button_down")
        self.verticalLayout_2.addWidget(self.button_down)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.button_merge = QtWidgets.QPushButton(self.groupBox)
        self.button_merge.setObjectName("button_merge")
        self.verticalLayout_6.addWidget(self.button_merge)
        self.button_encrypt = QtWidgets.QPushButton(self.groupBox)
        self.button_encrypt.setObjectName("button_encrypt")
        self.verticalLayout_6.addWidget(self.button_encrypt)
        self.button_decrypt = QtWidgets.QPushButton(self.groupBox)
        self.button_decrypt.setObjectName("button_decrypt")
        self.verticalLayout_6.addWidget(self.button_decrypt)
        self.verticalLayout.addLayout(self.verticalLayout_6)
        self.label_notice = QtWidgets.QLabel(self.groupBox)
        self.label_notice.setText("")
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
        self.actionUp = QtWidgets.QAction(MainWindow)
        self.actionUp.setObjectName("actionUp")
        self.actionDown = QtWidgets.QAction(MainWindow)
        self.actionDown.setObjectName("actionDown")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionEncrypt = QtWidgets.QAction(MainWindow)
        self.actionEncrypt.setObjectName("actionEncrypt")
        self.actionDecrypt = QtWidgets.QAction(MainWindow)
        self.actionDecrypt.setObjectName("actionDecrypt")
        self.menuFile.addAction(self.actionAdd_File)
        self.menuFile.addAction(self.actionDelete)
        self.menuFile.addAction(self.actionUp)
        self.menuFile.addAction(self.actionDown)
        self.menuFile.addAction(self.actionSave)
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

        # Dictionary type of document conversion
        self.dictConvert = {
            "HTML" : ("pdftohtml"       , False),
            "TXT"  : ("pdftotext"       , False),
            "PNG"  : ("pdftocairo -png" , True),
            "JPEG" : ("pdftocairo -jpeg", True),
        }
        for pdftocairo in ("PS", "EPS", "SVG"):
            self.dictConvert[pdftocairo] = (f'pdftocairo -{pdftocairo.lower()}', False)

        # Disable Elements
        self.checkBox_range.setEnabled(False)
        self.spinBox_range_initial.setEnabled(False)
        self.spinBox_range_final.setEnabled(False)
        self.button_view.setEnabled(False)
        self.button_separate.setEnabled(False)
        self.button_convert.setEnabled(False)

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionUp.triggered.connect(self.move_up)
        self.actionDown.triggered.connect(self.move_down)
        self.actionSave.triggered.connect(self.merge_pdf)
        self.actionHelp.triggered.connect(self._help)
        self.actionAbout.triggered.connect(self._about)
        self.actionExit.triggered.connect(self._exit)
        self.actionEncrypt.triggered.connect(lambda: self.encrypt_decrypt(True))
        self.actionDecrypt.triggered.connect(lambda: self.encrypt_decrypt(False))

        # checkBox
        self.checkBox_range.stateChanged.connect(self.click_checkBox_range)

        # spinBox
        # --> Min range:
        self.spinBox_range_initial.setMinimum(spinBox_range[0])
        self.spinBox_range_final.setMinimum(spinBox_range[0])
        # --> Max range:
        self.spinBox_range_initial.setMaximum(spinBox_range[1])
        self.spinBox_range_final.setMaximum(spinBox_range[1])
        # --> Change range:
        self.spinBox_range_initial.valueChanged.connect(self.spinbox_initial_changed)
        self.spinBox_range_final.valueChanged.connect(self.spinbox_final_changed)

        # Buttons
        self.button_view.clicked.connect(self.click_view)
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_up.clicked.connect(self.move_up)
        self.button_down.clicked.connect(self.move_down)
        self.button_merge.clicked.connect(self.merge_pdf)
        self.button_encrypt.clicked.connect(lambda: self.encrypt_decrypt(True))
        self.button_decrypt.clicked.connect(lambda: self.encrypt_decrypt(False))
        self.button_separate.clicked.connect(self.separate_pdf)
        self.button_convert.clicked.connect(self.convert)

        # listWidget:
        self.listWidget.selectionModel().selectionChanged.connect(self.click_listWidget)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PDF GUI Tools"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Options and Utilities"))
        self.checkBox_range.setText(_translate("MainWindow", "Page Range"))
        self.label_3.setText(_translate("MainWindow", "Final"))
        self.label_2.setText(_translate("MainWindow", "Initial"))
        self.label_4.setText(_translate("MainWindow", "Password"))
        self.button_view.setText(_translate("MainWindow", "View PDF"))
        self.button_separate.setText(_translate("MainWindow", "Separate PDF"))
        self.button_convert.setText(_translate("MainWindow", "Convert PDF"))
        self.combo_filetype.setItemText(0, _translate("MainWindow", "PNG"))
        self.combo_filetype.setItemText(1, _translate("MainWindow", "JPEG"))
        self.combo_filetype.setItemText(2, _translate("MainWindow", "PS"))
        self.combo_filetype.setItemText(3, _translate("MainWindow", "EPS"))
        self.combo_filetype.setItemText(4, _translate("MainWindow", "SVG"))
        self.combo_filetype.setItemText(5, _translate("MainWindow", "HTML"))
        self.combo_filetype.setItemText(6, _translate("MainWindow", "TXT"))
        self.label.setText(_translate("MainWindow", "Select a document"))
        self.groupBox.setTitle(_translate("MainWindow", "List PDFs"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_up.setText(_translate("MainWindow", "/\\"))
        self.button_down.setText(_translate("MainWindow", "\\/"))
        self.button_merge.setText(_translate("MainWindow", "Merge"))
        self.button_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.button_decrypt.setText(_translate("MainWindow", "Decrypt"))
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
        self.actionSave.setText(_translate("MainWindow", "Merge"))
        self.actionSave.setStatusTip(_translate("MainWindow", "Merge PDFs"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("MainWindow", "Help"))
        self.actionHelp.setShortcut(_translate("MainWindow", "F1"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))
        self.actionEncrypt.setText(_translate("MainWindow", "Encrypt"))
        self.actionEncrypt.setStatusTip(_translate("MainWindow", "Encrypt PDF"))
        self.actionEncrypt.setShortcut(_translate("MainWindow", "Ctrl+E"))
        self.actionDecrypt.setText(_translate("MainWindow", "Decrypt"))
        self.actionDecrypt.setStatusTip(_translate("MainWindow", "Decrypt PDFs"))
        self.actionDecrypt.setShortcut(_translate("MainWindow", "Ctrl+D"))

# ======================================| Modify |=================================================================================+

    # Click listWidget
    def click_listWidget(self):
        if not self.dictPDFs:
            # --> Disabled buttons
            self.label.setText("Select a document")
            self.checkBox_range.setDisabled(True)
            self.spinBox_range_initial.setDisabled(True)
            self.spinBox_range_final.setDisabled(True)
            self.button_view.setDisabled(True)
            self.button_separate.setDisabled(True)
            self.button_convert.setDisabled(True)
            self.button_convert.setDisabled(True)
            return

        # -> Current item
        selected_item = self.listWidget.currentItem().text()

        # -> Enabled buttons
        self.checkBox_range.setEnabled(True)
        self.spinBox_range_initial.setEnabled(True)
        self.spinBox_range_final.setEnabled(True)
        self.button_view.setEnabled(True)
        self.button_separate.setEnabled(True)
        self.button_convert.setEnabled(True)
        self.button_convert.setEnabled(True)

        # -> Gets the state of the elements
        self.checkBox_range.setChecked(self.dictPDFs[selected_item][0]) 
        self.spinBox_range_initial.setValue(self.dictPDFs[selected_item][1][0])
        self.spinBox_range_final.setValue(self.dictPDFs[selected_item][1][1])
        item = os.path.basename(selected_item)
        self.label.setText(item)


    # Click checkBox 'Page Range'
    def click_checkBox_range(self):
        check_state = self.checkBox_range.checkState() > 0
        selected_item = self.listWidget.currentItem().text()
        self.dictPDFs[selected_item][0] = check_state


    # Gets the change from the spinBox
    def spinbox_initial_changed(self):
        get_value = self.spinBox_range_initial.value()
        selected_item = self.listWidget.currentItem().text()
        self.dictPDFs[selected_item][1][0] = get_value


    def spinbox_final_changed(self):
        get_value = self.spinBox_range_final.value()
        selected_item = self.listWidget.currentItem().text()
        self.dictPDFs[selected_item][1][1] = get_value
        

    def click_view(self):
        selected_item = self.listWidget.currentItem().text().replace(repeat_symbol, "")
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

                # ---> While loop in case a path is repeated
                while self.dictPDFs.get(file_name) is not None:
                    file_name += repeat_symbol
                print("Add file:", file_name)
                self.listWidget.addItem(file_name)
                self.dictPDFs[file_name] = [False, [1,1]]
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


# -------------------------------------| Utility Functions of pdfgui_tools |--------------------------------------------------------

    # Merge PDFs
    def merge_pdf(self):

        if self.listWidget.count() < 2:
            print("Add more files")
            self.inf_messages(*("Info", 'Add at least two files'))

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Notice
            self.label_notice.setText("Merge PDFs, please wait...")
            pdfs = []; pages = []

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row).text()
                print(f'File {row}:', item)
                pdfs.append(item.replace(repeat_symbol, ""))
                pages.append(self.dictPDFs[item])

            options = QFileDialog.Options()

            # --> Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", ".pdf", "PDF Files (*.pdf)", options=options)

            if file_name:
                status = PyPDF2utils.merge_pdf(name_file=file_name, pdfs=pdfs, pages=pages)
                if status is not True: self.inf_messages(*status); self.label_notice.setText(""); return
                self.inf_messages("Info", "The process has completed")
            else:
                print("Cancel...")

            self.label_notice.setText("")


    # Encrypt or Decrypt PDFs:
    def encrypt_decrypt(self, encrypt:bool):

        if self.listWidget.count() < 1:
            print("Add more files")
            self.inf_messages(*("Info", 'Add at least one file'))

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            if encrypt: notice = "Encrypting Files..."
            else:       notice = "Decrypting Files..."

            # --> Notice
            self.label_notice.setText(notice)
            pdfs = self.dictPDFs.keys()

            # --> Confirm the action of encrypting or decrypting
            confirm_dialog = QMessageBox.question(MainWindow, "Confirm the action", "Are you sure you want to perform the action?", QMessageBox.Yes | QMessageBox.No)
            if confirm_dialog == QMessageBox.No:
                print("Cancel..."); self.label_notice.setText(""); return

            # --> The 'Password' field is empty
            if not self.lineEdit_password.text():
                self.inf_messages("Info", "Enter a password"); self.label_notice.setText(""); return

            for pdf in pdfs:
                pdf = pdf.replace(repeat_symbol, "")
                if encrypt: status = PyPDF2utils.encrypt_pdf(pdf, self.lineEdit_password.text())
                else:       status = PyPDF2utils.decrypt_pdf(pdf, self.lineEdit_password.text())
                if status is not True: self.inf_messages(*status)

            self.inf_messages("Info", "The process has completed")
            self.label_notice.setText("")


    # Separate PDF
    def separate_pdf(self):

        if self.listWidget.count() < 1:
            print("you need to add file")
            self.inf_messages("Info", 'You need to add file')

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Command
            self.command = "pdfseparate"

            # --> Notice
            self.label_notice.setText("Separate pdf, please wait...")

            # --> Get Current Item
            item = self.listWidget.currentItem().text()
            data = self.dictPDFs[item]; item = item.replace(repeat_symbol, "")

            # --> File encrypted
            if PyPDF2utils.fileEncrypted(item):
                self.inf_messages("Info", f"The document {item} is encrypted, decrypt it to perform this action")
                self.label_notice.setText(""); return

            # --> Compare the status of the checkboxes
            if data[0]:
                self.command += ' ' + f'-f {self.spinBox_range_initial.value()}'
                self.command += ' ' + f'-l {self.spinBox_range_final.value()}'

            print(f'File separate:', item)
            self.command += ' "' + item + '"'

            options = QFileDialog.Options()
            options |= QFileDialog.ShowDirsOnly
            options |= QFileDialog.DontUseNativeDialog

            # --> Asks where to save and how to name the file, obtains the path
            directory, _ = QFileDialog.getSaveFileName(MainWindow, "Create Directory", "", "", options=options)
            directory_name = str(os.path.basename(directory))

            if directory:
                
                # ---> An attempt is made to create the directory
                try:
                    subprocess.run([f'mkdir "{directory}"'], check=True, shell=True)#-----------> The 'mkdir' command is executed
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Error while creating the directory, please try with another name')
                    self.label_notice.setText("");return

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


    # Convert PDF
    def convert(self):

        if self.listWidget.count() < 1:
            print("you need to add file")
            self.inf_messages("Info", 'You need to add file')

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Get the value of the ComboBox
            filetype = str(self.combo_filetype.currentText())
            lower_filetype = filetype.lower()
            item = self.listWidget.currentItem().text().replace(repeat_symbol, "")

            # --> Notice
            self.label_notice.setText(f"Convert pdf to {lower_filetype}, please wait...")

            # --> File encrypted
            if PyPDF2utils.fileEncrypted(item):
                self.inf_messages("Info", f"The document {item} is encrypted, decrypt it to perform this action")
                self.label_notice.setText(""); return

            # --> Obtains the type of conversion and command
            self.command = self.dictConvert[filetype][0]

            # --> Get Current Item
            print(f'File convert {lower_filetype}:', item)
            self.command += ' "' + item + '"'

            options = QFileDialog.Options()

            # --> Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", f".{lower_filetype}", f"{filetype} Files (*.{lower_filetype})", options=options)

            if file_name:
                if self.dictConvert[filetype][1]: self.command += " " + (f'"{file_name[:- len(filetype) - 1]}"')
                else: self.command += " " + (f'"{file_name}"')
                print(self.command)
                print("Save file:", file_name)

                try:
                    subprocess.run([self.command], check=True, shell=True)#-------------------> The 'pdftocairo' command is executed
                    self.inf_messages("Info", "The process has completed")
                except subprocess.CalledProcessError:
                    self.label_notice.setText("")
                    self.inf_messages("Error", 'Error Executing the command, please verify the name and integrity of the document')
            else:
                print("Cancel...")

            self.label_notice.setText("")


# --------------------------------------| About and Help window |-----------------------------------------------------------------------------------

    # Open the 'About' window
    def _about(self):
        about_window = QtWidgets.QMainWindow(MainWindow)
        about_ui = AboutWindow(about_window)
        about_ui.setupUi(about_window)
        about_window.show()

    # Function Help
    def _help(self):

    # Help Message:
        QMessageBox.about(MainWindow, "Help", """Controls:
- Add files to the list: Ctrl+A (Two files needed to merge)
- Delete an item: Backspace
- Move an item to another position: Use the 'up' and 'down' keys
- Merge the PDFs: Ctrl+S
- Encrypt PDFs: Ctrl+E (Requires the 'Password' field to have a password)
- Decrypt PDFs: Ctrl+D (Requires the 'Password' field to have a password)
                          
Advance Options:
- Page Range: CheckBox in case you require a PDF document to use a range of pages to combine with others and not the entire document.
- Initial: Page of the document where it will start merging the PDFs with the other PDF documents.
- Final: Final page of the document where it will finish merging with the other PDF documents.                
- Password: Field for setting an encryption or decryption password.
- View PDF: Open the PDF document in your default PDF document viewer using xdg-open.
- Separate PDF: Splits the PDF document into multiple pages, can be used in conjunction with the page range.                
- Convert PDF: It will convert the document to the selected format.
""")
                          
# -------------------------------------------------------------------------------------------------------------------------------------------------------

    # Exit
    def _exit(self):
        print('Exit...')
        MainWindow.close()

    # Messages
    def inf_messages(self, title, message):
        if title == "Error":
            QMessageBox.critical(MainWindow, title, message, QMessageBox.Ok)
        elif title == "Info":
            QMessageBox.information(MainWindow, title, message, QMessageBox.Ok)

# =================================================================================================================================+

# ----> About window <-----#
class AboutWindow(object):

    def __init__(self, window):
        self.window = window

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

        # Button Ok
        self.button_ok.clicked.connect(lambda: self.window.close())
        
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
  

# ============================================================================================================+

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    with open(Paths["styles"], "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec_())
