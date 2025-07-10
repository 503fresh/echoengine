from logic import mathcraft, gametheory, artofwar

print("EchoEngine: Modules loaded.")
import os
import fitz  # PyMuPDF

TEXT_DIR = "cardsystem/text"

def extract_text_from_pdfs():
    for filename in os.listdir(TEXT_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(TEXT_DIR, filename)
            doc = fitz.open(path)
            text = ""
            for page in doc:
                text += page.get_text()
            print(f"\n--- {filename} ---\n{text[:500]}...")  # print preview

if __name__ == "__main__":
    extract_text_from_pdfs()
