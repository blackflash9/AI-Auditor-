import re
from datetime import datetime

def clean_currency(value):
    """
    Removes symbols ($, JMD, USD) and commas, 
    returning a clean float for calculations.
    """
    if isinstance(value, str):
        # Remove anything that isn't a digit or a decimal point
        clean_val = re.sub(r'[^\d.]', '', value)
        return float(clean_val) if clean_val else 0.0
    return float(value)

def format_timestamp(ts_str):
    """
    Standardizes various date strings into ISO format.
    Useful for cross-referencing logs.
    """
    formats = ["%Y-%m-%d %H:%M:%S", "%d/%m/%Y %H:%M", "%m-%d-%Y"]
    for fmt in formats:
        try:
            return datetime.strptime(ts_str, fmt).isoformat()
        except (ValueError, TypeError):
            continue
    return ts_str  # Return as-is if no match found

def validate_hs_code(code):
    """
    Ensures the Tariff/HS code follows the standard 6 to 10 digit format.
    """
    clean_code = str(code).replace(".", "").strip()
    if clean_code.isdigit() and 6 <= len(clean_code) <= 10:
        return True
    return False

def get_exchange_rate(base="USD", target="JMD"):
    """
    Placeholder for an API call to get real-time rates.
    For now, returns a hardcoded static rate for testing.
    """
    rates = {"USD_JMD": 155.0, "GBP_JMD": 195.0}
    return rates.get(f"{base}_{target}", 1.0)
