from pathlib import Path
import html

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle
)
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    KeepTogether
)
from reportlab.lib import colors


# ============================================================
# TEXT HELPERS
# ============================================================

def clean_text(value):
    """
    Convert values into safe text for ReportLab.
    """

    if value is None:
        return "Not Available"

    return html.escape(str(value))


def display_name(key):
    """
    Convert snake_case keys into readable headings.
    """

    return key.replace("_", " ").title()


# ============================================================
# LIST RENDERER
# ============================================================

def add_bullet_list(
    story,
    items,
    bullet_style
):
    """
    Render a Python list as readable bullet points.
    """

    if not items:

        story.append(
            Paragraph(
                "Not Available",
                bullet_style
            )
        )

        return

    for item in items:

        # ----------------------------------------------------
        # Normal string item
        # ----------------------------------------------------

        if isinstance(item, str):

            story.append(
                Paragraph(
                    f"• {clean_text(item)}",
                    bullet_style
                )
            )

        # ----------------------------------------------------
        # Dictionary item
        # ----------------------------------------------------

        elif isinstance(item, dict):

            render_dict(
                story,
                item,
                bullet_style,
                bullet_style,
                level=1
            )

        else:

            story.append(
                Paragraph(
                    f"• {clean_text(item)}",
                    bullet_style
                )
            )


# ============================================================
# DICTIONARY RENDERER
# ============================================================

def render_dict(
    story,
    data,
    normal_style,
    subheading_style,
    level=0
):
    """
    Convert nested dictionaries into structured PDF sections.

    This prevents raw JSON from appearing in the PDF.
    """

    if not isinstance(data, dict):
        return

    for key, value in data.items():

        readable_key = display_name(key)

        # ====================================================
        # SIMPLE VALUE
        # ====================================================

        if isinstance(
            value,
            (str, int, float)
        ) or value is None:

            story.append(
                Paragraph(
                    f"<b>{clean_text(readable_key)}</b>",
                    subheading_style
                )
            )

            story.append(
                Paragraph(
                    clean_text(value),
                    normal_style
                )
            )

        # ====================================================
        # LIST
        # ====================================================

        elif isinstance(value, list):

            story.append(
                Paragraph(
                    clean_text(readable_key),
                    subheading_style
                )
            )

            add_bullet_list(
                story,
                value,
                normal_style
            )

            story.append(
                Spacer(1, 5)
            )

        # ====================================================
        # NESTED DICTIONARY
        # ====================================================

        elif isinstance(value, dict):

            story.append(
                Paragraph(
                    clean_text(readable_key),
                    subheading_style
                )
            )

            render_dict(
                story,
                value,
                normal_style,
                subheading_style,
                level + 1
            )

            story.append(
                Spacer(1, 5)
            )


# ============================================================
# SPECIAL COMPETITOR RENDERER
# ============================================================

def render_competitor_analysis(
    story,
    data,
    normal_style,
    subheading_style,
    small_heading_style
):
    """
    Render competitor analysis in a readable structure.
    """

    if not isinstance(data, dict):

        story.append(
            Paragraph(
                "Competitor analysis unavailable.",
                normal_style
            )
        )

        return

    # --------------------------------------------------------
    # Startup idea
    # --------------------------------------------------------

    if data.get("startup_idea"):

        story.append(
            Paragraph(
                "<b>Startup Idea</b>",
                subheading_style
            )
        )

        story.append(
            Paragraph(
                clean_text(
                    data["startup_idea"]
                ),
                normal_style
            )
        )

    # --------------------------------------------------------
    # Direct / Indirect competitors
    # --------------------------------------------------------

    for category in [
        "direct_competitors",
        "indirect_competitors"
    ]:

        competitors = data.get(
            category,
            []
        )

        if not competitors:
            continue

        story.append(
            Paragraph(
                display_name(category),
                subheading_style
            )
        )

        for competitor in competitors:

            if not isinstance(
                competitor,
                dict
            ):
                continue

            name = competitor.get(
                "name",
                "Unnamed Competitor"
            )

            story.append(
                Paragraph(
                    clean_text(name),
                    small_heading_style
                )
            )

            if competitor.get("description"):

                story.append(
                    Paragraph(
                        "<b>Description:</b> "
                        + clean_text(
                            competitor["description"]
                        ),
                        normal_style
                    )
                )

            if competitor.get("strengths"):

                story.append(
                    Paragraph(
                        "<b>Strengths</b>",
                        normal_style
                    )
                )

                add_bullet_list(
                    story,
                    competitor["strengths"],
                    normal_style
                )

            if competitor.get("weaknesses"):

                story.append(
                    Paragraph(
                        "<b>Weaknesses</b>",
                        normal_style
                    )
                )

                add_bullet_list(
                    story,
                    competitor["weaknesses"],
                    normal_style
                )

            story.append(
                Spacer(1, 6)
            )

    # --------------------------------------------------------
    # Remaining sections
    # --------------------------------------------------------

    for key in [
        "competitive_advantages",
        "market_gaps",
        "differentiation_opportunities"
    ]:

        if data.get(key):

            story.append(
                Paragraph(
                    display_name(key),
                    subheading_style
                )
            )

            add_bullet_list(
                story,
                data[key],
                normal_style
            )


# ============================================================
# SWOT RENDERER
# ============================================================

def render_swot(
    story,
    data,
    normal_style,
    subheading_style
):

    if not isinstance(data, dict):

        story.append(
            Paragraph(
                "SWOT analysis unavailable.",
                normal_style
            )
        )

        return

    for key in [
        "strengths",
        "weaknesses",
        "opportunities",
        "threats"
    ]:

        if data.get(key):

            story.append(
                Paragraph(
                    display_name(key),
                    subheading_style
                )
            )

            add_bullet_list(
                story,
                data[key],
                normal_style
            )

    if data.get("risk_level"):

        story.append(
            Paragraph(
                "Risk Level",
                subheading_style
            )
        )

        story.append(
            Paragraph(
                clean_text(
                    data["risk_level"]
                ),
                normal_style
            )
        )

    if data.get("risk_reasons"):

        story.append(
            Paragraph(
                "Risk Reasons",
                subheading_style
            )
        )

        add_bullet_list(
            story,
            data["risk_reasons"],
            normal_style
        )


# ============================================================
# MVP RENDERER
# ============================================================

def render_mvp(
    story,
    data,
    normal_style,
    subheading_style
):

    if not isinstance(data, dict):

        story.append(
            Paragraph(
                "MVP analysis unavailable.",
                normal_style
            )
        )

        return

    ordered_sections = [
        "startup_idea",
        "problem_statement",
        "target_users",
        "value_proposition",
        "core_features",
        "future_features",
        "recommended_tech_stack",
        "development_phases",
        "estimated_timeline",
        "success_metrics",
        "risks"
    ]

    for key in ordered_sections:

        if key not in data:
            continue

        value = data[key]

        story.append(
            Paragraph(
                display_name(key),
                subheading_style
            )
        )

        if isinstance(value, list):

            add_bullet_list(
                story,
                value,
                normal_style
            )

        elif isinstance(value, dict):

            render_dict(
                story,
                value,
                normal_style,
                subheading_style
            )

        else:

            story.append(
                Paragraph(
                    clean_text(value),
                    normal_style
                )
            )


# ============================================================
# GTM RENDERER
# ============================================================

def render_gtm(
    story,
    data,
    normal_style,
    subheading_style
):

    if not isinstance(data, dict):

        story.append(
            Paragraph(
                "GTM analysis unavailable.",
                normal_style
            )
        )

        return

    ordered_sections = [
        "startup_idea",
        "target_audience",
        "value_proposition",
        "positioning_statement",
        "marketing_channels",
        "pricing_strategy",
        "revenue_model",
        "customer_acquisition_strategy",
        "customer_retention_strategy",
        "launch_plan",
        "partnership_opportunities",
        "key_metrics",
        "estimated_budget",
        "risks"
    ]

    for key in ordered_sections:

        if key not in data:
            continue

        value = data[key]

        story.append(
            Paragraph(
                display_name(key),
                subheading_style
            )
        )

        # ----------------------------------------------------
        # List of dictionaries
        # ----------------------------------------------------

        if isinstance(value, list):

            for item in value:

                if isinstance(item, dict):

                    if item.get("segment"):

                        story.append(
                            Paragraph(
                                "<b>"
                                + clean_text(
                                    item["segment"]
                                )
                                + "</b>",
                                normal_style
                            )
                        )

                    if item.get("description"):

                        story.append(
                            Paragraph(
                                clean_text(
                                    item["description"]
                                ),
                                normal_style
                            )
                        )

                    if item.get("phase"):

                        story.append(
                            Paragraph(
                                "<b>"
                                + clean_text(
                                    item["phase"]
                                )
                                + "</b>",
                                normal_style
                            )
                        )

                    if item.get("activities"):

                        add_bullet_list(
                            story,
                            item["activities"],
                            normal_style
                        )

                else:

                    story.append(
                        Paragraph(
                            f"• {clean_text(item)}",
                            normal_style
                        )
                    )

        elif isinstance(value, dict):

            render_dict(
                story,
                value,
                normal_style,
                subheading_style
            )

        else:

            story.append(
                Paragraph(
                    clean_text(value),
                    normal_style
                )
            )


# ============================================================
# PDF GENERATOR
# ============================================================

def generate_report_pdf(
    shared_state: dict,
    output_path: str
):

    output_path = Path(
        output_path
    )

    output_path.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # ========================================================
    # DOCUMENT
    # ========================================================

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )

    # ========================================================
    # STYLES
    # ========================================================

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "ReportTitle",
        parent=styles["Title"],
        alignment=TA_CENTER,
        fontSize=20,
        leading=24,
        spaceAfter=12
    )

    subtitle_style = ParagraphStyle(
        "ReportSubtitle",
        parent=styles["BodyText"],
        alignment=TA_CENTER,
        fontSize=11,
        leading=14,
        spaceAfter=20
    )

    heading_style = ParagraphStyle(
        "ReportHeading",
        parent=styles["Heading2"],
        fontSize=15,
        leading=19,
        spaceBefore=16,
        spaceAfter=9
    )

    subheading_style = ParagraphStyle(
        "ReportSubHeading",
        parent=styles["Heading3"],
        fontSize=11,
        leading=14,
        spaceBefore=8,
        spaceAfter=4
    )

    small_heading_style = ParagraphStyle(
        "SmallHeading",
        parent=styles["Heading4"],
        fontSize=10,
        leading=13,
        spaceBefore=7,
        spaceAfter=4
    )

    normal_style = ParagraphStyle(
        "ReportNormal",
        parent=styles["BodyText"],
        fontSize=9.5,
        leading=13,
        spaceAfter=5
    )

    # ========================================================
    # STORY
    # ========================================================

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
            "<b>Startup Idea:</b> "
            + clean_text(
                shared_state.get(
                    "startup_idea"
                )
            ),
            subtitle_style
        )
    )

    # ========================================================
    # FINAL REPORT
    # ========================================================

    final_report = shared_state.get(
        "final_report",
        {}
    )

    if not isinstance(
        final_report,
        dict
    ):
        final_report = {}

    # ========================================================
    # FINAL VALIDATION SUMMARY
    # ========================================================

    story.append(
        Paragraph(
            "Final Validation Summary",
            heading_style
        )
    )

    summary_data = [
        [
            Paragraph(
                "<b>Validation Score</b>",
                normal_style
            ),
            Paragraph(
                "<b>Success Potential</b>",
                normal_style
            ),
            Paragraph(
                "<b>Recommendation</b>",
                normal_style
            )
        ],
        [
            Paragraph(
                clean_text(
                    final_report.get(
                        "validation_score"
                    )
                ),
                normal_style
            ),
            Paragraph(
                clean_text(
                    final_report.get(
                        "success_potential"
                    )
                ),
                normal_style
            ),
            Paragraph(
                clean_text(
                    final_report.get(
                        "recommendation"
                    )
                ),
                normal_style
            )
        ]
    ]

    summary_table = Table(
        summary_data,
        colWidths=[
            150,
            150,
            150
        ]
    )

    summary_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),
            (
                "ALIGN",
                (0, 0),
                (-1, -1),
                "CENTER"
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "MIDDLE"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                8
            )
        ])
    )

    story.append(
        summary_table
    )

    # ========================================================
    # SCORECARD
    # ========================================================

    story.append(
        Paragraph(
            "Validation Scorecard",
            heading_style
        )
    )

    scorecard_data = [
        [
            Paragraph(
                "<b>Category</b>",
                normal_style
            ),
            Paragraph(
                "<b>Score</b>",
                normal_style
            ),
            Paragraph(
                "<b>Assessment</b>",
                normal_style
            )
        ]
    ]

    scorecard_fields = [
        (
            "Problem Validation",
            "problem_validation"
        ),
        (
            "Market Potential",
            "market_potential"
        ),
        (
            "Competitive Position",
            "competitive_position"
        ),
        (
            "MVP Feasibility",
            "mvp_feasibility"
        ),
        (
            "Go-To-Market Readiness",
            "go_to_market_readiness"
        )
    ]

    for category_name, key in scorecard_fields:

        data = final_report.get(
            key,
            {}
        )

        if not isinstance(
            data,
            dict
        ):
            data = {}

        scorecard_data.append(
            [
                Paragraph(
                    clean_text(
                        category_name
                    ),
                    normal_style
                ),
                Paragraph(
                    clean_text(
                        data.get(
                            "score",
                            "N/A"
                        )
                    ),
                    normal_style
                ),
                Paragraph(
                    clean_text(
                        data.get(
                            "assessment",
                            "Not Available"
                        )
                    ),
                    normal_style
                )
            ]
        )

    scorecard_table = Table(
        scorecard_data,
        colWidths=[
            115,
            50,
            285
        ],
        repeatRows=1
    )

    scorecard_table.setStyle(
        TableStyle([
            (
                "BACKGROUND",
                (0, 0),
                (-1, 0),
                colors.lightgrey
            ),
            (
                "GRID",
                (0, 0),
                (-1, -1),
                1,
                colors.grey
            ),
            (
                "VALIGN",
                (0, 0),
                (-1, -1),
                "TOP"
            ),
            (
                "PADDING",
                (0, 0),
                (-1, -1),
                6
            )
        ])
    )

    story.append(
        scorecard_table
    )

    # ========================================================
    # FINAL ASSESSMENT
    # ========================================================

    story.append(
        Paragraph(
            "Final Assessment",
            heading_style
        )
    )

    story.append(
        Paragraph(
            clean_text(
                final_report.get(
                    "final_assessment"
                )
            ),
            normal_style
        )
    )

    # ========================================================
    # SUMMARY LISTS
    # ========================================================

    add_bullet_list(
        story,
        final_report.get(
            "key_strengths",
            []
        ),
        normal_style
    )

    # Rename heading correctly
    # The list above is intentionally preceded by its heading
    # below for clean ordering.

    # We need to reconstruct these sections in order.
    # Remove previous strengths rendering and render all explicitly.

    # ========================================================
    # KEY STRENGTHS
    # ========================================================

    story.append(
        Paragraph(
            "Key Strengths",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "key_strengths",
            []
        ),
        normal_style
    )

    # ========================================================
    # KEY WEAKNESSES
    # ========================================================

    story.append(
        Paragraph(
            "Key Weaknesses",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "key_weaknesses",
            []
        ),
        normal_style
    )

    # ========================================================
    # OPPORTUNITIES
    # ========================================================

    story.append(
        Paragraph(
            "Major Opportunities",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "major_opportunities",
            []
        ),
        normal_style
    )

    # ========================================================
    # RISKS
    # ========================================================

    story.append(
        Paragraph(
            "Major Risks",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "major_risks",
            []
        ),
        normal_style
    )

    # ========================================================
    # RECOMMENDED MVP
    # ========================================================

    story.append(
        Paragraph(
            "Recommended MVP",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "recommended_mvp",
            []
        ),
        normal_style
    )

    # ========================================================
    # FIRST MARKET
    # ========================================================

    story.append(
        Paragraph(
            "Recommended First Market",
            heading_style
        )
    )

    story.append(
        Paragraph(
            clean_text(
                final_report.get(
                    "recommended_first_market"
                )
            ),
            normal_style
        )
    )

    # ========================================================
    # SUCCESS FACTORS
    # ========================================================

    story.append(
        Paragraph(
            "Critical Success Factors",
            heading_style
        )
    )

    add_bullet_list(
        story,
        final_report.get(
            "critical_success_factors",
            []
        ),
        normal_style
    )

    # ========================================================
    # PAGE BREAK
    # ========================================================

    story.append(
        PageBreak()
    )

    # ========================================================
    # DETAILED COMPETITOR
    # ========================================================

    story.append(
        Paragraph(
            "Detailed Competitor Analysis",
            heading_style
        )
    )

    render_competitor_analysis(
        story,
        shared_state.get(
            "competitor_analysis"
        ),
        normal_style,
        subheading_style,
        small_heading_style
    )

    # ========================================================
    # DETAILED MARKET
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Detailed Market Analysis",
            heading_style
        )
    )

    render_dict(
        story,
        shared_state.get(
            "market_analysis"
        ),
        normal_style,
        subheading_style
    )

    # ========================================================
    # DETAILED SWOT
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Detailed SWOT Analysis",
            heading_style
        )
    )

    render_swot(
        story,
        shared_state.get(
            "swot_analysis"
        ),
        normal_style,
        subheading_style
    )

    # ========================================================
    # DETAILED MVP
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Detailed MVP Analysis",
            heading_style
        )
    )

    render_mvp(
        story,
        shared_state.get(
            "mvp_analysis"
        ),
        normal_style,
        subheading_style
    )

    # ========================================================
    # DETAILED GTM
    # ========================================================

    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "Detailed GTM Analysis",
            heading_style
        )
    )

    render_gtm(
        story,
        shared_state.get(
            "gtm_analysis"
        ),
        normal_style,
        subheading_style
    )

    # ========================================================
    # BUILD PDF
    # ========================================================

    doc.build(
        story
    ) 

    return str(
        output_path
    )