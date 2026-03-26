import re
import pandas as pd
from datetime import datetime

class AIAuditor:
    def __init__(self):
        # Improved regex to capture Date and Time separately
        self.log_pattern = r"\[(?P<date>\d{4}-\d{2}-\d{2}) (?P<time>\d{2}:\d{2})\] ID:(?P<shipment_id>\w+) Status:(?P<status>\w+)"

    def parse_logs(self, log_data):
        """Extracts structured data and flags malformed entries."""
        parsed_entries = []
        malformed_count = 0

        for line in log_data:
            match = re.search(self.log_pattern, line)
            if match:
                entry = match.groupdict()
                parsed_entries.append(entry)
            else:
                malformed_count += 1
                print(f"⚠️ Warning: Skipping malformed log line: {line}")
        
        df = pd.DataFrame(parsed_entries)
        return df, malformed_count

    def audit_compliance(self, df):
        """
        Advanced Audit:
        1. Checks for 'Approved' statuses.
        2. Flags shipments processed outside of 'Business Hours' (9 AM - 5 PM).
        """
        # 1. Status Check
        valid_statuses = ['Delivered', 'In-Transit', 'Pending']
        df['status_compliant'] = df['status'].isin(valid_statuses)

        # 2. Time-of-Day Audit (Crucial for logistics oversight)
        df['hour'] = df['time'].apply(lambda x: int(x.split(':')[0]))
        df['business_hour_compliant'] = df['hour'].between(9, 17)

        # 3. Overall Compliance Flag
        df['fully_compliant'] = df['status_compliant'] & df['business_hour_compliant']
        
        return df

if __name__ == "__main__":
    # Test data with a mix of good, bad, and "after-hours" logs
    raw_logs = [
        "[2026-03-25 10:00] ID:SHP123 Status:In-Transit",
        "[2026-03-25 22:30] ID:SHP456 Status:Delivered", # Night-time delivery (Flagged)
        "[2026-03-25 14:15] ID:SHP789 Status:Unauthorized", # Invalid Status (Flagged)
        "CORRUPT_DATA_LINE_12345", # Malformed (Flagged)
    ]

    auditor = AIAuditor()
    df, errors = auditor.parse_logs(raw_logs)
    
    if not df.empty:
        results = auditor.audit_compliance(df)
        print(f"\n--- Audit Summary ({errors} errors bypassed) ---")
        print(results[['shipment_id', 'status', 'time', 'fully_compliant']])
