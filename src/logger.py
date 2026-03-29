import os
from datetime import datetime
import json

class AuditLogger:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

    def log_results(self, report_name, data):
        """
        Saves the audit findings to a timestamped JSON file.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{report_name}_audit_{timestamp}.json"
        filepath = os.path.join(self.log_dir, filename)

        try:
            with open(filepath, 'w') as f:
                json.dump(data, f, indent=4)
            print(f"[+] Audit report saved to: {filepath}")
            return filepath
        except Exception as e:
            print(f"[!] Failed to save log: {e}")
            return None

    def quick_log_text(self, message):
        """
        Appends a simple status message to a rolling master log file.
        """
        master_log = os.path.join(self.log_dir, "master_audit_history.txt")
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(master_log, 'a') as f:
            f.write(f"[{timestamp}] {message}\n")
