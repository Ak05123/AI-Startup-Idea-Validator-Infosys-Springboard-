import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))



from app.config import client, MODEL_NAME

class SwotRiskAgent:

    def __init__(self):
        self.client = client

    def analyze(self, idea, competitors, market_analysis):

        prompt = f"""
You are an AI SWOT and Risk Analysis Agent.

Startup Idea:
{idea}

Competitor Analysis:
{competitors}

Market Analysis:
{market_analysis}

Analyze the startup idea using the competitor analysis and market analysis.

Return ONLY valid JSON.

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
4. Identify external threats from competitors, market conditions, technology, etc.
5. Identify major business risks.
6. Keep each item clear and specific.
7. Use the competitor and market information provided.
8. Do not explain anything outside the JSON.
9. Return ONLY valid JSON.
"""

        print("\nSending data to Gemini for SWOT and Risk Analysis...\n")

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("\nGemini Error:")
            print(e)

            return "{}"


if __name__ == "__main__":

    from agents.web_search_agent import WebSearchAgent
    from agents.competitor_agent import CompetitorAgent
    from agents.market_analysis_agent import MarketAnalysisAgent

    startup = input("Enter startup idea: ")

    web = WebSearchAgent()

    # Search for competitor information
    competitor_results = web.search(
        startup + " top competitors companies"
    )

    # Search for market information
    market_results = web.search(
        startup + " market size CAGR industry trends target customers"
    )

    competitor_agent = CompetitorAgent()
    market_agent = MarketAnalysisAgent()
    swot_agent = SwotRiskAgent()

    competitors = competitor_agent.analyze(
        competitor_results
    )

    market_analysis = market_agent.analyze(
        startup,
        market_results
    )

    swot_result = swot_agent.analyze(
        startup,
        competitors,
        market_analysis
    )

    print("\nSWOT AND RISK ANALYSIS:\n")
    print(swot_result)