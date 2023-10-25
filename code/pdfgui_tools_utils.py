#! /usr/bin/python3
#
# PDF GUI TOOLS - pdfgui_tools_utils
# 
# pdfgui_tools_utils - Utilities file.
# Author: Angel Gabriel Mortera Gual
# License: GNU GENERAL PUBLIC LICENSE v3
#
# Project: https://github.com/TheWatcherMultiversal/pdfgui_tools/
#
# -----------------------------------------------------------------------------------


from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
import os, subprocess

# Variables and Paths
version_app = "1.1.0"
spinBox_range = (1, 1000)
path_pdfgui_tools = ("/usr/share/pdfgui_tools")

Paths = {
    "icon_app"     : (f"{path_pdfgui_tools}/assets/pdfguitools.svg"),
    "styles"       : (f"{path_pdfgui_tools}/styles/styles.css"),
    "about_window" : (f"{path_pdfgui_tools}/about.py"),
    "poppler_path" : (f"{path_pdfgui_tools}/poppler_utils"),
    "pypdf2_path"  : (f"{path_pdfgui_tools}/pypdf2_utils"),
}

# ---------------------------% PyPDF2 Utils %----------------------------------#

# >> Merge PDFs:
def merge_pdf(name_file:str, pdfs:list, pages:list):
    """PDF Merger using the `PyPDF2` module`
  
    :param name_file: Name of the document where the PDFs will be merged

    :param pdfs: Receives a `list` with the paths of the PDFs to merge
    
    :param pages: Receives a `list` with the page ranges for merging each document"""

    try:
        pdf_merger = PdfFileMerger()

        try:
            for pdf, page in zip(pdfs, pages):
                if page[0]: page = (page[1][0] - 1, page[1][1])
                else: page = None
                pdf_merger.append(open(pdf, 'rb'), pages=page)

        except IndexError: return("Error", f"Index error in the file {pdf}, please enter a valid value")
        except: return("Error", f"The document {pdf} could not be processed, please check the integrity of the document")

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