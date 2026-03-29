from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.extract_text import extract_text
from utils.calculate_similarity import calculate_similarity
app = Flask(__name__)
CORS(app)

@app.route("/uploads", methods=["POST"])
def upload_files():
    try:
        file1 = request.files.get("file1")
        file2 = request.files.get("file2")

        text1_input = request.form.get("text1")
        text2_input = request.form.get("text2")

        threshold = float(request.form.get("threshold", 70)) / 100

        # Decide source
        text1 = extract_text(file1) if file1 else (text1_input or "")
        text2 = extract_text(file2) if file2 else (text2_input or "")

        if not text1.strip() or not text2.strip():
            return jsonify({"error": "Provide text or files"}), 400

        similarity, matches = calculate_similarity(text1, text2, threshold)

        return jsonify({
            "similarity": round(similarity * 100, 2),
            "matches": matches
        })

    except Exception as e:
        return jsonify({"error": f"Backend error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True)