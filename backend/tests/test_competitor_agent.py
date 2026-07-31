import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.web_search_agent import WebSearchAgent
from agents.competitor_agent import CompetitorAgent


def main():

    idea = input(
        "Enter startup idea: "
    ).strip()

    print("\nCOMPETITOR TEST START")

    web_agent = WebSearchAgent()
    competitor_agent = CompetitorAgent()

    search_results = web_agent.search(
        idea + " top competitors companies"
    )

    if not search_results:

        print("No web results found.")
        return

    result = competitor_agent.analyze(
        search_results
    )

    print("\nCOMPETITOR RESULT:\n")
    print(result)


if __name__ == "__main__":
    main()