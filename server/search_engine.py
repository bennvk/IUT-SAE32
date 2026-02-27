"""Search engine module."""

import os
from config import PATH_DOCUMENTS
from file_readers import (
    read_txt_file,
    read_html_file,
    read_excel_file,
    read_pdf_file
)


def search_in_file(file_path, keyword):
    """Search for a keyword in a file and return matches with line numbers."""
    matches = []

    if file_path.endswith(".txt"):
        lines = read_txt_file(file_path)
    elif file_path.endswith(".html"):
        lines = read_html_file(file_path)
    elif file_path.endswith(".xlsx"):
        lines = read_excel_file(file_path)
    elif file_path.endswith(".pdf"):
        lines = read_pdf_file(file_path)
    else:
        return matches

    for line_number, line in enumerate(lines, start=1):
        if keyword.lower() in line.lower():
            filename = os.path.basename(file_path)
            matches.append((filename, line_number, line.strip()))

    return matches


def search_in_directory(keyword):
    """Search for a keyword in all supported documents."""
    results = []

    for root, _, files in os.walk(PATH_DOCUMENTS):
        for file in files:
            file_path = os.path.join(root, file)
            file_results = search_in_file(file_path, keyword)
            results.extend(file_results)

    return results