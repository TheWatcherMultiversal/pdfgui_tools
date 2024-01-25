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

from pdfguiWindows     import (Ui_MainWindow, Ui_AboutWindow, QApplication, QMainWindow, QListWidgetItem, QSize, QCoreApplication, QIcon, QFont, QPixmap)
from pdfguiUtils       import (Paths, version_app, repeat_symbol, icon_pdf, icon_pdfEncrypt, spinBox_range, maxSizeDocument, PyPDF2utils, PyMuPDF_Utils)
from PySide6.QtWidgets import (QMessageBox, QFileDialog)# <---| 
from PySide6.QtCore    import (Qt)# <-------------------------| PySide6 v6.6.1
import sys, os, subprocess, argparse

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Arguments:

parser = argparse.ArgumentParser()
parser.add_argument('-m', '--man',     action='store_true', help='man page')
parser.add_argument('-v', '--version', action='store_true', help='print version')
args = parser.parse_args()

if   args.man     is True : os.system('man pdfgui_tools')          ; sys.exit()
elif args.version is True : print(f'PDF GUI Tools v{version_app}') ; sys.exit()

# ----------------------------------------------------------------------------------------------------------------
#   |
#   |
#   °-- Code pdfgui_tools:


# Class for the main window
class pdfguiMainWindow(Ui_MainWindow):

    # Setting values for the main window
    def __init__(self):
        # -> Icon app
        icon_app = QIcon(); icon_app.addPixmap(QPixmap(Paths["icon_app"]), QIcon.Normal, QIcon.Off)

        # -> Build the main window interface
        self.setupUi(MainWindow, icon_app) 

        # -> Dictionary of PDF Information
        self.dictPDFs = {}

        # -> Dictionary type of document conversion
        self.dictConvert = {
            "HTML" : ("pdftohtml"       , False),
            "TXT"  : ("pdftotext"       , False),
            "PNG"  : ("pdftocairo -png" , True),
            "JPEG" : ("pdftocairo -jpeg", True),
        }
        for pdftocairo in ("PS", "EPS", "SVG"):
            self.dictConvert[pdftocairo] = (f'pdftocairo -{pdftocairo.lower()}', False)

        # -> Disable Elements
        self.checkBox_range.setEnabled(False)
        self.spinBox_range_initial.setEnabled(False)
        self.spinBox_range_final.setEnabled(False)
        self.button_view.setEnabled(False)
        self.button_separate.setEnabled(False)
        self.button_convert.setEnabled(False)

        # -> Actions
        self.actionAdd_File.triggered.connect(self.click_add)
        self.actionDelete.triggered.connect(self.click_delete)
        self.actionUp.triggered.connect(self.move_up)
        self.actionDown.triggered.connect(self.move_down)
        self.actionView_Utils.triggered.connect(lambda: self.dockWidget.show())
        self.actionMerge.triggered.connect(self.merge_pdf)
        self.actionHelp.triggered.connect(self._help)
        self.actionAbout.triggered.connect(self._about)
        self.actionExit.triggered.connect(lambda: MainWindow.close())
        self.actionEncrypt.triggered.connect(lambda: self.encrypt_decrypt(True, icon_pdfEncrypt))
        self.actionDecrypt.triggered.connect(lambda: self.encrypt_decrypt(False, icon_pdf))

        # -> checkBox
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

        # -> Buttons
        self.button_view.clicked.connect(self.click_view)
        self.button_add.clicked.connect(self.click_add)
        self.button_delete.clicked.connect(self.click_delete)
        self.button_up.clicked.connect(self.move_up)
        self.button_down.clicked.connect(self.move_down)
        self.button_utils.clicked.connect(lambda: self.dockWidget.show())
        self.button_merge.clicked.connect(self.merge_pdf)
        self.button_encrypt.clicked.connect(lambda: self.encrypt_decrypt(True, icon_pdfEncrypt))
        self.button_decrypt.clicked.connect(lambda: self.encrypt_decrypt(False, icon_pdf))
        self.button_separate.clicked.connect(self.separate_pdf)
        self.button_convert.clicked.connect(self.convert)

        # -> listWidget:
        self.listWidget.selectionModel().selectionChanged.connect(self.click_listWidget)


    # Click listWidget
    def click_listWidget(self):
        # -> The index of the selected item is obtained
        selected_item = self.listWidget.selectionModel().selectedIndexes()

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
            # -> View Document:
            self.label_doc_view.setPixmap(QPixmap(""))
            return

        # -> Current item data
        item = selected_item[0].data()

        # -> Enabled buttons
        self.checkBox_range.setEnabled(True)
        self.spinBox_range_initial.setEnabled(True)
        self.spinBox_range_final.setEnabled(True)
        self.button_view.setEnabled(True)
        self.button_separate.setEnabled(True)
        self.button_convert.setEnabled(True)
        self.button_convert.setEnabled(True)

        # -> Gets the state of the elements
        self.checkBox_range.setChecked(self.dictPDFs[item][0]) 
        self.spinBox_range_initial.setValue(self.dictPDFs[item][1][0])
        self.spinBox_range_final.setValue(self.dictPDFs[item][1][1])
        self.label.setText(item)

        # -> Gets the scale and size of the document
        try:
            scale = PyMuPDF_Utils(self.dictPDFs[item][2]).documentScale()
            if scale is None: scale = 1
            self.scrollVerticalLayout_DocPreview.setMaximumSize(QSize(maxSizeDocument, int(maxSizeDocument * scale)))
        except:
            self.scrollVerticalLayout_DocPreview.setMaximumSize(QSize(maxSizeDocument, maxSizeDocument))

        # -> View Document:
        self.label_doc_view.setPixmap(QPixmap(self.dictPDFs[item][2]))


    # Click checkBox 'Page Range'
    def click_checkBox_range(self):
        check_state = self.checkBox_range.checkState().value > 0
        selected_item = self.listWidget.selectionModel().selectedIndexes()
        item = selected_item[0].data()
        self.dictPDFs[item][0] = check_state


    # Gets the change from the spinBox
    def spinbox_initial_changed(self):
        get_value = self.spinBox_range_initial.value()
        selected_item = self.listWidget.selectionModel().selectedIndexes()
        item = selected_item[0].data()
        self.dictPDFs[item][1][0] = get_value


    def spinbox_final_changed(self):
        get_value = self.spinBox_range_final.value()
        selected_item = self.listWidget.selectionModel().selectedIndexes()
        item = selected_item[0].data()
        self.dictPDFs[item][1][1] = get_value
        

    def click_view(self):
        selected_item = self.listWidget.selectionModel().selectedIndexes()
        item = selected_item[0].data()
        view_doc = self.dictPDFs[item][2]
        try:
            subprocess.run(f"xdg-open '{view_doc}'", shell=True, check=True)
        except subprocess.CalledProcessError:
            self.inf_messages(*("Error", 'The selected document could not be viewed'))


    # Function to add a file to 'self.listWidget'
    def click_add(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(MainWindow, "Select PDF Files", "", "PDF Files (*.pdf);;All Files (*)", options=options)
        if files:
            for pdf in files:
                path_file = pdf
                pdf = os.path.basename(pdf)
                # ---> While loop in case a path is repeated
                while self.dictPDFs.get(pdf) is not None:
                    pdf += repeat_symbol
                
                # ---> Set the icon type
                if PyPDF2utils.fileEncrypted(path_file): icon_file = icon_pdfEncrypt
                else: icon_file = icon_pdf
                icon = QIcon(QIcon.fromTheme(icon_file))
                font = QFont(); font.setPointSize(11); font.setBold(True)

                __qlistwidgetitem = QListWidgetItem(self.listWidget); __qlistwidgetitem.setTextAlignment(Qt.AlignCenter)
                __qlistwidgetitem.setFont(font)                     ; __qlistwidgetitem.setIcon(icon)
                __qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", pdf, None));

                self.dictPDFs[pdf] = [False, [1,1], path_file, __qlistwidgetitem]


    # Function to delete the selected item from the 'self.listWidget' widget
    def click_delete(self):
            selected_item = self.listWidget.currentItem()
            if selected_item:
                item = selected_item.text()
                del self.dictPDFs[item]#-------------------> Remove the element from the PDF Dictionary
                row = self.listWidget.row(selected_item)
                self.listWidget.takeItem(row)


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
            self.inf_messages(*("Info", 'Add at least two files'))

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Notice
            self.label_notice.setText("Merge PDFs, please wait..."); pdfs = []

            for row in range(self.listWidget.count()):
                item = self.listWidget.item(row).text()
                pdfs.append(self.dictPDFs[item])

            options = QFileDialog.Options()

            # --> Asks where to save and how to name the file, obtains the path
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", ".pdf", "PDF Files (*.pdf)", options=options)

            if file_name:
                status = PyPDF2utils.merge_pdf(name_file=file_name, pdfs=pdfs)
                if status is not True: self.inf_messages(*status); self.label_notice.setText(""); return
                self.inf_messages("Info", "The process has completed")

            self.label_notice.setText("")


    # Encrypt or Decrypt PDFs:
    def encrypt_decrypt(self, encrypt:bool, icon_file:str):
        if self.listWidget.count() < 1:
            self.inf_messages(*("Info", 'Add at least one file'))

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            if encrypt: notice = "Encrypting Files..."
            else:       notice = "Decrypting Files..."

            # --> Notice
            self.label_notice.setText(notice)

            # --> Get Values
            pdfs = self.dictPDFs.values()

            # --> Confirm the action of encrypting or decrypting
            confirm_dialog = QMessageBox.question(MainWindow, "Confirm the action", "Are you sure you want to perform the action?", QMessageBox.Yes | QMessageBox.No)
            if confirm_dialog == QMessageBox.No: self.label_notice.setText(""); return

            # --> The 'Password' field is empty
            if not self.lineEdit_password.text(): self.inf_messages("Info", "Enter a password"); self.label_notice.setText(""); return

            for pdf in pdfs:
                doc_pdf = pdf[2]; itemListWidget = pdf[3]
                if encrypt: status = PyPDF2utils.encrypt_pdf(doc_pdf, self.lineEdit_password.text())
                else:       status = PyPDF2utils.decrypt_pdf(doc_pdf, self.lineEdit_password.text())
                if status is not True: self.inf_messages(*status); continue
                
                # Change Icon Item
                itemListWidget.setIcon(QIcon(QIcon.fromTheme(icon_file)))

            self.inf_messages("Info", "The process has completed"); self.label_notice.setText("")


    # Separate PDF
    def separate_pdf(self):

        if self.listWidget.count() < 1:
            self.inf_messages("Info", 'You need to add file')

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Command
            self.command = "pdfseparate"

            # --> Notice
            self.label_notice.setText("Separate pdf, please wait...")

            # --> Get Current Item
            selected_item = self.listWidget.selectionModel().selectedIndexes() ; item = selected_item[0].data()
            path_pdf = self.dictPDFs[item][2]                                  ; checkRangeState = self.dictPDFs[item][0]

            # --> File encrypted
            if PyPDF2utils.fileEncrypted(path_pdf):
                self.inf_messages("Info", f"The document {item} is encrypted, decrypt it to perform this action")
                self.label_notice.setText(""); return

            # --> Compare the status of the checkboxes
            if checkRangeState:
                ran_pages = self.dictPDFs[item][1]
                self.command += ' ' + f'-f {ran_pages[0]}'
                self.command += ' ' + f'-l {ran_pages[1]}'

            # --> Add the path to the command
            self.command += ' "' + path_pdf + '"'

            # --> Asks where to save and how to name the file, obtains the path
            options = QFileDialog.Options()
            options |= QFileDialog.ShowDirsOnly
            options |= QFileDialog.DontUseNativeDialog
            directory, _ = QFileDialog.getSaveFileName(MainWindow, "Create Directory", "", "", options=options)
            directory_name = str(os.path.basename(directory))

            if directory:
                # ---> An attempt is made to create the directory
                try:
                    subprocess.run([f'mkdir "{directory}"'], check=True, shell=True)
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Error while creating the directory, please try with another name')
                    self.label_notice.setText(""); return

                self.command += " " + str(f'"{directory}/{directory_name}%d.pdf"')

                # ---> Run the 'pdfseparate' command in the system
                try:
                    subprocess.run([self.command], check=True, shell=True)
                    self.inf_messages("Info", "The process has completed")
                except subprocess.CalledProcessError:
                    self.inf_messages("Error", 'Verify the options and file integrity, use the F1 key for help')

            self.label_notice.setText("")


    # Convert PDF
    def convert(self):

        if self.listWidget.count() < 1:
            self.inf_messages("Info", 'You need to add file')

        # -> Concatenate the paths of the files stored in the list to the 'self.command' command
        else:
            # --> Get the value of the ComboBox
            filetype = str(self.combo_filetype.currentText())
            lower_filetype = filetype.lower()

            # --> Get Current Item
            selected_item = self.listWidget.selectionModel().selectedIndexes(); item = selected_item[0].data()
            path_pdf = self.dictPDFs[item][2]
            
            # --> Notice
            self.label_notice.setText(f"Convert pdf to {lower_filetype}, please wait...")

            # --> File encrypted
            if PyPDF2utils.fileEncrypted(path_pdf):
                self.inf_messages("Info", f"The document {item} is encrypted, decrypt it to perform this action")
                self.label_notice.setText(""); return

            # --> Obtains the type of conversion and command
            self.command = self.dictConvert[filetype][0]

            # --> Add the path to the command
            self.command += ' "' + path_pdf + '"'

            # --> Asks where to save and how to name the file, obtains the path
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getSaveFileName(MainWindow, "Save File", f".{lower_filetype}", f"{filetype} Files (*.{lower_filetype})", options=options)

            if file_name:
                if self.dictConvert[filetype][1]: self.command += " " + (f'"{file_name[:- len(filetype) - 1]}"')
                else: self.command += " " + (f'"{file_name}"')
                print(self.command)
                print("Save file:", file_name)

                # ---> Run the command in the system
                try:
                    subprocess.run([self.command], check=True, shell=True)
                    self.inf_messages("Info", "The process has completed")
                except subprocess.CalledProcessError:
                    self.label_notice.setText("")
                    self.inf_messages("Error", 'Error Executing the command, please verify the name and integrity of the document')

            self.label_notice.setText("")


# --------------------------------------| About and Help window |-----------------------------------------------------------------------------------

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

    def _about(self):
        aboutWin = QMainWindow(MainWindow); aboutWindow(aboutWin)
        aboutWin.show()

# -------------------------------------------------------------------------------------------------------------------------------------------------------

    # Messages
    def inf_messages(self, title, message):
        if   title == "Error" : QMessageBox.critical   (MainWindow, title, message, QMessageBox.Ok)
        elif title == "Info"  : QMessageBox.information(MainWindow, title, message, QMessageBox.Ok)



# Class for the Ui_AboutWindow window
class aboutWindow(Ui_AboutWindow):

    # Setting values for the about window
    def __init__(self, aboutWin):
        self.setupUi(aboutWin, Paths["icon_app"], version_app)
        self.button_ok.clicked.connect(lambda: aboutWin.close())



if __name__ == "__main__":
    app = QApplication(sys.argv) ; MainWindow = QMainWindow()
    pdfguiMainWindow()           ; MainWindow.show()
    with open(Paths["styles"], "r") as f:#-------------> Window style file
        _style = f.read()
        app.setStyleSheet(_style)
    sys.exit(app.exec())