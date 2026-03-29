import sys
import os
from parser import DataParser
from auditor import AIAuditor

def run_audit(file_path):
    """
    Orchestrates the flow from raw file to audited report.
    """
    print(f"--- Starting Audit for: {os.path.basename(file_path)} ---")

    # 1. Initialize Parser and extract data
    parser = DataParser(file_path)
    parsed_data = parser.parse()

    # Check if parsing failed
    if isinstance(parsed_data, dict) and "error" in parsed_data:
        print(f"[!] Critical Error: {parsed_data['error']}")
        return

    # 2. Initialize Auditor with the cleaned data
    auditor = AIAuditor(parsed_data)
    
    # 3. Execute Audit Logic
    # (Assuming your AIAuditor has a 'run_checks' or 'analyze' method)
    results = auditor.analyze()

    # 4. Output the Findings
    print("\n[Audit Results Summary]")
    print(f"Total Records Scanned: {len(parsed_data)}")
    print(f"Discrepancies Flagged: {len(results['flags'])}")
    
    if results['flags']:
        print("\n[!] Flagged Entries:")
        for flag in results['flags']:
            print(f"- {flag['timestamp']}: {flag['issue']} (Tariff: {flag['tariff_code']})")
    else:
        print("\n[+] Audit Clean: No discrepancies found.")

    print("\n--- Audit Complete ---")

if __name__ == "__main__":
    # Check if a file path was provided via command line
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_file>")
    else:
        run_audit(sys.argv[1])
