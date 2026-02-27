"""Configuration constants for the search server."""

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_PATH)

PATH_DOCUMENTS = os.path.join(PROJECT_ROOT, "documents")

PATH_EXCEL = os.path.join(PATH_DOCUMENTS, "excel")
PATH_PDF = os.path.join(PATH_DOCUMENTS, "pdf")
PATH_TXT = os.path.join(PATH_DOCUMENTS, "txt")
PATH_HTML = os.path.join(PATH_DOCUMENTS, "html")

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
BUFFER_SIZE = 4096
ENDING_MSG = "q"

SUPPORTED_EXTENSIONS = [".xlsx", ".pdf", ".txt", ".html"]