import docx
from PyPDF2 import PdfReader

def extract_text(file):
    filename = file.filename
    ext = filename.split('.')[-1].lower()

    text = ""

    if ext == 'pdf':
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    elif ext == 'docx':
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif ext == 'txt':
        try:
            text = file.read().decode("utf-8")
        except:
            text = file.read().decode("latin-1")

    return text