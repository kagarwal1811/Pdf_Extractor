Here’s an enhanced, more visually appealing README with emojis and styling. You can copy and paste this into your `README.md` file and adjust as needed:

---

# 🏦 PDF Bank Statement Table Extractor

A simple yet powerful tool to extract transaction data from system-generated bank statement PDFs, all without converting them to images! 

[![GitHub stars](https://img.shields.io/github/stars/kagarwal1811/Pdf_Extractor.svg)](https://github.com/kagarwal1811/Pdf_Extractor/stargazers)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](./LICENSE)

---

## ⚙️ Features

- **PDF Parsing**: Utilizes [pdfplumber](https://github.com/jsvine/pdfplumber) to reliably extract text from PDFs.
- **Transaction Extraction**: Uses regex and heuristics to identify transaction lines that may span multiple lines.
- **Excel Export**: Seamlessly converts extracted data into Excel format with the help of [pandas](https://pandas.pydata.org/) and [openpyxl](https://openpyxl.readthedocs.io/en/stable/).
- **CLI Support**: Simple command-line interface to specify input/output paths.

---

## 📂 Project Structure

```bash
Pdf_Extractor/
├── sample.py        # Main Python script for extraction
├── input.pdf        # Example input PDF file (place your own PDF here)
├── README.md        # This documentation file
└── ... (other files or folders if any)
```

---

## 📋 Requirements

- Python 3.x
- pdfplumber
- pandas
- openpyxl

> **Tip**: Use a virtual environment for clean dependency management.

---

## 🚀 Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kagarwal1811/Pdf_Extractor.git
   cd Pdf_Extractor
   ```

2. **Install Dependencies:**
   ```bash
   pip install pdfplumber pandas openpyxl
   ```
   > If you use Python 3 and your pip is configured as `pip3`, run:
   > ```bash
   > pip3 install pdfplumber pandas openpyxl
   > ```

---

## 💻 Usage

1. **Place the Input File**:  
   Make sure your PDF file (e.g., `input.pdf`) is located in the same folder as `sample.py`. If your file has a different name, adjust the command accordingly.

2. **Run the Script**:
   ```bash
   python sample.py input.pdf output.xlsx
   ```
   - `input.pdf` is the input PDF file.
   - `output.xlsx` is the name of the Excel file that will be created with the extracted transaction data.

3. **Review the Output**:  
   Open `output.xlsx` with Excel or any compatible spreadsheet application to view the extracted data.

---

## 🔍 How It Works

1. **PDF Parsing**:  
   - The script uses **pdfplumber** to open and read text from each page of your PDF statement.
   - Text is split into lines and processed sequentially to identify transaction entries.

2. **Transaction Detection**:
   - A regular expression identifies lines that match a date format (e.g., `DD-MMM-YYYY`) as the start of a transaction.
   - The subsequent line(s) (non-empty) is interpreted for transaction details like amount and balance.
   - The tool assembles all relevant fields:  
     - **Date**  
     - **Transaction Type**  
     - **Description**  
     - **Transaction Amount**  
     - **Balance**  

3. **Excel Export**:
   - The gathered data is structured into a **pandas** DataFrame.
   - The DataFrame is then written to an Excel file using **openpyxl** for easy distribution and analysis.

---

## 🌱 Future Improvements

- **Enhanced Parsing**: Improve logic to handle more intricate transaction formats or multi-line descriptions.
- **GUI**: Create a user-friendly graphical interface for those who prefer not to use the command line.
- **Extended Format Support**: Expand compatibility for different bank statement layouts.
- **Logging**: Integrate logging for better debugging and error tracing.

---

## 🤝 Contributing

Contributions are always welcome! If you have ideas or find any bugs:
1. **Fork** this repository.
2. **Create** a new branch.
3. **Commit** your changes.
4. **Submit** a Pull Request.

We’ll review and merge your changes as soon as possible. Don’t forget to ⭐ star the repo if you find it useful!

---

## 📝 License

This project is licensed under the **MIT License**. Check out the full license text in the [LICENSE](./LICENSE) file.

---

## 👨‍💻 Contact

**Author**: [Kunal Agarwal](https://github.com/kagarwal1811)  
**Repository**: [Pdf_Extractor](https://github.com/kagarwal1811/Pdf_Extractor/tree/master)

> If you have any questions, suggestions, or just want to say hi, feel free to open an issue or reach out through GitHub!

---

Happy coding! 🎉

---
