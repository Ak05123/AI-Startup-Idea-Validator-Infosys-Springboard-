import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.web_search_agent import WebSearchAgent
from agents.market_analysis_agent import MarketAnalysisAgent


def main():

    idea = input(
        "Enter startup idea: "
    ).strip()

    print("\nMARKET ANALYSIS TEST START")

    web_agent = WebSearchAgent()
    market_agent = MarketAnalysisAgent()

    search_results = web_agent.search(
        idea
        + " market size growth industry trends "
        + "target customers"
    )

    if not search_results:

        print("No web results found.")
        return

    result = market_agent.analyze(
        idea,
        search_results
    )

    print("\nMARKET ANALYSIS RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()