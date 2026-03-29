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
