import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

from tools.web_search import web_search


results = web_search.invoke(
    {
        "query": "bus booking competitors"
    }
)

print()

print("WEB SEARCH RESULTS")

print("=" * 60)

for index, result in enumerate(results, start=1):

    print(f"\nResult {index}")

    print("-" * 60)

    print("Title :", result["title"])

    print("Description :", result["description"])

    print("Link :", result["link"])