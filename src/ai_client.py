def get_refined_prompt(item_data, context_docs):
    return f"""
    ROLE: You are a Senior Customs Compliance Auditor.
    OBJECTIVE: Validate the HS Classification of an item using the General Rules of Interpretation (GRI).

    ### STEP 1: GRI-1 LEGAL CHECK
    Compare the item description to the Terms of the Headings and Section/Chapter Notes provided in the context.
    - Context: {context_docs}
    - Item: {item_data['description']}
    - Declared Code: {item_data['tariff_code']}

    ### STEP 2: MULTI-LEVEL VERIFICATION
    1. **Heading Level (First 4 Digits)**: Does the item fall under this broad category? 
    2. **Subheading Level (Next 2 Digits)**: Is the specific material/type accurate globally?
    3. **Regional Level (Remaining Digits)**: Does it match the Jamaica/UK specific duty rate requirements?

    ### STEP 3: FINANCIAL & RISK ANALYSIS
    - Check for 'Additional Stamp Duty' (ASD) if it's an agricultural or alcoholic product.
    - Flag if the item is 'Restricted' (requires a permit from MICAF or Trade Board).
    - Compare 'Declared Value' against 'De Minimis' thresholds (e.g., US$100 for Jamaica).

    ### OUTPUT JSON FORMAT:
    {{
        "analysis": {{
            "gri_rule_applied": "1, 2a, 3b, etc.",
            "heading_match": true/false,
            "legal_note_reference": "string"
        }},
        "status": {{
            "verdict": "PASS" | "FLAG" | "REJECT",
            "risk_score": 1-10,
            "suggested_code": "XXXX.XX.XX"
        }},
        "financials": {{
            "estimated_duty_rate": "percentage",
            "asd_applicable": true/false,
            "permit_required": "Name of Agency or None"
        }}
    }}
    """
