import sys
from pathlib import Path


# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


# ============================================================
# IMPORT PDF GENERATOR
# ============================================================

from app.pdf_generator import generate_report_pdf


# ============================================================
# TEST SHARED STATE
# ============================================================

shared_state = {

    "startup_idea": "bus booking",

    # --------------------------------------------------------
    # COMPETITOR
    # --------------------------------------------------------

    "competitor_analysis": {
        "competitors": [
            "RedBus",
            "AbhiBus",
            "Busbud"
        ],
        "competitive_advantage": [
            "Focus on underserved regional routes",
            "Simple booking experience"
        ]
    },

    # --------------------------------------------------------
    # MARKET
    # --------------------------------------------------------

    "market_analysis": {
        "target_market": "Online bus booking market",
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

    # --------------------------------------------------------
    # SWOT
    # --------------------------------------------------------

    "swot_analysis": {
        "strengths": [
            "Clear customer problem",
            "Scalable digital platform"
        ],
        "weaknesses": [
            "Strong existing competition"
        ],
        "opportunities": [
            "Underserved regional routes"
        ],
        "threats": [
            "Established booking platforms"
        ]
    },

    # --------------------------------------------------------
    # MVP
    # --------------------------------------------------------

    "mvp_analysis": {
        "problem_statement": (
            "Passengers need a convenient way to "
            "search and book bus tickets."
        ),
        "target_users": [
            "Daily commuters",
            "Students",
            "Budget travelers"
        ],
        "core_features": [
            "Route search",
            "Bus schedule filtering",
            "Seat selection",
            "Online payment",
            "Digital ticket generation"
        ],
        "recommended_tech_stack": {
            "frontend": "React",
            "backend": "Node.js",
            "database": "PostgreSQL"
        },
        "estimated_timeline": "8 weeks"
    },

    # --------------------------------------------------------
    # GTM
    # --------------------------------------------------------

    "gtm_analysis": {
        "target_audience": [
            "Daily commuters",
            "Students",
            "Budget travelers"
        ],
        "value_proposition": (
            "Simple and convenient bus booking "
            "for regional travelers."
        ),
        "positioning_statement": (
            "A convenient bus booking platform "
            "focused on underserved routes."
        )
    },

    # --------------------------------------------------------
    # FINAL REPORT
    # --------------------------------------------------------

    "final_report": {

        "startup_idea": "bus booking",

        "validation_score": 76,

        "success_potential": "Medium-High",

        "problem_validation": {
            "score": 78,
            "assessment": (
                "The idea addresses a clear "
                "convenience problem."
            )
        },

        "market_potential": {
            "score": 74,
            "assessment": (
                "The market has strong demand "
                "but significant competition."
            )
        },

        "competitive_position": {
            "score": 65,
            "assessment": (
                "Differentiation will be required "
                "to compete effectively."
            )
        },

        "mvp_feasibility": {
            "score": 82,
            "assessment": (
                "The MVP can be developed using "
                "established technologies."
            )
        },

        "go_to_market_readiness": {
            "score": 76,
            "assessment": (
                "The target audience and positioning "
                "are reasonably clear."
            )
        },

        "key_strengths": [
            "Clear customer problem",
            "Scalable digital platform",
            "Feasible MVP"
        ],

        "key_weaknesses": [
            "Strong competition",
            "Dependence on bus operators",
            "Customer acquisition challenges"
        ],

        "major_opportunities": [
            "Tier-2 and Tier-3 cities",
            "Regional bus operators",
            "Digital booking adoption"
        ],

        "major_risks": [
            "Strong competitors",
            "Low initial customer trust",
            "Operator integration issues"
        ],

        "recommended_mvp": [
            "Route search",
            "Schedule filtering",
            "Seat selection",
            "Secure payment",
            "Digital ticket generation"
        ],

        "recommended_first_market": (
            "Daily commuters and students "
            "traveling through regional routes."
        ),

        "critical_success_factors": [
            "Reliable operator partnerships",
            "Low customer acquisition cost",
            "Reliable payment processing"
        ],

        "final_assessment": (
            "The startup addresses a real problem "
            "and has a feasible MVP, but strong "
            "competition requires clear differentiation."
        ),

        "recommendation": "Proceed with caution"
    }
}


# ============================================================
# OUTPUT PATH
# ============================================================

output_path = (
    Path(__file__).resolve().parents[2]
    / "startup_validation_report.pdf"
)


# ============================================================
# GENERATE PDF
# ============================================================

print("\n========================================")
print("          PDF GENERATOR TEST")
print("========================================")

try:

    generated_file = generate_report_pdf(
        shared_state,
        str(output_path)
    )

    print("\n========================================")
    print("          PDF GENERATED")
    print("========================================")

    print(
        f"\nFile: {generated_file}"
    )

    # --------------------------------------------------------
    # VERIFY FILE
    # --------------------------------------------------------

    if output_path.exists():

        print(
            "\n✓ PDF file exists"
        )

        print(
            f"✓ File size: "
            f"{output_path.stat().st_size} bytes"
        )

        print(
            "\nPDF GENERATOR TEST SUCCESS"
        )

    else:

        print(
            "\n✗ PDF file was not created"
        )

except Exception as error:

    print("\n========================================")
    print("          PDF GENERATOR FAILED")
    print("========================================")

    print(
        f"\nError: {error}"
    )