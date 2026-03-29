import json
import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

def ingest_customs_data(json_path):
    """
    Converts UK Customs JSON into a searchable Vector Index.
    """
    # 1. Load the "Gold Set"
    with open(json_path, 'r') as f:
        data = json.load(f)
    
    documents = []
    
    # 2. Transform JSON entries into searchable 'Documents'
    for entry in data:
        # We put the HS Code and Description in the page_content for searching
        content = f"HS Code: {entry['hs_code']} | Description: {entry['description']}"
        
        # We keep the metadata (rates, refs) for the Agent to use in the Audit report
        metadata = {
            "hs_code": entry['hs_code'],
            "duty_rate": entry['duty_rate'],
            "reference": entry['regulation_reference']
        }
        documents.append(Document(page_content=content, metadata=metadata))
    
    # 3. Create Embeddings (The 'Rhythmic Precision' of the data)
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    
    # 4. Build and Save the Vector Store locally
    vector_db = FAISS.from_documents(documents, embeddings)
    vector_db.save_local("data/knowledge_base/faiss_index")
    
    print(f"✅ Ingested {len(documents)} compliance rules into the Vector Store.")

if __name__ == "__main__":
    # Point to the file we just discussed
    kb_file = os.path.join('data', 'knowledge_base', 'uk_customs_v1.json')
    ingest_customs_data(kb_file)
