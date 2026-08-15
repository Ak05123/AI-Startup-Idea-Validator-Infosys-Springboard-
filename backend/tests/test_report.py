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

from app.agent_factory import run_with_fallback

from agents.competitor import competitor_agent
from agents.market_analysis import market_agent
from agents.swot_risk import swot_agent
from agents.mvp import mvp_agent
from agents.gtm import gtm_agent
from agents.report import report_agent


# ============================================================
# USER INPUT
# ============================================================

idea = input(
    "Enter Startup Idea: "
).strip()


# ============================================================
# COMMON PAYLOAD
# ============================================================

def create_payload(instruction):

    return {
        "messages": [
            {
                "role": "user",
                "content": f"""
Startup Idea:

{idea}

{instruction}

Return ONLY valid JSON.
Do not use markdown.
Do not add explanations.
"""
            }
        ]
    }


# ============================================================
# RUN SPECIALIST AGENTS
# ============================================================

print("\n========================================")
print("       RUNNING STARTUP ANALYSES")
print("========================================")


# ------------------------------------------------------------
# COMPETITOR
# ------------------------------------------------------------

try:

    competitor_result = run_with_fallback(
        competitor_agent,
        create_payload(
            "Perform competitor analysis."
        ),
        require_json=True
    )

    competitor_analysis = json.loads(
        competitor_result
    )

    print("✓ Competitor Analysis completed")

except Exception:

    competitor_analysis = None

    print("✗ Competitor Analysis failed")


# ------------------------------------------------------------
# MARKET
# ------------------------------------------------------------

try:

    market_result = run_with_fallback(
        market_agent,
        create_payload(
            "Perform market analysis."
        ),
        require_json=True
    )

    market_analysis = json.loads(
        market_result
    )

    print("✓ Market Analysis completed")

except Exception:

    market_analysis = None

    print("✗ Market Analysis failed")


# ------------------------------------------------------------
# SWOT
# ------------------------------------------------------------

try:

    swot_result = run_with_fallback(
        swot_agent,
        create_payload(
            "Perform SWOT and risk analysis."
        ),
        require_json=True
    )

    swot_analysis = json.loads(
        swot_result
    )

    print("✓ SWOT Analysis completed")

except Exception:

    swot_analysis = None

    print("✗ SWOT Analysis failed")


# ------------------------------------------------------------
# MVP
# ------------------------------------------------------------

try:

    mvp_result = run_with_fallback(
        mvp_agent,
        create_payload(
            "Design a practical MVP."
        ),
        require_json=True
    )

    mvp_analysis = json.loads(
        mvp_result
    )

    print("✓ MVP Analysis completed")

except Exception:

    mvp_analysis = None

    print("✗ MVP Analysis failed")


# ------------------------------------------------------------
# GTM
# ------------------------------------------------------------

try:

    gtm_result = run_with_fallback(
        gtm_agent,
        create_payload(
            "Create a concise Go-To-Market strategy."
        ),
        require_json=True
    )

    gtm_analysis = json.loads(
        gtm_result
    )

    print("✓ GTM Analysis completed")

except Exception:

    gtm_analysis = None

    print("✗ GTM Analysis failed")


# ============================================================
# BUILD SHARED STATE
# ============================================================

shared_state = {

    "startup_idea": idea,

    "competitor_analysis":
        competitor_analysis,

    "market_analysis":
        market_analysis,

    "swot_analysis":
        swot_analysis,

    "mvp_analysis":
        mvp_analysis,

    "gtm_analysis":
        gtm_analysis
}


# ============================================================
# DISPLAY SHARED STATE STATUS
# ============================================================

print("\n========================================")
print("          SHARED STATE READY")
print("========================================")

print(
    json.dumps(
        shared_state,
        indent=4
    )
)


# ============================================================
# REPORT AGENT
# ============================================================

print("\n========================================")
print("          RUNNING REPORT AGENT")
print("========================================")


try:

    report_result = run_with_fallback(
        report_agent,
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""
Create the final startup validation report
using the following completed shared state.

SHARED STATE:

{json.dumps(shared_state, indent=4)}

Evaluate the startup based on all available analyses.

Return ONLY valid JSON.
"""
                }
            ]
        },
        require_json=True
    )


    # --------------------------------------------------------
    # VALIDATE JSON
    # --------------------------------------------------------

    final_report = json.loads(
        report_result
    )


    # ========================================================
    # FINAL OUTPUT
    # ========================================================

    print("\n========================================")
    print("       FINAL VALIDATION REPORT")
    print("========================================")

    print(
        json.dumps(
            final_report,
            indent=4
        )
    )


except Exception:

    print("\n========================================")
    print("       REPORT AGENT FAILED")
    print("========================================")

    print(
        "report_agent could not complete the request."
    )