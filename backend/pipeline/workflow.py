import sys
from pathlib import Path

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

# ==================================================
# IMPORTS
# ==================================================

from app.orchestrator import deep_agent


# ==================================================
# WORKFLOW
# ==================================================

class StartupWorkflow:

    def __init__(self):

        self.agent = deep_agent


    def _invoke(self, prompt):

        result = self.agent.invoke(

            {
                "messages": [

                    {
                        "role": "user",
                        "content": prompt
                    }

                ]
            }

        )

        messages = result["messages"]

        return messages[-1].content


    # ------------------------------------------------
    # Competitor
    # ------------------------------------------------

    def competitor(
        self,
        idea
    ):

        prompt = f"""
Perform competitor analysis.

Startup Idea:

{idea}

Delegate to the Competitor Analysis Specialist.

Return only competitor analysis.
"""

        return self._invoke(prompt)


    # ------------------------------------------------
    # Market
    # ------------------------------------------------

    def market(
        self,
        idea,
        competitor_output
    ):

        prompt = f"""
Perform market analysis.

Startup Idea:

{idea}

Competitor Analysis:

{competitor_output}

Delegate to the Market Analysis Specialist.

Return only market analysis.
"""

        return self._invoke(prompt)