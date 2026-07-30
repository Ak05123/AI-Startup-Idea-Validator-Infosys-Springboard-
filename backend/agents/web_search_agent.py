from ddgs import DDGS


class WebSearchAgent:

    def search(self, query):

        search_engine = DDGS()

        results = search_engine.text(
            query,
            max_results=3
        )

        cleaned_results = []

        for result in results:

            cleaned_results.append({

                "title": result["title"],

                "description": result["body"],

                "link": result["href"]

            })

        return cleaned_results


if __name__ == "__main__":
    agent = WebSearchAgent()

    idea = input("Enter your startup idea: ")

    data = agent.search(idea + " top competitors companies")



    for i, result in enumerate(data, 1):

        print("\n==============================")
        print(f"Search Result {i}")
        print("==============================")

        print("Title:")
        print(result["title"])

        print("\nDescription:")
        print(result["description"])

        print("\nLink:")
        print(result["link"])