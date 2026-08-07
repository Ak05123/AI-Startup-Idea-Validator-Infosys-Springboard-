import sys
from pathlib import Path
import json

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

# ==================================================
# IMPORTS
# ==================================================

from deepagents import create_deep_agent

from app.config import gemini_model_2

from agents.subagents.gtm import gtm_subagent

# ==================================================
# CREATE DEEP AGENT
# ==================================================

agent = create_deep_agent(

    model=gemini_model_2,

    subagents=[
        gtm_subagent
    ]

)

# ==================================================
# USER INPUT
# ==================================================

idea = input("Enter Startup Idea: ").strip()

# ==================================================
# INVOKE AGENT
# ==================================================

result = agent.invoke(

    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Startup Idea:

{idea}

You are required to generate ONLY the Go-To-Market (GTM) Strategy.

Delegate ONLY to gtm_agent.

The final response MUST be exactly the JSON returned by gtm_agent.

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
- Estimated Budget
- Minimum 5 Risks

Rules:

- Return ONLY valid JSON.
- Do NOT explain.
- Do NOT summarize.
- Do NOT use markdown.
- Do NOT mention delegation.
"""
            }
        ]
    }

)

# ==================================================
# PRINT RESULT
# ==================================================

response = result["messages"][-1].content

if isinstance(response, list):
    response = response[0]["text"]

print("\n========== GO TO MARKET STRATEGY ==========\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except Exception:
    print(response)

print("\n==========================================")