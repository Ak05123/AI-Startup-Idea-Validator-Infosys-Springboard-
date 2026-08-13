import sys
from pathlib import Path
import json

# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

# ============================================================
# IMPORTS
# ============================================================

from agents.report import report_agent
from app.pdf_generator import generate_report_pdf


# ============================================================
# USER INPUT
# ============================================================

idea = input("Enter Startup Idea: ").strip()


# ============================================================
# SAMPLE SPECIALIST ANALYSIS
# ============================================================

specialist_analysis = {
    "startup_idea": idea,

    "competitor_analysis": {
        "direct_competitors": [],
        "indirect_competitors": [],
        "competitive_advantages": [],
        "market_gaps": [],
        "references": []
    },

    "market_analysis": {
        "industry": "",
        "industry_overview": "",
        "market_size": {},
        "growth_rate": "",
        "target_customers": [],
        "market_trends": [],
        "opportunities": [],
        "challenges": [],
        "references": []
    },

    "swot_analysis": {
        "strengths": [],
        "weaknesses": [],
        "opportunities": [],
        "threats": [],
        "risk_level": "",
        "recommendations": []
    },

    "mvp_recommendation": {
        "problem_statement": "",
        "target_users": [],
        "value_proposition": "",
        "core_features": [],
        "future_features": [],
        "recommended_tech_stack": {},
        "development_phases": [],
        "estimated_timeline": "",
        "success_metrics": [],
        "risks": []
    },

    "gtm_strategy": {
        "target_audience": [],
        "value_proposition": "",
        "positioning_statement": "",
        "marketing_channels": [],
        "pricing_strategy": "",
        "revenue_model": "",
        "customer_acquisition_strategy": [],
        "customer_retention_strategy": [],
        "launch_plan": [],
        "partnership_opportunities": [],
        "key_metrics": [],
        "estimated_budget": "",
        "risks": []
    }
}


# ============================================================
# INVOKE REPORT AGENT
# ============================================================

result = report_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Generate the final Startup Validation Report.

Startup Idea:

{idea}

Specialist Analysis:

{json.dumps(specialist_analysis, indent=4)}

Evaluate the startup using the supplied
specialist analyses.

Return ONLY valid JSON.

Do not explain.
Do not summarize.
Do not use markdown.
Do not add text before or after the JSON.
"""
            }
        ]
    }
)


# ============================================================
# GET RESPONSE
# ============================================================

response = result["messages"][-1].content

if isinstance(response, list):
    response = response[0]["text"]


# ============================================================
# PARSE REPORT
# ============================================================

try:

    report = json.loads(response)

except json.JSONDecodeError:

    print("\nReport Agent did not return valid JSON.")
    print(response)
    sys.exit(1)


# ============================================================
# PRINT JSON
# ============================================================

print("\n========== FINAL VALIDATION REPORT ==========\n")

print(
    json.dumps(
        report,
        indent=4
    )
)


# ============================================================
# GENERATE PDF
# ============================================================

output_path = Path(
    __file__
).resolve().parents[2] / "startup_validation_report.pdf"


generate_report_pdf(
    report,
    str(output_path)
)


# ============================================================
# SUCCESS MESSAGE
# ============================================================

print("\n============================================")
print("PDF REPORT GENERATED SUCCESSFULLY")
print("============================================")

print(
    f"\nPDF Location:\n{output_path}"
)