import pytesseract
from PIL import Image
from PyPDF2 import PdfReader
from docx import Document

def extract_text_from_file(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        text = ""
        reader = PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
        return text

    elif filename.endswith(".docx"):
        doc = Document(file)
        return "\n".join([p.text for p in doc.paragraphs])

    else:
        image = Image.open(file)
        return pytesseract.image_to_string(image)
