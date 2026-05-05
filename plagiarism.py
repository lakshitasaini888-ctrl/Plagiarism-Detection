from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from utils import chunk_text

# Load once (VERY IMPORTANT)
model = SentenceTransformer('all-MiniLM-L6-v2')


def advanced_plagiarism(text1, text2):

    # ================= SMART CHUNKING =================
    chunks1 = chunk_text(text1, 15)
    chunks2 = chunk_text(text2, 15)

    # Limit size (critical for performance)
    chunks1 = chunks1[:200]
    chunks2 = chunks2[:200]

    if not chunks1 or not chunks2:
        return {"score": 0, "matches": []}

    # ================= BATCH EMBEDDING =================
    emb1 = model.encode(chunks1, batch_size=32, show_progress_bar=False)
    emb2 = model.encode(chunks2, batch_size=32, show_progress_bar=False)

    # ================= SIMILARITY =================
    sim_matrix = cosine_similarity(emb1, emb2)

    similarity_scores = []
    matches = []

    for i in range(len(chunks1)):
        best_score = float(np.max(sim_matrix[i]))
        best_index = int(np.argmax(sim_matrix[i]))

        similarity_scores.append(best_score)

        # Only meaningful matches
        if best_score > 0.65:
            matches.append({
                "text1": chunks1[i][:300],
                "text2": chunks2[best_index][:300],
                "score": round(best_score, 2)
            })

    # ================= FINAL SCORE =================
    avg_similarity = np.mean(similarity_scores)

    # Non-linear scaling (more realistic)
    final_score = (avg_similarity ** 1.3) * 100

    return {
        "score": round(final_score, 2),
        "matches": matches[:15]  # limit UI overload
    }