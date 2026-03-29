import sys
import os
from ingest import DataIngestor
from parser import DataParser
from auditor import AIAuditor
from logger import AuditLogger

def run_batch_audit():
    # 1. Initialize our components
    ingestor = DataIngestor(watch_dir="data/incoming", processed_dir="data/processed")
    logger = AuditLogger(log_dir="audit_reports")
    
    # 2. Check for new files
    new_files = ingestor.fetch_new_files()
    
    if not new_files:
        print("[Ingest] No new manifests found in 'data/incoming'.")
        return

    print(f"--- Found {len(new_files)} new files. Starting Batch Audit ---")

    for filename in new_files:
        file_path = os.path.join(ingestor.watch_dir, filename)
        print(f"\n[Processing] {filename}...")

        # 3. Parsing Phase
        parser = DataParser(file_path)
        parsed_data = parser.parse()

        if isinstance(parsed_data, dict) and "error" in parsed_data:
            print(f" [!] Skip: {parsed_data['error']}")
            continue

        # 4. Auditing Phase
        auditor = AIAuditor(parsed_data)
        audit_results = auditor.analyze()

        # 5. Logging Phase
        report = {
            "meta": {"file": filename, "total_records": len(parsed_data)},
            "findings": audit_results
        }
        logger.log_results(filename.split('.')[0], report)

        # 6. Archive Phase (Move file so it's not audited twice)
        ingestor.move_to_processed(filename)

    print("\n--- Batch Audit Complete ---")

if __name__ == "__main__":
    run_batch_audit()
