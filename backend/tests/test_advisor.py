import sys
from pathlib import Path


# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


# ============================================================
# IMPORTS
# ============================================================

from agents.advisor import advisor_agent
from app.agent_factory import run_with_fallback


# ============================================================
# SAMPLE VALIDATION DATA
# ============================================================

startup_data = {

    "startup_idea": "bus booking",

    "competitor_analysis": {
        "direct_competitors": [
            "RedBus",
            "AbhiBus",
            "Busbud"
        ],
        "competitive_advantages": [
            "Focus on underserved regional routes",
            "Simple booking experience"
        ]
    },

    "market_analysis": {

        "target_market": (
            "Online intercity and regional "
            "bus ticketing market"
        ),

        "target_customers": [
            "Daily commuters",
            "Students",
            "Budget travelers"
        ],

        "market_opportunities": [
            "Tier-2 and Tier-3 cities",
            "Digital booking adoption"
        ]
    },

    "swot_analysis": {

        "strengths": [
            "Clear customer problem",
            "Scalable digital platform"
        ],

        "weaknesses": [
            "Strong existing competition",
            "Dependence on bus operators"
        ],

        "opportunities": [
            "Regional routes",
            "Digital adoption"
        ],

        "threats": [
            "Established competitors",
            "Operator reliability issues"
        ]
    },

    "mvp_analysis": {

        "problem_statement": (
            "Passengers need a convenient way "
            "to search and book bus tickets."
        ),

        "core_features": [
            "Route search",
            "Schedule filtering",
            "Seat selection",
            "Online payment",
            "Digital ticket generation"
        ],

        "estimated_timeline": "8 weeks"
    },

    "gtm_analysis": {

        "target_audience": [
            "Daily commuters",
            "Students",
            "Budget travelers"
        ],

        "value_proposition": (
            "Simple and convenient bus booking "
            "for regional travelers."
        )
    },

    "final_report": {

        "validation_score": 76,

        "success_potential": "Medium-High",

        "competitive_position": {
            "score": 65,
            "assessment": (
                "Strong competition requires "
                "clear differentiation."
            )
        },

        "mvp_feasibility": {
            "score": 82,
            "assessment": (
                "The MVP can be developed using "
                "established technologies."
            )
        },

        "recommendation": "Proceed with caution",

        "major_risks": [
            "Strong competition",
            "Low initial customer trust",
            "Operator integration issues"
        ]
    }
}


# ============================================================
# USER QUESTION
# ============================================================

print("\n========================================")
print("       CONVERSATIONAL ADVISOR TEST")
print("========================================")

question = input(
    "\nAsk your question: "
).strip()


# ============================================================
# PROMPT
# ============================================================

prompt = f"""

STARTUP VALIDATION DATA:

{startup_data}


USER QUESTION:

{question}


Answer the user's question using ONLY the
startup validation data provided above.

Be practical and conversational.

Do not invent information.

Do not return JSON.
"""


# ============================================================
# RUN ADVISOR
# ============================================================

try:

    result = run_with_fallback(

        advisor_agent,

        {
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        },

        require_json=False
    )


    # ========================================================
    # OUTPUT
    # ========================================================

    

    print(result)

    print(
        "\n========================================"
    )

except Exception:

    

    print(
        "\nError: advisor could not complete the request."
    )