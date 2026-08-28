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
from agents.gtm import gtm_agent


# ============================================================
# HEADER
# ============================================================

print("\n========================================")
print("          GTM AGENT TEST")
print("========================================")


# ============================================================
# USER INPUT
# ============================================================

startup_idea = input(
    "\nEnter Startup Idea: "
).strip()


# ============================================================
# INPUT VALIDATION
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

Create ONLY a concise Go-To-Market strategy.

Use ONLY the startup idea.

Do NOT use:

- Competitor Analysis
- Market Analysis
- SWOT Analysis
- MVP Analysis
- Final Report

Do NOT perform web searches.

Return ONLY valid JSON.

Do not explain.
Do not summarize.
Do not use markdown.
"""
        }

    ]
}


# ============================================================
# RUN GTM AGENT
# ============================================================

try:

    response = run_with_fallback(
        agent_definition=gtm_agent,
        payload=payload
    )

except Exception as error:

    print("\n========================================")
    print("GTM AGENT FAILED")
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
    print("JSON VALIDATION FAILED")
    print("========================================")

    print("\nRaw response:")
    print(response)

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
print("          GTM TEST COMPLETE")
print("========================================")