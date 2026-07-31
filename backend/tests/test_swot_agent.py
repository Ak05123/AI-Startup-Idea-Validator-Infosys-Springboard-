import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.swot_risk_agent import SwotRiskAgent


def main():

    idea = input(
        "Enter startup idea: "
    ).strip()

    print("\nSWOT TEST START")

    web_agent = WebSearchAgent()
    competitor_agent = CompetitorAgent()
    market_agent = MarketAnalysisAgent()
    swot_agent = SwotRiskAgent()

    competitor_results = web_agent.search(
        idea + " top competitors companies"
    )

    competitors = competitor_agent.analyze(
        competitor_results
    )

    market_results = web_agent.search(
        idea
        + " market size growth industry trends "
        + "target customers"
    )

    market_analysis = market_agent.analyze(
        idea,
        market_results
    )

    result = swot_agent.analyze(
        idea,
        competitors,
        market_analysis
    )

    print("\nSWOT RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()