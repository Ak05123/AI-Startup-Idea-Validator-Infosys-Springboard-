import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.config import model


class CompetitorAgent:

    def __init__(self):
        self.model = model

    def analyze(self, search_results):

        text = ""

        for result in search_results:
            text += f"""
Title: {result['title']}
Description: {result['description']}
"""

        prompt = f"""
You are an AI Competitor Analysis Agent.

Below are web search results:

{text}

Task:
Identify the main competitor companies related to the startup idea.

Rules:
- Return only competitor company names.
- Ignore article titles.
- Ignore blogs.
- Ignore Wikipedia.
- Ignore investors.
- Ignore funding companies.
- Ignore market reports.
- Do not explain anything.

Return the result as a simple Python-style list.

Example:
["LeetCode", "HackerRank", "GeeksforGeeks"]
"""

        try:

            response = self.model.invoke(prompt)

            return response.content

        except Exception as e:

            print("\nGemini Error:")
            print(e)

            return []