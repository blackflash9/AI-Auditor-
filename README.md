# <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/robot.svg" width="30" height="30" align="center" alt="AI" /> AI Logistics Auditor

---

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/bolt.svg" width="18" height="18" align="center" alt="Bolt" /> AI-powered Compliance for International Trade
<p align="left">
  <img src="https://img.shields.io/badge/Status-MVP-success?style=for-the-badge&logo=github" alt="Status: MVP" />
  <img src="https://img.shields.io/badge/Tech_Stack-Python_%7C_AI-blue?style=for-the-badge" alt="Tech Stack" />
  <img src="https://img.shields.io/badge/Location-Kingston_%2F_London-purple?style=for-the-badge&logo=googlemaps" alt="Location: London May 2026" />
</p>

---

## <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/eye.svg" width="22" height="22" align="center" alt="Overview" /> Project Overview
The **AI Logistics Auditor** is a robust solution designed to automate the costly and error-prone process of auditing international shipping manifests and customs documentation. By utilizing cutting-edge Large Language Models (LLMs) and Agentic RAG workflows, it provides real-time validation, ensures regulatory compliance, and accelerates operational speed.

### 🏗️ System Architecture (Agentic RAG)

```mermaid
graph TD
    %% Define Node Styles
    classDef storage fill:#f9f,stroke:#333,stroke-width:2px;
    classDef process fill:#e1f5fe,stroke:#01579b,stroke-width:1px,rx:10,ry:10;
    classDef agent fill:#e8f5e9,stroke:#1b5e20,stroke-width:2px,rx:15,ry:15;
    classDef error fill:#ffebee,stroke:#b71c1c,stroke-width:1px,stroke-dasharray: 5 5;

    %% 1. Input Layer
    subgraph Data_Ingestion ["1. Input Layer"]
        PDF[("📜 Logistics PDF<br>(Manifest/Customs Doc)")]
        Parser["🛠️ Layout-Aware Parser<br>(Extracts Tables & OCR)"]
        Clean[("🧹 Clean Markdown")]
        PDF --> Parser
        Parser --> Clean
    end

    %% 2. Agentic Core
    subgraph Agent_Core ["2. Agentic Core (LangGraph)"]
        Orchestrator{{"🤖 Orchestrator<br>(State Management)"}}
        DraftAgent[/"📝 Drafting Agent"/]
        VerifyAgent[/"🕵️ Verification Agent"/]
        
        Orchestrator --> DraftAgent
        DraftAgent --> Orchestrator
        Orchestrator --> VerifyAgent
    end

    %% 3. Retrieval
    subgraph Knowledge_Layer ["3. Hybrid Retrieval"]
        VectorDB[("🗄️ Vector Store<br>(Regulations)")]
        BM25[("🗂️ Keyword Index<br>(HS Codes)")]
        Reranker["⚖️ Cross-Encoder Reranker"]
        
        Orchestrator -.-> VectorDB
        Orchestrator -.-> BM25
        VectorDB --> Reranker
        BM25 --> Reranker
        Reranker -.-> Orchestrator
    end

    %% 4. Output
    subgraph Output_Layer ["4. Verification & Output"]
        Decision{"🔄 Audit Status?"}
        FinalReport[("✅ Verified Audit Report")]
        HumanReview[/"🚨 Flag for Human Review"/]
        
        VerifyAgent --> Decision
        Decision -->|Pass| FinalReport
        Decision -->|Fail| Orchestrator
        Decision -->|Low Confidence| HumanReview
        
        class HumanReview error;
    end

    class PDF,Clean,VectorDB,BM25,FinalReport storage;
    class Parser,Reranker,Decision process;
    class Orchestrator,DraftAgent,VerifyAgent agent;

<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/star.svg" width="22" height="22" align="center" alt="Features" /> Key Features & Capabilities
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/check-double.svg" width="16" height="16" align="center" alt="Verification" /> Automated Doc Verification: Instant extraction and auditing of data from invoices, packing lists, and manifests.
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/network-wired.svg" width="16" height="16" align="center" alt="Network" /> Multi-Model Orchestration: Uses dynamic switching between GPT-4o and Claude 3.5 Sonnet for optimal reasoning accuracy.
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/shield-halved.svg" width="16" height="16" align="center" alt="Shield" /> Global Regulatory Compliance: Compares shipping data against current international trade laws to flag immediate risks.
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/chart-line.svg" width="16" height="16" align="center" alt="Chart" /> Operational Metrics: Early-stage analysis shows a ~60% reduction in manual document auditing time.
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/layer-group.svg" width="22" height="22" align="center" alt="Tech" /> Technology Stack
​<p align="left">
<img src="https://img.shields.io/badge/language-Python_3.10+-blue?style=flat-square&logo=python" alt="Python" />
<img src="https://www.google.com/search?q=https://img.shields.io/badge/AI/ML-LangGraph_%257C_RAG-black%3Fstyle%3Dflat-square%26logo%3Dopenai" alt="AI Stack" />
<img src="https://www.google.com/search?q=https://img.shields.io/badge/architecture-Agentic_SaaS-lightgrey%3Fstyle%3Dflat-square" alt="Architecture" />
<img src="https://img.shields.io/badge/Dev_Tools-GitHub_Codespaces-6E5494?style=flat-square&logo=github" alt="Dev Tools" />
</p>
​<img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/house-user.svg" width="22" height="22" align="center" alt="Local Setup" /> Local Setup & Installation
​1. Clone the Repository
git clone [https://github.com/blackflash9/AI-Auditor-.git](https://github.com/blackflash9/AI-Auditor-.git)
cd AI-Auditor-

2. Environment Provisioning

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt

3. Execution (Standard Audit)
# Run the auditor in diagnostic mode
python main.py --mode audit --telemetry enabled

<img src="https://www.google.com/search?q=https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/trophy.svg" width="22" height="22" alt="Architect" /> Lead Architect
​Almando Douglas Lead AI Solutions Architect | 1x Grammy Winner | 3x Grammy Nominee
​<p align="left">
<a href="https://www.google.com/search?q=https://github.com/blackflash9">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/GitHub-Profile-lightgrey%3Fstyle%3Dfor-the-badge%26logo%3Dgithub" alt="GitHub" />
</a>
<a href="https://www.google.com/search?q=https://www.linkedin.com/in/almando-douglas-1ba389226">
<img src="https://www.google.com/search?q=https://img.shields.io/badge/LinkedIn-Contact-blue%3Fstyle%3Dfor-the-badge%26logo%3Dlinkedin" alt="LinkedIn" />
</a>
</p>
​"I build AI systems with the same rhythmic precision I use to craft a Grammy-winning record. Where technical architecture meets creative intuition."
