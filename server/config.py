"""Configuration constants for the search server."""

import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(BASE_PATH)
PATH_DOCUMENTS = os.path.join(PROJECT_ROOT, "documents")
SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5000
