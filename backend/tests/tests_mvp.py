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

from agents.subagents.mvp import mvp_subagent

# ==================================================
# CREATE DEEP AGENT
# ==================================================

agent = create_deep_agent(

    model=gemini_model_1,

    subagents=[
        mvp_subagent
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

You are required to design ONLY the Minimum Viable Product (MVP).

Delegate the task ONLY to mvp_agent.

The final response MUST be exactly the JSON returned by mvp_agent.

Generate:

- Problem Statement
- Minimum 3 Target User Groups
- Value Proposition
- Minimum 6 Core Features
- Minimum 6 Future Features
- Recommended Tech Stack
- Development Phases
- Estimated Timeline
- Minimum 5 Success Metrics
- Minimum 5 Risks

Rules:

- Return ONLY valid JSON.
- Do NOT explain.
- Do NOT summarize.
- Do NOT use markdown.
- Do NOT mention delegation.
- Do NOT add any extra text before or after the JSON.
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

print("\n========== MVP PLAN ==========\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except Exception:
    print(response)

print("\n====================================")