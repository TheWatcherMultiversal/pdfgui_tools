## Designer

Here the UI files are stored to work directly with Qt 5 Designer. Each file must be converted to a Python file in order to be used and apply the programming logic in the program. Use the following command to perform this action:

    pyuic5 -x file.ui -o file.py

### Files: 

- `pdfgui_tools.ui` - main section of the app
- `pdfgui_pdfunite.ui` - merge PDFs
- `pdfgui_pdfseparate.py` - separate PDF
- `pdfgui_pdftocairo.py` - PDF to media file
- `pdfgui_pdftohtml.ui` - PDF to html
- `pdfgui_pdftotext.ui` - PDF to text
- `about.py.ui` - about window