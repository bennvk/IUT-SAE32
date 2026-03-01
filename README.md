# SAE3.02

## Project Overview

SAE3.02 is a simple web application that allows you to search for keywords in various file types (TXT, HTML, PDF, Excel) within a specified documents directory. The results show the file name, line number, and content where the keyword appears.

## Features

- Search in TXT, HTML, PDF, and Excel files.
- Display results with line numbers and Excel column numbers.
- Clean extraction of text from HTML and PDF files.

## Installation

1. Clone the repository
```
git clone <repository_url>
cd <repository_folder>
```

2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate  # Linux / macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies
```
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```
python app.py
```
2. Open your browser and go to `http://127.0.0.1:5000`.
3. Enter a keyword in the search box and view the results.
## Dependencies

```
Flask==2.3.2
pandas==2.1.1
pdfplumber==0.9.0
beautifulsoup4==4.12.2
openpyxl==3.1.2
```

