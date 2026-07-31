import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.swot_risk_agent import SwotRiskAgent
from agents.mvp_recommendation_agent import MvpRecommendationAgent
from agents.gtm_strategy_agent import GtmStrategyAgent


def main():

    idea = input(
        "Enter startup idea: "
    ).strip()

    print("\nGTM TEST START")

    web_agent = WebSearchAgent()
    competitor_agent = CompetitorAgent()
    market_agent = MarketAnalysisAgent()
    swot_agent = SwotRiskAgent()
    mvp_agent = MvpRecommendationAgent()
    gtm_agent = GtmStrategyAgent()

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

    swot_analysis = swot_agent.analyze(
        idea,
        competitors,
        market_analysis
    )

    mvp_recommendation = mvp_agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis
    )

    result = gtm_agent.analyze(
        idea,
        competitors,
        market_analysis,
        swot_analysis,
        mvp_recommendation
    )

    print("\nGTM RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()