"""Search engine module."""

import os
from collections import defaultdict
from config import PATH_DOCUMENTS
from file_readers import (
    read_txt_file,
    read_html_file,
    read_excel_file,
    read_pdf_file
)

SUPPORTED_READERS = {
    ".txt": read_txt_file,
    ".html": read_html_file,
    ".xlsx": read_excel_file,
    ".pdf": read_pdf_file,
}


def get_reader(file_path):
    _, ext = os.path.splitext(file_path)
    return SUPPORTED_READERS.get(ext.lower())


def search_in_file(file_path, keyword):
    reader = get_reader(file_path)
    if not reader:
        return []

    try:
        lines = reader(file_path)
    except Exception:
        return []

    matches = []
    keyword = keyword.lower()
    filename = os.path.basename(file_path)

    for line_number, line in enumerate(lines, start=1):
        if keyword in line.lower():
            matches.append({
                "line": line_number,
                "content": line.strip(),
            })

    return filename, matches


def search_in_directory(keyword):
    if not keyword.strip():
        return {}, 0, 0

    grouped_results = defaultdict(list)
    total_matches = 0

    for root, _, files in os.walk(PATH_DOCUMENTS):
        for file in files:
            file_path = os.path.join(root, file)
            filename, matches = search_in_file(file_path, keyword)

            if matches:
                grouped_results[filename].extend(matches)
                total_matches += len(matches)

    total_files = len(grouped_results)

    return grouped_results, total_matches, total_files