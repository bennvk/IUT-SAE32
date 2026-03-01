"""File reading fonctions for txt, html, excel and pdf files"""

import os
import pandas as pd
import pdfplumber
from bs4 import BeautifulSoup


def read_txt_file(file_path):
    """Return a list of lines from a TXT file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_html_file(file_path):
    """
    Extract visible text from an HTML file and return it as a list of clean lines.
    Ignores scripts, styles, noscript, and comments.
    """
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Supprimer les balises non visibles
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    # Supprimer les commentaires
    for comment in soup.find_all(string=lambda text: isinstance(text, type(soup.Comment))):
        comment.extract()

    # Récupérer tout le texte visible
    text = soup.get_text(separator="\n")  # Utiliser "\n" pour séparer les blocs

    # Nettoyer et filtrer les lignes vides
    lines = [line.strip() for line in text.splitlines() if line.strip()]

    return lines


def read_excel_file(file_path):
    """Return structured data from Excel file."""
    sheets = pd.read_excel(file_path, sheet_name=None, engine="openpyxl")
    data = []

    for sheet_name, dataframe in sheets.items():
        for row_index, row in dataframe.iterrows():
            for col_index, cell in enumerate(row):
                if pd.notna(cell):
                    data.append({
                        "row": row_index + 2,      # +2 car Excel commence à 1 + header
                        "column": col_index + 1,
                        "content": str(cell)
                    })

    return data


def read_pdf_file(file_path):
    """Return a list of text lines extracted from a PDF file."""
    lines = []

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # splitlines() conserve les vraies lignes reconstruites
                lines.extend(text.splitlines())

    return lines
