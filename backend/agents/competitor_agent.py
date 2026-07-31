import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.config import client, MODEL_NAME




class CompetitorAgent:

    def __init__(self):
        self.client = client
        

    def analyze(self, search_results):

        # Convert DuckDuckGo results into text
        text = ""

        for result in search_results:
            text += f"""
Title: {result['title']}
Description: {result['description']}
"""

        prompt = f"""
You are an AI Competitor Analysis Agent.

Below are DuckDuckGo search results.

{text}

Task:
Extract ONLY the names of competitor companies related to this startup idea.

Rules:
- Ignore article titles.
- Ignore websites.
- Ignore Wikipedia.
- Ignore blogs.
- Ignore investors.
- Ignore funding companies.
- Ignore market reports.

Return ONLY a Python list.

Example:

[
"Swiggy",
"Zomato",
"DoorDash",
"Uber Eats",
"Deliveroo"
]

Do not explain anything.
"""

        print("\nSending data to Gemini...\n")

        try:
            response = self.client.models.generate_content(
                # Use the SAME model that worked in gemini_test.py
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text

        except Exception as e:
            print("\nGemini Error:")
            print(e)
            return []


if __name__ == "__main__":
    from web_search_agent import WebSearchAgent

    
    startup = input("Enter startup idea: ")

    web = WebSearchAgent()

    search_results = web.search(startup)

    agent = CompetitorAgent()

    competitors = agent.analyze(search_results)

    print("\nCompetitors Found:\n")
    print(competitors)