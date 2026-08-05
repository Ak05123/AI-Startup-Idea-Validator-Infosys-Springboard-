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

from agents.subagents.swot_risk import swot_subagent

# ==================================================
# CREATE DEEP AGENT
# ==================================================

agent = create_deep_agent(

    model=gemini_model_2,

    subagents=[
        swot_subagent
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

You are required to perform ONLY SWOT analysis.

Delegate the task ONLY to swot_agent.

The final response MUST be exactly the JSON returned by swot_agent.

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

Rules:

- Return ONLY valid JSON.
- Do NOT explain.
- Do NOT summarize.
- Do NOT use markdown.
- Do NOT mention delegation.
- Do NOT add any text before or after the JSON.
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

print("\n========== SWOT ANALYSIS ==========\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except Exception:
    print(response)

print("\n==================================")