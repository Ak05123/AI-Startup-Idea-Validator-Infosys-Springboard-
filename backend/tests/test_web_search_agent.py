import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from agents.web_search_agent import WebSearchAgent


def main():

    query = input(
        "Enter search query: "
    ).strip()

    print("\nWEB SEARCH TEST START")

    agent = WebSearchAgent()

    results = agent.search(query)

    print("\nWEB SEARCH RESULTS:\n")

    if not results:
        print("No results found.")
        return

    for index, result in enumerate(results, start=1):

        print(f"\nResult {index}")
        print("-" * 50)
        print("Title:", result.get("title"))
        print("Description:", result.get("description"))
        print("Link:", result.get("link"))


if __name__ == "__main__":
    main()