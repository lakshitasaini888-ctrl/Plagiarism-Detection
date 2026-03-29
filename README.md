# 🔍 Plagiarism Detection

## 📌 Project Overview

This project is a **Plagiarism Detection** tool that compares two text inputs or files and calculates the similarity between them.
It helps in identifying copied content using **Natural Language Processing (NLP)** techniques.

---

## 🚀 Features

* 📄 Upload files (PDF, DOCX, TXT)
* ✍️ Direct text input support
* 📊 Similarity percentage calculation
* 🔎 Sentence-level matching
* 🎯 Adjustable similarity threshold
* 📥 Download plagiarism report
* 🌙 Dark mode UI

---

## 🛠️ Technologies Used

### Frontend:

* HTML
* CSS
* JavaScript

### Backend:

* Python
* Flask
* Flask-CORS

### NLP & ML:

* NLTK
* TF-IDF Vectorizer
* Cosine Similarity (from Scikit-learn)

---

## ⚙️ How It Works

1. User uploads or enters two texts
2. Text is preprocessed (lowercase, tokenization)
3. TF-IDF vectorization is applied
4. Cosine similarity is calculated
5. Sentence-level comparison detects matching parts
6. Final similarity percentage is displayed

---

## 📂 Project Structure

```
Plagiarism-Detection/
│── backend/
│   ├── app.py
│   ├── utils/
│   │   ├── extract_text.py
│   │   └── similarity.py
│
│── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
│── README.md
```

---

## ▶️ How to Run

### 1. Backend Setup

```
cd backend
pip install -r requirements.txt
python app.py
```

👉 Backend runs on: http://127.0.0.1:5000

---

### 2. Frontend Setup

* Open `index.html` using Live Server

---

## ⚠️ Important Notes

* Works best with text-based PDFs (not scanned)
* Ensure backend server is running before using frontend

---

## 🔮 Future Improvements

* BERT-based semantic similarity
* Database integration
* Multi-file comparison
* Deployment on cloud

---

## 👩‍💻 Authors

**Lakshita Saini**  And
**Sapriha**

---

## ⭐ Acknowledgment

This project was built as part of a academic work to demonstrate practical use of NLP in plagiarism detection.
