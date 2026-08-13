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

from agents.gtm import gtm_agent


# ============================================================
# USER INPUT
# ============================================================

idea = input("Enter Startup Idea: ").strip()


# ============================================================
# INVOKE GTM AGENT
# ============================================================

result = gtm_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Startup Idea:

{idea}

You are required to generate ONLY the
Go-To-Market (GTM) Strategy.

Generate:

- Minimum 3 Target Audience Segments
- Value Proposition
- Positioning Statement
- Minimum 6 Marketing Channels
- Pricing Strategy
- Revenue Model
- Minimum 5 Customer Acquisition Strategies
- Minimum 5 Customer Retention Strategies
- Launch Plan
- Minimum 5 Partnership Opportunities
- Minimum 6 KPIs
- Estimated Marketing Budget
- Minimum 5 GTM Risks

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

print("\n========== GO-TO-MARKET STRATEGY ==========\n")

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


print("\n===========================================")