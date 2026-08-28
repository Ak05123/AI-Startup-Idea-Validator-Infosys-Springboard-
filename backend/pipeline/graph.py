import sys
from pathlib import Path

sys.path.append(
    str(Path(__file__).resolve().parent.parent)
)

from app.orchestrator import deep_agent
from state.memory import create_state
from pipeline.context_passer import update_state


def execute_pipeline(startup_idea):

    state = create_state(startup_idea)

    prompt = f"""
Startup Idea:

{startup_idea}

Perform a complete startup validation.

Delegate work to the appropriate specialist agents.

Generate:

1. Competitor Analysis
2. Market Analysis
3. SWOT Analysis
4. MVP Recommendation
5. GTM Strategy
6. Final Report
"""

    result = deep_agent.invoke(

        {
            "messages": [

                {
                    "role": "user",
                    "content": prompt
                }

            ]
        }

    )

    output = result["messages"][-1].content

    if isinstance(output, list):

        output = "\n".join(

            block.get("text", "")

            for block in output

            if isinstance(block, dict)

        )

    update_state(
        state,
        "final_report",
        output
    )

    return state