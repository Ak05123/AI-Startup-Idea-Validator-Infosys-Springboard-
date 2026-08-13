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
# IMPORT
# ============================================================

from agents.swot_risk import swot_agent


# ============================================================
# USER INPUT
# ============================================================

idea = input("Enter Startup Idea: ").strip()


# ============================================================
# INVOKE SWOT AGENT
# ============================================================

result = swot_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Startup Idea:

{idea}




Perform ONLY SWOT analysis.

Generate:

- At least 5 strengths
- At least 5 weaknesses
- At least 5 opportunities
- At least 5 threats
- At least 5 recommendations

Risk Level must be one of:

- Low
- Medium
- High

Return ONLY valid JSON.

Do NOT explain.
Do NOT summarize.
Do NOT use markdown.
Do NOT add any text before or after the JSON.
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
# PRINT RESULT
# ============================================================

print("\n========== SWOT ANALYSIS ==========\n")

try:
    parsed = json.loads(response)

    print(
        json.dumps(
            parsed,
            indent=4
        )
    )

except json.JSONDecodeError:
    print(response)


print("\n==================================")