import sys
from pathlib import Path

# Adds the project root (AI STARTUP) to Python's search path
sys.path.append(str(Path("C:\\Users\\WELCOME\\Desktop\\ai startup\\agents").resolve().parent))

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent
from agents.market_analysis_agent import MarketAnalysisAgent

class Coordinator:

    def __init__(self):

        self.web_agent = WebSearchAgent()
        self.competitor_agent = CompetitorAgent()
        self.market_agent = MarketAnalysisAgent()

    def analyze_startup(self, idea):

    # Different search queries for different agents
        competitor_query = idea + " top competitors companies"

        market_query = idea + " market size CAGR industry trends target customers"

        print("\nSearching competitors...\n")
        competitor_results = self.web_agent.search(competitor_query)

        print("\nSearching market data...\n")
        market_results = self.web_agent.search(market_query)

        print("\nCompetitor Search Results:\n")

        for i, result in enumerate(competitor_results, 1):

            print("==============================")
            print(f"Search Result {i}")
            print("==============================")
            print("Title:", result["title"])
            print("Description:", result["description"])
            print("Link:", result["link"])
            print()

        

        competitors = self.competitor_agent.analyze(competitor_results)



        market_analysis = self.market_agent.analyze(
            idea,
            market_results
        )

        return {
            "competitors": competitors,
            "market_analysis": market_analysis
        }