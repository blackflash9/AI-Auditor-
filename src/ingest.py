import os
import shutil
import time

class DataIngestor:
    def __init__(self, watch_dir="data/incoming", processed_dir="data/processed"):
        self.watch_dir = watch_dir
        self.processed_dir = processed_dir
        
        # Ensure directories exist
        for folder in [self.watch_dir, self.processed_dir]:
            if not os.path.exists(folder):
                os.makedirs(folder)

    def fetch_new_files(self):
        """
        Scans the incoming folder for any new logistics files.
        """
        files = [f for f in os.listdir(self.watch_dir) if os.path.isfile(os.path.join(self.watch_dir, f))]
        valid_extensions = ('.csv', '.xlsx', '.json')
        return [f for f in files if f.lower().endswith(valid_extensions)]

    def move_to_processed(self, filename):
        """
        Moves a file to the 'processed' folder after the audit is done 
        to avoid auditing the same file twice.
        """
        src = os.path.join(self.watch_dir, filename)
        dest = os.path.join(self.processed_dir, filename)
        shutil.move(src, dest)
        print(f"[Ingest] Moved {filename} to archive.")

# Example Logic:
# ingestor = DataIngestor()
# new_shipments = ingestor.fetch_new_files()
