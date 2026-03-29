# <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/robot.svg" width="30" height="30" align="center" alt="AI" /> AI Logistics Auditor

---

### <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/bolt.svg" width="18" height="18" align="center" alt="Bolt" /> Enterprise-Grade Compliance for Global Trade
<p align="left">
  <img src="https://img.shields.io/badge/Status-Production--Ready-success?style=for-the-badge&logo=github" alt="Status: Production-Ready" />
  <img src="https://img.shields.io/badge/Stack-Python_%7C_LangGraph_%7C_RAG-3776AB?style=for-the-badge&logo=python" alt="Stack" />
  <img src="https://img.shields.io/badge/Location-Kingston_%2F_London-purple?style=for-the-badge&logo=googlemaps" alt="Location: London May 2026" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" alt="License" />
</p>

---

## <img src="https://raw.githubusercontent.com/FortAwesome/Font-Awesome/6.x/svgs/solid/eye.svg" width="22" height="22" align="center" alt="Overview" /> Project Overview
The **AI Logistics Auditor** is a sophisticated **Multi-Agent RAG system** designed to solve the $100B problem of manual customs non-compliance. Unlike simple chatbot interfaces, this system functions as an **Autonomous Auditor**—parsing complex shipping manifests, cross-referencing global trade regulations, and self-correcting its findings through an iterative agentic loop.

### 🌟 Key Differentiators (Why this stands out)
* **Agentic Self-Correction:** Uses a LangGraph-managed feedback loop where a **Verification Agent** critiques the **Drafting Agent**, drastically reducing hallucinations in HS Code matching.
* **Hybrid Retrieval Logic:** Combines Dense Vector Search (semantic) with Sparse BM25 (keyword) and a Cross-Encoder Reranker to ensure high-precision regulatory lookups.
* **Layout-Aware Ingestion:** Custom parsing pipeline specifically tuned for nested tables and multi-page logistics PDFs—data that breaks standard OCR.

---

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

### 🛠️ Technical Implementation

Component Technology Engineering Decision
Logic Layer LangGraph Chosen over linear chains to support cyclic logic and human-in-the-loop triggers.
Embedding Model OpenAI text-embedding-3-large 3072 dimensions to capture the nuance of legal and technical trade jargon.
Re-ranking Cohere Rerank v3 Applied post-retrieval to optimize the top-k context before LLM injection.
Observability LangSmith Used for tracing agent trajectories and monitoring per-token costs.
