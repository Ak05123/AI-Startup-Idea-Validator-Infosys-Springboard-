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


# ============================================================
# HEADER
# ============================================================

print("\n========================================")
print("       COMPETITOR AGENT TEST")
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

Perform ONLY competitor analysis.

Use ONLY the startup idea.

Use web search when current competitor
information is required.

Do NOT perform:

- Market Analysis
- SWOT Analysis
- MVP Planning
- GTM Strategy
- Final Report

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
# RUN WITH FALLBACK
# ============================================================

try:

    response = run_with_fallback(
        agent_definition=competitor_agent,
        payload=payload
    )

except Exception as error:

    print("\n========================================")
    print("       COMPETITOR AGENT FAILED")
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
# SUCCESS
# ============================================================

print("\n========================================")
print("      JSON VALIDATION: SUCCESS")
print("========================================")

print(
    json.dumps(
        parsed_response,
        indent=4
    )
)

print("\n========================================")
print("       COMPETITOR TEST COMPLETE")
print("========================================")