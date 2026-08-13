import sys
from pathlib import Path
import json

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from app.advisor import ask_advisor


# ============================================================
# SAMPLE VALIDATION RESULT
# ============================================================

validation_context = {

    "startup_idea": "AI-powered technical interview platform",

    "market_analysis": {
        "industry": "EdTech / AI Interview Preparation",
        "target_customers": [
            "Computer Science students",
            "Fresh graduates",
            "Working software professionals"
        ],
        "market_trends": [
            "AI-powered learning",
            "Personalized interview preparation"
        ]
    },

    "competitor_analysis": {
        "direct_competitors": [
            "LeetCode",
            "HackerRank"
        ],
        "competitive_advantages": [
            "AI-powered personalized feedback"
        ],
        "market_gaps": [
            "Limited personalized interview simulations"
        ]
    },

    "swot": {
        "strengths": [
            "AI personalization"
        ],
        "weaknesses": [
            "New brand"
        ],
        "opportunities": [
            "Growing demand for interview preparation"
        ],
        "threats": [
            "Established competitors"
        ],
        "risk_level": "Medium"
    },

    "mvp": {
        "core_features": [
            "AI mock interviews",
            "Performance analysis",
            "Personalized recommendations"
        ]
    },

    "gtm": {
        "target_audience": [
            "Final-year students",
            "Fresh graduates"
        ],
        "pricing_strategy": "Freemium"
    },

    "final_report": {
        "validation_score": 78,
        "risk_level": "Medium",
        "verdict": "Promising with execution risks"
    }
}


# ============================================================
# CHAT LOOP
# ============================================================

print("\n======================================")
print("      AI STARTUP CONVERSATIONAL ADVISOR")
print("======================================")

while True:

    question = input("\nYou: ").strip()

    if question.lower() in ["exit", "quit"]:
        print("Advisor: Goodbye!")
        break

    if not question:
        continue

    answer = ask_advisor(
        question,
        validation_context
    )

    print("\nAdvisor:")
    print(answer)