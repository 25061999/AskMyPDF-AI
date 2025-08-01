import fitz  # PyMuPDF

def load_pdf_text("C://Users//VKUMAR86//Downloads//Explainx.ai_RAG.pdf"):
    """
    Extracts text from a PDF file using PyMuPDF.
    """
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    doc.close()
    return text