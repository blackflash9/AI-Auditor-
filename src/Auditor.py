import os
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# 1. Initialize the "Knowledge Brain"
def get_retriever():
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    vector_db = FAISS.load_local(
        "data/knowledge_base/faiss_index", 
        embeddings, 
        allow_dangerous_deserialization=True # Only for local trusted data
    )
    return vector_db.as_retriever(search_kwargs={"k": 2})

# 2. Define the Auditing Logic
def run_compliance_audit(manifest_item_text, declared_duty):
    """
    manifest_item_text: e.g., "Industrial Aluminum Wire 8mm"
    declared_duty: e.g., "0.0%"
    """
    retriever = get_retriever()
    
    # Retrieve the official "Gold Set" rules for this item
    relevant_rules = retriever.get_relevant_documents(manifest_item_text)
    context = "\n".join([doc.page_content + f" | Duty: {doc.metadata['duty_rate']}" for doc in relevant_rules])

    # 3. The "Judge" Prompt (London Enterprise Style)
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    
    prompt = ChatPromptTemplate.from_template("""
    You are a Senior Customs Auditor for a UK Logistics Firm.
    Compare the MANIFEST ITEM against the OFFICIAL REGULATIONS.

    MANIFEST ITEM: {item}
    DECLARED DUTY: {declared}
    
    OFFICIAL REGULATIONS:
    {context}

    Your task:
    1. Identify the correct HS Code.
    2. Check if the DECLARED DUTY matches the OFFICIAL DUTY.
    3. Flag as "COMPLIANT", "NON-COMPLIANT", or "INSUFFICIENT_DATA".
    4. Provide a brief technical rationale.

    Return ONLY a JSON object.
    """)

    chain = prompt | llm | JsonOutputParser()
    
    result = chain.invoke({
        "item": manifest_item_text,
        "declared": declared_duty,
        "context": context
    })
    
    return result

# --- QUICK TEST ---
if __name__ == "__main__":
    # Simulate a "Dirty" Manifest entry
    test_item = "Aluminum wiring for industrial use (9mm)"
    test_duty = "0.0%" # This is a lie; it should be 7.5% per our JSON
    
    print(f"🔍 Auditing: {test_item}...")
    report = run_compliance_audit(test_item, test_duty)
    
    print("\n📝 AUDIT REPORT:")
    print(report)
