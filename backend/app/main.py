import sys
from pathlib import Path

# ==================================================
# PATH SETUP
# ==================================================

sys.path.append(
    str(Path(__file__).resolve().parents[1])
)

import json

from app.orchestrator import startup_validator


def validate_startup(idea: str):

    return startup_validator.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": idea
                }
            ]
        }
    )


if __name__ == "__main__":

    startup_idea = input("Enter Startup Idea: ").strip()

    print("\n==============================================")
    print("       AI STARTUP VALIDATION")
    print("==============================================")
    print(f"\nStartup Idea: {startup_idea}")
    print("\nRunning validation agents...")
    print("----------------------------------------------")

    result = validate_startup(startup_idea)

    # Get final response from report agent
    response = result["messages"][-1].content

    # Deep Agents may return content as a list
    if isinstance(response, list):
        response = response[0]["text"]

    print("\n==============================================")
    print("           FINAL VALIDATION REPORT")
    print("==============================================\n")

    try:
        parsed = json.loads(response)

        print(
            json.dumps(
                parsed,
                indent=4,
                ensure_ascii=False
            )
        )

    except json.JSONDecodeError:
        print(response)

    print("\n==============================================")
    print("          VALIDATION COMPLETED")
    print("==============================================")