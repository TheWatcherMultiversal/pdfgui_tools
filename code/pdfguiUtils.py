#! /usr/bin/python3
#
# PDF GUI TOOLS - pdfguiUtils
# 
# pdfguiUtils - Utilities file.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------

from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter # <--- PyPDF2  v1.26.0
import os, subprocess, fitz # <-------------------------------------- PyMuPDF v1.23.5

# Variables and Paths
title_app         = "PDF GUI Tools"#-------------------> Title app
version_app       = "2.0.0"#---------------------------> Version pdfgui_tools
path_pdfgui_tools = ("/usr/share/pdfgui_tools")#-------> Path pdfgui_tools
spinBox_range     = (1, 1000)#-------------------------> Allowed spinbox range
repeat_symbol     = "*"#-------------------------------> Symbol of repeated PDFs in the list (avoids conflicts in the self.dictPDFs dictionary)
maxSizeDocument   = 300#-------------------------------> Maximum document display size.
icon_pdf          = "application-pdf"#-----------------> Qt icon name for PDF document
icon_pdfEncrypt   = "encrypted"#-----------------------> Qt icon name for encrypted files


Paths = {
    "icon_app" : (f"{path_pdfgui_tools}/assets/pdfguitools.svg"),
    "styles"   : (f"{path_pdfgui_tools}/styles/styles.css"),
}

# ---------------------------% PyPDF2 Utils %----------------------------------#

class PyPDF2utils:

    # >> Merge PDFs:
    def merge_pdf(name_file:str, pdfs:list):
        """PDF Merger using the `PyPDF2` module`
    
        :param name_file: Name of the document where the PDFs will be merged

        :param pdfs: Receives a `list` with the paths of the PDFs to merge"""

        try:
            pdf_merger = PdfFileMerger()

            try:
                for pdf in pdfs:
                    path_pdf = pdf[2]; checkRangeBox = pdf[0]; pdf_range = (pdf[1][0], pdf[1][1])

                    if PyPDF2utils.fileEncrypted(path_pdf): 
                        return("Info", f"The document {path_pdf} is encrypted, decrypt it to perform this action")

                    if checkRangeBox: ran_page = pdf_range
                    else: ran_page = None

                    pdf_merger.append(open(path_pdf, 'rb'), pages=ran_page)

            except IndexError: return("Error", f"Index error in the file {path_pdf}, please enter a valid value")
            except: return("Error", f"The document {path_pdf} could not be processed, please check the integrity of the document")

            with open(name_file, 'wb') as f:
                pdf_merger.write(f)

        except: return("Error", "The documents could not be processed")
        return True


    # >> Separate PDFs:
    def separate_pdf(pdf:str, dest:str):
        """PDF Splitter using the `PyPDF2` module
        
        :param pdf: PDF Document Path

        :param dest: Path to the directory to create, where the separated PDF documents will be stored"""

        try:
            pdf_reader = PdfFileReader(pdf)
            dest_name = os.path.basename(dest)
            
            try:
                subprocess.run([f'mkdir {dest}'], check=True, shell=True)
            except subprocess.CalledProcessError:
                return("Error", f"The directory {dest} could not be created.")

            for i in range(pdf_reader.numPages):
                pdf_writer = PdfFileWriter()
                pdf_writer.addPage(pdf_reader.getPage(i))

                with open(f"{dest}/{dest_name}_{i + 1}.pdf", 'wb') as f:
                    pdf_writer.write(f)
        except: return("Error", "The document could not be processed, please check the integrity of the file.")
        return True


    # >> Extract Text:
    def extract_text(name_file:str, pdf:str):
        """Text Extractor using the `PyPDF2` module.
        
        :param name_file: PDF Document Name in Text
        
        :param pdf: PDF Document Path"""

        try:
            pdf_reader = PdfFileReader(pdf)
            extract_content = ""

            for i in range(pdf_reader.numPages):
                text_page = pdf_reader.getPage(i).extractText().replace("\n", " ")
                extract_content += f'{text_page}\r\n \r\n'

            with open(name_file, "w", encoding="utf-8") as f:
                f.write(extract_content)
        except: return("Error", "The document could not be processed, please check the text format and the integrity of the document")
        return True


    # >> Encrypt PDFs:
    def encrypt_pdf(pdf:str, password:str):
        """Encrypt PDF documents using the `PyPDF2` module
        
        :param pdf: PDF Document Path
        
        :param password: Gets the password to use for encrypting the document"""

        try:
            pdf_writer = PdfFileWriter()
            pdf_reader = PdfFileReader(pdf)

            if pdf_reader.isEncrypted:
                return("Info", f"The document {pdf} is already encrypted")

            for i in range(pdf_reader.numPages):
                page = pdf_reader.getPage(i)
                pdf_writer.addPage(page)

            pdf_writer.encrypt(password)

            with open(pdf, "wb") as f:
                pdf_writer.write(f)
        
        except: return("Error", "The file could not be encrypted, please check the document's integrity")
        return True


    # >> Decrypt PDFs:
    def decrypt_pdf(pdf:str, password:str):
        """Decrypt PDF documents using the `PyPDF2` module
        
        :param pdf: PDF Document Path
        
        :param password: Gets the password to use for decrypting the file"""

        try:
            pdf_writer = PdfFileWriter()
            pdf_reader = PdfFileReader(pdf)

            if not pdf_reader.isEncrypted:
                return("Info", f"The document {pdf} is already decrypted.")

            returncode = pdf_reader.decrypt(password)
            if returncode == 0:
                return("Info", f"Incorrect password for the document {pdf}, please try another password")
            
            for i in range(pdf_reader.numPages):
                page = pdf_reader.getPage(i)
                pdf_writer.addPage(page)
                
            with open(pdf, "wb") as f:
                pdf_writer.write(f)

        except: return("Error", "The file could not be encrypted, please check the document's integrity")
        return True


    # >> PDF id Encrypted:
    def fileEncrypted(pdf):
        try: return PdfFileReader(pdf).isEncrypted
        except: return False



class PyMuPDF_Utils(object):

    def __init__(self, pdf:str):
        """Utilities included in the `fitz` module of PyMuPDF"""

        self.document = fitz.open(pdf)
        self.isEncrypted = PyPDF2utils.fileEncrypted(pdf)


    # Obtains the dimensions of the PDF document
    def getSize(self):
        """Obtains the dimensions of the PDF document"""

        if not self.isEncrypted:
            firts_page = self.document[0]
            return (firts_page.rect.width, firts_page.rect.height)


    # Obtains the scale of the PDF document
    def documentScale(self):
        """Obtains the scale of the PDF document"""

        if not self.isEncrypted:
            documentSize = self.getSize()
            if documentSize is None: return
            return round(documentSize[1] / documentSize[0], 2)
