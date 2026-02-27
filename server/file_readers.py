"""File reading fonctions for txt, html, excel and pdf files"""

import os
import pandas as pd
import PyPDF2


def read_txt_file(file_path):
    """Return a list of lines from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_html_file(file_path):
    """Return a list of lines from an HTML file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_excel_file(file_path):
    """Return a list of rows from an Excel file."""
    dataframe = pd.read_excel(file_path)
    rows = []
    for index, row in dataframe.iterrows():
        rows.append(" ".join(map(str, row.values)))
    return rows


def read_pdf_file(file_path):
    """Return a list of text lines extracted from a PDF file."""
    lines = []
    with open(file_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            if text:
                lines.extend(text.split("\n"))
    return lines