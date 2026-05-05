from PyPDF2 import PdfReader


def extract_text_from_file(file):

    filename = file.filename.lower()

    # ================= PDF =================
    if filename.endswith('.pdf'):
        try:
            reader = PdfReader(file)
            text = []

            for page in reader.pages[:300]:  # limit pages
                try:
                    page_text = page.extract_text()
                    if page_text:
                        text.append(page_text)
                except:
                    continue

            return " ".join(text)[:300000]

        except:
            return ""

    # ================= TEXT =================
    else:
        try:
            return file.read().decode('utf-8', errors='ignore')[:300000]
        except:
            return ""


# ================= SMART CHUNKING =================
def chunk_text(text, chunk_size=15):
    words = text.split()

    return [
        " ".join(words[i:i + chunk_size])
        for i in range(0, len(words), chunk_size)
    ]