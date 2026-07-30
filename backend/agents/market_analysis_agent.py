from google import genai




from app.config import client, MODEL_NAME

class MarketAnalysisAgent:

    def __init__(self):
        self.client = client

    def analyze(self, idea, search_results):

        # Convert search results into text
        text = ""

        for result in search_results:
            text += f"""
Title: {result['title']}
Description: {result['description']}
Link: {result['link']}

"""

        prompt = f"""
You are an AI Market Analysis Agent.

Startup Idea:
{idea}

Below are DuckDuckGo search results.

{text}

Analyze the startup market and return ONLY the following information.

Return ONLY valid JSON.

{{
    "industry": "",
    "market_size": "",
    "growth_rate": "",
    "target_customers": [],
    "market_trends": [],
    "opportunities": [],
    "challenges": []
}}

Rules:

1. Identify the industry.
2. Estimate the market size if available.
3. Identify the market growth rate if available.
4. List target customers.
5. List current market trends.
6. List business opportunities.
7. List major market challenges.
8. Do not explain anything.
9. Return only JSON.
"""

        print("\nSending Market Analysis to Gemini...\n")

        try:

            response = self.client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("\nGemini Error:")
            print(e)

            return "{}"
if __name__ == "__main__":

    from web_search_agent import WebSearchAgent

    startup = input("Enter startup idea: ")

    web = WebSearchAgent()

    search_results = web.search(startup)

    agent = MarketAnalysisAgent()

    result = agent.analyze(startup, search_results)

    print("\nMarket Analysis:\n")
    print(result)