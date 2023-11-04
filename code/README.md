# Code

Here is where the code and program logic are stored. Modify the files only if you know what you're doing; the code is documented to enhance readability. If you intend to modify something, I recommend reading this first: https://doc.qt.io/qtforpython-6/

# Sections
### File `pdfgui_tools.py`
- [Description](#pdfgui_toolspy)
- [class pdfguiMainWindow](#class-pdfguimainwindowui_mainwindow)
- [class aboutWindow](#class-aboutwindowui_aboutwindow)

### File `pdfguiUtils.py`
- [Description](#pdfguiutilspy)
- [class PyPDF2utils](#class-pypdf2utils)
- [class PyMuPDF_Utils](#class-pymupdf_utilsobject)

### File `pdfguiWindows.py`
- [Description](#pdfguiwindowspy)
- [class Ui_MainWindow](#class-ui_mainwindowobject)
- [class class Ui_AboutWindow](#class-ui_aboutwindowobject)
---

## `pdfgui_tools.py`:
This is the main file to run **pdfgui_tools**; it is the Python code that **connects to the logic** in `pdfguiUtils.py` and the **interface** in `Ui_Windows.py`. It links **user interactions** in the pdfgui_tools interface to the functions it includes for working with PDF documents.

### Classes from the file:

#### `class pdfguiMainWindow(Ui_MainWindow)`
This class inherits from the **main window** class of **pdfgui_tools**. It solely connects **user interactions** with the app and makes a few modifications depending on user interactions. If you want to modify the interface, go to the `designer` directory of this repository

- Methods:
```python
# Methods:                  # Arguments:                         # Description:
def __init__                (self):                              # -> Set up the main window and connect user interactions to the rest of the app's functions
def click_listWidget        (self):                              # -> Make changes when an item in the QListWidget is touched
def click_checkBox_range    (self):                              # -> Detects the change in the range checkbox and stores it in the value of the self.dictPDFs dictionary
def spinbox_initial_changed (self):                              # -> Detects the change in the initial range spinbox, and stores it in the self.dictPDFs dictionary
def spinbox_final_changed   (self):                              # -> Detects the change in the final range spinbox, and stores it in the self.dictPDFs dictionary
def click_view              (self):                              # -> Open the PDF document in the default PDF viewer using xdg-open
def click_add               (self):                              # -> Add the PDF documents to the QListWidget from their paths
def click_delete            (self):                              # -> Delete the currently selected item from the QListWidget
def move_up                 (self):                              # -> Move the currently selected item one position up in the QListWidget
def move_down               (self):                              # -> Move the currently selected item one position down in the QListWidget
def merge_pdf               (self):                              # -> Merge all the PDF documents from the QListWidget into a single PDF
def encrypt_decrypt         (self, encrypt:bool, icon_file:str): # -> Encrypt or decrypt the PDF documents from the QListWidget
def separate_pdf            (self):                              # -> Split the selected PDF document into parts in the QListWidget
def convert                 (self):                              # -> Convert the selected document in the QListWidget into a selected multimedia file
def _help                   (self):                              # -> Display a help window
def _about                  (self):                              # -> Show the 'About' window
def inf_messages            (self, title, message):              # -> Function to call in case of an information or error message
```

#### `class aboutWindow(Ui_AboutWindow)`

This class inherits from the **Ui_AboutWindow** window class. If you need to make modifications, use the design file from the `designer` directory of this repository.

- Methods:
```python
# Methods:      # Arguments:       # Description:
def __init__    (self, aboutWin):  # -> Set up the About window and connect the OK button to a lambda function.
```

---

## `pdfguiUtils.py`: 
This is the main utilities file for **pdfgui_tools**, where all the application's utilities are included and will continue to be included. This file will contain variables and classes with their respective functions that will provide functionality to **pdfgui_tools**. Any module can be used as long as it is **stable**.

### Classes from the file:

#### `class PyPDF2utils`
It contains methods for the utilities included in the `PyPDF2` module. These methods return a value depending on the state and integrity of the **PDF document**. They should return a **tuple** with information for the **QMessageBox** window in case of an **error** or **informational** message regarding the **PDF documents**.

- Methods:
```python
# Methods:        # Arguments:                            # Description:
def merge_pdf     (name_file:str, pdfs:list, pages:list): # -> Combine the PDFs from the list.
def separate_pdf  (pdf:str, dest:str):                    # -> Split a PDF document into multiple parts, which are saved in a directory.
def extract_text  (name_file:str, pdf:str):               # -> Extract the text from a PDF per page.
def encrypt_pdf   (pdf:str, password:str):                # -> Encrypt a PDF
def decrypt_pdf   (pdf:str, password:str):                # -> Decrypt a PDF
def fileEncrypted (pdf):                                  # -> Determines if a file is encrypted, to prevent importing the PyPDF2 module twice.
```
#### `class PyMuPDF_Utils(object)`
This contains the utilities included in `PyMuPDF`. Currently, its functionality is not extensive within pdfgui_tools, more features from this Python module will be added. 

This class takes a path to a PDF document as an argument, opens the document, and checks if it is encrypted to work with it. 

- Methods:
```python
# Methods:        # Arguments:     # Description:
def __init__      (self, pdf:str): # -> It takes a PDF path as an argument and opens the document with fitz
def getSize       (self):          # -> Obtains the dimensions of the PDF document
def documentScale (self):          # -> Obtains the scale of the PDF document
```

---

## `pdfguiWindows.py`: 
This file contains the configuration of the **pdfgui_tools interface**. This Python file is generated by the corresponding design file in the `designer` directory of this repository, and it encompasses a combination of all the interfaces created in **Qt Designer**.

### Classes from the file:

#### `class Ui_MainWindow(object)`
This class contains the code generated by the `pdfgui_tools.ui` file in the `designer` directory. It constructs the main interface of **pdfgui_tools**.

- Methods:
```python
# Methods:        # Arguments:              # Description:
def setupUi       (self, MainWindow, icon): # -> File to generate the main interface, it takes two arguments, the window and the icon of pdfgui_tools
def retranslateUi (self, MainWindow):       # -> Generated by pyside6-uic, this file for translations and setting text
```

#### `class Ui_AboutWindow(object):`
This contains the code generated by `about.ui` from the `designer` directory, generating an **About window** with information about **pdfgui_tools**.

- Methods:
```python
# Methods:        # Arguments:                            # Description:
def setupUi       (self, AboutWindow, icon, version_app): # -> This generates the About window, taking three arguments: the About window, the pdfgui_tools icon, and its version
def retranslateUi (self, AboutWindow, version_app):       # -> Generated by pyside6-uic, this file for translations and setting text
```