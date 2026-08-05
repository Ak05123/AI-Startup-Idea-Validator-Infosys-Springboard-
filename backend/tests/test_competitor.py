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

from app.config import gemini_model_1

from agents.subagents.competitor import competitor_subagent

# ==================================================
# CREATE DEEP AGENT
# ==================================================

agent = create_deep_agent(

    model=gemini_model_1,

    subagents=[
        competitor_subagent
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

Perform ONLY competitor analysis.

Delegate ONLY to competitor_agent.

Return ONLY valid JSON.

Do not explain.
Do not summarize.
Do not use markdown.
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

print("\nRESULT\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except Exception:
    print(response)