import re
import pandas as pd

class AIAuditor:
    def __init__(self):
        # Pattern for: [TIMESTAMP] ID:XXXX Status:XXXX
        self.log_pattern = r"\[(?P<timestamp>.*?)\] ID:(?P<shipment_id>\w+) Status:(?P<status>\w+)"

    def parse_logs(self, log_data):
        """Extracts structured data from raw log strings."""
        parsed_entries = []
        for line in log_data:
            match = re.search(self.log_pattern, line)
            if match:
                parsed_entries.append(match.groupdict())
        
        return pd.DataFrame(parsed_entries)

    def audit_compliance(self, df):
        """Flags shipments that aren't 'Delivered' or 'In-Transit'."""
        valid_statuses = ['Delivered', 'In-Transit']
        # Identify anomalies
        df['compliance_issue'] = ~df['status'].isin(valid_statuses)
        return df

if __name__ == "__main__":
    # Sample logistics data to test the logic
    raw_logs = [
        "[2026-03-25 10:00] ID:SHP123 Status:In-Transit",
        "[2026-03-25 10:05] ID:SHP456 Status:Delivered",
        "[2026-03-25 10:10] ID:SHP789 Status:Delayed", # This should be flagged
    ]

    auditor = AIAuditor()
    structured_data = auditor.parse_logs(raw_logs)
    audit_results = auditor.audit_compliance(structured_data)

    print("--- Audit Results ---")
    print(audit_results)
