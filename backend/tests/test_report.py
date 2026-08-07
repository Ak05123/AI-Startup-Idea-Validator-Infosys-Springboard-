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

from agents.subagents.report import report_subagent

# ==================================================
# CREATE DEEP AGENT
# ==================================================

agent = create_deep_agent(

    model=gemini_model_2,

    subagents=[
        report_subagent
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

Generate ONLY the Final Startup Validation Report.

Delegate ONLY to report_agent.

The final response MUST be exactly the JSON returned by report_agent.

Generate:

- Complete Startup Scorecard

- Overall Validation Score

- Validation Confidence

- Viability Estimate

- Risk Level

- Final Verdict

- Minimum 5 Strongest Factors

- Minimum 5 Weakest Factors

- Minimum 5 Key Risks

- Minimum 5 Next Actions

Rules:

Return ONLY valid JSON.

Do NOT explain.

Do NOT summarize.

Do NOT use markdown.

Do NOT mention delegation.

Do NOT add text before or after the JSON.
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

print("\n========== FINAL VALIDATION REPORT ==========\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except Exception:
    print(response)

print("\n============================================")