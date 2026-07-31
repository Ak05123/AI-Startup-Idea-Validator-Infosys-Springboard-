import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.config import model


class SwotRiskAgent:

    def __init__(self):
        self.model = model

    def analyze(
        self,
        idea,
        competitors,
        market_analysis
    ):

        prompt = f"""
You are an AI SWOT and Risk Analysis Agent.

Startup Idea:
{idea}

Competitor Analysis:
{competitors}

Market Analysis:
{market_analysis}

Analyze the startup idea using the competitor
analysis and market analysis.

Return ONLY valid JSON in exactly this structure:

{{
    "strengths": [],
    "weaknesses": [],
    "opportunities": [],
    "threats": [],
    "risks": []
}}

Rules:

1. Identify the major strengths of the startup idea.
2. Identify the major weaknesses.
3. Identify business opportunities.
4. Identify external threats from competitors,
   market conditions, technology, and other factors.
5. Identify major business risks.
6. Keep every item clear and specific.
7. Use the competitor and market information provided.
8. Do not invent unsupported facts.
9. Do not add explanations outside the JSON.
10. Return ONLY valid JSON.
"""

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\n[SWOT and Risk Analysis Error]")
            print(e)

            return "{}"