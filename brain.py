import requests
import json
import os

def analyze_invoice_context(text):
    # Retrieve your key from the environment
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return "ERROR: No API Key found. Run 'export GOOGLE_API_KEY=your_key'"

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
    
    payload = {
        "contents": [{
            "parts": [{
                "text": f"You are a Professional Logistics Auditor. Analyze this text and return ONLY a JSON object with keys: item_name, total_value, suggested_duty_rate, and risk_level.\n\nTEXT: {text}"
            }]
        }]
    }

    headers = {'Content-Type': 'application/json'}
    
    response = requests.post(url, headers=headers, data=json.dumps(payload))
    
    if response.status_code == 200:
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"API Error: {response.status_code} - {response.text}"

if __name__ == "__main__":
    print("REST-based AI Brain initialized.")

