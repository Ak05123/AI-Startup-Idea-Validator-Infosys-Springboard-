import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.config import model


def _limit_text(value, max_chars=5000):
    """
    Prevent very large previous-agent outputs from
    being sent to the MVP model.
    """
    if value is None:
        return ""

    value = str(value)

    if len(value) <= max_chars:
        return value

    return value[:max_chars] + "\n...[truncated]"


class MvpRecommendationAgent:

    def __init__(self):
        self.model = model

    def analyze(
        self,
        idea,
        competitors,
        market_analysis,
        swot_analysis
    ):

        competitors = _limit_text(competitors)
        market_analysis = _limit_text(market_analysis)
        swot_analysis = _limit_text(swot_analysis)

        prompt = f"""
You are an AI MVP Recommendation Agent.

Startup Idea:
{idea}

Competitor Analysis:
{competitors}

Market Analysis:
{market_analysis}

SWOT and Risk Analysis:
{swot_analysis}

Recommend a focused Minimum Viable Product.

Choose the best initial customer segment based on:
- market demand
- customer need
- competition
- strengths
- weaknesses
- opportunities
- risks
- feasibility

Return ONLY valid JSON:

{{
    "mvp_goal": "",
    "primary_mvp_users": [],
    "core_features": [],
    "secondary_features": [],
    "features_to_avoid_initially": [],
    "development_priority": [],
    "validation_metrics": []
}}

Rules:

1. Choose ONE primary initial customer segment.
2. Keep the MVP small and realistic.
3. Recommend essential features only.
4. Include useful secondary features.
5. Identify features to avoid initially.
6. Give development priorities.
7. Give measurable validation metrics.
8. Use the supplied competitor, market and SWOT information.
9. Do not invent unsupported facts.
10. Return ONLY JSON.
"""

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\n[MVP Recommendation Error]")
            print(e)

            return "{}"