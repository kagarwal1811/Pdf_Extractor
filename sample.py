import pdfplumber
import re
import pandas as pd
import argparse
import os

def parse_bank_statement(pdf_path):
    """
    Parses a bank statement PDF and extracts transaction rows.
    
    This function uses a simple heuristic:
      - It identifies lines that begin with a date (format: DD-MMM-YYYY).
      - It assumes that each transaction header is followed by a non-empty line that contains the amounts.
      
    Returns:
        list: A list of dictionaries with keys:
              'Date', 'Transaction Type', 'Description',
              'Transaction Amount', and 'Balance'.
    """
    rows = []
    # Regular expression to detect a date at the start of a line.
    date_pattern = re.compile(r'^\d{1,2}-[A-Za-z]{3}-\d{4}')

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if not text:
                continue
            lines = text.split('\n')
            i = 0
            while i < len(lines):
                line = lines[i].strip()
                # Check if the line starts with a date (transaction header)
                if date_pattern.match(line):
                    tokens = line.split()
                    date = tokens[0]
                    txn_type = ""
                    description = ""
                    # Check if the second token is 'T' or 'C' (transaction type)
                    if len(tokens) > 1 and tokens[1].upper() in ['T', 'C']:
                        txn_type = tokens[1].upper()
                        description = " ".join(tokens[2:])
                    else:
                        description = " ".join(tokens[1:])
                    
                    # Look for the next non-empty line which contains the amounts.
                    amounts_line = ""
                    j = i + 1
                    while j < len(lines):
                        candidate = lines[j].strip()
                        if candidate:
                            amounts_line = candidate
                            break
                        j += 1
                    
                    # Process the amounts line by splitting on whitespace.
                    amounts_tokens = amounts_line.split()
                    transaction_amount = None
                    balance = None
                    if len(amounts_tokens) == 1:
                        # In cases like 'B/F' where only a balance is present.
                        balance = amounts_tokens[0]
                    elif len(amounts_tokens) >= 2:
                        transaction_amount = amounts_tokens[0]
                        balance = amounts_tokens[1]
                    
                    row = {
                        "Date": date,
                        "Transaction Type": txn_type,
                        "Description": description,
                        "Transaction Amount": transaction_amount,
                        "Balance": balance
                    }
                    rows.append(row)
                    # Move index past the amounts line.
                    i = j + 1
                else:
                    i += 1
    return rows

def save_to_excel(rows, output_excel_path):
    """
    Saves the list of transaction rows to an Excel file.
    
    Args:
        rows (list): List of dictionaries representing the transactions.
        output_excel_path (str): The path for the resulting Excel file.
    """
    df = pd.DataFrame(rows)
    df.to_excel(output_excel_path, index=False)
    print(f"Excel file successfully saved to {output_excel_path}")

def main():
    parser = argparse.ArgumentParser(
        description='Extract transaction rows from a bank statement PDF and export to an Excel file.'
    )
    parser.add_argument('input', help='Path to the input PDF file.')
    parser.add_argument('output_excel', help='Path for the output Excel file.')
    args = parser.parse_args()

    # Check if the input file exists in the same folder.
    if not os.path.exists(args.input):
        print(f"Error: The file {args.input} does not exist.")
        return
    
    print("Processing PDF and extracting transaction rows...")
    rows = parse_bank_statement(args.input)
    
    if not rows:
        print("No transaction rows were found in the PDF.")
    else:
        print(f"Extracted {len(rows)} transaction rows. Exporting to Excel...")
        save_to_excel(rows, args.output_excel)

if __name__ == "__main__":
    main()
