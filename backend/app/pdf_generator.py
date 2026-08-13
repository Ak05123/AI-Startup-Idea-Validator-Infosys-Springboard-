from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak
)
from reportlab.lib import colors


# ============================================================
# PDF GENERATOR
# ============================================================

def generate_report_pdf(report: dict, output_path: str):

    output_path = Path(output_path)

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        spaceBefore=15,
        spaceAfter=8
    )

    normal_style = ParagraphStyle(
        "NormalReport",
        parent=styles["BodyText"],
        fontSize=10,
        leading=14,
        spaceAfter=6
    )

    story = []

    # ========================================================
    # TITLE
    # ========================================================

    story.append(
        Paragraph(
            "AI STARTUP VALIDATION REPORT",
            title_style
        )
    )

    story.append(
        Paragraph(
            f"<b>Startup Idea:</b> "
            f"{report.get('startup_idea', 'Not Available')}",
            normal_style
        )
    )

    story.append(Spacer(1, 10))

    # ========================================================
    # OVERALL SUMMARY
    # ========================================================

    story.append(
        Paragraph(
            "Overall Validation",
            heading_style
        )
    ) 

    summary_data = [
        [
            "Overall Score",
            "Confidence",
            "Viability",
            "Risk Level"
        ],
        [
            str(report.get("overall_validation_score", "N/A")),
            str(report.get("validation_confidence", "N/A")),
            str(report.get("viability_estimate_percent", "N/A")) + "%",
            str(report.get("risk_level", "N/A"))
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[120, 120, 120, 120]
    )

    summary_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, 1), "Helvetica-Bold"),
            ("PADDING", (0, 0), (-1, -1), 8)
        ])
    )

    story.append(summary_table)
    story.append(Spacer(1, 15))

    # ========================================================
    # FINAL VERDICT
    # ========================================================

    story.append(
        Paragraph(
            "Final Verdict",
            heading_style
        )
    )

    story.append(
        Paragraph(
            str(report.get("final_verdict", "Not Available")),
            normal_style
        )
    )

    # ========================================================
    # SCORECARD
    # ========================================================

    story.append(
        Paragraph(
            "Startup Scorecard",
            heading_style
        )
    )

    scorecard = report.get("scorecard", {})

    scorecard_data = [
        ["Category", "Score", "Reason"]
    ]

    for category, data in scorecard.items():

        category_name = category.replace("_", " ").title()

        score = data.get("score", "N/A")
        reason = data.get("reason", "Not Available")

        scorecard_data.append([
            category_name,
            str(score),
            str(reason)
        ])

    scorecard_table = Table(
        scorecard_data,
        colWidths=[130, 60, 300],
        repeatRows=1
    )

    scorecard_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
            ("GRID", (0, 0), (-1, -1), 1, colors.grey),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("PADDING", (0, 0), (-1, -1), 6)
        ])
    )

    story.append(scorecard_table)

    # ========================================================
    # LIST SECTIONS
    # ========================================================

    sections = [
        ("Strongest Factors", "strongest_factors"),
        ("Weakest Factors", "weakest_factors"),
        ("Key Risks", "key_risks"),
        ("Next Actions", "next_actions")
    ]

    for title, key in sections:

        story.append(
            Paragraph(
                title,
                heading_style
            )
        )

        items = report.get(key, [])

        if not items:
            story.append(
                Paragraph(
                    "Not Available",
                    normal_style
                )
            )
            continue

        for index, item in enumerate(items, start=1):

            story.append(
                Paragraph(
                    f"{index}. {item}",
                    normal_style
                )
            )

    # ========================================================
    # BUILD PDF
    # ========================================================

    doc.build(story)

    return str(output_path)