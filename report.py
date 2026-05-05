import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf_report(result):

    os.makedirs("reports", exist_ok=True)

    score = result.get("score", 0)
    plag = score
    original = 100 - score

    # ================= PIE CHART =================
    plt.figure(figsize=(5,5))
    plt.pie(
        [plag, original],
        labels=["Plagiarized", "Original"],
        autopct="%1.1f%%",
        colors=["#ff4d4d", "#2ecc71"]
    )
    plt.title("Plagiarism Distribution")
    pie_path = "reports/pie.png"
    plt.savefig(pie_path)
    plt.close()

    # ================= BAR GRAPH =================
    plt.figure(figsize=(6,4))
    plt.bar(["Plagiarized", "Original"], [plag, original])
    plt.title("Content Analysis")
    bar_path = "reports/bar.png"
    plt.savefig(bar_path)
    plt.close()

    # ================= PDF =================
    pdf_path = "reports/report.pdf"

    doc = SimpleDocTemplate(pdf_path)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("AI Plagiarism Report", styles['Title']))
    content.append(Spacer(1, 10))
    content.append(Paragraph(f"Score: {score}%", styles['Normal']))
    content.append(Spacer(1, 10))

    # add images in pdf
    content.append(Image(pie_path, width=300, height=300))
    content.append(Spacer(1, 10))
    content.append(Image(bar_path, width=300, height=200))
    content.append(Spacer(1, 10))

    doc.build(content)

    return {
        "pie": pie_path,
        "bar": bar_path,
        "pdf": pdf_path
    }