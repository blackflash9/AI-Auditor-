import sys
import os
from datetime import datetime
from parser import DataParser
from auditor import AIAuditor
from logger import AuditLogger

def run_audit(file_path):
    # Initialize the logger
    logger = AuditLogger(log_dir="audit_reports")
    file_name = os.path.basename(file_path)
    
    print(f"--- Starting Audit: {file_name} ---")
    logger.quick_log_text(f"Started audit for {file_name}")

    # 1. Parsing Phase
    parser = DataParser(file_path)
    parsed_data = parser.parse()

    if isinstance(parsed_data, dict) and "error" in parsed_data:
        error_msg = f"Parsing failed for {file_name}: {parsed_data['error']}"
        print(f"[!] {error_msg}")
        logger.quick_log_text(error_msg)
        return

    # 2. Auditing Phase
    auditor = AIAuditor(parsed_data)
    # This calls the logic we built in auditor.py
    audit_results = auditor.analyze() 

    # 3. Reporting & Logging Phase
    report = {
        "meta": {
            "file_processed": file_name,
            "timestamp": datetime.now().isoformat(),
            "total_records": len(parsed_data)
        },
        "findings": audit_results
    }

    # Save the detailed JSON report
    saved_path = logger.log_results(file_name.split('.')[0], report)
    
    # Summary Output for Terminal
    print("\n[Audit Summary]")
    print(f"Items Scanned: {len(parsed_data)}")
    print(f"Flags Raised: {len(audit_results)}")
    
    if audit_results:
        print("\n[!] Discrepancies found. Review the log file for details.")
    else:
        print("\n[+] No issues detected. Compliance verified.")

    logger.quick_log_text(f"Completed audit for {file_name}. Flags: {len(audit_results)}")
    print(f"\n--- Process Finished ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logistics_file>")
    else:
        target_file = sys.argv[1]
        if os.path.exists(target_file):
            run_audit(target_file)
        else:
            print(f"[!] File not found: {target_file}")
