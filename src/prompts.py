def get_audit_prompt(item_data, legal_context):
    return f"""
    ROLE: Senior Customs Compliance Officer (Specialist in GRI Rules).
    
    LEGAL CONTEXT (Sourced from 2026 Jamaica Integrated Tariff):
    {legal_context}

    ITEM UNDER REVIEW:
    - Description: {item_data['description']}
    - Declared HS Code: {item_data['tariff_code']}
    - CIF Value: {item_data.get('value', '0.00')}

    AUDIT LOGIC FLOW:
    1. **GRI-1 Verification**: Does the item match the 4-digit Heading terms? (e.g., Is it a 'Live Animal' in Chapter 01?)
    2. **Chapter Note Exclusion**: Check if this item is explicitly excluded from this Chapter (e.g., 'Not for human consumption').
    3. **Permit Detection**: If this is a restricted item (Meats, Firearms, Chemicals, or pharmaceuticals), identify the required agency (MICAF, Trade Board, or Ministry of Health).
    4. **Financial Sanity Check**: In Jamaica, personal imports under US$100 (De Minimis) are duty-free. Is this applicable?

    STRICT JSON OUTPUT:
    {{
        "legal_basis": "GRI 1 | GRI 3b | GRI 6",
        "validation": {{
            "heading_match": true/false,
            "heading_reason": "string",
            "subheading_match": true/false
        }},
        "compliance": {{
            "status": "PASS" | "FLAG" | "REJECT",
            "permit_required": "string or None",
            "risk_score": 1-10
        }},
        "tax_impact": {{
            "duty_rate": "percentage",
            "asd_applicable": true/false,
            "estimated_tax": "value"
        }}
    }}
    """
