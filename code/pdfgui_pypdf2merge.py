#! /usr/bin/python3
#
# PDF GUI TOOLS - pypdf2merge
# 
# pypdf2merge - Merge multiple PDFs into a single PDF.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFileDialog
from pdfgui_tools_utils import Paths, spinBox_range, merge_pdf
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
        self.spinBox_range_initial = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_range_initial.setObjectName("spinBox_range_initial")
        self.gridLayout.addWidget(self.spinBox_range_initial, 0, 0, 1, 1)
        self.spinBox_range_final = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_range_final.setObjectName("spinBox_range_final")
        self.gridLayout.addWidget(self.spinBox_range_final, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 1, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
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
        self.button_up = QtWidgets.QPushButton(self.groupBox)
        self.button_up.setObjectName("button_up")
        self.verticalLayout_2.addWidget(self.button_up)
        self.button_down = QtWidgets.QPushButton(self.groupBox)
        self.button_down.setObjectName("button_down")
        self.verticalLayout_2.addWidget(self.button_down)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.button_merge = QtWidgets.QPushButton(self.groupBox)
        self.button_merge.setObjectName("button_merge")
        self.verticalLayout.addWidget(self.button_merge)
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

        # Dictionary of PDF Information
        self.dictPDFs = {}

        # Disable Elements
        self.checkBox_range.setEnabled(False)
        self.spinBox_range_initial.setEnabled(False)
        self.spinBox_range_final.setEnabled(False)
        self.button_view.setEnabled(False)

        # Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionUp.triggered.connect(self.move_up)
        self.actionDown.triggered.connect(self.move_down)
        self.actionSave.triggered.connect(self.merge_pdf)
        self.actionHelp.triggered.connect(self._help)
        self.actionAbout.triggered.connect(self._about)
        self.actionExit.triggered.connect(self._exit)

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

        # listWidget:
        self.listWidget.selectionModel().selectionChanged.connect(self.click_listWidget)

# ==============================================================+

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Merge PDFs"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Advance Options"))
        self.label.setText(_translate("MainWindow", "Select a document"))
        self.checkBox_range.setText(_translate("MainWindow", "Page Range"))
        self.label_2.setText(_translate("MainWindow", "Initial"))
        self.label_3.setText(_translate("MainWindow", "Final"))
        self.button_view.setText(_translate("MainWindow", "View PDF"))
        self.groupBox.setTitle(_translate("MainWindow", "Merge PDFs"))
        self.button_add.setText(_translate("MainWindow", "Add File"))
        self.button_delete.setText(_translate("MainWindow", "Delete"))
        self.button_up.setText(_translate("MainWindow", "/\\"))
        self.button_down.setText(_translate("MainWindow", "\\/"))
        self.button_merge.setText(_translate("MainWindow", "Merge"))
        self.label_notice.setText(_translate("MainWindow", ""))
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

    # Click listWidget
    def click_listWidget(self):
        if not self.dictPDFs:
            # Disabled buttons
            self.label.setText("Select a document")
            self.checkBox_range.setDisabled(True)
            self.spinBox_range_initial.setDisabled(True)
            self.spinBox_range_final.setDisabled(True)
            self.button_view.setDisabled(True)
            return

        # Current item
        selected_item = self.listWidget.currentItem().text()

        # Enabled buttons
        self.checkBox_range.setEnabled(True)
        self.spinBox_range_initial.setEnabled(True)
        self.spinBox_range_final.setEnabled(True)
        self.button_view.setEnabled(True)

        # Gets the state of the elements
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
        selected_item = self.listWidget.currentItem().text().replace("*", "")
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

                # While loop in case a path is repeated
                while self.dictPDFs.get(file_name) is not None:
                    file_name += "*"
                print("Add file:", file_name)
                new_element = file_name
                self.listWidget.addItem(new_element)
                self.dictPDFs[new_element] = [False, [1,1]]
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

    # Merge PDFs
    def merge_pdf(self):

        if self.listWidget.count() < 2:
            print("Add more files")
            self.inf_messages(*("Info", 'Add at least two files'))

        # Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # Notice
            self.label_notice.setText("Merge PDFs, please wait...")
            pdfs = []; pages = []

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row).text()
                print(f'File {row}:', item)
                pdfs.append(item.replace("*", ""))
                pages.append(self.dictPDFs[item])

            options = QFileDialog.Options()

            # Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", ".pdf", "PDF Files (*.pdf)", options=options)

            if file_name:
                status = merge_pdf(name_file=file_name, pdfs=pdfs, pages=pages)
                if status is not True: self.inf_messages(*status); self.label_notice.setText(""); return
                self.inf_messages("Info", "The process has completed")
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
- Merge the PDFs: Ctrl+S
                          
Advance Options:
- Page Range: CheckBox in case you require a PDF document to use a range of pages to combine with others and not the entire document.
- Initial: Page of the document where it will start merging the PDFs with the other PDF documents.
- Final: Final page of the document where it will finish merging with the other PDF documents.
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
