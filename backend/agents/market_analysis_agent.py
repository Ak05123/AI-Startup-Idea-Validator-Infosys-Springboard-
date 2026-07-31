

import sys
from pathlib import Path


# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)


# ==================================================
# IMPORT MODEL
# ==================================================

from app.config import model


# ==================================================
# MARKET ANALYSIS AGENT
# ==================================================

class MarketAnalysisAgent:

    def __init__(self):
        self.model = model

    def analyze(
        self,
        idea,
        search_results
    ):

        # --------------------------------------------------
        # Convert search results into text
        # --------------------------------------------------

        text = ""

        for result in search_results:

            text += f"""
Title: {result.get('title', '')}
Description: {result.get('description', '')}
Link: {result.get('link', '')}
"""


        # --------------------------------------------------
        # Prompt
        # --------------------------------------------------

        prompt = f"""
You are an AI Market Analysis Agent.

Startup Idea:
{idea}

Web Search Results:
{text}

Analyze the startup market.

Return ONLY valid JSON in exactly this structure:

{{
    "industry": "",
    "market_size": "",
    "growth_rate": "",
    "target_customers": [],
    "market_trends": [],
    "opportunities": [],
    "challenges": []
}}

Rules:

1. Identify the industry.
2. Identify market size if reliable information is available.
3. Identify growth rate if reliable information is available.
4. Identify target customers.
5. Identify current market trends.
6. Identify business opportunities.
7. Identify major market challenges.
8. Do not invent specific statistics.
9. If reliable information is unavailable, say "Not available".
10. Return ONLY JSON.
"""


        # --------------------------------------------------
        # Gemini
        # --------------------------------------------------

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\n[Market Analysis Error]")
            print(e)

            return "{}"