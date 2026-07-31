import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.config import model


class GtmStrategyAgent:

    def __init__(self):
        self.model = model

    def analyze(
        self,
        idea,
        competitors,
        market_analysis,
        swot_analysis,
        mvp_recommendation
    ):

        prompt = f"""
You are an AI Go-To-Market (GTM) Strategy Agent.

Your job is to create a practical launch and
customer acquisition strategy for the startup.

Startup Idea:
{idea}

Competitor Analysis:
{competitors}

Market Analysis:
{market_analysis}

SWOT and Risk Analysis:
{swot_analysis}

MVP Recommendation:
{mvp_recommendation}

Create a focused GTM strategy for launching the MVP.

Return ONLY valid JSON in exactly this structure:

{{
    "target_market": [],
    "primary_customer_segment": "",
    "value_proposition": "",
    "positioning": "",
    "pricing_strategy": "",
    "customer_acquisition_channels": [],
    "launch_strategy": [],
    "partnership_strategy": [],
    "retention_strategy": [],
    "key_metrics": [],
    "major_gtm_risks": []
}}

Rules:

1. Select the most promising target market.
2. Select the primary customer segment for launch.
3. Explain the startup's value proposition clearly.
4. Define how the startup should be positioned against competitors.
5. Recommend a realistic pricing strategy.
6. Recommend practical customer acquisition channels.
7. Give a phased launch strategy.
8. Suggest useful partnership opportunities.
9. Suggest strategies for customer retention.
10. Provide measurable GTM metrics.
11. Identify major GTM risks.
12. Use the competitor, market, SWOT, and MVP information.
13. Keep the strategy realistic for an early-stage startup.
14. Do not invent unsupported facts.
15. Return ONLY valid JSON.
"""

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\n[GTM Strategy Error]")
            print(e)

            return "{}"