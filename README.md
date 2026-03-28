# <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/robot.svg" width="30" height="30" align="center" alt="AI" /> AI Logistics Auditor

---

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/bolt.svg" width="18" height="18" align="center" alt="Bolt" /> AI-powered Compliance for International Trade
<p align="left">
  <img src="https://img.shields.io/badge/Status-MVP-success?style=for-the-badge&logo=github" alt="Status: MVP" />
  <img src="https://img.shields.io/badge/Tech_Stack-Python_%7C_AI-blue?style=for-the-badge" alt="Tech Stack" />
  <img src="https://img.shields.io/badge/Location-Kingston_%2F_London-purple?style=for-the-badge&logo=googlemaps" alt="Location: London May 2026" />
</p>

---

## 👁️ Project Overview
The **AI Logistics Auditor** is a robust SaaS solution designed to automate the costly and error-prone process of auditing international shipping manifests and customs documentation. By utilizing cutting-edge Large Language Models (LLMs) via Python, it provides real-time validation, ensures regulatory compliance, and accelerates operational speed.

### Key Capabilities:
* **Automated Data Extraction:** Scans invoices and manifests using OCR and Vision LLMs.
* **Multi-Model Orchestration:** Uses dynamic API switching between **GPT-4** and **Claude** for optimal reasoning accuracy.
* **Global Regulatory Compliance:** Compares shipping data against current international trade laws to flag immediate risks.
* **Operational Metrics:** Early-stage analysis shows a **~60% reduction** in manual document auditing time.

---

## 🛠️ Technology Stack
<p align="left">
  <img src="https://img.shields.io/badge/language-Python_3.x-blue?style=flat-square&logo=python" alt="Python" />
  <img src="https://img.shields.io/badge/AI/ML-OpenAI_GPT--4_%7C_Anthropic-black?style=flat-square&logo=openai" alt="AI Stack" />
  <img src="https://img.shields.io/badge/Dev_Tools-Replit_%7C_GitHub-blue?style=flat-square&logo=replit" alt="Dev Tools" />
</p>

---

## 💻 Technical Implementation
This project showcases clean, production-ready Python that prioritizes data integrity and modularity.

```python
import os
from pydantic import BaseModel, Field
from typing import List, Optional
import openai

# Define a structured schema for the Audit Result
class AuditResult(BaseModel):
    is_compliant: bool = Field(description="True if the document meets all trade regulations.")
    confidence_score: float = Field(ge=0, le=1)
    flagged_discrepancies: List[str] = Field(default_factory=list)
    suggested_corrections: Optional[str]

class LogisticsAuditor:
    def __init__(self, api_key: str):
        self.client = openai.OpenAI(api_key=api_key)

    def audit_manifest(self, document_text: str) -> AuditResult:
        """
        Analyzes shipping manifest text for customs compliance.
        """
        response = self.client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a Senior Trade Compliance Auditor."},
                {"role": "user", "content": document_text}
            ],
            response_format=AuditResult,
        )
        return response.choices[0].message.parsed
