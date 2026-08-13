import sys
from pathlib import Path

# ============================================================
# PATH SETUP
# ============================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

# ============================================================
# IMPORTS
# ============================================================

from deepagents import create_deep_agent

from app.config import gemini_model_1


# ============================================================
# SWOT SYSTEM PROMPT
# ============================================================

SWOT_SYSTEM_PROMPT = """

You are an AI Startup Strategy Expert.

Your ONLY responsibility is to generate a detailed SWOT analysis.

You may receive:

1. Startup Idea
2. Competitor Analysis
3. Market Analysis

Do NOT perform web searches.

Instead, analyze the provided information carefully.

Return ONLY valid JSON.

Use EXACTLY this schema:

{
    "startup_idea": "",
    "strengths": [],
    "weaknesses": [],
    "opportunities": [],
    "threats": [],
    "risk_level": "",
    "recommendations": []
}

INSTRUCTIONS:

Generate:

- Minimum 5 strengths
- Minimum 5 weaknesses
- Minimum 5 opportunities
- Minimum 5 threats
- Minimum 5 recommendations

Strengths:

- Internal advantages
- Competitive capabilities
- Technology strengths
- Business strengths

Weaknesses:

- Internal limitations
- Resource constraints
- Operational challenges
- Product limitations

Opportunities:

- Market gaps
- Industry trends
- Customer demand
- Future expansion possibilities

Threats:

- Competition
- Regulatory risks
- Market uncertainty
- Technological disruption
- Financial risks

Recommendations:

Provide practical, actionable recommendations
to improve the startup.

Risk Level:

Return ONLY one value:

Low
Medium
High

RULES:

1. Return ONLY valid JSON.

2. Do NOT explain.

3. Do NOT summarize.

4. Do NOT use markdown.

5. Do NOT add extra keys.

6. Do NOT leave fields empty.

7. Every point should be meaningful and specific
   to the startup idea.

8. Recommendations should directly address
   identified weaknesses and threats.

"""
    

# ============================================================
# CREATE STANDALONE SWOT AGENT
# ============================================================

swot_agent = create_deep_agent(
    model=gemini_model_1,
    system_prompt=SWOT_SYSTEM_PROMPT
)