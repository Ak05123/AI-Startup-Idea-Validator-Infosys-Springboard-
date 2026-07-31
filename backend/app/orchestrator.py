import sys
from pathlib import Path

# Add backend folder to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.market_analysis_agent import MarketAnalysisAgent
from agents.swot_risk_agent import SwotRiskAgent


class Coordinator:

    def __init__(self):

        self.web_agent = WebSearchAgent()
        self.competitor_agent = CompetitorAgent()
        self.market_agent = MarketAnalysisAgent()
        self.swot_agent = SwotRiskAgent()

    def analyze_startup(self, idea):

        competitor_query = idea + " top competitors companies"

        market_query = (
            idea +
            " market size CAGR industry trends target customers"
        )

        print("\nSearching competitors...\n")
        competitor_results = self.web_agent.search(competitor_query)

        print("\nSearching market data...\n")
        market_results = self.web_agent.search(market_query)

        print("\nAnalyzing competitors...\n")
        competitors = self.competitor_agent.analyze(
            competitor_results
        )

        print("\nAnalyzing market...\n")
        market_analysis = self.market_agent.analyze(
            idea,
            market_results
        )

        print("\nPerforming SWOT and Risk Analysis...\n")
        swot_analysis = self.swot_agent.analyze(
            idea,
            competitors,
            market_analysis
        )

        return {
            "competitors": competitors,
            "market_analysis": market_analysis,
            "swot_analysis": swot_analysis
        }