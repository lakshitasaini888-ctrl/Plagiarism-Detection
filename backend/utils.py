# utils.py
import PyPDF2
import docx
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk

nltk.download('punkt')  # for sentence tokenization

def extract_text(file):
    if file.filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return " ".join([page.extract_text() or "" for page in reader.pages])
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])
    return ""

def preprocess(text):
    return text.lower()

def get_sentences(text):
    return nltk.sent_tokenize(text)

def calculate_similarity(text1, text2, threshold=0.7):
    text1 = preprocess(text1)
    text2 = preprocess(text2)

    # TF-IDF for full text similarity
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([text1, text2])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]

    # Sentence-level matching
    sentences1 = get_sentences(text1)
    sentences2 = get_sentences(text2)
    matches = []

    for s1 in sentences1:
        for s2 in sentences2:
            vec = vectorizer.fit_transform([s1, s2])
            score = cosine_similarity(vec[0], vec[1])[0][0]
            if score > threshold:
                matches.append({
                    "text1": s1,
                    "text2": s2,
                    "score": round(score*100, 2)
                })

    return similarity, matches