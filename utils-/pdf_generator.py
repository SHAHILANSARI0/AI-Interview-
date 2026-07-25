from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(filename, user, role, level, score):

    doc = SimpleDocTemplate(filename, pagesize=letter)

    styles = getSampleStyleSheet()

    story = []

    story.append(Paragraph("<b>AI Interview Report</b>", styles["Title"]))

    story.append(Paragraph(f"Candidate : {user}", styles["BodyText"]))

    story.append(Paragraph(f"Role : {role}", styles["BodyText"]))

    story.append(Paragraph(f"Level : {level}", styles["BodyText"]))

    story.append(Paragraph(f"Score : {score}%", styles["BodyText"]))

    if score >= 90:
        performance = "Excellent"

    elif score >= 75:
        performance = "Good"

    elif score >= 50:
        performance = "Average"

    else:
        performance = "Needs Improvement"

    story.append(
        Paragraph(
            f"Performance : {performance}",
            styles["BodyText"]
        )
    )

    doc.build(story)

    return filename
