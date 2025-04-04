# PDF Bank Statement Table Extractor

## Overview

This project is a Python-based tool designed to extract transaction rows from system-generated bank statement PDFs. It uses **pdfplumber** to read PDF contents, applies heuristics and regular expressions to detect transaction lines, and exports the extracted data into an Excel file using **pandas** and **openpyxl**. This solution avoids using external table extraction libraries like Tabula or Camelot, and it does not convert PDFs into images.

## Features

- **PDF Parsing:** Utilizes pdfplumber to extract text from PDFs.
- **Transaction Extraction:** Applies regex and heuristics to identify transaction rows that span multiple lines.
- **Excel Export:** Converts the extracted transactions into an Excel spreadsheet.
- **Command-Line Interface:** Simple CLI for specifying the input PDF and output Excel file paths.

## Project Structure

pdf_table_extractor/ ├── sample.py # Main Python script for extraction ├── input.pdf # Example input PDF file (place your own PDF here) └── README.md # This documentation file


## Requirements

- Python 3.x
- [pdfplumber](https://github.com/jsvine/pdfplumber)
- [pandas](https://pandas.pydata.org/)
- [openpyxl](https://openpyxl.readthedocs.io/en/stable/)

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/pdf_table_extractor.git
   cd pdf_table_extractor
Install Dependencies:

Use pip to install the required libraries:

pip install pdfplumber pandas openpyxl
If you’re using Python 3 and your pip is configured as pip3, run:

pip3 install pdfplumber pandas openpyxl
Usage
Place the Input File:

Ensure your PDF file (e.g., input.pdf) is located in the same folder as sample.py. If your file has a different name, adjust the command accordingly.

Run the Script:

Open your terminal or command prompt, navigate to the project folder, and run:

python sample.py input.pdf output.xlsx
input.pdf is the input PDF file.

output.xlsx is the name of the Excel file that will be created with the extracted transaction data.

Review the Output:

After the script completes, open output.xlsx with Excel or any compatible spreadsheet application to view the extracted data.

How It Works
PDF Parsing:

The script uses pdfplumber to open and extract text from each page of the PDF.

The text is split into lines and processed sequentially.

Transaction Detection:

A regular expression identifies lines starting with a date (in the format DD-MMM-YYYY), marking the beginning of a transaction.

The following non-empty line is assumed to contain the transaction amount and balance.

The script captures details such as Date, Transaction Type, Description, Transaction Amount, and Balance.

Excel Export:

The extracted data is organized into a pandas DataFrame.

The DataFrame is then written to an Excel file using openpyxl.

Future Improvements
Enhanced Parsing: Improve the logic to handle more complex transaction formats or multi-line transactions.

Graphical User Interface (GUI): Develop a user-friendly GUI for users who prefer not to use the command line.

Extended Format Support: Enhance compatibility with various bank statement formats.

Detailed Logging: Add logging functionality for easier debugging and error tracking.

License
This project is open source and available under the MIT License. Contributions and modifications are welcome.

Contributing
Contributions are encouraged! Feel free to open issues or submit pull requests with improvements, bug fixes, or new features.

Contact
For questions or feedback, please reach out via [your email address or GitHub profile].

Happy coding!
