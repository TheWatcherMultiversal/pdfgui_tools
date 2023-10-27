# Code

Here is where the code and program logic are stored. Modify the files only if you know what you're doing; the code is documented to enhance readability. If you intend to modify something, I recommend reading this first: https://doc.qt.io/qtforpython-6/

## File `pdfguiUtils.py`: 
This is the main utilities file for **pdfgui_tools**, where all the application's utilities are included and will continue to be included. This file will contain variables and classes with their respective functions that will provide functionality to **pdfgui_tools**. Any module can be used as long as it is **stable**.

### Classes from the file:

#### `class PyPDF2utils`
It contains functions for the utilities included in the `PyPDF2` module. These functions return a value depending on the state and integrity of the **PDF document**. They should return a **tuple** with information for the **QMessageBox** window in case of an **error** or **informational** message regarding the **PDF documents**.

- Functions:
```python
# Functions:      # Arguments:                            # Description:
def merge_pdf     (name_file:str, pdfs:list, pages:list): # -> Combine the PDFs from the list.
def separate_pdf  (pdf:str, dest:str):                    # -> Split a PDF document into multiple parts, which are saved in a directory.
def extract_text  (name_file:str, pdf:str):               # -> Extract the text from a PDF per page.
def encrypt_pdf   (pdf:str, password:str):                # -> Encrypt a PDF
def decrypt_pdf   (pdf:str, password:str):                # -> Decrypt a PDF
def fileEncrypted (pdf):                                  # -> Determines if a file is encrypted, to prevent importing the PyPDF2 module twice.
```
