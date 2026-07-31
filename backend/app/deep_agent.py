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

from deepagents import create_deep_agent

from app.config import model
from app.pipeline import StartupValidationPipeline


# ==================================================
# PIPELINE
# ==================================================

pipeline = StartupValidationPipeline()


# ==================================================
# DEEP AGENT
# ==================================================

# The Deep Agent is kept as the AI reasoning/orchestration
# layer for future natural-language requests.
#
# It has NO custom tool loop here, because the deterministic
# pipeline already handles the actual startup analysis.

deep_agent = create_deep_agent(

    model=model,

    tools=[],

    system_prompt="""
You are the AI Startup Validation Assistant.

The backend pipeline performs the actual startup
analysis.

Your role is to provide clear, concise explanations
of the requested analysis result.

Do not invent information.
Do not perform new research.
Use only the information provided to you.
"""
)


# ==================================================
# DISPLAY HELPER
# ==================================================

def display_result(result):

    print(
        "\n" + "=" * 70
    )

    if isinstance(result, list):

        for block in result:

            if isinstance(block, dict):

                text = block.get("text")

                if text:
                    print(text)

            elif isinstance(block, str):

                print(block)

    else:

        print(result)

    print(
        "=" * 70
    )


# ==================================================
# RUN
# ==================================================

if __name__ == "__main__":

    idea = input(
        "Enter startup idea: "
    ).strip()

    task = input(
        "Enter analysis "
        "(competitor/market/swot/mvp/gtm/report/full): "
    ).strip().lower()


    # --------------------------------------------------
    # Validation
    # --------------------------------------------------

    if not idea:

        print(
            "\nStartup idea cannot be empty."
        )

        sys.exit(1)


    valid_tasks = {
        "competitor",
        "market",
        "swot",
        "mvp",
        "gtm",
        "report",
        "full"
    }


    if task not in valid_tasks:

        print(
            "\nInvalid analysis task."
        )

        print(
            "Use:"
        )

        print(
            "competitor, market, swot, "
            "mvp, gtm, report, full"
        )

        sys.exit(1)


    # --------------------------------------------------
    # Start
    # --------------------------------------------------

    print(
        "\n[Startup Validator] "
        "Starting requested analysis..."
    )


    try:

        # ==================================================
        # RUN PIPELINE DIRECTLY
        # ==================================================

        result = pipeline.run_task(
            idea,
            task
        )


        # ==================================================
        # DISPLAY
        # ==================================================

        print(
            "\n" + "=" * 70
        )

        print(
            "              AI STARTUP VALIDATOR"
        )

        print(
            "=" * 70
        )

        print(
            f"\nStartup Idea: {idea}"
        )

        print(
            f"Requested Analysis: {task}"
        )

        print(
            "\n" + "=" * 70
        )

        display_result(
            result
        )


    except Exception as error:

        print(
            "\n" + "=" * 70
        )

        print(
            "          STARTUP VALIDATION ERROR"
        )

        print(
            "=" * 70
        )

        print(
            "\nReason:"
        )

        print(error)

        print(
            "\nThe pipeline already includes "
            "retry handling for transient failures."
        )