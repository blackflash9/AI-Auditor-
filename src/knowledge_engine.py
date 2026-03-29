import fitz  # PyMuPDF
import json
import os

class KnowledgeEngine:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.chunks = []

    def process_tariff(self):
        """
        Splits the PDF into chunks, ensuring each chunk 
        retains its Chapter/Heading context.
        """
        doc = fitz.open(self.pdf_path)
        current_chapter = "Unknown"

        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text = page.get_text("text")

            # Simple logic to track which Chapter we are in
            if "CHAPTER" in text:
                lines = text.split('\n')
                for line in lines:
                    if "CHAPTER" in line:
                        current_chapter = line.strip()
                        break

            # Create a chunk for this page
            # In a pro setup, we'd split this by Heading (4-digits)
            chunk = {
                "content": text,
                "metadata": {
                    "source": os.path.basename(self.pdf_path),
                    "page": page_num + 1,
                    "chapter": current_chapter
                }
            }
            self.chunks.append(chunk)
        
        return self.chunks

    def save_knowledge_base(self, output_path="data/knowledge_base.json"):
        with open(output_path, 'w') as f:
            json.dump(self.chunks, f, indent=4)
        print(f"[Knowledge] Processed {len(self.chunks)} pages into searchable chunks.")
