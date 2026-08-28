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
from agents.mvp import mvp_agent


# ============================================================
# HEADER
# ============================================================

print("\n========================================")
print("             MVP AGENT TEST")
print("========================================")


# ============================================================
# USER INPUT
# ============================================================

startup_idea = input(
    "\nEnter Startup Idea: "
).strip()


# ============================================================
# VALIDATE INPUT
# ============================================================

if not startup_idea:

    print("\nStartup idea cannot be empty.")
    sys.exit(1)


# ============================================================
# PAYLOAD
# ============================================================

payload = {

    "messages": [

        {
            "role": "user",

            "content": f"""
Startup Idea:

{startup_idea}

Perform ONLY MVP planning.

Use ONLY the startup idea.

Do NOT use:

- Competitor Analysis
- Market Analysis
- SWOT Analysis
- GTM Strategy
- Final Report

Do NOT perform web searches.

Return ONLY valid JSON.

Do not explain.
Do not summarize.
Do not use markdown.
Do not add text outside the JSON.
"""
        }

    ]
}


# ============================================================
# RUN WITH CENTRALIZED FALLBACK
# ============================================================

try:

    response = run_with_fallback(
        agent_definition=mvp_agent,
        payload=payload
    )

except Exception as error:

    print("\n========================================")
    print("             MVP AGENT FAILED")
    print("========================================")

    print(f"\nError: {error}")

    sys.exit(1)


# ============================================================
# JSON VALIDATION
# ============================================================

try:

    parsed_response = json.loads(response)

except json.JSONDecodeError:

    print("\n========================================")
    print("       JSON VALIDATION FAILED")
    print("========================================")

    print("\nRaw response:")
    print(response)

    sys.exit(1)


# ============================================================
# REQUIRED FIELD VALIDATION
# ============================================================

required_fields = [
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


missing_fields = [
    field
    for field in required_fields
    if field not in parsed_response
]


if missing_fields:

    print("\n========================================")
    print("       MVP STRUCTURE VALIDATION FAILED")
    print("========================================")

    print(
        "\nMissing fields:"
    )

    for field in missing_fields:
        print(f"- {field}")

    sys.exit(1)


# ============================================================
# SUCCESS
# ============================================================

print("\n========================================")
print("       JSON VALIDATION: SUCCESS")
print("========================================")

print(
    json.dumps(
        parsed_response,
        indent=4
    )
)

print("\n========================================")
print("           MVP TEST COMPLETE")
print("========================================")