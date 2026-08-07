from ddgs import DDGS
from langchain_core.tools import tool


@tool
def web_search(query: str) -> list[dict]:
    """
    Search the web using DuckDuckGo and return the top search results.
    """

    with DDGS(timeout=20) as search:

        results = search.text(
            query,
            max_results=5
        )

        cleaned_results = []

        for result in results:

            cleaned_results.append(
                {
                    "title": result.get("title", ""),
                    "description": result.get("body", ""),
                    "link": result.get("href", "")
                }
            )

    return cleaned_results