from ddgs import DDGS


class WebSearchAgent:

    def search(self, query):

        search_engine = DDGS(timeout=10)

        results = search_engine.text(
            query,
            max_results=1
        )

        cleaned_results = []

        for result in results:

            cleaned_results.append({
                "title": result["title"],
                "description": result["body"],
                "link": result["href"]
            })

        return cleaned_results