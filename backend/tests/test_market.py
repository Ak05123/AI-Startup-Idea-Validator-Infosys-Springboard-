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

from agents.market_analysis import market_agent


# ============================================================
# USER INPUT
# ============================================================

idea = input("Enter Startup Idea: ").strip()


# ============================================================
# INVOKE MARKET AGENT
# ============================================================

result = market_agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": f"""
Startup Idea:

{idea}

Perform ONLY market analysis.

Return ONLY valid JSON.

Do not explain.
Do not summarize.
Do not use markdown.
Do not add any text before or after the JSON.
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

print("\n========== MARKET ANALYSIS ==========\n")

try:
    parsed = json.loads(response)
    print(json.dumps(parsed, indent=4))
except json.JSONDecodeError:
    print(response)

print("\n=====================================")