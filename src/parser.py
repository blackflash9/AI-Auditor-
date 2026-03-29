import pandas as pd
import json
import os

class DataParser:
    def __init__(self, input_source):
        self.input_source = input_source
        self.file_ext = os.path.splitext(input_source)[1].lower()

    def parse(self):
        """Main entry point to convert raw files into structured dictionaries."""
        try:
            if self.file_ext == '.csv':
                data = pd.read_csv(self.input_source)
            elif self.file_ext in ['.xlsx', '.xls']:
                data = pd.read_excel(self.input_source)
            elif self.file_ext == '.json':
                with open(self.input_source, 'r') as f:
                    data = pd.DataFrame(json.load(f))
            else:
                return {"error": f"Unsupported extension: {self.file_ext}"}
            
            return self._clean_and_validate(data)
            
        except Exception as e:
            return {"error": f"Parsing failed: {str(e)}"}

    def _clean_and_validate(self, df):
        """
        Standardizes the dataset for the AI Logistics Auditor.
        """
        # Normalize column headers to lowercase and remove spaces
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]

        # Critical mapping for Jamaican/International Customs codes
        rename_map = {
            'hs_code': 'tariff_code',
            'item_description': 'description',
            'entry_date': 'timestamp'
        }
        df.rename(columns=rename_map, inplace=True)

        # Drop rows that are missing essential audit data
        essential_cols = ['tariff_code', 'timestamp']
        df.dropna(subset=[col for col in essential_cols if col in df.columns], inplace=True)

        return df.to_dict(orient='records')

# Example run:
# parser = DataParser('docs/manifest_march.csv')
# clean_data = parser.parse()
