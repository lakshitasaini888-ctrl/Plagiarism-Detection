from flask import Flask, render_template, request, send_from_directory
from utils import extract_text_from_file
from plagiarism import advanced_plagiarism
from report import generate_pdf_report
import os

app = Flask(__name__)

# 🔥 Allow large file uploads (important for big PDFs)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024


# ================= HOME =================
@app.route('/')
def home():
    return render_template('dashboard.html')


# ================= FILE COMPARISON =================
@app.route('/analyze', methods=['POST'])
def analyze():

    file1 = request.files.get('file1')
    file2 = request.files.get('file2')

    if not file1 or not file2:
        return "Please upload both files."

    # Extract text
    text1 = extract_text_from_file(file1)
    text2 = extract_text_from_file(file2)

    if not text1.strip() or not text2.strip():
        return "Could not extract text from one of the files."

    # AI analysis
    result = advanced_plagiarism(text1, text2)

    # Generate charts + PDF
    charts = generate_pdf_report(result)

    return render_template(
        "result.html",
        result=result,
        charts=charts
    )


# ================= TEXT COMPARISON =================
@app.route('/text-analyze', methods=['POST'])
def text_analyze():

    text1 = request.form.get('text1', '')
    text2 = request.form.get('text2', '')

    if not text1.strip() or not text2.strip():
        return "Please enter both texts."

    # AI analysis
    result = advanced_plagiarism(text1, text2)

    # Generate charts + PDF
    charts = generate_pdf_report(result)

    return render_template(
        "result.html",
        result=result,
        charts=charts
    )


# ================= SERVE REPORT FILES =================
@app.route('/reports/<path:filename>')
def serve_reports(filename):
    return send_from_directory('reports', filename)


# ================= RUN =================
if __name__ == "__main__":
    os.makedirs("reports", exist_ok=True)
    app.run(host="0.0.0.0", port=10000)